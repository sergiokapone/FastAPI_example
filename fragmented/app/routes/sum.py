from fastapi import APIRouter
from app.schemas.numbers import Numbers

router = APIRouter()


@router.post("/sum")
async def sum_numbers(numbers: Numbers):
    return {"hello": numbers.a + numbers.b}
