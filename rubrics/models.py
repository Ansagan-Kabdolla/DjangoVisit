from django.shortcuts import reverse
from datetime import datetime
from django.db import models
from django.db.models import Q

class ArticleManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            #or_lookup = (Q(title__in = query) | Q(content__in = query) | Q(address__in = query))
            try:
                qs = qs.filter(Q(title__icontains = query) | Q(content__icontains = query) | Q(short_description__icontains = query) | Q(address__icontains = query))
            except:
                qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(short_description__icontains = query))
        return qs

class Cities(models.Model):
    name = models.CharField(max_length=50,verbose_name='Название')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class TypesEat(models.Model):
    name = models.CharField(max_length=50,verbose_name='Название')
    slug = models.SlugField(max_length=70, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тип (Где покушать)'
        verbose_name_plural = 'Типы (Где покушать)'

class TypesGo(models.Model):
    name = models.CharField(max_length=50,verbose_name='Название')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тип (Куда сходить)'
        verbose_name_plural = 'Типы (Куда сходить)'

class TypesStay(models.Model):
    name = models.CharField(max_length=50,verbose_name='Название')
    slug = models.SlugField(max_length=70, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тип (Где остановиться)'
        verbose_name_plural = 'Типы (Где остановиться)'

class EatPhotos(models.Model):
    name = models.ForeignKey('Eat',on_delete=models.CASCADE,verbose_name='Рубрика',related_name='gallery')
    images = models.FileField(upload_to='gallery',verbose_name='Фотографии')
    def __str__(self):
        return str(self.name)

class Eat(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название')
    type = models.ForeignKey(TypesEat, on_delete=models.CASCADE, verbose_name='Тип', related_name='Eat')
    date = models.DateTimeField(default=datetime.now)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE,null=True,blank=True, verbose_name='Город', related_name='Eat')
    price = models.IntegerField(verbose_name='Цена')
    short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    content = models.TextField(null=True,blank=True,verbose_name='Контент')
    thumbnail = models.FileField(upload_to='thumbnail/',verbose_name='Главное фото')
    address = models.CharField(max_length=100,verbose_name='Адрес')
    phone = models.CharField(max_length=100,verbose_name='Телефон')
    site = models.SlugField(max_length=50,null=True,blank=True,verbose_name='Сайт')
    mail = models.CharField(max_length=50,null=True,blank=True,verbose_name='Эл.почта')
    inst = models.CharField(max_length=50,null=True,blank=True,verbose_name='Инстаграмм')
    fb = models.CharField(max_length=50,null=True,blank=True,verbose_name='Феисбук')
    vk = models.CharField(max_length=50,null=True,blank=True,verbose_name='Вконтакте')
    latitude = models.DecimalField(max_digits=19,decimal_places=15,verbose_name='Ширина')
    longitude = models.DecimalField(max_digits=19,decimal_places=15,verbose_name='Долгота')
    slug = models.SlugField(max_length=70, unique=True, blank=True, null=True)
    objects = ArticleManager()
    def get_absolute_url(self):
        return reverse('eat_detail', args=[str(self.id)])
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Где покушать'
        verbose_name_plural = 'Где покушать'

class GoPhotos(models.Model):
    name = models.ForeignKey('Go',on_delete=models.CASCADE,verbose_name='Рубрика',related_name='gallery')
    images = models.FileField(upload_to='gallery', verbose_name='Фотографии')
    def __str__(self):
        return str(self.name)

class Go(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    type = models.ForeignKey(TypesGo, on_delete=models.CASCADE, verbose_name='Тип', related_name='Go')
    city = models.ForeignKey(Cities,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Город',related_name='Go')
    date = models.DateTimeField(default=datetime.now)
    short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    content = models.TextField(null=True,blank=True,verbose_name='Контент')
    thumbnail = models.FileField(upload_to='thumbnail/', verbose_name='Главное фото')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.CharField(max_length=100,null=True,blank=True, verbose_name='Телефон')
    slug = models.SlugField(max_length=70, unique=True, blank=True, null=True)
    objects = ArticleManager()
    def get_absolute_url(self):
        return reverse('go_detail', args=[str(self.id)])
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Куда сходить'
        verbose_name_plural = 'Куда сходить'



class StayPhoto(models.Model):
    name = models.ForeignKey('Stay', on_delete=models.CASCADE, verbose_name='Рубрика', related_name='gallery')
    images = models.FileField(upload_to='gallery', verbose_name='Фотографии')
    def __str__(self):
        return str(self.name)

class Stay(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    type = models.ForeignKey(TypesStay, on_delete=models.CASCADE, verbose_name='Тип', related_name='Stay')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Город', related_name='Stay')
    date = models.DateTimeField(default=datetime.now)
    price = models.IntegerField(verbose_name='Цена')
    stars = models.IntegerField(null=True,blank=True,verbose_name='Количество звезд')
    short_description = models.TextField(null=True,blank=True,verbose_name='Краткое описание')
    content = models.TextField(null=True,blank=True,verbose_name='Контент')
    thumbnail = models.FileField(upload_to='thumbnail/', verbose_name='Главное фото')
    address = models.CharField(max_length=100,verbose_name='Адрес')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    site = models.SlugField(max_length=50,null=True,blank=True, verbose_name='Сайт')
    mail = models.CharField(max_length=50,null=True,blank=True, verbose_name='Эл.почта')
    inst = models.CharField(max_length=50,null=True,blank=True, verbose_name='Инстаграмм')
    fb = models.CharField(max_length=50,null=True,blank=True, verbose_name='Феисбук')
    vk = models.CharField(max_length=50,null=True,blank=True, verbose_name='Вконтакте')
    latitude = models.DecimalField(max_digits=19, decimal_places=15, verbose_name='Ширина')
    longitude = models.DecimalField(max_digits=19, decimal_places=15, verbose_name='Долгота')
    isActive = models.BooleanField(default=True,verbose_name='Активно')
    isTop = models.BooleanField(default=False,verbose_name='Топ')
    slug = models.SlugField(max_length=70, unique=True, blank=True, null=True)
    objects = ArticleManager()
    def get_absolute_url(self):
        return reverse('stay_detail', args=[str(self.id)])
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Где остановиться'
        verbose_name_plural = 'Где остановиться'



class ReviewsEat(models.Model):
    rubric = models.ForeignKey(Eat,on_delete=models.CASCADE,related_name='reviews',verbose_name='Rubric')
    name = models.CharField(max_length=100,verbose_name='Имя')
    email = models.CharField(max_length=100,unique=True,verbose_name='Email')
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв(Где поесть)'
        verbose_name_plural = 'Отзывы(Где поесть)'

class ReviewsStay(models.Model):
    rubric = models.ForeignKey(Stay, on_delete=models.CASCADE,related_name='reviews', verbose_name='Rubric')
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100 ,verbose_name='Email')
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв(Где остановиться)'
        verbose_name_plural = 'Отзывы(Где остановиться)'


class News(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок')
    thumbnail = models.FileField(upload_to='thumbnail_news/',null=True,blank=True, verbose_name='Главное фото')
    short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=70,unique=True,blank=True,null=True)
    objects = ArticleManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.slug)])
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Akmola(models.Model):
    title = models.CharField(max_length=100,verbose_name=' Заголовок')
    thumbnail = models.FileField(upload_to='thumbnail_akmola',null=True,blank=True, verbose_name='Главное фото')
    short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=50,unique=True)
    objects = ArticleManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('akmola_detail', args=[str(self.slug)])
    class Meta:
        verbose_name = 'Об области'
        verbose_name_plural = 'Об области'

