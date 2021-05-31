from .user_company_db import UserCompanyDB
from ..ModelManager import ModelManager


class UserCompanyModel(ModelManager):
    db_objects = UserCompanyDB()

    def __init__(self):
        self.company_id = None
        self.username = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
