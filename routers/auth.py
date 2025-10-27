from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login():
    pass


@router.post("/logout")
async def logout():
    pass


@router.post("register")
async def register():
    pass


@router.post("/token/refresh")
async def get_refresh_token():
    pass
