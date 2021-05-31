from .importer_modules import *
from .importer_model_serializers import CompanyModel, CompanySerializers


@api_view(['GET'])
def company_list(request, format=None):
    if request.method == 'GET':
        items = CompanyModel.db_objects.get_all_data_from_database()
        serializer = CompanySerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def company_insert(request, format=None):
    serializer = CompanySerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def company_detail(request, id, format=None):

    companys = CompanyModel.db_objects.get_data_from_database_by_id(id)

    if companys is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CompanySerializers(companys)
        return Response(serializer.data)
    if request.method == 'DELETE':
        companys.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
