from .importer_modules import *
from .importer_model_serializers import AllUsersSerializers, AllUsersModel


@api_view(['GET'])
def all_users_list(request, format="None"):
    if request.method == 'GET':
        items = AllUsersModel.db_objects.get_all_data_from_database()
        serializer = AllUsersSerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def all_users_insert(request, format=None):
    serializer = AllUsersSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def all_users_detail(request, id, format=None):

    all_users = AllUsersModel.db_objects.get_data_from_database_by_id(id)

    if all_users is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AllUsersSerializers(all_users)
        return Response(serializer.data)
    if request.method == 'DELETE':

        all_users.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
