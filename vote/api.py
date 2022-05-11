from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from authentication.permissions import ReadOnly
from comment.models import Comment, ActionType
from news.models import Submission
from authentication.permissions import Check_API_KEY_Auth
from vote.models import Vote
from vote.serializers import VoteSerializerSubm,VoteSerializerComm


class VoteSubmissionApiView(APIView):
    permission_classes = [Check_API_KEY_Auth | ReadOnly]

    def get_submission(self, submission_id):
        try:
            return Submission.objects.get(id=submission_id)
        except Submission.DoesNotExist:
            return None

    def post(self, request, id):

            act = ActionType.objects.get(name="Submission")
            user = request.user
            data = {
                'submission': id,
                'comment': None,
                'type': act.id,
                'user': user.id,
            }
            if User.objects.filter(id=user.id).exists():
                userVal = User.objects.get(id=user.id)
                if userVal is None:
                    return Response(
                        {"res": "User with this id does not exists"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                if(Submission.objects.filter(id=id).exists()):
                    subm = Submission.objects.get(id=id)
                    if(userVal == subm.author):
                        return Response(
                            {"res": "The User who posted the submission can't vote his own submission."},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    serializer = VoteSerializerSubm(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    if (Vote.objects.filter(submission=self.get_submission(id)).exists()):
                        return Response({"res: Vote already submitted."}, status=status.HTTP_409_CONFLICT)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        {"res": "Submission with that id doesn't exist!"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {"res": "User with that id doesn't exist!"},
                    status=status.HTTP_400_BAD_REQUEST
                )

    def delete(self, request, id):

        submission = self.get_submission(id)
        user = request.user

        if User.objects.filter(id=user.id).exists():
            userVal = User.objects.get(id=user.id)
            if userVal is None:
                return Response(
                    {"res": "User with this id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if submission is None:
                return Response(
                    {"res": "Submission with this id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not Vote.objects.filter(submission=submission,user=userVal).exists():
                return Response(
                    {"res": "Vote doesn't exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                vote = Vote.objects.get(submission=submission,user=userVal)
                vote.delete()
                return Response(
                    {"res": "Object deleted!"},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"res": "User with that id doesn't exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

class VoteCommentApiView(APIView):
    permission_classes = [Check_API_KEY_Auth | ReadOnly]
    def get_comment(self, comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return None

    def post(self, request, id):

        act = ActionType.objects.get(name="Comment")
        user = request.user
        data = {
            'submission': None,
            'comment': id,
            'type': act.id,
            'user': user.id,
        }
        if User.objects.filter(id=user.id).exists():
            userVal = User.objects.get(id=user.id)
            if userVal is None:
                return Response(
                    {"res": "User with this id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if(Comment.objects.filter(id=id).exists()):
                comment = Comment.objects.get(id=id)
                if (userVal == comment.user):
                    return Response(
                        {"res": "The User who pos   ted the comment can't vote his own comment."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                serializer = VoteSerializerComm(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                if (Vote.objects.filter(comment=self.get_comment(id)).exists()):
                    return Response({"res: Vote already submitted."}, status=status.HTTP_409_CONFLICT)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else :
                return Response(
                    {"res": "Comment with that id doesn't exist!"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                {"res": "User with that id doesn't exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id):

        comment = self.get_comment(id)
        user = request.user
        if User.objects.filter(id=user.id).exists():
            userVal = User.objects.get(id=user.id)
            if userVal is None:
                return Response(
                    {"res": "User with this id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if comment is None:
                return Response(
                    {"res": "Comment with this id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not Vote.objects.filter(comment=comment,user=userVal).exists():
                return Response(
                    {"res": "Vote doesn't exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                vote = Vote.objects.get(comment=comment,user=userVal)
                vote.delete()
                return Response(
                    {"res": "Object deleted!"},
                    status=status.HTTP_200_OK
                )
        else :
            return Response(
                {"res": "User with that id doesn't exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )














