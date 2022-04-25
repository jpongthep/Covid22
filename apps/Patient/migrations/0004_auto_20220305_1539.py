# Generated by Django 3.2.12 on 2022-03-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0003_auto_20220305_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='symptom',
            field=models.TextField(blank=True, null=True, verbose_name='อาการ'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_day',
            field=models.DateField(null=True, verbose_name='วันเกิด'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency_mobile',
            field=models.CharField(max_length=20, null=True, verbose_name='เบอร์ฉุกเฉิน'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency_name',
            field=models.CharField(max_length=150, null=True, verbose_name='ผู้ติดต่อฉุกเฉิน'),
        ),
    ]
