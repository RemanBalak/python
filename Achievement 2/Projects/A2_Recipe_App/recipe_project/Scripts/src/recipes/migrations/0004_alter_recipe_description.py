# Generated by Django 4.2.5 on 2023-09-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]