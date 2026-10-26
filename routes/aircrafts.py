from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/aircrafts")
def add_aircraft(data: schemas.AircraftCreate, db: Session = Depends(database.get_db)):
    new_aircraft = models.Aircraft(**data.dict())
    db.add(new_aircraft)
    db.commit()
    db.refresh(new_aircraft)
    return {"message": "Aircraft added successfully", "data": new_aircraft}


@router.get("/aircrafts")
def get_aircrafts(db: Session = Depends(database.get_db)):
    aircrafts = db.query(models.Aircraft).all()
    return aircrafts


@router.get("/aircrafts/{aircraft_id}")
def get_aircraft_by_id(aircraft_id: int, db: Session = Depends(database.get_db)):
    aircraft = db.query(models.Aircraft).filter(models.Aircraft.id == aircraft_id).first()
    if not aircraft:
        return {"error": f"Aircraft with ID {aircraft_id} not found"}
    return aircraft


@router.put("/aircrafts/{aircraft_id}")
def update_aircraft(aircraft_id: int, data: schemas.AircraftCreate, db: Session = Depends(database.get_db)):
    aircraft = db.query(models.Aircraft).filter(models.Aircraft.id == aircraft_id).first()
    if not aircraft:
        return {"error": f"Aircraft with ID {aircraft_id} not found"}

    for key, value in data.dict().items():
        setattr(aircraft, key, value)

    db.commit()
    db.refresh(aircraft)
    return {"message": "Aircraft updated successfully", "data": aircraft}


@router.delete("/aircrafts/{aircraft_id}")
def delete_aircraft(aircraft_id: int, db: Session = Depends(database.get_db)):
    aircraft = db.query(models.Aircraft).filter(models.Aircraft.id == aircraft_id).first()
    if not aircraft:
        return {"error": f"Aircraft with ID {aircraft_id} not found"}

    db.delete(aircraft)
    db.commit()
    return {"message": f"Aircraft with ID {aircraft_id} deleted successfully"}

