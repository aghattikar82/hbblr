from django.contrib import admin
from django.urls import path
from HBAPP import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

# rahul

    path('Customeroder',views.Customeroder),
    

#SHIVU START
    path('hotelregister',views.hregister,name="hotelregister"),
    path('superadminlogin',views.logincode),
    path('register',views.superadminregister,name="register"),
    path('admindisplay',views.superadmmindisplay,name="admindisplay"),
    path('hotelsearch',views.hotelsearch,name="hotelsearch"),
    path('adminsearch',views.adminsearch,name="adminsearch"),

#SHIVU END


#ANUP START
    path('hotelchangepassword',views.changepasswordhotel),
    path('login',views.logincodehotel),
    path('hotelhome',views.hotelhome),

#ANUP END

    path('addcoupans',views.addcoupans,name="addcoupans"),
    path('displaycoupans',views.displaycoupan,name="displaycoupan"),
    path('searchcoupan',views.searchcoupan,name="searchcoupan"),
    path('cmtfeedback',views.cmtfeedback,name="cmtfeedback"),
    path('hotelhome',views.hotelhome),
    path('mstcategory',views.categorycode,name="mstcategory"),
    path('categorysearch',views.categorysearch,name="categorysearch"),
    path('hoteldisplay',views.hoteldisplay,name="hoteldisplay"),
    path('hotelchangepassword',views.changepasswordhotel,name="hotelchangepassword"),
    path('index',views.index,name="index"),
    path('hotellogin',views.hotellogin,name="hotellogin"),

    #path('admin/', admin.site.urls),
    path('changepassword',views.changepassword,name="changepassword"),
    path('itemlist',views.itemlist,name="itemlist"),
    path('itemdisplay',views.itemdisplay,name="itemdisplay"),
    path('itemsearch',views.itemsearch,name="itemsearch"),
    path('mstmembershipregister',views.MstMembershipRegister,name="mstmembershipregister"),
    path('mstmembershipdisplay',views.MstMembershipDisplay,name="mstmembershipdisplay"),
    
    # AJAY START #
    path('ctregister',views.CustomerRegister,name="ctregister"),
    path('ctdisplay',views.CustomerDisplay,name="ctdisplay"),
    path('ctsearch',views.CustomerSearch,name="ctsearch"),
    path('ctlogin',views.CustomerLogincode,name="ctlogin"),
    path('',views.CustomerLogincode,name="ctlogin"),
    path('ctchangepassword',views.CtChangePassword,name="ctchangepassword"),
    path('cthome',views.CustomerHome,name="cthome"),
    path('ctItemOrder',views.ctItemOrder,name="ctItemOrder"),
    path('ctcart',views.Cart,name="ctcart"),
    path('ctorderhistory',views.OrderHistory,name="ctorderhistory"),
    path('ctfeedback',views.Feedback,name="ctfeedback"),
    #AJAY END #
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
