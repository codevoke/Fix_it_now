from peewee import *
from db import BaseModel


class UserModel(BaseModel):
    MetaTableName = 'User_data'

    id = AutoField(primary_key=True)
    username = TextField(unique=True)
    login = CharField(max_length=30, unique=True)
    password = CharField(max_length=30)
    role = CharField(choices=['teacher', 'worker', 'admin'])
