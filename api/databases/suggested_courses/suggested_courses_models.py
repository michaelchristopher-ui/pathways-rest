from .suggested_courses_db import SuggestedCoursesDB
from ..ModelManager import ModelManager


class SuggestedCoursesModel(ModelManager):
    db_objects = SuggestedCoursesDB()

    def __init__(self):
        self.name = None
        self.link_to_course = None
        self.course_id = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
