import os
print(os.listdir())
from typing import Union

from ...osa_utils.db_api import db_commands

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/all_teachers/{faculty}")
async def read_item(faculty: str):
    teachers = await db_commands.get_all_teachers(faculty=faculty)
    return {"teachers": teachers}
