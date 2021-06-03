from .user_general_does_challenges_db import UserGeneralDoesChallengesDB
from ..ModelManager import ModelManager


class UserGeneralDoesChallengesModel(ModelManager):
    db_objects = UserGeneralDoesChallengesDB()

    def __init__(self):
        self.username = None
        self.job_opening_id = None
        self.order_number = None
        self.data_related = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
