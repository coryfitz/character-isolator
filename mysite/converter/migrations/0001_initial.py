# Generated by Django 3.1.7 on 2022-01-23 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FilteredCharacters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtered_chars', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FilterPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.CharField(choices=[('NO', 'None'), ('F250', 'First 250'), ('F500', 'First 500'), ('F750', 'First 750'), ('F1000', 'First 1000')], default='NO', max_length=100)),
            ],
        ),
    ]
