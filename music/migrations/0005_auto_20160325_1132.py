
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='playlist_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
