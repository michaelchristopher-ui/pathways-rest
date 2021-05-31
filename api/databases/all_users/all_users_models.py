from .all_users_db import AllUsersDB
from ..ModelManager import ModelManager


class AllUsersModel(ModelManager):
    db_objects = AllUsersDB()

    def __init__(self):
        self.username = None
        self.email = None
        self.user_password = None
        self.type_of_user = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
