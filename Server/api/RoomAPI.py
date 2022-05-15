from fastapi import APIRouter, Depends
from services.RoomServices import create_room, delete_room, read_rooms, update_room, delete_room
from schemas.RoomSchema import RoomSchema, RoomCreateSchema, RoomUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get('', response_model=List[RoomSchema])
def get_roomss(db: Session = Depends(get_db)): 
    return read_rooms(db)

@router.post('', response_model=RoomSchema)
def post_room(room_create: RoomCreateSchema, db: Session = Depends(get_db)): 
    print(1)
    print(room_create)
    return create_room(db, room_create)

@router.put('/{id1}-{id2}', response_model=RoomSchema)
def put(id: int, room_update_info: RoomUpdateSchema, db: Session = Depends(get_db)):
    return update_room(db, id, room_update_info)

@router.delete('/{id1}-{id2}')
def get_one(id: int, db: Session = Depends(get_db)): 
    return delete_room(db, id)
    