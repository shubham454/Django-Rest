from django.db import models


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=50)
    hospital_address = models.CharField(max_length=50)
    hospital_bed = models.IntegerField()

    def __str__(self):
        return self.hospital_name


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=50)
    doctor_gender = models.CharField(max_length=50)
    doctor_experience = models.FloatField()
    def __str__(self):
        return self.doctor_name