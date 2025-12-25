from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField()
    attendance_percentage = models.FloatField()
    absent_days = models.IntegerField()
    prediction = models.CharField(max_length=20)

    def __str__(self):
        return str(self.roll_no)


class UserSignIn(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    success = models.BooleanField(default=False)



    def __str__(self):
        return f"{self.username} - {'Success' if self.success else 'Failed'}"
   