# Generated by Django 5.0.3 on 2024-04-03 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_color_varient_cartitems_color_variant_and_more'),
        ('products', '0006_rename_colorvariant_colorvarient_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ColorVarient',
            new_name='ColorVariant',
        ),
        migrations.RenameModel(
            old_name='SizeVarient',
            new_name='SizeVariant',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='color_varient',
            new_name='color_variant',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='size_varient',
            new_name='size_variant',
        ),
    ]
