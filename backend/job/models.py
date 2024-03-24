from datetime import *
from django.db import models
from django.contrib.auth.models import User


from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point

# Create your models here.

class JobType(models.TextChoices):
    Permanent='Permanent'
    Temporary='Temporary'
    Internship='Internship'
    Voluntarily='Voluntarily'
    PartTime='Part Time'

class Education(models.TextChoices):
    HighSchool='High School Degree'
    AssociateDegree='Associate Degree'
    Bachelors='Bachelor Degree'
    Masters='Master Degree'
    Phd='Phd'

class Industry(models.TextChoices):
    Business='Business'
    IT='Information Technology'
    Finance='Finance'
    Telecommunication='Telecommuication'
    Education='Education/Training'
    Healthcare='Healthcare'
    HR='Human Resource'
    Aviation='Aviation'
    Sales='Sales'
    Accounting='Accounting'
    Management='Management'
    Others='Others'
    

class Experience(models.TextChoices):
    NewGraduate='New Graduate'
    OneYear='1 Year'
    TwoYear='2 Year'
    ThreeYearPlus='3 Year and Above'

def return_date_time():
    now=datetime.now()
    return now + timedelta(days=7)

class job(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    email=models.EmailField(null=True)
    address=models.CharField(max_length=256,null=True)
    jobType=models.CharField(
        max_length=32,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education=models.CharField(
        max_length=32,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry=models.CharField(
        max_length=32,
        choices=Industry.choices,
        default=Industry.IT
    )
    experience=models.CharField(
        max_length=32,
        choices=Experience.choices,
        default=Experience.NewGraduate
    )
    salary=models.IntField(default=1,validators=[MinValueValidator(1),MaxValueValidator(9999999999)])
    positions=models.IntegerField(default=1)
    company=models.CharField(max_length=100,null=True)
    point=gismodels.PointField(default=Point(0.0,0.0))
    deadline=models.DateTimeField(default=return_date_time)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    createdat=models.DateTimeField(auto_now_add=True)