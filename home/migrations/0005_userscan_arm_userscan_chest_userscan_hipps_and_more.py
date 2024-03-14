# Generated by Django 5.0.1 on 2024-03-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_userscan_submitdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscan',
            name='arm',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userscan',
            name='chest',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userscan',
            name='hipps',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userscan',
            name='inseem',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userscan',
            name='waist',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
    ]