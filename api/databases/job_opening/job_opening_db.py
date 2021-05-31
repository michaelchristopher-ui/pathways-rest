from ..DBManager import DBManager


class JobOpeningDB(DBManager):
    def __init__(self):
        pass

    def insert_data_to_database(self, db_models):
        database_query = """INSERT INTO job_opening
            (id, title, company, location, salary, job_description, username_of_creator)
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');""".format(
            db_models.id,
            db_models.title,
            db_models.company,
            db_models.location,
            db_models.salary,
            db_models.job_description,
            db_models.username_of_creator
        )

        self.query_database(database_query)
        return

    def update_data_to_database(self, db_models):
        database_query = """UPDATE job_opening SET
            id = '{0}',
            title = '{1}',
            company = '{2}',
            location = '{3}',
            salary = '{4}',
            job_description = '{5}',
            username_of_creator = '{6}'
            WHERE id = '{0}';""".format(
            db_models.id,
            db_models.title,
            db_models.company,
            db_models.location,
            db_models.salary,
            db_models.job_description,
            db_models.username_of_creator
        )
        self.query_database(database_query)
        return

    def get_all_data_from_database(self):
        database_query = """SELECT * FROM job_opening; """
        cursor = self.query_database(database_query)
        from .job_opening_models import JobOpeningModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = JobOpeningModel()
            db_object.id = db_row[0]
            db_object.title = db_row[1]
            db_object.company = db_row[2]
            db_object.location = db_row[3]
            db_object.salary = db_row[4]
            db_object.job_description = db_row[5]
            db_object.username_of_creator = db_row[6]
            list_of_db_objects.append(db_object)
        return list_of_db_objects

    def get_data_from_database_by_id(self, id_to_find):
        database_query = """SELECT *
                            FROM job_opening
                            WHERE id = '{0}'; """.format(id_to_find)
        cursor = self.query_database(database_query)
        from .job_opening_models import JobOpeningModel
        list_of_db_objects = []

        for db_row in cursor.fetchall():
            db_object = JobOpeningModel()
            db_object.id = db_row[0]
            db_object.title = db_row[1]
            db_object.company = db_row[2]
            db_object.location = db_row[3]
            db_object.salary = db_row[4]
            db_object.job_description = db_row[5]
            db_object.username_of_creator = db_row[6]
            list_of_db_objects.append(db_object)
        return None if len(list_of_db_objects) == 0 else list_of_db_objects[0]

    def delete_data_from_database(self, db_models):
        database_query = """DELETE FROM job_opening
                            WHERE id = '{0}';""".format(db_models.id)

        self.query_database(database_query)
        return

    def query_database(self, database_query):
        return super().query_database(database_query)
