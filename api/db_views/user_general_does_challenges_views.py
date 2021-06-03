from .importer_modules import *
from .importer_model_serializers import UserGeneralDoesChallengesModel, UserGeneralDoesChallengesSerializers


@api_view(['GET'])
def user_general_does_challenges_list(request, format=None):
    if request.method == 'GET':
        items = UserGeneralDoesChallengesModel.db_objects.get_all_data_from_database()
        serializer = UserGeneralDoesChallengesSerializers(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_general_does_challenges_insert(request, format=None):
    serializer = UserGeneralDoesChallengesSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print("data is valid")
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    print("data is not valid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def user_general_does_challenges_detail(request, id, id2, id3, format=None):

    user_general_does_challengess = UserGeneralDoesChallengesModel.db_objects.get_data_from_database_by_id(
        id, id2, id3)

    if user_general_does_challengess is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserGeneralDoesChallengesSerializers(
            user_general_does_challengess)
        return Response(serializer.data)
    if request.method == 'DELETE':
        user_general_does_challengess.init_delete_data_from_database()
        return HttpResponse(status=status.HTTP_200_OK)
