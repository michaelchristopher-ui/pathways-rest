from rest_framework import serializers
from .suggested_courses_models import SuggestedCoursesModel


class SuggestedCoursesSerializers(serializers.Serializer):
    name = serializers.CharField()
    link_to_course = serializers.CharField()
    course_id = serializers.CharField()

    def create(self, validated_data):
        db_object = SuggestedCoursesModel()
        db_object.name = validated_data.get("name")
        db_object.link_to_course = validated_data.get("link_to_course")
        db_object.course_id = validated_data.get("course_id")
        print("at serializer create")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        print("at serializer update")
        db_object.name = validated_data.get(
            "name", db_object.name)
        db_object.link_to_course = validated_data.get(
            "link_to_course", db_object.link_to_course)
        db_object.course_id = validated_data.get(
            "course_id", db_object.course_id)

        db_object.init_save_data_to_database()
        return db_object
