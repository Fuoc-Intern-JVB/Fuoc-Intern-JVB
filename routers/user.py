from fastapi import APIRouter

router = APIRouter()

@router.get("users/me")
async def get_current_user():
    pass

@router.get("users/all")
async def get_all_users():
    pass