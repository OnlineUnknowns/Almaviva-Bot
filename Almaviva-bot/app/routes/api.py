"""API route definitions (thin controllers).

Keep logic in `app.modules` and only use routes to validate input/return responses.
"""
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.modules import login as login_module
from app.modules import booking as booking_module
from app.modules import captcha_solver as captcha_module
from app.modules import scheduler as scheduler_module

router = APIRouter()


class LoginIn(BaseModel):
    username: str
    password: str


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/login")
async def login(payload: LoginIn):
    return login_module.login(payload.username, payload.password)


class BookingIn(BaseModel):
    user_id: int
    data: str


@router.post("/book")
async def book(payload: BookingIn):
    return booking_module.book(payload.user_id, payload.data)


class CaptchaIn(BaseModel):
    image_path: str


@router.post("/solve_captcha")
async def solve_captcha(payload: CaptchaIn):
    return {"solution": captcha_module.solve_captcha(payload.image_path)}


class ScheduleIn(BaseModel):
    user_id: int
    when: str


@router.post("/schedule")
async def schedule(payload: ScheduleIn):
    return scheduler_module.schedule_appointment(payload.user_id, payload.when)
