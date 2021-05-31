from ..DBManager import DBManager


class SuggestedCoursesDB(DBManager):
    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        print("at insert db")
        database_query = """INSERT INTO suggested_courses
        (name, link_to_course, course_id) VALUES
        ('{0}', '{1}', '{2}');""".format(
            db_models.name,
            db_models.link_to_course,
            db_models.course_id
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE suggested_courses SET
        name = '{0}',
        link_to_course = '{1}',
        course_id = '{2}'
        WHERE course_id = '{2}';""".format(
            db_models.name,
            db_models.link_to_course,
            db_models.course_id
        )

        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * from suggested_courses;"""
        cursor = self.query_database(database_query)
        from .suggested_courses_models import SuggestedCoursesModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = SuggestedCoursesModel()
            db_object.name = db_row[0]
            db_object.link_to_course = db_row[1]
            db_object.course_id = db_row[2]
            list_of_db_objects.append(db_object)

        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find):
        database_query = """SELECT * from suggested_courses WHERE course_id = '{0}';""".format(
            id_to_find)
        cursor = self.query_database(database_query)
        from .suggested_courses_models import SuggestedCoursesModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = SuggestedCoursesModel()
            db_object.name = db_row[0]
            db_object.link_to_course = db_row[1]
            db_object.course_id = db_row[2]
            list_of_db_objects.append(db_object)

        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM suggested_courses WHERE course_id = '{0}';""".format(
            db_models.course_id)
        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
