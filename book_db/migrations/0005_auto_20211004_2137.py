# Generated by Django 3.0.6 on 2021-10-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_db', '0004_auto_20211004_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.CharField(max_length=100, null=True),
        ),
    ]