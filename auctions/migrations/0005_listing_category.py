# Generated by Django 4.0.3 on 2022-03-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_remove_bid_currentlisting_bid_currentlisting'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(default=True, max_length=64),
            preserve_default=False,
        ),
    ]