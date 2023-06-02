from django.shortcuts import render,redirect
from HBAPP.models import mstcategory,hotelregister,MstMembershipData,addcoupons
from HBAPP.models import superadminreg,mstitemlist,CustomerData,itemorderdetails,customeroderdetails
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import datetime







def Customeroder(request):
    if request.method=="POST":
        g=customeroderdetails()
        g.mobilenumber=request.session["mobilenumber"]
        g.totalamount=request.POST['amount']
        g.hotelid=request.POST['hotelid']
        g.delivery_type=request.POST['ddfield']
        g.addcoupons=request.POST['addcoupon']
        g.ordedatetime=datetime.datetime.now()
        g.save()
        msg="customeroder successfully"
    else:
        msg=""
    return render(request,"Customeroder.html",{"msg":msg})
        


def changepasswordhotel(request):
    msg=""
    if request.method=="POST":
        sessionmobilenumber=request.session["mobilenumber"]
        currentpassword=request.POST["txtcurrentpasswordd"]
        newpassword=request.POST["txtnewpassword"]
        confirmnewpassword=request.POST["txtconfirmnewpassword"]
        if newpassword != confirmnewpassword:
            msg="New Password And Confirm New Password Must Be Same"
        else:
            if hotelregister.objects.filter(mobilenumber=sessionmobilenumber,password=currentpassword,softdelete=0).exists():
                data=hotelregister.objects.filter(mobilenumber=sessionmobilenumber,password=currentpassword,softdelete=0)
                data.update(password=newpassword)
                msg="Password Changed Successfully"
            else:
                msg="Current Password Does Not Match"
    return render(request,"hotelchangepassword.html",{"msg":msg})

def hotelhome(request):
    return render(request,"hotelhome.html")

def logincodehotel(request):
    msg=""
    data=""
    if request.method=="POST":
        usermobilenumber=request.POST["txtmobilenumber"]
        userpassword=request.POST["txtpassword"]
        request.session["mobilenumber"]=usermobilenumber
        if hotelregister.objects.filter(mobilenumber=usermobilenumber,password=userpassword,softdelete=0).exists():
            return render(request,"hotelhome.html")
        else:
            msg="Invalid Mobile Number Or Password"
    return render(request,"hotellogin.html",{"msg":msg})

def cmtfeedback(request):
    msg=""
    if request.method=="POST":
        action=request.POST["btnsubmit"]
        if action=="Submit":
            Feedbackname=request.POST["Feedback"]
            msg="add successfully"
    return render(request,"cmtfeedback.html",{"msg":msg})
def searchcoupan(request):
    msg=""
    data=""
    if request.method=="POST":
        action=request.POST["btnsubmit"]
        if action=='Update':
            did=request.POST['did']
            data=addcoupons.objects.filter(id=did)
            data.update(CouponName=request.POST["txtcoponname"],discription=request.POST["txtdiscription"],Min_cost=request.POST["mincost"])
            msg="Updeted successfully"
            return render(request,"displaycoupan.html",{"data":data,"msg":msg})

        elif action=="edit":
            did=request.POST["did"]
            data=addcoupons.objects.filter(id=did)
            return render(request,"editcoupan.html",{"data":data})
        elif action=="Delete":
            did=request.POST["did"]
            addcoupons.objects.filter(id=did).delete()
            msg="Record Not Found"
        else:
            fieldname=request.POST["ddfield"]
            search=request.POST["txtsearch"]
            if search.isnumeric() and fieldname=="id":
                if addcoupons.objects.filter(id=search).exists():
                    data=addcoupons.objects.filter(id=search)
                else:
                    msg="Record Not Found"
            else:
                if (fieldname=="CoupanName"):   
                    if addcoupons.objects.filter(CouponName__icontains=search).exists():
                        data=addcoupons.objects.filter(CouponName__icontains=search)
                    else:
                        msg="Record Not Found"
    return render(request,"searchcoupan.html",{"data":data,"msg":msg})


def displaycoupan(request):
    data=""
    data=addcoupons.objects.all()
    return render(request,"displaycoupan.html",{"data":data})



def addcoupans(request):
    msg=""
    data=""
    if request.method=="POST":
        f=addcoupons()
        f.CouponName=request.POST["txtcoponname"]
        f.discription=request.POST["Description"]
        f.Min_cost=request.POST["mincost"]
        f.Discont=request.POST["discont"]
        f.Unit=request.POST["dfname"]
        f.cost=request.POST["txtcost"]
        f.created_date=datetime.datetime.now()
        f.save()
        msg="Coupon add successfully"
    else:
        msg=""
    return render(request,"addcoupans.html",{"msg":msg,"data":data})

