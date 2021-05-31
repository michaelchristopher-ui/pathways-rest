from ..DBManager import DBManager


class AllUsersDB(DBManager):
    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO all_users
        (username, email, user_password, type_of_user)
        VALUES ('{0}', '{1}', '{2}', '{3}');""".format(
            db_models.username,
            db_models.email,
            db_models.user_password,
            db_models.type_of_user
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE all_users SET
        username = '{0}',
        email = '{1}',
        user_password = '{2}',
        type_of_user = '{3}'
        WHERE username = '{0}';""".format(
            db_models.username,
            db_models.email,
            db_models.user_password,
            db_models.type_of_user
        )
        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM all_users; """
        cursor = self.query_database(database_query)
        from .all_users_models import AllUsersModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = AllUsersModel()
            db_object.username = db_row[0]
            db_object.email = db_row[1]
            db_object.user_password = db_row[2]
            db_object.type_of_user = db_row[3]
            list_of_db_objects.append(db_object)

            print("haha")
            print(db_object.username)

        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find):
        database_query = """SELECT *
        FROM all_users
        where username = '{0}'; """.format(id_to_find)
        cursor = self.query_database(database_query)
        from .all_users_models import AllUsersModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = AllUsersModel()
            db_object.username = db_row[0]
            db_object.email = db_row[1]
            db_object.user_password = db_row[2]
            db_object.type_of_user = db_row[3]
            list_of_db_objects.append(db_object)

        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM all_users
        WHERE username = '{0}';""".format(db_models.username)
        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
