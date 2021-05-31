from .importer_modules import *
from .importer_model_serializers import ExperienceModel, ExperienceSerializers


@api_view(['GET'])
def experience_list(request, format=None):
    if request.method == 'GET':
        items = ExperienceModel.db_objects.get_all_data_from_database()
        serializer = ExperienceSerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def experience_insert(request, format=None):
    serializer = ExperienceSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def experience_detail(request, id, id2, format=None):

    experiences = ExperienceModel.db_objects.get_data_from_database_by_id(
        id, id2)

    if experiences is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ExperienceSerializers(experiences)
        return Response(serializer.data)
    if request.method == 'DELETE':
        experiences.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
