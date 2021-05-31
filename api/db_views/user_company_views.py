from .importer_modules import *
from .importer_model_serializers import UserCompanySerializers, UserCompanyModel


@api_view(['GET'])
def user_company_list(request, format=None):
    if request.method == 'GET':
        items = UserCompanyModel.db_objects.get_all_data_from_database()
        serializer = UserCompanySerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_company_insert(request, format=None):
    serializer = UserCompanySerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def user_company_detail(request, id, format=None):

    user_companys = UserCompanyModel.db_objects.get_data_from_database_by_id(
        id)

    if user_companys is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserCompanySerializers(user_companys)
        return Response(serializer.data)
    if request.method == 'DELETE':
        user_companys.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
