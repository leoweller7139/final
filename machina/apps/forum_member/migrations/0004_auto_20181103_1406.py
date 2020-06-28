# Generated by Django 2.1.2 on 2018-11-03 19:06

from django.db import migrations
import machina.apps.forum_member.abstract_models
import machina.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum_member', '0003_auto_20160227_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumprofile',
            name='avatar',
            field=machina.models.fields.ExtendedImageField(blank=True, null=True, upload_to=machina.apps.forum_member.abstract_models.get_profile_avatar_upload_to, verbose_name='Avatar'),
        ),
    ]