class Events(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок')
    thumbnail = models.FileField(upload_to='thumbnail_events',null=True,blank=True, verbose_name='Главное фото')
    short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    address = models.CharField(max_length=200,verbose_name='Адрес')
    date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=50, unique=True)

    objects = ArticleManager()
    def __str__(self):
        return self.title
    #def get_absolute_url(self):
    #    return reverse('event_detail', args=[str(self.slug)])
    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

class Tours(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    thumbnail = models.FileField(upload_to='thumbnail_tours', null=True, blank=True, verbose_name='Главное фото')
    short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=50, unique=True)

    objects = ArticleManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('tours_detail', args=[str(self.slug)])
    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class Tourists(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    thumbnail = models.FileField(upload_to='thumbnail_tourists', null=True, blank=True, verbose_name='Главное фото')
    short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=50, unique=True)

    objects = ArticleManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('tourists_detail', args=[str(self.slug)])
    class Meta:
        verbose_name = 'Туристу'
        verbose_name_plural = ' Туристу'

class StaticPages(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    thumbnail = models.FileField(upload_to='thumbnail_static_pages', null=True, blank=True, verbose_name='Главное фото')
    content = models.TextField(verbose_name='Контент')
    date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=50, unique=True)
    types_choice = (
        ('where_to_stay','Где остановиться'),
        ('where_to_eat','Где поесть'),
    )
    type = models.CharField(max_length=30,choices=types_choice,null=True, blank=True, verbose_name='Тип')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статичная страница'
        verbose_name_plural = 'Статичные страницы'


class Gallery(models.Model):
    number = models.IntegerField(default=0,verbose_name='id')
    title = models.CharField(max_length=30,verbose_name='Описание')
    images = models.FileField(upload_to='gallery_pages', null=True, blank=True, verbose_name='Галлерея фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'


class SidebarToStay(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    thumbnail = models.FileField(upload_to='thumbnail_tops_stay', null=True, blank=True, verbose_name='Главное фото')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='tops', verbose_name='Город')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('top_stay', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Сайдбар(где остановиться)'
        verbose_name_plural = 'Сайдбар(где остановиться)'


class NationalFoods(models.Model):
    title = models.CharField(max_length=50,verbose_name='')
    thumbnail = models.FileField(upload_to='thumbnail_national_foods', null=True, blank=True, verbose_name='Главное фото')
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Национальное блюдо'
        verbose_name_plural = 'Национальные блюда'
