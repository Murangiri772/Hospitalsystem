# Generated by Django 5.1.6 on 2025-03-03 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='YourEmail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Subject',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='YourName',
            new_name='subject',
        ),
    ]
