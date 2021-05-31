from ..DBManager import DBManager


class UserGeneralAppliesJobOpeningDB(DBManager):

    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO user_general_applies_job_opening
        (username, job_id, done_challenges) VALUES ('{0}', '{1}', {2});""".format(
            db_models.username,
            db_models.job_id,
            db_models.done_challenges
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE user_general_applies_job_opening
        username = '{0}',
        job_id = '{1}', done_challenges = '{2}' WHERE username = '{0}' AND job_id = '{1}';""".format(
            db_models.username,
            db_models.job_id,
            db_models.done_challenges
        )
        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM user_general_applies_job_opening; """
        cursor = self.query_database(database_query)
        from .user_general_applies_job_opening_models import UserGeneralAppliesJobOpeningModel
        list_of_db_objects = []
        for db_row in cursor.fetchall():
            db_object = UserGeneralAppliesJobOpeningModel()
            db_object.username = db_row[0]
            db_object.job_id = db_row[1]
            db_object.done_challenges = db_row[2]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM user_general_applies_job_opening; """
        cursor = self.query_database(database_query)
        from .user_general_applies_job_opening_models import UserGeneralAppliesJobOpeningModel
        list_of_db_objects = []
        for db_row in cursor.fetchall():
            db_object = UserGeneralAppliesJobOpeningModel()
            db_object.username = db_row[0]
            db_object.job_id = db_row[1]
            db_object.done_challenges = db_row[2]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find, id_to_find2):
        database_query = """SELECT * FROM user_general_applies_job_opening WHERE username = '{0}' AND job_id = '{1}'; """.format(
            id_to_find, id_to_find2)
        cursor = self.query_database(database_query)
        from .user_general_applies_job_opening_models import UserGeneralAppliesJobOpeningModel
        list_of_db_objects = []
        for db_row in cursor.fetchall():
            db_object = UserGeneralAppliesJobOpeningModel()
            db_object.username = db_row[0]
            db_object.job_id = db_row[1]
            db_object.done_challenges = db_row[2]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM user_general_applies_job_opening
                            WHERE username = '{0}' AND job_id = '{1}';""".format(db_models.username, db_models.job_id)

        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
