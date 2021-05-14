# Generated by Django 3.2.3 on 2021-05-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('order', 'title')},
        ),
        migrations.AddField(
            model_name='client',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='order',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
