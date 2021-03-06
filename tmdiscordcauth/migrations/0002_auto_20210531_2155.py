# Generated by Django 3.2.3 on 2021-05-31 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmdiscordcauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discorduser',
            name='account_id',
        ),
        migrations.RemoveField(
            model_name='discorduser',
            name='display_name',
        ),
        migrations.AddField(
            model_name='discorduser',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='TrackmaniaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.BigIntegerField()),
                ('display_name', models.CharField(max_length=100)),
                ('linked_discord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmdiscordcauth.discorduser')),
            ],
        ),
    ]
