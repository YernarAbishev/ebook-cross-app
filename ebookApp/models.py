from django.db import models
from datetime import datetime
from pytils.translit import slugify

class Genre(models.Model):
    genreName = models.CharField("Наименование жанра", max_length=255)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genreName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genreName)
        super().save(*args, **kwargs)


class Ebook(models.Model):
    title = models.CharField("Наименование книги", max_length=255)
    author = models.CharField("Автор", max_length=255)
    year = models.IntegerField("Год выпуска")
    imageCover = models.ImageField("Обложка", upload_to="books/covers/")
    description = models.TextField("Описание")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    postDate = models.DateTimeField("Дата и время публикации", default=datetime.now)
    audioFile = models.FileField("Файл mp3", upload_to="books/audio/")
    isRecommended = models.BooleanField("Включить/отключить рекомендацию", default=False, blank=True, null=True)
    isChart = models.BooleanField("Включить/отключить чарт", default=False, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.title} - {self.author} - {self.year}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)