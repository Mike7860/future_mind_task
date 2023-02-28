from django.db import models
from PIL import Image as Img
from io import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
import pathlib
import os


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.ImageField('upload', upload_to='uploads/', default='uploads', height_field=None, width_field=None, max_length=100)
    title = models.CharField("title", max_length=128)
    width = models.IntegerField("width")
    height = models.IntegerField("height")

    def save(self, *args, **kwargs):
        if self.url:
            image = Img.open(self.url, 'r')
            size = (self.width, self.height)
            image = image.resize(size, Img.ANTIALIAS)
            img_extension = pathlib.Path(self.url.path).suffix
            upload_loc = os.path.split(self.url.path)
            new_loc = upload_loc[0] + "/uploads/" + self.title + img_extension
            image.save(new_loc)
            server_url = "/uploads/" + self.title + img_extension
            self.url = server_url

        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.id
