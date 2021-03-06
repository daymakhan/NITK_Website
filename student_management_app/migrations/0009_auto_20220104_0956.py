# Generated by Django 3.2.10 on 2022-01-04 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0008_auto_20220104_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.courses'),
        ),
        migrations.AddField(
            model_name='students',
            name='session_year_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.sessionyearmodel'),
        ),
    ]
