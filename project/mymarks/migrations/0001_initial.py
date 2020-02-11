# Generated by Django 3.0.2 on 2020-02-10 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120, verbose_name='Имя')),
                ('mail', models.EmailField(default=0, max_length=254, verbose_name='E-mail')),
                ('school', models.IntegerField(default=0, verbose_name='Школа')),
                ('level', models.IntegerField(default=0, verbose_name='Класс')),
                ('password1', models.CharField(max_length=50, verbose_name='Пароль')),
                ('password2', models.CharField(max_length=50, verbose_name='Пароль2')),
                ('fiscul', models.BooleanField(default=False, verbose_name='Физ-ра')),
                ('lit', models.BooleanField(default=False, verbose_name='Литература')),
                ('algebra', models.BooleanField(default=False, verbose_name='Алгебра')),
                ('geomet', models.BooleanField(default=False, verbose_name='Геометрия')),
                ('history', models.BooleanField(default=False, verbose_name='История')),
                ('music', models.BooleanField(default=False, verbose_name='Музыка')),
                ('obg', models.BooleanField(default=False, verbose_name='ОБЖ')),
                ('paiting', models.BooleanField(default=False, verbose_name='Рисование')),
                ('russian', models.BooleanField(default=False, verbose_name='Рус-яз')),
                ('inostr', models.BooleanField(default=False, verbose_name='Ин-Яз')),
                ('technology', models.BooleanField(default=False, verbose_name='Технология')),
                ('geography', models.BooleanField(default=False, verbose_name='География')),
                ('biology', models.BooleanField(default=False, verbose_name='Биология')),
                ('itk', models.BooleanField(default=False, verbose_name='Информатика')),
                ('social', models.BooleanField(default=False, verbose_name='Обществознание')),
                ('drawing', models.BooleanField(default=False, verbose_name='Черчение')),
                ('physics', models.BooleanField(default=False, verbose_name='Физика')),
                ('chemistry', models.BooleanField(default=False, verbose_name='Химия')),
                ('fiscul_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Физ-ра--цель')),
                ('lit_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Литература--цель')),
                ('algebra_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Алгебра--цель')),
                ('geomet_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Геометрия--цель')),
                ('history_t', models.FloatField(blank=True, default=None, null=True, verbose_name='История--цель')),
                ('odg_t', models.FloatField(blank=True, default=None, null=True, verbose_name='ОБЖ--цель')),
                ('music_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Музыка--цель')),
                ('paiting_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Рисование--цель')),
                ('russian_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Рус-яз--цель')),
                ('inostr_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Ин-яз--цель')),
                ('technology_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Технология--цель')),
                ('geography_t', models.FloatField(blank=True, default=None, null=True, verbose_name='География--цель')),
                ('biology_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Биология--цель')),
                ('itk_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Информатика--цель')),
                ('social_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Обществознание--цель')),
                ('drawing_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Черчение--цель')),
                ('physics_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Физика--цель')),
                ('chemistry_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Химия--цель')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=0, verbose_name='Оценка')),
                ('reg', models.IntegerField(default=0, verbose_name='Коэффициент')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymarks.Students')),
            ],
        ),
    ]
