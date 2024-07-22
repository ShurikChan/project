from django.db import models

# Create your models here.
class PerevalUsers(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)

    class Meta:
        db_table = 'pereval_users'
        constraints = [models.UniqueConstraint(fields=['email', 'phone'], name='unique_email_phone')]

class PerevalCoords(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)
    height = models.IntegerField()

    class Meta:
        db_table = 'pereval_coords'

class PerevalLevels(models.Model):
    id = models.AutoField(primary_key=True)
    winter = models.CharField(max_length=20)
    summer = models.CharField(max_length=20)
    autumn = models.CharField(max_length=20)
    spring = models.CharField(max_length=20)

    class Meta:
        db_table = 'pereval_levels'

class PerevalAdded(models.Model):
    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(auto_now_add=True)
    beautyTitle = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    other_titles = models.CharField(max_length=200)
    connect = models.CharField(max_length=200)
    add_time = models.DateTimeField()
    id_user = models.ForeignKey(PerevalUsers, on_delete=models.CASCADE)
    id_coords = models.ForeignKey(PerevalCoords, on_delete=models.CASCADE)
    id_levels = models.ForeignKey(PerevalLevels, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='new')

    class Meta:
        db_table = 'pereval_added'


class PerevalImages(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'pereval_images'


class PerevalAddedImages(models.Model):
    id = models.AutoField(primary_key=True)
    id_added = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    id_image = models.ForeignKey(PerevalImages, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pereval_added_images'