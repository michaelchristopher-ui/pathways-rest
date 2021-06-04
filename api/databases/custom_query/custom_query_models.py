from .custom_query_db import CustomQueryDB
from ..ModelManager import ModelManager


class CustomQueryModel(ModelManager):
    db_objects = CustomQueryDB()

    def __init__(self):
        self.task_title = None
        self.data_related = None
