# Generated by Django 3.0.2 on 2020-05-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0008_auto_20200507_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination1',
            name='link',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='destination2',
            name='link',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='destination3',
            name='link',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='destination4',
            name='link',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='destination5',
            name='link',
            field=models.URLField(max_length=300, null=True),
        ),
    ]
