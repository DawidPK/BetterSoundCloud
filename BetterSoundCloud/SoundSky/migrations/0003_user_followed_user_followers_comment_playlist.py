# Generated by Django 5.0.4 on 2024-04-24 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoundSky', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followed',
            field=models.ManyToManyField(blank=True, related_name='followed_rel', to='SoundSky.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers_rel', to='SoundSky.user'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoundSky.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoundSky.user')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('songs', models.ManyToManyField(to='SoundSky.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoundSky.user')),
            ],
            options={
                'verbose_name_plural': 'Playlists',
            },
        ),
    ]
