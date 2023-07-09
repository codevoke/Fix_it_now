from peewee import *
from db import BaseModel


class ProblemCardModel(BaseModel):
    MetaTableName = 'ProblemCards_data'

    id = AutoField(primary_key=True)
    author_id = IntegerField()
    title = TextField()
    description = TextField()
    repair_date = DateTimeField()
    status = CharField(choices=['open', 'in_progress', 'fixed', 'closed'])
