from django.db import models

class hotelregister(models.Model):
    hotelname=models.CharField(max_length=100)
    ownername=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=100)
    emailid=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    fssaiimage=models.CharField(max_length=100,default="noimage.png")
    panimage=models.CharField(max_length=100,default="noimage.png")
    hownerphoto=models.CharField(max_length=100,default="noimage.png")
    hregphoto=models.CharField(max_length=100,default="noimage.png")
    latitude=models.CharField(max_length=100,default=0)
    longitude=models.CharField(max_length=100,default=0)
    gstnumber=models.CharField(max_length=100,default="")
    date=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    createdon=models.CharField(max_length=100)
    createdby=models.CharField(max_length=100,default="SuperAdmin")
    softdelete=models.CharField(max_length=100,default=0)
    deletedon=models.CharField(max_length=100,default="-")


class addcoupons(models.Model):
    CouponName=models.CharField(max_length=100)
    discription=models.CharField(max_length=5000)
    Min_cost=models.IntegerField()
    Discont=models.IntegerField()
    Unit=models.CharField(max_length=100)
    cost=models.CharField(max_length=100,default="")
    deletedon=models.CharField(max_length=100,default="")
    created_by=models.CharField(max_length=100,default='')
    created_date=models.CharField(max_length=100 ,default="")
    softdelete=models.IntegerField(default=0)




class mstcategory(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.CharField(max_length=225,default="onimage.png")
    gstnumber=models.CharField(max_length=2000,default="")
    created_on=models.CharField(max_length=100,default="admin")
    created_by=models.CharField(max_length=100,default="")
    registerdate=models.CharField(max_length=100)
    softdelete=models.IntegerField(default=0)


#ajay



class MstMembershipData(models.Model):
    membertype=models.CharField(max_length=200,default="")
    gstnumber=models.CharField(max_length=200,default="")
    cost=models.IntegerField(default=0)
    creatdby=models.CharField(max_length=200,default="")
    registerdate=models.CharField(max_length=100,default="")

class mstitemlist(models.Model):
    itemname=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    discription=models.CharField(max_length=5000)
    cost=models.IntegerField(default=0)
    itemphoto=models.CharField(max_length=255,default='noimage.png')
    categoryid=models.IntegerField(default="1")
    created_on=models.CharField(max_length=100)
    created_by=models.CharField(max_length=100,default='shiva')
    gstnumber=models.CharField(max_length=2000,default="")
    softdelete=models.IntegerField(default=1)


class CustomerData(models.Model):
    customer_name=models.CharField(max_length=200,default="")
    mobile_number=models.CharField(max_length=200, primary_key=False,default="9845356246")
    gmail=models.EmailField(max_length=100,default="")
    aadhar_number=models.BigIntegerField(default="")
    address=models.CharField(max_length=1000,default="")
    Current_location=models.CharField(max_length=1000,default="")
    image=models.CharField(max_length=255,default="")
    password=models.CharField(max_length=200,default="")
    registerdate=models.CharField(max_length=100,default="")
    softdelete=models.IntegerField(default=0)


class itemorderdetails(models.Model):
    mobilenumber=models.CharField(max_length=200,default="")
    gstnumber=models.CharField(max_length=50,default="")
    itemid=models.IntegerField(default="")
    quantity=models.IntegerField(default=0)
    itemcost=models.FloatField(default=0)
    status=models.CharField(max_length=100,default="NEW_ORDER")
    canceldate=models.CharField(max_length=100,default="")
    created_on=models.CharField(max_length=100,default="")
    orderid=models.IntegerField(default=0)
    amount=models.FloatField(default=0)



class  superadminreg(models.Model):
    adminname=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=13)
    password=models.CharField(max_length=200)
    softdelete=models.IntegerField(default=0)
    createdby=models.CharField(max_length=100,default='admin')
    createdon=models.CharField(max_length=100)
    deletedon=models.CharField(max_length=100,default='-')

