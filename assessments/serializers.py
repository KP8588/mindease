from rest_framework import serializers
from .models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = [
            'q1','q2','q3','q4','q5',
            'q6','q7','q8','q9'
        ]