# Generated by Django 2.1.5 on 2019-03-07 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=255)),
                ('eventlocation', models.CharField(max_length=255)),
                ('eventdate', models.DateField()),
                ('eventtime', models.TimeField()),
                ('eventdescription', models.TextField()),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=255)),
                ('movieyear', models.CharField(max_length=255)),
                ('moviebudget', models.CharField(max_length=255)),
                ('moviedescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewtitle', models.CharField(max_length=255)),
                ('reviewdate', models.DateField()),
                ('reviewrating', models.SmallIntegerField()),
                ('reviewtext', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Movie')),
            ],
            options={
                'db_table': 'moviereview',
            },
        ),
        migrations.CreateModel(
            name='MovieType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=255)),
                ('typedescription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'movietype',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producername', models.CharField(max_length=255)),
                ('directorname', models.CharField(max_length=255)),
                ('productionlocation', models.CharField(max_length=255)),
                ('productionurl', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'production',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='movietype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movieapp.MovieType'),
        ),
        migrations.AddField(
            model_name='movie',
            name='production',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movieapp.Production'),
        ),
    ]
