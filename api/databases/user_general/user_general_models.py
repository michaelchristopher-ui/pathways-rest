from .user_general_db import UserGeneralDB
from ..ModelManager import ModelManager


class UserGeneralModel(ModelManager):
    db_objects = UserGeneralDB()

    def __init__(self):
        self.username = None
        self.interest_subject = None
        self.interest_job = None
        self.profile_picture = None
        self.short_description = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
