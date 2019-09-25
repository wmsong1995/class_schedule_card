# Generated by Django 2.2.5 on 2019-09-25 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automatic_card', '0002_auto_20190925_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeRule',
            fields=[
                ('rule_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=10)),
                ('column_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automatic_card.ColumnCard')),
                ('grade', models.ManyToManyField(to='automatic_card.Grade')),
                ('row_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automatic_card.RowCard')),
            ],
        ),
    ]