from api.databases.job_opening.job_opening_db import JobOpeningDB
from .user_general_applies_job_opening_db import UserGeneralAppliesJobOpeningDB
from ..ModelManager import ModelManager


class UserGeneralAppliesJobOpeningModel(ModelManager):
    db_objects = UserGeneralAppliesJobOpeningDB()

    def __init__(self):
        self.username = None
        self.job_id = None
        self.done_challenges = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
