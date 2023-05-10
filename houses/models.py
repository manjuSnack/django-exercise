from django.db import models

# Create your models here.
class House(models.Model):

    """ Model Definition for house    """

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)

"""
models.Model
: Model Class를 상속받을 때 사용

models.CharField()
: 글자 수를 제한주고자 할 때

max_length=숫자
: 최대 글자 수

models.PositiveIntegerField()
: 양수인 정수로만 값을 받을 때

models.TextField()
: 긴 글자를 가질 때

"""