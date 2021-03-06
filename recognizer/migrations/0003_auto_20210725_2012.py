# Generated by Django 3.2.5 on 2021-07-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognizer', '0002_auto_20210724_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='board_img',
            field=models.ImageField(default=None, upload_to='board_img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='board_matrix_abbr',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='board_matrix_unicode',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='fen',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
