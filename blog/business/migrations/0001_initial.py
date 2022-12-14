# Generated by Django 4.1 on 2022-08-20 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('type_article', models.IntegerField(choices=[(0, 'Scientific'), (1, 'Publicity'), (2, 'Interview')])),
                ('content', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Public'), (1, 'Private')])),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='keyword_set', to='business.article')),
            ],
        ),
    ]
