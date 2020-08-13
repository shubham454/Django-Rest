# Generated by Django 2.2.2 on 2020-06-10 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=50)),
                ('hospital_address', models.CharField(max_length=50)),
                ('hospital_bed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_gender', models.CharField(max_length=50)),
                ('doctor_experience', models.FloatField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Hospital')),
            ],
        ),
    ]
