from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)
    icd10_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class DiseaseRecord(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='records')
    district = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    average_age = models.FloatField()
    cases = models.IntegerField()
    record_date = models.DateField()
    source = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.disease.name} - {self.district} - {self.record_date}"
