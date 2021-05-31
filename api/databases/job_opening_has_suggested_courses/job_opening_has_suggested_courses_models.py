from .job_opening_has_suggested_courses_db import JobOpeningHasSuggestedCoursesDB
from ..ModelManager import ModelManager


class JobOpeningHasSuggestedCoursesModel(ModelManager):
    db_objects = JobOpeningHasSuggestedCoursesDB()

    def __init__(self):
        self.job_opening_id = None
        self.course_id = None

    def init_save_data_to_database(self):
        return super().init_save_data_to_database(self.db_objects)

    def init_delete_data_from_database(self):
        return super().init_delete_data_from_database(self.db_objects)
