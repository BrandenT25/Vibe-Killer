from fastapi import APIRouter
from chainlit.utils import mount_chainlit

router = APIRouter()

@router.get("/")
def read_main():
    return {"message": "Hello from main app"}
