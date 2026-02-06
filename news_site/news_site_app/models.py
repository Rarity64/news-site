import os
from django.db import models
from django.conf import settings

# CharField - текстовое поле
# IntegerField - целочисленное поле
# FloatField - дробное поле
# DateField - поле даты

def news_text_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "news_texts")

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR1, "images")

def item_description_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "item_descriptions")

class News(models.Model):
    news_title = models.CharField(max_length = 100) # заголовок новости
    news_subtitle = models.CharField(max_length = 150) # подзаголовок
    pub_date = models.DateField() # дата публикации
    image = models.ImageField() # изображение к новости
    news_text = models.TextField() # текст новости
    author = models.CharField(max_length = 70) # автор новости

    def __str__(self):
        return self.news_title

class Item(models.Model):
    item_title = models.CharField(max_length = 100) # название товара
    price = models.IntegerField() # цена
    description = models.TextField() # описание
    photo = models.ImageField() # Фото товара
    material = models.CharField(max_length = 20) # материал
    clothing_type = models.CharField(max_length = 20) # вид одежды
    clothing_color = models.CharField(max_length = 20) # цвет одежды
    clothing_size = models.CharField(max_length = 3) # размер одежды

    def __str__(self):
        return f'{self.id}. {self.item_title}'
