# Generated by Django 2.2.6 on 2019-10-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nogidb', '0003_auto_20191026_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(default='media/images/medamayaki.png', null=True, upload_to='images/', verbose_name='メンバー画像'),
        ),
    ]
