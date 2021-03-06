# Generated by Django 4.0.4 on 2022-05-24 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Absentdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates_of_absent', models.DateField(blank=True, null=True)),
                ('day', models.CharField(blank=True, max_length=100, null=True)),
                ('no_of_classes_absent', models.IntegerField(blank=True, default=0, null=True)),
                ('attendanceid', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ADMIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_taking_status', models.BooleanField(default=False)),
                ('course_syllabus', models.TextField()),
                ('course_name', models.CharField(choices=[('CSN221', 'CSN221'), ('CSN291', 'CSN291'), ('PHN005', 'PHN005'), ('MAN005', 'MAN005'), ('CEN105', 'CEN105')], default='1', max_length=10)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EE', 'EE'), ('ME', 'ME')], default='CSE', max_length=10)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=10)),
                ('day', models.CharField(choices=[('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY')], default='MONDAY', max_length=20)),
                ('time', models.CharField(choices=[('10:00-11:00', '10:00-11:00'), ('11:00-12:00', '11:00-12:00'), ('14:00-15:00', '14:00-15:00'), ('15:00-16:00', '15:00-16:00')], default='10:00-11:00', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='notices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passwordchangerid', models.IntegerField(blank=True, null=True)),
                ('passwordchangerotp', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profprofilepic', models.FileField(blank=True, null=True, upload_to=home.models.faculty_directory_path)),
                ('spamprofilepic', models.FileField(blank=True, null=True, upload_to='spam_faculty_images/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spamprofilepic', models.FileField(blank=True, null=True, upload_to='spam_student_images/')),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=2)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EE', 'EE'), ('ME', 'ME')], default='CSE', max_length=5)),
                ('studprofilepic', models.FileField(blank=True, null=True, upload_to=home.models.student_directory_path)),
                ('courses', models.ManyToManyField(to='home.course')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('answered_status', models.BooleanField(default=False)),
                ('send_status', models.IntegerField()),
                ('from_prof', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.professor')),
                ('from_stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student')),
                ('to_adm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.admin')),
                ('to_course', models.ManyToManyField(to='home.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.professor'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended_classes_count', models.IntegerField(blank=True, null=True)),
                ('total_classes_count', models.IntegerField(blank=True, null=True)),
                ('attended_status', models.BooleanField(default=False)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('limits', models.IntegerField(default=2)),
                ('absentdates', models.ManyToManyField(to='home.absentdates')),
                ('cour', models.ManyToManyField(to='home.course')),
                ('stud', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]
