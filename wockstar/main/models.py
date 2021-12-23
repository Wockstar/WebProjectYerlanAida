from django.db import models

class Database(models.Model):
    clientid =  models.IntegerField('Client_id')
    firstname = models.CharField('Firstname',max_length=50)
    lastname = models.CharField('Lastname',max_length=50)
    age = models.IntegerField('Age')
    phone = models.CharField('Phone',max_length=50)
    email = models.CharField('Email',max_length=50)

    def __str__(self):
        return str(self.clientid)

    class Meta:
        verbose_name_plural = 'Клиенты'