def ctItemOrder(request):
    itemdata=""
    categorydata=""
    msg=""
    if request.method=="POST":
        iod=itemorderdetails()
        iod.mobilenumber=request.session["mobilenumber"]
        iod.hotelid=request.POST["hotelid"]
        iod.itemid=request.POST["itemid"]
        iod.quantity=request.POST["qty"]
        iod.itemcost=request.POST["itemcost"]
        iod.canceldate=datetime.datetime.now()
        iod.created_on=datetime.datetime.now()
        print(request.POST["itemcost"])
        iod.amount=float(request.POST["qty"])*float(request.POST["itemcost"])
        iod.save()
        msg="Item added to Cart"
    return render(request,"successpage.html",{"msg":msg})
def CustomerHome(request):
    itemdata=""
    categorydata=""
    if request.method=="POST":
        action=request.POST.get("btnsubmit","")
        print("----------"+action);
        iid=request.POST["iid"]
        data=mstitemlist.objects.filter(id=iid)
        return render(request,"cthome.html",{"data":data})
    else:
        if mstitemlist.objects.all().exists():
            itemdata=mstitemlist.objects.all()
        if mstcategory.objects.all().exists(): 
            categorydata=mstcategory.objects.all()
        return render(request,"cthome.html",{"itemdata":itemdata,"categorydata":categorydata})

def index(request):
    data=mstitemlist.objects.all()
    return render(request,"index.html",{"data":data})
def changepassword(request):
    msg=""
    if request.method=="POST":
        sessionmobilenumber=request.session["mobilenumber"]
        currentpassword=request.POST["txtcurrentpasswordd"]
        newpassword=request.POST["txtnewpassword"]
        confirmnewpassword=request.POST["txtconfirmnewpassword"]
        if newpassword != confirmnewpassword:
            msg="New Password And Confirm New Password Must Be Same"
        else:
            if hotelregister.objects.filter(mobilenumber=sessionmobilenumber,password=currentpassword,softdelete=0).exists():
                data=hotelregister.objects.filter(mobilenumber=sessionmobilenumber,password=currentpassword,softdelete=0)
                data.update(password=newpassword)
                msg="Password Changed Successfully"
            else:
                msg="Current Password Does Not Match"
    return render(request,"hotelchangepassword.html",{"msg":msg})


def logincode(request):
    msg=""
    data=""
    if request.method=="POST":
        usermobilenumber=request.POST["txtmobilenumber"]
        userpassword=request.POST["txtpassword"]
        request.session["mobilenumber"]=usermobilenumber
        if usermobilenumber=="9876543210" and userpassword=="9876543210":
            return redirect("hotelhome.html")
        else:
            msg="Invalid Mobile Number Or Password"
    return render(request,"hotellogin.html",{"msg":msg})



def hotelsearch(request):
    msg=""
    data=""
    if request.method=="POST":
        action=request.POST["btnsubmit"]
        if action=="Update":
            hid=request.POST["hid"]
            data=hotelregister.objects.filter(id=hid)

            hr=hotelregister()

            ownimg = request.FILES['ownimg']
            fs = FileSystemStorage()
            hownerphoto = fs.save(ownimg.name, ownimg)
            
            regimg = request.FILES['regimg']
            fs = FileSystemStorage()
            hregphoto = fs.save(regimg.name, regimg)

            data.update(hotelname=request.POST["hotelname"],ownername=request.POST["ownername"],mobilenumber=request.POST["mobilenumber"],emailid=request.POST["emailid"],address=request.POST["address"],hownerphoto=fs.url(ownimg),hregphoto=fs.url(regimg))
            msg="Hotel Details Updated"
            return render(request,"hotelsearch.html",{"msg":msg,"data":data})

        elif action=="Edit":
            hid=request.POST["hid"]
            data=hotelregister.objects.filter(id=hid)
            return render(request,"hoteledit.html",{"data":data})
        elif action=='Items':
            itemid=request.POST['hid']
            data=mstitemlist.objects.filter(id=itemid)
            return render(request,"itemdisplay.html",{"data":data})

        elif  action=="Delete":
            hid=request.POST["hid"]
            hotelregister.objects.filter(id=hid).delete()
            msg="Hotel Removed Successfully"
        else:        
            search=request.POST["txtsearch"]
            fieldname=request.POST["ddlfield"]
            
            if search.isnumeric() and fieldname=="id":
                if hotelregister.objects.filter(id=search).exists():
                    data=hotelregister.objects.filter(id=search)
                else:
                    msg="Record Not Found"
            else:
                if (fieldname=="hotelname"):   
                    if hotelregister.objects.filter(hotelname__icontains=search).exists():
                        data=hotelregister.objects.filter(hotelname__icontains=search)
                    else:
                        msg="Record Not Found"
                    
                elif fieldname=="ownername":
                    if hotelregister.objects.filter(ownername__icontains=search).exists():
                        data=hotelregister.objects.filter(ownername__icontains=search)
                    else:
                        msg="Record Not Found"   
                   
                elif fieldname=="mobilenumber":
                        if hotelregister.objects.filter(mobilenumber__icontains=search).exists():
                            data=hotelregister.objects.filter(mobilenumber__contains=search)
                        else:
                            msg="Record Not Found" 
                

    return render(request,"hotelsearch.html",{"data":data,"msg":msg})


