from .company_db import CompanyDB
from ..ModelManager import ModelManager


class CompanyModel(ModelManager):
    db_objects = CompanyDB()

    def __init__(self):
        self.id = None
        self.company_name = None
        self.company_description = None
        self.size = None
        self.avg_processing_time = None
        self.industry = None
        self.location = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
