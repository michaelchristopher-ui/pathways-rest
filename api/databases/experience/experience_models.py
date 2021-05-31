from .experience_db import ExperienceDB
from ..ModelManager import ModelManager


class ExperienceModel(ModelManager):
    db_objects = ExperienceDB()

    def __init__(self):
        self.order_no = None
        self.username = None
        self.position = None
        self.company_name = None
        self.start_date = None
        self.end_date = None
        self.position_description = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
