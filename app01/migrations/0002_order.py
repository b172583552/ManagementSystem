# Generated by Django 4.2.2 on 2023-06-17 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('status', models.SmallIntegerField(choices=[(1, 'unpaid'), (2, 'paid')], default=1)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin')),
            ],
        ),
    ]
