from django.db import models
from accounts.models import User

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()

    total_score = models.IntegerField()
    severity = models.CharField(max_length=50)
    risk_flag = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)