def hoteldisplay(request):
    data=""
    data = hotelregister.objects.all()
    return render(request,"hoteldisplay.html",{"data":data})

def hotelhome(request):
    return render(request,"hotelhome.html")

def hotellogin(request):
    msg=""
    data=""
    if request.method=="POST":
        usermobilenumber=request.POST["txtmobilenumber"]
        userpassword=request.POST["txtpassword"]
        request.session["mobilenumber"]=usermobilenumber
        if hotelregister.objects.filter(mobilenumber=usermobilenumber,password=userpassword,softdelete=0).exists():
            return render(request,"hotelhome.html")
        else:
            msg="Invalid Mobile Number Or Password"
    return render(request,"hotellogin.html",{"msg":msg})


# Create your views here.
def hregister(request):
    msg=""
    if request.method=="POST":
        hr=hotelregister()
        hr.hotelname=request.POST["txthotelname"]
        hr.ownername=request.POST["txtownername"]
        hr.mobilenumber=request.POST["txtmobilenumber"]
        hr.emailid=request.POST["txtemailid"]
        hr.address=request.POST["txtaddress"]

        ownerphoto = request.FILES['ownerphoto']
        fs = FileSystemStorage()
        hownerphoto = fs.save(ownerphoto.name, ownerphoto)
        
        regphoto = request.FILES['regphoto']
        fs = FileSystemStorage()
        hregphoto = fs.save(regphoto.name, regphoto)

        fssaiimage = request.FILES['fssaiimage']
        fs = FileSystemStorage()
        hfssaiimage = fs.save(fssaiimage.name, fssaiimage)

        panimage = request.FILES['panimage']
        fs = FileSystemStorage()
        hpanimage = fs.save(panimage.name, panimage)

        hr.gstnumber=request.POST["txtgstnumber"]
        hr.date=request.POST["txtdate"]
        hr.password=request.POST["txtpassword"]
        hr.createdon=datetime.datetime.now()
        
        hr.hownerphoto=fs.url(hownerphoto)

        hr.hregphoto=fs.url(hregphoto)

        hr.fssaiimage=fs.url(hpanimage)

        hr.panimage=fs.url(panimage)
        hr.latitude=request.POST["txtlatitude"]
        hr.longitude=request.POST["txtlongitude"]
        
        hr.save()
        msg="Registered Successfully"
    else:
        msg=""
    return render(request,"hotelregister.html",{"msg":msg})

def categorysearch(request):
	msg=""
	data=""
	if request.method=="POST":
		action=request.POST["btnsubmit"]
		if action=="update":
			s=mstcategory()

			mfile=request.FILES["image"]
			fs=FileSystemStorage()
			image=fs.save(mfile.name,mfile)
			s.image=fs.url(image)

			sid=request.POST["sid"]
			data=mstcategory.objects.filter(id=sid)
			data.update(name=request.POST["cname"],image=fs.url(image))
			msg="Updeted successfully"
			return render(request,"categorysearch.html",{"msg":msg,"data":data})
		elif action=="edit":
			sid=request.POST["sid"]
			data=mstcategory.objects.filter(id=sid)
			return render(request,"edit.html",{"data":data})


		elif action=="Delete":
			sid=request.POST["sid"]
			mstcategory.objects.filter(id=sid).delete()
			msg="Record Delete"
		else:
			filename=request.POST["ddfname"]
			searchvalue=request.POST["txtsearch"]
			if searchvalue.isnumeric() and filename=="id":
				if mstcategory.objects.filter(id=searchvalue):
					data=mstcategory.objects.filter(id=searchvalue)
				else:
					msg="Record Not found"
			else:
				if(filename=="name"):
					if mstcategory.objects.filter(name__icontains=searchvalue).exists():
						data=mstcategory.objects.filter(name__icontains=searchvalue)
					else:
						msg="Record Not found"
	return render(request,"categorysearch.html",{"msg":msg,"data":data})

