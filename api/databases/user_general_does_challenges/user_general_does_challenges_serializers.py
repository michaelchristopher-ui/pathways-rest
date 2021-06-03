from rest_framework import serializers
from .user_general_does_challenges_models import UserGeneralDoesChallengesModel


class UserGeneralDoesChallengesSerializers(serializers.Serializer):
    username = serializers.CharField()
    job_opening_id = serializers.CharField()
    order_number = serializers.CharField()
    data_related = serializers.CharField()

    def create(self, validated_data):
        db_object = UserGeneralDoesChallengesModel()
        db_object.username = validated_data.get("username")
        db_object.job_opening_id = validated_data.get("job_opening_id")
        db_object.order_number = validated_data.get("order_number")
        db_object.data_related = validated_data.get("data_related")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.username = validated_data.get("username", db_object.username)
        db_object.job_opening_id = validated_data.get(
            "job_opening_id", db_object.job_opening_id)
        db_object.order_number = validated_data.get(
            "order_number", db_object.order_number)
        db_object.data_related = validated_data.get(
            "data_related", db_object.data_related)
        db_object.init_save_data_to_database()
        return db_object
