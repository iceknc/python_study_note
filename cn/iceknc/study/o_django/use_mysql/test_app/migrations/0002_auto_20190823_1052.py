# Generated by Django 2.2.4 on 2019-08-23 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='bprice',
            field=models.DecimalField(db_column='price', decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bcomment',
            field=models.IntegerField(db_column='comment', default=0),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_date',
            field=models.DateField(db_column='pub_date'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bread',
            field=models.IntegerField(db_column='read', default=0),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(db_column='title', max_length=20),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(db_column='comment', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.BooleanField(db_column='gender', default=True),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hname',
            field=models.CharField(db_column='name', max_length=20),
        ),
    ]