from .importer_modules import *
from .importer_model_serializers import ChallengesModel, ChallengesSerializers


@api_view(['GET'])
def challenges_list(request, format=None):
    if request.method == 'GET':
        items = ChallengesModel.db_objects.get_all_data_from_database()
        serializer = ChallengesSerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def challenges_insert(request, format=None):
    serializer = ChallengesSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def challenges_detail(request, id, id2, format=None):

    challengess = ChallengesModel.db_objects.get_data_from_database_by_id(
        id, id2)

    if challengess is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ChallengesSerializers(challengess)
        return Response(serializer.data)
    if request.method == 'DELETE':
        challengess.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
