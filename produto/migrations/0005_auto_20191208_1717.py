# Generated by Django 2.2.6 on 2019-12-08 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20191208_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]