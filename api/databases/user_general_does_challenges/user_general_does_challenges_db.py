from ..DBManager import DBManager


class UserGeneralDoesChallengesDB(DBManager):

    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO user_general_does_challenges
        (username, job_opening_id, order_number, data_related) VALUES ('{0}', '{1}', '{2}', '{3}');""".format(
            db_models.username,
            db_models.job_opening_id,
            db_models.order_number,
            db_models.data_related
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE user_general_does_challenges SET
        username = '{0}',
        job_opening_id = '{1}', order_number = '{2}', data_related = '{3}' WHERE username = '{0}' AND job_opening_id = '{1}' AND order_number = '{2}';""".format(
            db_models.username,
            db_models.job_opening_id,
            db_models.order_number,
            db_models.data_related
        )
        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM user_general_does_challenges; """
        cursor = self.query_database(database_query)
        from .user_general_does_challenges_models import UserGeneralDoesChallengesModel
        list_of_db_objects = []
        for db_row in cursor.fetchall():
            db_object = UserGeneralDoesChallengesModel()
            db_object.username = db_row[0]
            db_object.job_opening_id = db_row[1]
            db_object.order_number = db_row[2]
            db_object.data_related = db_row[3]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find, id_to_find2, id_to_find3):
        database_query = """SELECT * FROM user_general_does_challenges WHERE username = '{0}' AND job_opening_id = '{1}' AND order_number = '{2}'; """.format(
            id_to_find, id_to_find2, id_to_find3)
        cursor = self.query_database(database_query)
        from .user_general_does_challenges_models import UserGeneralDoesChallengesModel
        list_of_db_objects = []
        for db_row in cursor.fetchall():
            db_object = UserGeneralDoesChallengesModel()
            db_object.username = db_row[0]
            db_object.job_opening_id = db_row[1]
            db_object.order_number = db_row[2]
            db_object.data_related = db_row[3]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM user_general_applies_job_opening
                            WHERE WHERE username = '{0}' AND job_opening_id = '{1}' AND order_number = '{2}';""".format(db_models.username, db_models.job_id)

        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
