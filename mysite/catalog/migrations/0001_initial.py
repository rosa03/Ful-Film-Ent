# Generated by Django 3.0.1 on 2019-12-20 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter title', max_length=200)),
                ('text', models.TextField(help_text='Enter a brief description', max_length=1000)),
                ('link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name', max_length=200)),
                ('text', models.TextField(help_text='Enter a brief description', max_length=1000)),
                ('socials', models.ManyToManyField(help_text='Enter Socials', to='catalog.Socials')),
            ],
        ),
    ]
