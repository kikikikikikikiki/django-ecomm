# Generated by Django 2.2.5 on 2020-02-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0002_auto_20200216_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1)),
            ],
        ),
    ]
