# Generated by Django 3.1.1 on 2020-10-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='icon',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='votes_total',
            field=models.IntegerField(default=1, null=True),
        ),
    ]