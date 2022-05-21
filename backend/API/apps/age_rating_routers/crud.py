from sqlalchemy.orm import Session
from apps.age_rating_routers import shemas, models


def create_db_age_raiting(age_raiting):
    return models.age_rating_type(
        ageRaiting=age_raiting.ageRaiting,
        PGraiting=age_raiting.PGraiting,
        minAge=age_raiting.minAge,
        description=age_raiting.description,
    )

def add_age_raiting(age_raiting, db):
    db_age_raiting = create_db_age_raiting(age_raiting)
    db.add(db_age_raiting)
    db.commit()
    db.refresh(db_age_raiting)


def delete_age_raiting(age_raiting, db):
    db_age_raiting = db.query(models.age_rating_type).filter(
        models.age_rating_type.ageRaiting == age_raiting.ageRaiting).first()
    if type(db_age_raiting) == models.age_rating_type:
        db.delete(db_age_raiting)
        db.commit()
        return True
    else:
        raise False


def update_age_raiting(age_raiting, db):
    db_age_raiting = create_db_age_raiting(age_raiting)
    db.query(models.age_rating_type).filter(
        models.age_rating_type.ageRaiting == age_raiting.ageRaiting)\
        .update({'ageRaiting': db_age_raiting.ageRaiting,
                 'PGraiting': db_age_raiting.PGraiting,
                 'minAge': db_age_raiting.minAge,
                 'description': db_age_raiting.description
                 })
    db.commit()


def get_age_raiting(age_raiting, db):
    if age_raiting:
        return db.query(models.age_rating_type).filter(
            models.age_rating_type.ageRaiting == age_raiting.ageRaiting).first()
    else:
        return db.query(models.age_rating_type).limit(100).all()
