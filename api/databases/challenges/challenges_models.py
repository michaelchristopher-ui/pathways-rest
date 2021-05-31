from .challenges_db import ChallengesDB
from ..ModelManager import ModelManager


class ChallengesModel(ModelManager):
    db_objects = ChallengesDB()

    def __init__(self):
        self.task_title = None
        self.task_type = None
        self.data_related = None
        self.job_opening_id = None
        self.order_number = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
