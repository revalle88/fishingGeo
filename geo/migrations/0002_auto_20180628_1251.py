# Generated by Django 2.0.5 on 2018-06-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='pounds',
        ),
        migrations.AddField(
            model_name='pound',
            name='fishes',
            field=models.ManyToManyField(to='geo.Fish'),
        ),
    ]