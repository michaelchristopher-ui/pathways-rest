from .importer_modules import *
from .importer_model_serializers import JobOpeningHasSuggestedCoursesModel, JobOpeningHasSuggestedCoursesSerializers


@api_view(['GET'])
def job_opening_has_suggested_courses_list(request, format=None):
    if request.method == 'GET':
        items = JobOpeningHasSuggestedCoursesModel.db_objects.get_all_data_from_database()
        serializer = JobOpeningHasSuggestedCoursesSerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def job_opening_has_suggested_courses_insert(request, format=None):
    serializer = JobOpeningHasSuggestedCoursesSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def job_opening_has_suggested_courses_detail(request, id, id2, format=None):

    job_opening_has_suggested_coursess = JobOpeningHasSuggestedCoursesModel.db_objects.get_data_from_database_by_id(
        id, id2)

    if job_opening_has_suggested_coursess is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = JobOpeningHasSuggestedCoursesSerializers(
            job_opening_has_suggested_coursess)
        return Response(serializer.data)
    if request.method == 'DELETE':
        job_opening_has_suggested_coursess.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
