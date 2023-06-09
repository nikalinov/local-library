# Generated by Django 4.2.1 on 2023-06-09 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_manipulate_authors', 'Can create, edit, and  delete authors'),)},
        ),
    ]
