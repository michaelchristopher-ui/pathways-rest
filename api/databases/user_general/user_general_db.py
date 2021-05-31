from ..DBManager import DBManager


class UserGeneralDB(DBManager):
    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO user_general
        (username, interest_subject, interest_job, profile_picture, short_description) VALUES 
        ('{0}', '{1}', '{2}', '{3}', '{4}');""".format(
            db_models.username,
            db_models.interest_subject,
            db_models.interest_job,
            db_models.profile_picture,
            db_models.short_description
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE user_general SET
            username = '{0}',
            interest_subject = '{1}',
            interest_job = '{2}',
            profile_picture = '{3}',
            short_description  = '{4}' WHERE username = '{0}';""".format(
            db_models.username,
            db_models.interest_subject,
            db_models.interest_job,
            db_models.profile_picture,
            db_models.short_description
        )

        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM user_general; """
        cursor = self.query_database(database_query)
        from .user_general_models import UserGeneralModel
        list_of_db_objects = []
        for db_row in cursor.fetchall():
            db_object = UserGeneralModel
            db_object.username = db_row[0]
            db_object.interest_subject = db_row[1]
            db_object.interest_job = db_row[2]
            db_object.profile_picture = db_row[3]
            db_object.short_description = db_row[4]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find):
        database_query = """SELECT * FROM user_general WHERE username = '{0}'; """.format(
            id_to_find)
        cursor = self.query_database(database_query)
        from .user_general_models import UserGeneralModel
        list_of_db_objects = []
        for db_row in cursor.fetchall():
            db_object = UserGeneralModel()
            db_object.username = db_row[0]
            db_object.interest_subject = db_row[1]
            db_object.interest_job = db_row[2]
            db_object.profile_picture = db_row[3]
            db_object.short_description = db_row[4]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM user_general
                            WHERE username = '{0}';""".format(db_models.username)

        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
