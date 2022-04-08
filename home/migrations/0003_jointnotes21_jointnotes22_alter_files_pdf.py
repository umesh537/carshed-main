# Generated by Django 4.0.1 on 2022-01-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='JointNotes21',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/joint_notes_2021_pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='JointNotes22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('supervisor', models.CharField(max_length=225)),
                ('pdf', models.FileField(upload_to='pdfs/joint_notes_2022_pdf/')),
            ],
        ),
        migrations.AlterField(
            model_name='files',
            name='pdf',
            field=models.FileField(upload_to='pdfs/kcs_layout/'),
        ),
    ]