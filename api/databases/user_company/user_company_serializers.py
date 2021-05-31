from rest_framework import serializers
from .user_company_models import UserCompanyModel


class UserCompanySerializers(serializers.Serializer):
    company_id = serializers.CharField()
    username = serializers.CharField()

    def create(self, validated_data):
        db_object = UserCompanyModel()
        db_object.company_id = validated_data.get("company_id")
        db_object.username = validated_data.get("username")

        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.company_id = validated_data.get(
            "company_id", db_object.company_id)
        db_object.username = validated_data.get("username", db_object.username)
        db_object.init_save_data_to_database()
        return db_object
