# Generated by Django 4.2.4 on 2023-09-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_papers_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]