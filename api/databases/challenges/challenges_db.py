from ..DBManager import DBManager


class ChallengesDB(DBManager):

    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO challenges
        (task_title, task_type, data_related,
         job_opening_id, order_number)
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');""".format(
            db_models.task_title,
            db_models.task_type,
            db_models.data_related,
            db_models.job_opening_id,
            db_models.order_number,
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE challenges SET
        task_title = '{0}'
        task_type = '{1}'
        data_related = '{2}'
        jobs_opening_id = '{3}'
        order_number = '{4}'
        WHERE jobs_opening_id = '{3}' AND order_number = '{4}'';""".format(
            db_models.task_title,
            db_models.task_type,
            db_models.data_related,
            db_models.job_opening_id,
            db_models.order_number,
        )
        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM challenges;"""
        cursor = self.query_database(database_query)
        from .challenges_models import ChallengesModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = ChallengesModel()
            db_object.task_title = db_row[0]
            db_object.task_type = db_row[1]
            db_object.data_related = db_row[2]
            db_object.job_opening_id = db_row[3]
            db_object.order_number = db_row[4]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find, id_to_find2):
        database_query = """SELECT *  
        FROM challenges WHERE job_opening_id = '{0}' AND order_number = '{1}';""".format(id_to_find, id_to_find2)
        cursor = self.query_database(database_query)
        from .challenges_models import ChallengesModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = ChallengesModel()
            db_object.task_title = db_row[0]
            db_object.task_type = db_row[1]
            db_object.data_related = db_row[2]
            db_object.job_opening_id = db_row[3]
            db_object.order_number = db_row[4]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM challenges WHERE job_opening_id = '{0}' AND order_number = '{1}';""".format(
            db_models.job_opening_id, db_models.order_number)
        self.query_database(database_query)
        return
