from app.models.dataset import Dataset, EliminatedData

def save(db, dataset):
    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    return dataset

def save_eliminated(db, eliminated_data):
    db.add(eliminated_data)
    db.commit()
    db.refresh(eliminated_data)
    return eliminated_data