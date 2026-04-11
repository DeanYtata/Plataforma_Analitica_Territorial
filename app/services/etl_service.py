import csv
import io
from sqlalchemy import text
from app.models.dataset import Dataset, EliminatedData
from app.repositories.dataset_repository import save, save_eliminated

# ============================================================
# VARIABLES GLOBALES
# ============================================================
# 🔥 Almacenan los datos procesados en memoria
datos_limpios = []
datos_eliminados = []


def procesar_csv(file, db):
    """
    ============================================================
    PROCESO ETL COMPLETO
    ============================================================

    ✔ PUNTO 1: Cargar archivo CSV
    ✔ PUNTO 2: Eliminar nulos
    ✔ PUNTO 3: Eliminar duplicados
    ✔ PUNTO 4: Normalizar datos
    ✔ PUNTO 5: Imprimir resultados
    ✔ PUNTO 6: Guardar en PostgreSQL
    """

    global datos_limpios, datos_eliminados

    # ============================================================
    # LIMPIAR VARIABLES EN MEMORIA
    # ============================================================
    datos_limpios.clear()
    datos_eliminados.clear()

    # ============================================================
    # LIMPIAR BASE DE DATOS (REINICIAR TABLAS)
    # ============================================================
    print("🧹 LIMPIANDO DATOS ANTERIORES...")

    db.execute(text("TRUNCATE TABLE dataset RESTART IDENTITY CASCADE"))
    db.execute(text("TRUNCATE TABLE eliminated_data RESTART IDENTITY CASCADE"))
    db.commit()

    print("✅ Tablas limpiadas correctamente")

    # ============================================================
    # PUNTO 1: CARGAR ARCHIVO CSV
    # ============================================================
    # 🔥 Convertimos archivo binario a texto
    try:
        contenido = file.file.read().decode("utf-8")
    except:
        contenido = file.file.read().decode("latin-1")  # fallback

    reader = csv.reader(io.StringIO(contenido))

    # Saltar encabezado
    next(reader, None)

    # Set para controlar duplicados
    unicos = set()

    # ============================================================
    # RECORRER FILAS DEL CSV
    # ============================================================
    for fila in reader:

        # Validar estructura mínima
        if len(fila) < 3:
            continue

        # ============================================================
        # PUNTO 4: NORMALIZACIÓN
        # ============================================================
        ciudad = fila[0].strip()
        ingresos_str = fila[1].strip()
        poblacion_str = fila[2].strip()

        # ============================================================
        # PUNTO 2: ELIMINAR NULOS
        # ============================================================
        if not ciudad or not ingresos_str or not poblacion_str:
            print(f"⚠️ FILA ELIMINADA (nulo): {fila}")

            eliminado = EliminatedData(
                ciudad=ciudad or "N/A",
                ingresos=ingresos_str or "NULO",
                poblacion=poblacion_str or "NULO",
                razon_eliminacion="Valor nulo/vacío"
            )

            save_eliminated(db, eliminado)
            datos_eliminados.append(eliminado)
            continue

        # Convertir ciudad a minúsculas
        ciudad = ciudad.lower()

        # ============================================================
        # PUNTO 3: ELIMINAR DUPLICADOS
        # ============================================================
        clave = ciudad + ingresos_str + poblacion_str

        if clave in unicos:
            print(f"⚠️ FILA ELIMINADA (duplicado): {fila}")

            eliminado = EliminatedData(
                ciudad=ciudad,
                ingresos=ingresos_str,
                poblacion=poblacion_str,
                razon_eliminacion="Duplicado"
            )

            save_eliminated(db, eliminado)
            datos_eliminados.append(eliminado)
            continue

        # Registrar clave única
        unicos.add(clave)

        # ============================================================
        # VALIDAR TIPOS DE DATOS (CONVERSIÓN)
        # ============================================================
        try:
            ingresos = float(ingresos_str)
            poblacion = int(poblacion_str)
        except:
            print(f"⚠️ FILA ELIMINADA (error conversión): {fila}")

            eliminado = EliminatedData(
                ciudad=ciudad,
                ingresos=ingresos_str,
                poblacion=poblacion_str,
                razon_eliminacion="Error en conversión"
            )

            save_eliminated(db, eliminado)
            datos_eliminados.append(eliminado)
            continue

        # ============================================================
        # CREAR OBJETO LIMPIO
        # ============================================================
        dataset = Dataset(
            ciudad=ciudad,
            ingresos=ingresos,
            poblacion=poblacion
        )

        # ============================================================
        # PUNTO 6: GUARDAR RESULTADO
        # ============================================================
        save(db, dataset)
        datos_limpios.append(dataset)

    # ============================================================
    # PUNTO 5: MOSTRAR RESULTADOS
    # ============================================================
    print("\n" + "="*60)
    print("✅ DATOS LIMPIOS:")
    print("="*60)

    for d in datos_limpios:
        print(f"  • {d.ciudad.upper():20} | ${d.ingresos:>10} | {d.poblacion:>10}")

    print("="*60)

    print("\n⚠️ DATOS ELIMINADOS:")
    print("="*60)

    for d in datos_eliminados:
        print(f"  • {d.ciudad:20} | {d.ingresos:>10} | {d.poblacion:>10} | {d.razon_eliminacion}")

    print("="*60 + "\n")

    # Retornar datos limpios
    return datos_limpios


# ============================================================
# GENERAR CSV DESDE MEMORIA
# ============================================================
def generar_csv():
    """
    Genera un archivo CSV con los datos ya procesados
    """

    csv_data = "ciudad,ingresos,poblacion\n"

    for d in datos_limpios:
        csv_data += f"{d.ciudad},{d.ingresos},{d.poblacion}\n"

    return csv_data