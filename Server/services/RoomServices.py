from sqlalchemy.orm import Session
from models import Room
from schemas.RoomSchema import RoomCreateSchema, RoomUpdateSchema
from fastapi import HTTPException

def read_rooms(db: Session):
    return db.query(Room).all()

def create_room(db: Session, room_create: RoomCreateSchema):
    new_room = Room(roomNumber = room_create.roomNumber, 
                    roomType = room_create.roomType,
                    status = room_create.status)
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room
    
def update_room(db: Session, id: int, update_room_info: RoomUpdateSchema):
    room_update = db.query(Room).filter(Room.roomNumber == id).first()
    if (not room_update):
         raise HTTPException(status_code=404, detail="room not found")
    room_data = update_room_info.dict(exclude_unset=True)
    for key, value in room_data.items():
        setattr(room_update, key, value)
    db.add(room_update)
    db.commit()
    db.refresh(room_update)
    return(room_update)

def delete_room(db: Session, id: int):
    room_delete = db.query(Room).filter(Room.roomNumber == id).first()
    if (not room_delete):
        raise HTTPException(status_code=404, detail="room not found")
    db.delete(room_delete)
    db.commit()
    return {
        'message': 'Successfully'
    }
