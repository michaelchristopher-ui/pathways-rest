from rest_framework import serializers
from .all_users_models import AllUsersModel


class AllUsersSerializers(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    user_password = serializers.CharField()
    type_of_user = serializers.CharField()

    def create(self, validated_data):
        db_object = AllUsersModel()
        db_object.username = validated_data.get("username")
        db_object.email = validated_data.get("email")
        db_object.user_password = validated_data.get("user_password")
        db_object.type_of_user = validated_data.get("type_of_user")
        db_object.init_save_data_to_database()
        return db_object

    def update(self, db_object, validated_data):
        db_object.username = validated_data.get("username", db_object.username)
        db_object.email = validated_data.get("email", db_object.email)
        db_object.user_password = validated_data.get(
            "user_password", db_object.user_password)
        db_object.type_of_user = validated_data.get(
            "type_of_user", db_object.type_of_user)
        db_object.init_save_data_to_database()
        return db_object
