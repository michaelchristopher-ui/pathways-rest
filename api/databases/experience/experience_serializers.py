from rest_framework import serializers
from .experience_models import ExperienceModel


class ExperienceSerializers(serializers.Serializer):
    order_no = serializers.CharField()
    username = serializers.CharField()
    position = serializers.CharField()
    company_name = serializers.CharField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    position_description = serializers.CharField()

    def create(self, validated_data):
        db_object = ExperienceModel()
        db_object.order_no = validated_data.get("order_no")
        db_object.username = validated_data.get("username")
        db_object.position = validated_data.get("position")
        db_object.company_name = validated_data.get("company_name")
        db_object.start_date = validated_data.get("start_name")
        db_object.end_date = validated_data.get("end_date")
        db_object.position_description = validated_data.get(
            "position_description")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.order_no = validated_data.get("order_no", db_object.order_no)
        db_object.username = validated_data.get("username", db_object.username)
        db_object.position = validated_data.get("position", db_object.position)
        db_object.company_name = validated_data.get(
            "company_name", db_object.company_name)
        db_object.start_date = validated_data.get(
            "start_name", db_object.start_date)
        db_object.end_date = validated_data.get("end_date", db_object.end_date)
        db_object.position_description = validated_data.get(
            "position_description", db_object.position_description)
        db_object.init_save_data_to_database()
        return db_object
