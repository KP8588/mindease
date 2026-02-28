from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Assessment
from .serializers import AssessmentSerializer
from rest_framework.generics import ListAPIView

def calculate_severity(score):
    if score <= 4:
        return "Minimal"
    elif score <= 9:
        return "Mild"
    elif score <= 14:
        return "Moderate"
    elif score <= 19:
        return "Moderately Severe"
    else:
        return "Severe"


class SubmitAssessmentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AssessmentSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            total_score = sum(data.values())
            severity = calculate_severity(total_score)
            risk_flag = True if data['q9'] > 0 else False

            assessment = Assessment.objects.create(
                user=request.user,
                total_score=total_score,
                severity=severity,
                risk_flag=risk_flag,
                **data
            )

            return Response({
                "total_score": total_score,
                "severity": severity,
                "risk_flag": risk_flag
            })

        return Response(serializer.errors, status=400)
    

class AssessmentHistoryView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Assessment.objects.filter(user=self.request.user).order_by('-created_at')

    def list(self, request):
        assessments = self.get_queryset()

        data = [
            {
                "date": a.created_at,
                "total_score": a.total_score,
                "severity": a.severity,
                "risk_flag": a.risk_flag
            }
            for a in assessments
        ]

        return Response(data)