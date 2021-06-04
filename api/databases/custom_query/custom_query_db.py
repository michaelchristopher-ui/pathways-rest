from ..DBManager import DBManager


class CustomQueryDB(DBManager):
    def __init__(self):
        pass

    def get_data_from_database_by_id(self, id_to_find):
        database_query = """select A.task_title, A.data_related from challenges A inner join (select * from user_general_does_challenges where username = '{0}') B ON A.job_opening_id = B.job_opening_id AND A.order_number = B.order_number;""".format(
            id_to_find
        )
        cursor = self.query_database(database_query)
        list_of_db_objects = []
        from .custom_query_models import CustomQueryModel
        for db_row in cursor.fetchall():
            db_object = CustomQueryModel()
            db_object.task_title = db_row[0]
            db_object.data_related = db_row[1]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def query_database(self, database_query):
        return super().query_database(database_query)
