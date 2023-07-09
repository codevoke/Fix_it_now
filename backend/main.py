from fastapi import FastAPI
from resources.user import user_router
from resources.problem_card import problem_card_router
from resources.problem_photo import problem_photo_router

app = FastAPI()

app.include_router(user_router)
app.include_router(problem_card_router)
app.include_router(problem_photo_router)
