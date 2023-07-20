from django.db import models


# from config import host, user, password, db_name


class Articles(models.Model):
    title = models.CharField('Название', max_length=150)
    anons = models.CharField('Анонс', max_length=250)
    Full_text = models.TextField('Содержание') 
    data = models.DateField('Дата публикаций')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



