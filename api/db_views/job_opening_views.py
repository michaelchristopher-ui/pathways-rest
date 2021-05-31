from .importer_modules import *
from .importer_model_serializers import JobOpeningModel, JobOpeningSerializers


@api_view(['GET'])
def job_opening_list(request, format=None):
    if request.method == 'GET':
        items = JobOpeningModel.db_objects.get_all_data_from_database()
        serializer = JobOpeningSerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def job_opening_insert(request, format=None):
    serializer = JobOpeningSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def job_opening_detail(request, id, format=None):

    job_openings = JobOpeningModel.db_objects.get_data_from_database_by_id(id)

    if job_openings is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = JobOpeningSerializers(job_openings)
        return Response(serializer.data)
    if request.method == 'DELETE':
        job_openings.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
