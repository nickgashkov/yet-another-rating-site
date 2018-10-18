# Generated by Django 2.1.2 on 2018-10-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'thing',
                'verbose_name_plural': 'things',
            },
        ),
    ]
