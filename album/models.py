from django.db import models
from nogidb.models import Member


class Image(models.Model):
    picture = models.ImageField('画像', upload_to='images/')
    name = models.ForeignKey(verbose_name='名前', to=Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name
    
    class Meta:
        db_table = 'image'
        verbose_name_plural = 'メンバー画像'
    