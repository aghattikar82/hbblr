# Generated by Django 4.1.3 on 2023-03-17 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addcoupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CouponName', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=5000)),
                ('Min_cost', models.IntegerField()),
                ('Discont', models.IntegerField()),
                ('Unit', models.CharField(max_length=100)),
                ('cost', models.CharField(default='', max_length=100)),
                ('deletedon', models.CharField(default='', max_length=100)),
                ('created_by', models.CharField(default='', max_length=100)),
                ('created_date', models.CharField(default='', max_length=100)),
                ('softdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='', max_length=200)),
                ('mobile_number', models.CharField(default='9845356246', max_length=200)),
                ('gmail', models.EmailField(default='', max_length=100)),
                ('aadhar_number', models.BigIntegerField(default='')),
                ('address', models.CharField(default='', max_length=1000)),
                ('Current_location', models.CharField(default='', max_length=1000)),
                ('image', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=200)),
                ('registerdate', models.CharField(default='', max_length=100)),
                ('softdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='hotelregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=100)),
                ('ownername', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('fssaiimage', models.CharField(default='noimage.png', max_length=100)),
                ('panimage', models.CharField(default='noimage.png', max_length=100)),
                ('hownerphoto', models.CharField(default='noimage.png', max_length=100)),
                ('hregphoto', models.CharField(default='noimage.png', max_length=100)),
                ('latitude', models.CharField(default=0, max_length=100)),
                ('longitude', models.CharField(default=0, max_length=100)),
                ('gstnumber', models.CharField(default='', max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('createdon', models.CharField(max_length=100)),
                ('createdby', models.CharField(default='SuperAdmin', max_length=100)),
                ('softdelete', models.CharField(default=0, max_length=100)),
                ('deletedon', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='itemorderdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenumber', models.CharField(default='', max_length=200)),
                ('gstnumber', models.CharField(default='', max_length=50)),
                ('itemid', models.IntegerField(default='')),
                ('quantity', models.IntegerField(default=0)),
                ('itemcost', models.FloatField(default=0)),
                ('status', models.CharField(default='NEW_ORDER', max_length=100)),
                ('canceldate', models.CharField(default='', max_length=100)),
                ('created_on', models.CharField(default='', max_length=100)),
                ('orderid', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='mstcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.CharField(default='onimage.png', max_length=225)),
                ('gstnumber', models.CharField(default='', max_length=2000)),
                ('created_on', models.CharField(default='admin', max_length=100)),
                ('created_by', models.CharField(default='', max_length=100)),
                ('registerdate', models.CharField(max_length=100)),
                ('softdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='mstitemlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=5000)),
                ('cost', models.IntegerField(default=0)),
                ('itemphoto', models.CharField(default='noimage.png', max_length=255)),
                ('categoryid', models.IntegerField(default='1')),
                ('created_on', models.CharField(max_length=100)),
                ('created_by', models.CharField(default='shiva', max_length=100)),
                ('gstnumber', models.CharField(default='', max_length=2000)),
                ('softdelete', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MstMembershipData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membertype', models.CharField(default='', max_length=200)),
                ('gstnumber', models.CharField(default='', max_length=200)),
                ('cost', models.IntegerField(default=0)),
                ('creatdby', models.CharField(default='', max_length=200)),
                ('registerdate', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='superadminreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=200)),
                ('softdelete', models.IntegerField(default=0)),
                ('createdby', models.CharField(default='admin', max_length=100)),
                ('createdon', models.CharField(max_length=100)),
                ('deletedon', models.CharField(default='-', max_length=100)),
            ],
        ),
    ]
