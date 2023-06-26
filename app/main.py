from osa_utils.db_api.database import create_db, drop_connection
from osa_utils.db_api import db_commands
import uvicorn
from fastapi import FastAPI, HTTPException
from urllib.parse import unquote

from osa_utils.db_api.models import User, Teacher, Teacher_classes, Vote, Vote_classes, Group,\
    Group_classes, Question
from config import HOST

app = FastAPI()


@app.on_event('startup')
async def startup_event():
    await create_db()


@app.get('/all_teachers/{faculty}')
async def get_all_teachers(faculty: str):
    faculty = unquote(faculty)
    teachers: list[Teacher] = await db_commands.get_all_teachers(faculty)

    t_list = [{'faculty': faculty}]
    for teacher in teachers:
        t_list.append({'id': teacher.id, 'full_name': teacher.full_name, 'type': teacher.type})
    return {'teachers': t_list}


@app.get('/all_groups/{faculty}')
async def get_all_groups(faculty: str):
    faculty = unquote(faculty)
    groups: list[Group] = await db_commands.get_all_groups(faculty)

    g_list = [{'faculty': faculty}]
    for group in groups:
        g_list.append({'id': group.id, 'name': group.name, 'teachers': group.teachers})
    return {'groups': g_list}


@app.get('/group/{faculty}/{group_name}')
async def get_group(faculty: str, group_name: str):
    group_name = unquote(group_name)
    # print(group_name)

    group = await db_commands.get_group_by_name(faculty, group_name)

    if group:
        g_list = {'faculty': faculty, 'id': group.id, 'name': group.name, 'teachers': group.teachers}
        return g_list
    else:
        raise HTTPException(status_code=404, detail="Group not found")

uvicorn.run('app.main:app', port=8000, log_level='debug', host=HOST)




