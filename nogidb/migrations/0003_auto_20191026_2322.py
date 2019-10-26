# Generated by Django 2.2.6 on 2019-10-26 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nogidb', '0002_auto_20191022_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='メンバー画像'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name_kana',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='「名前（かな）」は、ひらがな・カタカナのみで空白を入れずに入力してください', regex='^[ぁ-んァ-ンー]+$')], verbose_name='名前（かな）'),
        ),
    ]
