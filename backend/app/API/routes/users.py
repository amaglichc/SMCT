from fastapi import APIRouter
from app.Models.user import SignUpUser, SignInUser


router = APIRouter(tags=["Users"], prefix="/users")


@router.post("/signup")
async def signup(user: SignUpUser):
    pass


@router.post("/signin")
async def signin(user: SignInUser):
    pass
