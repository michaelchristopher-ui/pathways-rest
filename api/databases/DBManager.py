from django.db import connection


class DBManager():

    def set_database_path(self):
        print("Executing SQL command to SET SEARCH PATH...")
        cursor = connection.cursor()
        database_query = "SET SEARCH_PATH TO pathways_app_database;"
        print(database_query)
        cursor.execute(database_query)
        print("SET SEARCH_PATH success...")
        return

    def query_database(self, database_query):
        print("Executing SQL command to query the database...")

        DBManager.set_database_path(self)
        cursor = connection.cursor()
        print(database_query)
        cursor.execute(database_query)
        print("Execution to query data success")
        return cursor
