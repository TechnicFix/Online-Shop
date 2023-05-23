from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=255)


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.SET_NULL, null=True, related_name='articles'),
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Textpreview')
    text = models.TextField(verbose_name='Текст статі')
    created_at = models.DateTimeField(verbose_name='Дата створення')
    updated_at = models.DateTimeField(verbose_name='Дата зміни')
    
    class Meta:
        verbose_name='Стаття'
        verbose_name_plural = 'Cтатті'
        ordering = ["-created_at"]
        

