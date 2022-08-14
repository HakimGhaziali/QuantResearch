# Generated by Django 4.1 on 2022-08-14 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Static',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_trade', models.IntegerField()),
                ('average_loss', models.IntegerField()),
                ('net_profit', models.IntegerField()),
                ('win_rate', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='Article.post')),
            ],
        ),
    ]