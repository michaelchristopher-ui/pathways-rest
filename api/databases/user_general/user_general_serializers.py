from rest_framework import serializers
from .user_general_models import UserGeneralModel


class UserGeneralSerializers(serializers.Serializer):
    username = serializers.CharField()
    interest_subject = serializers.CharField()
    interest_job = serializers.CharField()
    profile_picture = serializers.CharField()
    short_description = serializers.CharField()

    def create(self, validated_data):
        db_object = UserGeneralModel()
        db_object.username = validated_data.get("username")
        db_object.interest_subject = validated_data.get("interest_subject")
        db_object.interest_job = validated_data.get("interest_job")
        db_object.profile_picture = validated_data.get("profile_picture")
        db_object.short_description = validated_data.get("short_description")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.username = validated_data.get("username", db_object.username)
        db_object.interest_subject = validated_data.get(
            "interest_subject", db_object.interest_subject)
        db_object.interest_job = validated_data.get(
            "interest_job", db_object.interest_job)
        db_object.profile_picture = validated_data.get(
            "profile_picture", db_object.profile_picture)
        db_object.short_description = validated_data.get(
            "short_description", db_object.short_description)
        db_object.init_save_data_to_database()
        return db_object
