from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    # __str__ 함수 쓰는 이유 : 클래스를 사용할 때 Book 클래스를 대표성을 띄는 키값을 반환하도록 개발자가 설정한 것. (PK로 하면 되는듯). 이거 안넣어두면 이상한 해시 넘버, 아이디 같은 값들이 나와서 알 수 없다.
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

