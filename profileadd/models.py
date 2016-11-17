from django.db import models

# Create your models here.


class BroadInsightsConditions(models.Model):
    unique_id = models.CharField(max_length=10)
    rule_id = models.IntegerField()
    sub_rule_id = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    versions = models.CharField(max_length=10)
    priority = models.IntegerField(null=True)
    rule_title = models.CharField(max_length=20)
    derived = models.IntegerField(null=True)
    derived_from = models.CharField(max_length=20)
    dt_14764 = models.IntegerField(null=True)
    mt_25196 = models.IntegerField(null=True)
    mt_26007= models.IntegerField(null=True)
    mt_27905 = models.IntegerField(null=True)
    mt_28065 = models.IntegerField(null=True)
    condition_data = models.CharField(max_length=1000)
    insight = models.CharField(max_length=500)

    def __str__(self):
        return str(self.unique_id)+" Rule ID"+str(self.rule_id)
