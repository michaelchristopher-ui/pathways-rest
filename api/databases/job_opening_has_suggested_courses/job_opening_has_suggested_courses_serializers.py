from rest_framework import serializers
from .job_opening_has_suggested_courses_models import JobOpeningHasSuggestedCoursesModel


class JobOpeningHasSuggestedCoursesSerializers(serializers.Serializer):

    job_opening_id = serializers.CharField()
    course_id = serializers.CharField()

    def create(self, validated_data):
        db_object = JobOpeningHasSuggestedCoursesModel()
        db_object.job_opening_id = validated_data.get("job_opening_id")
        db_object.course_id = validated_data.get("course_id")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.job_opening_id = validated_data.get(
            "job_opening_id", db_object.job_opening_id)
        db_object.course_id = validated_data.get(
            "course_id", db_object.course_id)
        db_object.init_save_data_to_database()
        return db_object
