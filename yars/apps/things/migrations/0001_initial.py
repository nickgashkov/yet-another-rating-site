# Generated by Django 2.1.2 on 2018-10-27 13:59

from django.db import migrations, models
import django.db.models.deletion


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
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'thing',
                'verbose_name_plural': 'things',
            },
        ),
        migrations.CreateModel(
            name='ThingKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'thing kind',
                'verbose_name_plural': 'things kinds',
            },
        ),
        migrations.AddField(
            model_name='thing',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.ThingKind'),
        ),
    ]
