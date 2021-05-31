from django.db.utils import IntegrityError


class ModelManager():

    def init_save_data_to_database(self, db_objects):
        print("trying to insert/update data to database...")
        try:
            print("Trying to Insert data...")
            db_objects.insert_data_to_database(self)
            print("INSERT data success")
        except Exception as e:
            print(e)
            print("Data already exists, UPDATING data to database")
            db_objects.update_data_to_database(self)
            return

    def init_delete_data_from_database(self, db_objects):
        print("Trying to delete data from database")
        db_objects.delete_data_from_database(self)
        return
