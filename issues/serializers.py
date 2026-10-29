
from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    reported_by = serializers.ReadOnlyField(
        source='reported_by.username'
    )

    vote_count = serializers.SerializerMethodField()

    def get_vote_count(self, obj):
        return obj.votes.count()

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'category',
            'image',
            'location',
            'status',
            'reported_by',
            'created_at',
            'updated_at',
            'vote_count',
        ]

        read_only_fields = [
            'id',
            'reported_by',
            'status',
            'created_at',
            'updated_at',
            'vote_count',
        ]