def categorycode(request):
    data=""
    msg=""
    if request.method=="POST":
        s=mstcategory()
        s.name=request.POST["txtname"]
        s.description=request.POST["Description"]
        file=request.FILES["myfile"]
        fs=FileSystemStorage()
        image=fs.save(file.name,file)
        s.image=fs.url(image)
        s.registerdate=datetime.datetime.now()
        s.save()
        msg="Added successfully"
    else:
        msg=""
    return render(request,"mstcategory.html",{"data":data,"msg":msg})

#ajay#

def Cart(request):
    msg=""
    data=""
    
    if itemorderdetails.objects.filter(mobilenumber=request.session["mobilenumber"],status="NEW_ORDER").exists():
        data=itemorderdetails.objects.filter(mobilenumber=request.session["mobilenumber"],status="NEW_ORDER")
        totalamount=0
        for i in data:
            totalamount+=i.amount
            hotelid=i.hotelid 



    return render(request,"ctcart.html",{"data":data,"msg":msg,"hotelid":hotelid,"totalamount":totalamount})
    

def OrderHistory(request):
    msg=""
    data=""
    return render(request,"ctorderhistory.html",{"data":data})
    

def Feedback(request):
    msg=""
    data=""
    return render(request,"ctfeedback.html",{"data":data,"msg":msg})
    


def CustomerDisplay(request):
    data=""
    msg=""
    data=CustomerData.objects.all()
    return render(request,"ctdisplay.html",{"data":data})

def CustomerLogincode(request):
    msg=""
    data=""
    if request.method=="POST":
        usermobilenumber=request.POST["mobilenumber"]
        userpassword=request.POST["password"]
        request.session["mobilenumber"]=usermobilenumber
        if CustomerData.objects.filter(mobile_number=usermobilenumber,password=userpassword,softdelete=0).exists():
            messages.success(request,"Login Successful")
            return redirect("cthome")
        else:
            msg="Invalid Mobile Number Or Password"
    return render(request,"ctlogin.html",{"msg":msg})


def CtChangePassword(request):
    msg=""
    if request.method=="POST":
        currentpassword=request.POST["txtcurrentpasswordd"]
        newpassword=request.POST["txtnewpassword"]
        confirmnewpassword=request.POST["txtconfirmnewpassword"]
        if newpassword != confirmnewpassword:
            msg="New Password And Confirm New Password Must Be Same"
        else:
            if CustomerData.objects.filter(mobile_number=mobilenumber,password=currentpassword,softdelete=0).exists():
                data=CustomerData.objects.filter(mobile_number=mobilenumber,password=currentpassword,softdelete=0)
                data.update(password=newpassword)
                msg="Password Changed Successfully"
            else:
                msg="Current Password Does Not Match"
    return render(request,"ctchangepassword.html",{"msg":msg})




def MstMembershipDisplay(request):
    data=""
    msg=""
    data=MstMembershipData.objects.all()
    if request.method=="POST":
        action=request.POST["btnsubmit"]
        if action=="Update":
            cid=request.POST["cid"]
            data=MstMembershipData.objects.filter(id=cid)
            data.update(membertype=request.POST["membertype"],cost=request.POST["cost"])
            msg="Member Details Updated"
            return render(request,"mstmembershipdisplay.html",{"msg":msg,"data":data})

        elif action=="Delete":
            cid=request.POST["cid"]
            data=MstMembershipData.objects.filter(id=cid).delete()
            msg="Member Data deleted"
            data=MstMembershipData.objects.all()
            return render(request,"mstmembershipdisplay.html",{"msg":msg,"data":data})
        else:
            if action=="Edit":
                cid=request.POST["cid"]
                data=MstMembershipData.objects.filter(id=cid)
                return render(request,"mstmembershipedit.html",{"data":data})
    return render(request,"mstmembershipdisplay.html",{"msg":msg,"data":data})



