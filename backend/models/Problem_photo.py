from peewee import *
from db import BaseModel


class ProblemPhotoModel(BaseModel):
    MetaTableName = 'ProblemPhotos_data'

    id = AutoField(primary_key=True)
    problem_id = IntegerField()
    format = CharField(max_length=3, choices=['png', 'jpg'])
