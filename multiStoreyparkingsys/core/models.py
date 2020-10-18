from django.db import models

class Car(models.Model):
    slot = models.PositiveIntegerField(primary_key=True)
    color = models.CharField(max_length=128)
    r_no = models.CharField(max_length=128)

    def __str__(self):
        return "R.No."+": "+self.r_no+"Slot: "+self.slot