def CustomerSearch(request):
    msg=""
    data=""
    if request.method=="POST":
        action=request.POST["btnsubmit"]
        if action=="Update":
            cid=request.POST["cid"]
            file=request.FILES["newimage"]
            fs=FileSystemStorage()
            image=fs.save(file.name,file)
            image=fs.url(file)
            data=CustomerData.objects.filter(id=cid)
            data.update(mobile_number=request.POST["mobile_number"],gmail=request.POST["gmail"],address=request.POST["address"],Current_location=request.POST["Current_location"],image=fs.url(file))
            msg="Customer Details Updated"
            return render(request,"ctsearch.html",{"msg":msg,"data":data})

        elif action=="Edit":
            cid=request.POST["cid"]
            data=CustomerData.objects.filter(id=cid)
            return render(request,"ctedit.html",{"msg":msg,"data":data})

        elif action=="Delete":
            cid=request.POST["cid"]
            data=CustomerData.objects.filter(id=cid).delete()
            msg="Customer data deleted successfully"
        else:
            searchby=request.POST["searchby"]
            searchvaluve=request.POST["searchvaluve"]
            if searchvaluve.isnumeric() and searchby=="id":
                if CustomerData.objects.filter(id=searchvaluve).exists():
                    data=CustomerData.objects.filter(id=searchvaluve)
                else:
                    msg="Record Not Found"

            elif searchby=="name":
                if CustomerData.objects.filter(customer_name__icontains=searchvaluve).exists():
                    data=CustomerData.objects.filter(customer_name__icontains=searchvaluve)
                else:
                    msg="Record Not Found"

            elif searchby=="mobile_number":
                if CustomerData.objects.filter(mobile_number__icontains=searchvaluve).exists():
                    data=CustomerData.objects.filter(mobile_number__icontains=searchvaluve)
                else:
                    msg="Record Not Found"


    return render(request,"ctsearch.html", {"msg":msg,"data":data})


def MstMembershipRegister(request):
    msg=""
    data=""
    if request.method=="POST":
        md=MstMembershipData()
        md.membertype=request.POST["membertype"]
        md.cost=request.POST["cost"]
        md.registerdate=datetime.datetime.now()
        md.save()
        msg="Registered successfully"
    else:
        msg=""
    return render(request,"mstmembershipregister.html",{"msg":msg})



def CustomerRegister(request):
    data=""
    msg=""
    if request.method=="POST":
        if CustomerData.objects.filter(aadhar_number=request.POST["aadhar_n"]).exists():
            msg=" your Aadhar Number Alreaday Registered"

        else: 
            cr=CustomerData()
            cr.customer_name=request.POST["customer_name"]
            cr.mobile_number=request.POST["mobile_number"]
            cr.gmail=request.POST["gmail"]
            cr.aadhar_number=request.POST["aadhar_n"]
            cr.address=request.POST["address"]
            cr.Current_location=request.POST["Current_location"]
            file=request.FILES["myimage"]
            fs=FileSystemStorage()
            image=fs.save(file.name,file)
            cr.image=fs.url(file)
            cr.password=request.POST["password"]
            cr.registerdate=datetime.datetime.now()
            cr.save()
            msg="Registered successfully" 
            
    return render(request,"ctregister.html",{"msg":msg}) 
#ajay





def itemsearch(request):
    data=''
    msg=''
    if request.method=="POST":
        operation=request.POST['btnsubmit']
        if operation=='Update':
            itemid=request.POST['itemid']
            data=mstitemlist.objects.filter(id=itemid)
            itemimg=request.FILES['txtitemimage']
            fs=FileSystemStorage()
            itemphoto=fs.save(itemimg.name,itemimg)
        
            data.update(itemname=request.POST['txtitemname'],cost=request.POST['txtcost'],itemphoto=fs.url(itemimg))
            msg="Item Details Updated Successfully"
            return render(request,"itemdisplay.html",{"msg":msg,"data":data})

        if operation=="Delete":
            itemid=request.POST["itemid"]
            mstitemlist.objects.filter(id=itemid).delete()
            msg="Item Details Deleted Successfully"
        elif operation=='Edit':
            itemid=request.POST['itemid']
            data=mstitemlist.objects.filter(id=itemid)
            return render(request,"itemedit.html",{"data":data})

        else:
            search=request.POST['txtseacrh']
            fieldname=request.POST['ddlfield']
            if search.isnumeric() and fieldname=="id":
                if mstitemlist.objects.filter(id=search).exists():
                    data=mstitemlist.objects.filter(id=search)
                else:
                    msg="Item Not Found"
            else:
                if fieldname=="itemname":
                    if mstitemlist.objects.filter(itemname__icontains=search).exists():
                        data=mstitemlist.objects.filter(itemname__icontains=search)
                    else:
                        msg="Item Not Found "
                elif fieldname=='category':
                    if mstitemlist.objects.filter(category__icontains=search).exists():
                        data=mstitemlist.objects.filter(category__icontains=search)
                    else:
                        msg="Item Not Found "


    return render(request,"itemsearch.html",{"data":data,"msg":msg})


