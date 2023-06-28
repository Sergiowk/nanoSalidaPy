from django.db import models

# Everytime that we do modifications in the models:
# We will need to delete the migrations folder 
# and execute: 
# python manage.py makemigrations drivers
# python manage.py migrate

# In case we modify a model and we have problems we can:
# Delete db.sqlite3 file
# And create again the admin user:
# python manage.py createsuperuser


# Create your models here.
class Drivers(models.Model):
    name=models.CharField(max_length=250)
    number=models.IntegerField()
    nationality=models.CharField(max_length=250)
    dob=models.DateField()
    comments=models.TextField()
    # Every model has another extra (hidden) field, which is the id

    def __str__(self):
        return self.name
