from .importer_modules import *
from .importer_model_serializers import SuggestedCoursesModel, SuggestedCoursesSerializers


@api_view(['GET'])
def suggested_courses_list(request, format=None):
    if request.method == 'GET':
        items = SuggestedCoursesModel.db_objects.get_all_data_from_database()
        serializer = SuggestedCoursesSerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def suggested_courses_insert(request, format=None):
    print("at views post")
    serializer = SuggestedCoursesSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def suggested_courses_detail(request, id, format=None):

    suggested_courses = SuggestedCoursesModel.db_objects.get_data_from_database_by_id(
        id)

    if suggested_courses is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SuggestedCoursesSerializers(suggested_courses)
        return Response(serializer.data)
    if request.method == 'DELETE':
        suggested_courses.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
