from rest_framework import serializers
from .job_opening_models import JobOpeningModel


class JobOpeningSerializers(serializers.Serializer):
    # The variable name affects how it appears on the REST FRAMEWORK
    id = serializers.CharField()
    title = serializers.CharField()
    company = serializers.CharField()
    location = serializers.CharField()
    salary = serializers.CharField()
    job_description = serializers.CharField()
    username_of_creator = serializers.CharField()

    def create(self, validated_data):
        db_object = JobOpeningModel()
        db_object.id = validated_data.get("id")
        db_object.title = validated_data.get("title")
        db_object.company = validated_data.get("company")
        db_object.location = validated_data.get("location")
        db_object.salary = validated_data.get("salary")
        db_object.job_description = validated_data.get("job_description")
        db_object.username_of_creator = validated_data.get(
            "username_of_creator")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.id = validated_data.get("id", db_object.id)
        db_object.title = validated_data.get("title", db_object.title)
        db_object.company = validated_data.get("company", db_object.company)
        db_object.location = validated_data.get("location", db_object.location)
        db_object.salary = validated_data.get("salary", db_object.salary)
        db_object.job_description = validated_data.get(
            "job_description", db_object.job_description)
        db_object.username_of_creator = validated_data.get(
            "username_of_creator", db_object.username_of_creator)
        db_object.init_save_data_to_database()
        return db_object
