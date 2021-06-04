from rest_framework import serializers


class CustomQuerySerializers(serializers.Serializer):
    task_title = serializers.CharField()
    data_related = serializers.CharField()