def itemdisplay(request):
    data=mstitemlist.objects.all()
    return render(request,"itemdisplay.html",{"data":data})


def itemlist(request):
    msg=''
    category=""
    if request.method=="POST":
        il=mstitemlist()
        il.itemname=request.POST['txtitemname']
        il.category=request.POST['categoryname']
        il.discription=request.POST['txtdiscription']
        il.cost=request.POST['txtcost']
        itemimg=request.FILES['txtitemimg']
        fs=FileSystemStorage()
        itemphoto=fs.save(itemimg.name,itemimg)
        il.itemphoto=fs.url(itemphoto)
        il.created_on=datetime.datetime.now()
        il.save()
        msg="Item Added Successfully"
    else:
        msg=""
    category=mstcategory.objects.all()
    return render(request,"mstitemlist.html",{"msg":msg,"category":category})


def changepassword(request):
    msg=""
    if request.method=="POST":
        sessionmobilenumber=request.session["contactnbr"]
        currentpassword=request.POST["txtcurrentpassword"]
        newpassword=request.POST["txtnewpassword"]
        confirmnewpassword=request.POST["txtconfirmpassword"]
        if newpassword != confirmnewpassword:
            msg="New Password And Confirm New Password Must Be Same"
        else:
            if superadminreg.objects.filter(mobilenumber=sessionmobilenumber,password=currentpassword,softdelete=0).exists():
                data=superadminreg.objects.filter(mobilenumber=sessionmobilenumber,password=currentpassword,softdelete=0)
                data.update(password=newpassword)
            else:
                msg="Current Password Does Not Match"
    return render(request,"changepassword.html",{"msg":msg})

def logincode(request):
    msg=""
    data=""
    if request.method=="POST":
        superadmin=request.POST['txtmobilenumber']
        superadminpassword=request.POST['txtpassword']
        request.session["contactnbr"]=superadmin
        if superadmin=="9876543210" and superadminpassword=="9876543210":
            return render(request,"adminhhome.html",{"msg":msg,"data":data})
        else:
            msg="Invalid Mobile Number or Password"
    return render(request,"adminlogin.html",{"msg":msg})

def adminsearch(request):
    data=''
    msg=""
    if request.method=="POST":
        operation=request.POST["btnsubmit"]
        if operation=="Update":
            adminid=request.POST['aid']
            data=superadminreg.objects.filter(id=adminid)
            data.update(adminname=request.POST['txtname'],mobilenumber=request.POST['txtnumber'])
            msg="Admin Details Updated Successfully"
            return render(request,"admindisplay.html",{"msg":msg,"data":data})
        if operation=="Delete":
            adminid=request.POST["aid"]
            superadminreg.objects.filter(id=adminid).delete()
            msg="Admin Details Deleted Successfully"
        elif operation=="Edit":
            adminid=request.POST['aid']
            data=superadminreg.objects.filter(id=adminid)
            return render(request,"adminedit.html",{"data":data})
        else:

            if (request.POST['txtseacrh'].isnumeric()):
                mobilenumber=request.POST['txtseacrh']

                adminname=request.POST['txtseacrh']
                if superadminreg.objects.filter(mobilenumber=mobilenumber).exists():
                    data=superadminreg.objects.filter(mobilenumber=mobilenumber)
            else:
                adminname=request.POST['txtseacrh']
                if superadminreg.objects.filter(adminname__icontains=adminname).exists():
                    data=superadminreg.objects.filter(adminname__icontains=adminname)
                else:
                    msg="Details Not Found"
    return render(request,"adminsearch.html",{"data":data,"msg":msg,})



def superadmmindisplay(request):
    data=superadminreg.objects.all()
    return render(request,"admindisplay.html",{"data":data})


def superadminregister(request):
    msg=''
    if request.method=="POST":
        sa=superadminreg()
        sa.adminname=request.POST["txtname"]
        sa.mobilenumber=request.POST["txtmobilenumber"]
        sa.password=request.POST["txtpassword"]
        sa.createdon=datetime.datetime.now()
        sa.save()
        msg="Registered Successfully"
    else:
        msg=""

    return render(request,"superadminreg.html",{'msg':msg})
