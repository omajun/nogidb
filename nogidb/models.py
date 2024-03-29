from django.db import models
from django.core import validators
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

import pandas as pd


class Member(models.Model):

    JOIN_CLASS_CHOICES = (
        (1, '1期生'),
        (2, '2期生'),
        (3, '3期生'),
        (4, '4期生'),
    )

    ACTIVE = 0
    GRADUATE = 1

    STATUS_CHOICES = (
        (ACTIVE, '活動中'),
        (GRADUATE, '卒業生'),
    )

    name = models.CharField('名前', max_length=50)

    name_kana = models.CharField('名前（かな）', max_length=50, validators=[validators.RegexValidator(
            regex=u'^[ぁ-んァ-ンー]+$', 
            message='「名前（かな）」は、ひらがな・カタカナのみで空白を入れずに入力してください')]
    )

    birthday = models.DateField(verbose_name='生年月日', auto_now=False, auto_now_add=False)

    join_class = models.PositiveIntegerField(verbose_name='加入時期', choices=JOIN_CLASS_CHOICES)

    status = models.PositiveIntegerField('活動状況', choices=STATUS_CHOICES)

    picture = models.ImageField(verbose_name='メンバー画像', null=True, upload_to='images/')

    thumbnail = ImageSpecField(source='picture', processors=[ResizeToFill(250,330)], format='JPEG')



    def __str__(self):
        return self.name

    def status_display(self):
        if self.status == 0:
            return '活動中'
        else:
            return '卒業生'

    def join_class_display(self):
        return '{}期生'.format(self.join_class)
    
    def age(self):
        today    = int(pd.to_datetime('today').strftime('%Y%m%d'))
        birthday = int(self.birthday.strftime('%Y%m%d'))
        return int((today - birthday) / 10000)

    
    class Meta:
        db_table = 'member'
        verbose_name_plural = 'メンバー'
