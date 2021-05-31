from rest_framework import serializers
from .challenges_models import ChallengesModel


class ChallengesSerializers(serializers.Serializer):
    task_title = serializers.CharField()
    task_type = serializers.CharField()
    data_related = serializers.CharField()
    job_opening_id = serializers.CharField()
    order_number = serializers.CharField()

    def create(self, validated_data):
        db_object = ChallengesModel()
        db_object.task_title = validated_data.get("task_title")
        db_object.task_type = validated_data.get("task_type")
        db_object.data_related = validated_data.get("data_related")
        db_object.job_opening_id = validated_data.get("job_opening_id")
        db_object.order_number = validated_data.get("order_number")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.task_title = validated_data.get(
            "task_title", db_object.task_title)
        db_object.task_type = validated_data.get(
            "task_type", db_object.task_type)
        db_object.data_related = validated_data.get(
            "data_related", db_object.data_related)
        db_object.job_opening_id = validated_data.get(
            "job_opening_id", db_object.job_opening_id)
        db_object.order_number = validated_data.get(
            "order_number", db_object.order_number)

        db_object.init_save_data_to_database()
        return db_object
