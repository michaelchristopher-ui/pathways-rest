from rest_framework import serializers
from .company_models import CompanyModel


class CompanySerializers(serializers.Serializer):
    id = serializers.CharField()
    company_name = serializers.CharField()
    company_description = serializers.CharField()
    size = serializers.CharField()
    avg_processing_time = serializers.CharField()
    industry = serializers.CharField()
    location = serializers.CharField()

    def create(self, validated_data):
        db_object = CompanyModel()
        db_object.id = validated_data.get("id")
        db_object.company_name = validated_data.get("company_name")
        db_object.company_description = validated_data.get(
            "company_description")
        db_object.size = validated_data.get("size")
        db_object.avg_processing_time = validated_data.get(
            "avg_processing_time")
        db_object.industry = validated_data.get("industry")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.id = validated_data.get("id", db_object.id)
        db_object.company_name = validated_data.get(
            "company_name", db_object.company_name)
        db_object.company_description = validated_data.get(
            "company_description", db_object.company_description)
        db_object.size = validated_data.get("size", db_object.size)
        db_object.avg_processing_time = validated_data.get(
            "avg_processing_time", db_object.avg_processing_time)
        db_object.industry = validated_data.get("industry", db_object.industry)
        db_object.init_save_data_to_database()
        return db_object
