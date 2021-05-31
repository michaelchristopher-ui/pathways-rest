from .importer_modules import *
from .importer_model_serializers import UserGeneralModel, UserGeneralSerializers


@api_view(['GET'])
def user_general_list(request, format=None):
    if request.method == 'GET':
        items = UserGeneralModel.db_objects.get_all_data_from_database()
        serializer = UserGeneralSerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_general_insert(request, format=None):
    serializer = UserGeneralSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def user_general_detail(request, id, format=None):

    user_generals = UserGeneralModel.db_objects.get_data_from_database_by_id(
        id)

    if user_generals is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserGeneralSerializers(user_generals)
        return Response(serializer.data)
    if request.method == 'DELETE':
        user_generals.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
