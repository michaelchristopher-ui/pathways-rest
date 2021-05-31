from ..DBManager import DBManager


class ExperienceDB(DBManager):
    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO experience
        (order_no, username, position, company_name,
         start_date, end_date, position_description)
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'); """.format(
            db_models.order_no,
            db_models.username,
            db_models.position,
            db_models.company_name,
            db_models.start_date,
            db_models.end_date,
            db_models.position_description
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE experience SET
        order_no = '{0}',
        username = '{1}',
        position = '{2}',
        company_name = '{3}',
        start_date = '{4}',
        end_date = '{5}',
        position_description = '{6}'
        WHERE order_no = '{0}' AND username = '{1}';""".format(
            db_models.order_no,
            db_models.username,
            db_models.position,
            db_models.company_name,
            db_models.start_date,
            db_models.end_date,
            db_models.position_description
        )

        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM experience;"""
        cursor = self.query_database(database_query)
        from .experience_models import ExperienceModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = ExperienceModel()
            db_object.order_no = db_row[0]
            db_object.username = db_row[1]
            db_object.position = db_row[2]
            db_object.company_name = db_row[3]
            db_object.start_date = db_row[4]
            db_object.end_date = db_row[5]
            db_object.position_description = db_row[6]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find, id_to_find_2):
        database_query = """SELECT * FROM experience WHERE order_no = '{0}' AND username = '{1}';""".format(
            id_to_find,
            id_to_find_2
        )
        cursor = self.query_database(database_query)
        from .experience_models import ExperienceModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = ExperienceModel()
            db_object.order_no = db_row[0]
            db_object.username = db_row[1]
            db_object.position = db_row[2]
            db_object.company_name = db_row[3]
            db_object.start_date = db_row[4]
            db_object.end_date = db_row[5]
            db_object.position_description = db_row[6]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM experience
                            WHERE order_no = '{0}' AND username = '{1}';""".format(db_models.order_no, db_models.username)

        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
