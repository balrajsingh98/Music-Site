
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20160325_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
