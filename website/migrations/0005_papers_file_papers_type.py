# Generated by Django 4.2.4 on 2023-09-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_papers'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='file',
            field=models.FileField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='papers',
            name='type',
            field=models.CharField(choices=[('journal', 'Journal'), ('article', 'Article')], default=None, max_length=20),
            preserve_default=False,
        ),
    ]