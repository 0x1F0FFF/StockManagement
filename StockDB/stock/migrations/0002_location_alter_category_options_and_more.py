# Generated by Django 4.2.15 on 2024-08-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='user',
        ),
    ]
