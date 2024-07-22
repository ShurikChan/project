from django.db import models
import datetime
# Create your models here.
class PerevalUsers(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)

    class Meta:
        db_table = 'pereval_users'
        constraints = [models.UniqueConstraint(fields=['email', 'phone'], name='unique_email_phone')]

class PerevalCoords(models.Model):
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)
    height = models.IntegerField()

    class Meta:
        db_table = 'pereval_coords'

class PerevalLevels(models.Model):
    winter = models.CharField(max_length=20, blank =True)
    summer = models.CharField(max_length=20, blank =True)
    autumn = models.CharField(max_length=20, blank =True)
    spring = models.CharField(max_length=20, blank =True)

    class Meta:
        db_table = 'pereval_levels'


class Pereval(models.Model):
    new = "new"
    pending = "pending"
    confirmed = "confirmed"
    rejected = "rejected"
    STATUS = [
        (new, 'новая'),
        (pending, 'в ожидании'),
        (confirmed, 'подтверждена'),
        (rejected, 'отклонена'),
    ]

    beautyTitle = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    other_titles = models.CharField(max_length=200)
    connect = models.CharField(max_length=200, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(PerevalUsers, on_delete=models.CASCADE)
    coord = models.ForeignKey(PerevalCoords, on_delete=models.CASCADE)
    level = models.ForeignKey(PerevalLevels, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default=new, blank=False)

    class Meta:
        db_table = 'pereval'



class PerevalImages(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE,  default=None)
    image = models.ImageField(upload_to='pereval_images/', null=True)

    class Meta:
        db_table = 'pereval_images'