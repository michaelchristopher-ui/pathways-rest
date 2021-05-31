from ..DBManager import DBManager


class UserCompanyDB(DBManager):
    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO user_company
        (company_id, username) VALUES ('{0}', '{1}');""".format(
            db_models.company_id,
            db_models.username
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE user_company SET
        company_id = '{0}',
        username = '{1}'
        WHERE username = '{1}';""".format(
            db_models.company_id,
            db_models.username
        )
        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM  user_company; """
        cursor = self.query_database(database_query)
        from .user_company_models import UserCompanyModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = UserCompanyModel()
            db_object.company_id = db_row[0]
            db_object.username = db_row[1]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find):
        database_query = """SELECT * FROM  user_company
        WHERE username = '{0}'; """.format(id_to_find)
        cursor = self.query_database(database_query)
        from .user_company_models import UserCompanyModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = UserCompanyModel()
            db_object.company_id = db_row[0]
            db_object.username = db_row[1]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM user_company
        WHERE username = '{0}'; """.format(db_models.username)
        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
