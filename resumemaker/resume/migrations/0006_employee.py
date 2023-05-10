# Generated by Django 4.1.7 on 2023-04-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_delete_technology'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('tools', models.CharField(max_length=255)),
                ('coding', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('professional_summary', models.CharField(max_length=1000)),
                ('employee_status', models.CharField(max_length=10)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]