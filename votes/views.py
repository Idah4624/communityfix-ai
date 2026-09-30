from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from issues.models import Issue

from .models import Vote
from .serializers import VoteSerializer


class VoteCreateView(generics.CreateAPIView):

    queryset = Vote.objects.all()

    serializer_class = VoteSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(self, serializer):

        issue_id = self.kwargs.get('issue_id')

        try:
            issue = Issue.objects.get(id=issue_id)

        except Issue.DoesNotExist:
            raise ValidationError(
                'Issue does not exist.'
            )

        if Vote.objects.filter(
            user=self.request.user,
            issue=issue
        ).exists():

            raise ValidationError(
                'You have already voted for this issue.'
            )

        serializer.save(
            user=self.request.user,
            issue=issue
        )