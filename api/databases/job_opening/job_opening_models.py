from .job_opening_db import JobOpeningDB
from ..ModelManager import ModelManager


class JobOpeningModel(ModelManager):
    db_objects = JobOpeningDB()

    def __init__(self):
        self.id = None
        self.title = None
        self.company = None
        self.location = None
        self.salary = None
        self.job_description = None
        self.username_of_creator = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
