

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0009_auto_20200712_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_title', models.CharField(max_length=500)),
                ('playlist_logo', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.playlist'),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
