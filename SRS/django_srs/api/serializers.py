from rest_framework import serializers
from students.models import StudentShiftInfo


class ResultInfoSerializer(serializers.Serializer):
    """Serializer for student result information."""

    board = serializers.CharField(max_length=12)
    roll = serializers.IntegerField()


class StudentInfoSerializer(serializers.ModelSerializer):
    """Serializer for student shift information."""

    class Meta:
        model = StudentShiftInfo
        fields = '__all__'
