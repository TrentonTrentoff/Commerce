# Generated by Django 4.0.3 on 2022-03-28 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_listing_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('currentListing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchListing', to='auctions.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
