# Generated by Django 4.0.1 on 2022-02-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_newrake_coach_position_alter_newrake_unit_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMEMO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway', models.CharField(max_length=224)),
                ('date', models.DateField(max_length=100)),
                ('time', models.TimeField(max_length=100)),
                ('unit_no', models.BigIntegerField(max_length=500)),
                ('coach_no', models.IntegerField(max_length=100)),
                ('line_no', models.IntegerField(max_length=100)),
                ('rake_formation', models.BigIntegerField(max_length=224)),
                ('poh', models.DateField(max_length=100)),
                ('IA', models.DateField(max_length=100)),
                ('TI', models.DateField(max_length=100)),
                ('W', models.DateField(max_length=100)),
                ('M', models.DateField(max_length=100)),
                ('IC', models.DateField(max_length=100)),
                ('UST', models.DateField(max_length=100)),
                ('train_no', models.IntegerField(max_length=224)),
                ('report_by', models.CharField(max_length=224)),
                ('nature_of_defects', models.CharField(max_length=224)),
                ('repercussion', models.CharField(max_length=224)),
                ('place_of_failure', models.CharField(max_length=224)),
                ('failure_report', models.TextField(max_length=224)),
                ('report_signee', models.CharField(max_length=224)),
                ('investigation', models.TextField(max_length=224)),
                ('image', models.ImageField(upload_to='pdfs/ememo/')),
                ('investigation_signee', models.CharField(max_length=224)),
                ('remarks', models.TextField(max_length=224)),
            ],
        ),
    ]
