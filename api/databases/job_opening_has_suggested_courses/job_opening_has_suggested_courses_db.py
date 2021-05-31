from ..DBManager import DBManager


class JobOpeningHasSuggestedCoursesDB(DBManager):
    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO job_opening_has_suggested_courses
        (job_opening_id, course_id) VALUES ('{0}', '{1}');""".format(
            db_models.job_opening_id,
            db_models.course_id
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE job_opening_has_suggested_courses SET
        job_opening_id = '{0}',
        course_id = '{1}'
        WHERE job_opening_id = '{0}' AND course_id = '{1}'; """.format(
            db_models.job_opening_id,
            db_models.course_id
        )

        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM job_opening_has_suggested_courses;"""
        cursor = self.query_database(database_query)
        from .job_opening_has_suggested_courses_models import JobOpeningHasSuggestedCoursesModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = JobOpeningHasSuggestedCoursesModel()
            db_object.job_opening_id = db_row[0]
            db_object.course_id = db_row[1]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find, id_to_find_2):
        database_query = """SELECT * FROM job_opening_has_suggested_courses WHERE job_opening_id = '{0}' AND course_id = '{1}';""".format(
            id_to_find, id_to_find_2)
        cursor = self.query_database(database_query)
        from .job_opening_has_suggested_courses_models import JobOpeningHasSuggestedCoursesModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = JobOpeningHasSuggestedCoursesModel()
            db_object.job_opening_id = db_row[0]
            db_object.course_id = db_row[1]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM job_opening_has_suggested_courses WHERE job_opening_id = '{0}' AND course_id = '{1}';""".format(
            db_models.job_opening_id, db_models.course_id)
        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
