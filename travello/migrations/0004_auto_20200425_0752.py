# Generated by Django 3.0.2 on 2020-04-25 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_destination_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisrt_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('msg', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='destination',
            name='seller_fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='seller_lname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
