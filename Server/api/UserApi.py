from fastapi import APIRouter

router = APIRouter()

@router.get('')
def get(): 
    return 'abc'
@router.get('/abc/{id}')
def index(id):
    return {'data': {id}}
