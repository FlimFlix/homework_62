# Generated by Django 2.1.7 on 2019-03-04 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Hall')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Hall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(to='webapp.Category'),
        ),
    ]