from ..DBManager import DBManager


class CompanyDB(DBManager):
    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO company
        (id, company_name, company_description, size,
         avg_processing_time, industry, location)
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');""".format(
            db_models.id,
            db_models.company_name,
            db_models.company_description,
            db_models.size,
            db_models.avg_processing_time,
            db_models.industry,
            db_models.location
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE company SET
        id = '{0}',
        company_name = '{1}'
        company_description = '{2}',
        size = '{3}',
        avg_processing_time = '{4}',
        industry = '{5}',
        location = '{6}'
        WHERE id = '{0}';
        """.format(
            db_models.id,
            db_models.company_name,
            db_models.company_description,
            db_models.size,
            db_models.avg_processing_time,
            db_models.industry,
            db_models.location
        )

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM company; """
        cursor = self.query_database(database_query)
        from .company_models import CompanyModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = CompanyModel()
            db_object.id = db_row[0]
            db_object.company_name = db_row[1]
            db_object.company_description = db_row[2]
            db_object.size = db_row[3]
            db_object.avg_processing_time = db_row[4]
            db_object.industry = db_row[5]
            db_object.location = db_row[6]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find):
        database_query = """SELECT * FROM company WHERE id  = '{0}'; """.format(
            id_to_find)
        cursor = self.query_database(database_query)
        from .company_models import CompanyModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = CompanyModel()
            db_object.id = db_row[0]
            db_object.company_name = db_row[1]
            db_object.company_description = db_row[2]
            db_object.size = db_row[3]
            db_object.avg_processing_time = db_row[4]
            db_object.industry = db_row[5]
            db_object.location = db_row[6]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM company WHERE id = '{0}';""".format(
            db_models.id)

        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
