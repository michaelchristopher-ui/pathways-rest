from rest_framework import serializers
from .user_general_applies_job_opening_models import UserGeneralAppliesJobOpeningModel


class UserGeneralAppliesJobOpeningSerializers(serializers.Serializer):
    username = serializers.CharField()
    job_id = serializers.CharField()
    done_challenges = serializers.CharField()

    def create(self, validated_data):
        db_object = UserGeneralAppliesJobOpeningModel()
        db_object.username = validated_data.get("username")
        db_object.job_id = validated_data.get("job_id")
        db_object.done_challenges = validated_data.get("done_challenges")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.username = validated_data.get("username", db_object.username)
        db_object.job_id = validated_data.get("job_id", db_object.job_id)
        db_object.done_challenges = validated_data.get(
            "done_challenges", db_object.done_challenges)
        db_object.init_save_data_to_database()
        return db_object
