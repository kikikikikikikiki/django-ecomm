# Generated by Django 2.2.5 on 2020-02-16 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0003_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='image',
            name='status',
            field=models.CharField(choices=[('sh', 'Shirt'), ('le', 'Leggings'), ('ju', 'Jumper')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
