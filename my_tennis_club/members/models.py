from django.db import models

class PhotoAlbum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Photo(models.Model):
  album = models.ForeignKey(PhotoAlbum, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='photos')
  caption = models.CharField(max_length=100, blank=True)
