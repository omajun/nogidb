# Generated by Django 2.2.6 on 2019-10-27 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nogidb', '0004_auto_20191027_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='メンバー画像'),
        ),
    ]
