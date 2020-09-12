# Generated by Django 3.1.1 on 2020-09-12 00:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0006_auto_20200906_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('urlImage', models.CharField(max_length=500)),
                ('publicIdImage', models.CharField(max_length=500)),
                ('pokemon', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pokedex.pokemon')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
