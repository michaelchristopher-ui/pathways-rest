from .importer_modules import *
from .importer_model_serializers import CustomQuerySerializers, CustomQueryModel


@api_view(['GET'])
def custom_query_list_detail(request, id, format=None):
    custom_querys = CustomQueryModel.db_objects.get_data_from_database_by_id(
        id)

    if request.method == 'GET':
        serializer = CustomQuerySerializers(custom_querys, many=True)
        return Response(serializer.data)
