# Generated by Django 2.0.5 on 2018-06-28 13:39

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_pound_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pound',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
    ]