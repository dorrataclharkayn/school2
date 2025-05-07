
# Create your views here.
from decimal import Decimal
from datetime import date


from django.shortcuts import render
from .models import login11,matiere,nstudent101,student101,anne,regeleve,stok,stok11,visamoy,mony,school,ps123note,regeleveps,mediaschool,videoschool,newsschool,structurecarnet
from django.template import loader
from .form02 import loginform
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from num2words import num2words
# Create your views here.
#news
def changean (request):
 x=request.POST.get('anne2031')
 y=request.POST.get('anne2033')

 if x!=None and y!=None:
   sss=matiere.objects.filter(anne=x)
   for ii in sss:
     ii.anne=y
     ii.save()
 print("hi")
 print(x)
 return HttpResponseRedirect(reverse('form10033m'))



def news(request):
 d=request.POST.get('datnews')
 if d == date.today():
   d="1-1-1990"
 nn=""
 if d != "YYYY-mm-dd" and d != None  and d != ""  and d != date.today():
   nn=newsschool.objects.filter(dat=d) 
 if d == date.today():
   nn=newsschool.objects.filter(dat="1-1-1990")
 
 
 newto=newsschool.objects.filter(dat=(date.today()))
 
 ss={'rd':nn,'da':d,'toi':newto,'ddd':date.today()} 
 
 print(d)
 
 print("x")
 print(date.today())
 return render(request,'app1/index.html',ss)
 





##### code automatique for matiere
def autocodemat(request):
  anr=anne.objects.all()
  
  anmat=request.POST.get('anne2031')
  sec05=request.POST.get('section08')
  tt="nonnnn"
  anmat1=anmat
  zzmat=matiere.objects.filter(anne=anmat1,section=sec05)
  for i in zzmat:
    tt=i.anne
  if tt == "nonnnn":
     data=matiere(code="yyyabbas",nommatiere="yyybbas",classe="yyabbas",section="yyabbas",score=0)
     data.save()

     if sec05 != None and anmat != None and anmat!="":
      data=matiere(code="p1"+sec05+anmat,anne=anmat,nommatiere="arab1",classe="ps1",section=sec05,score=0)
      data.save()
      data=matiere(code="p2"+sec05+anmat,anne=anmat,nommatiere="arab1",classe="ps2",section=sec05,score=0)
      data.save()
      data=matiere(code="p3"+sec05+anmat,anne=anmat,nommatiere="arab1",classe="ps3",section=sec05,score=0)
      data.save()
      data=matiere(code="pf1"+sec05+anmat,anne=anmat,nommatiere="francais1",classe="ps1",section=sec05,score=0)
      data.save()
      data=matiere(code="pf2"+sec05+anmat,anne=anmat,nommatiere="francais1",classe="ps2",section=sec05,score=0)
      data.save()
      data=matiere(code="pf3"+sec05+anmat,anne=anmat,nommatiere="francais1",classe="ps3",section=sec05,score=0)
      data.save()

  
  
      cl1("eb1",sec05,anmat1)
      cl1("eb2",sec05,anmat1)
      cl1("eb3",sec05,anmat1)
      cl1("eb4",sec05,anmat1)
      cl1("eb5",sec05,anmat1)
      cl1("eb6",sec05,anmat1)
      cl1("eb7",sec05,anmat1)
      cl1("eb8",sec05,anmat1)
      cl1("eb9",sec05,anmat1)
      cl1("sec-sc",sec05,anmat1)
      cl1("bacc1-sc",sec05,anmat1)
      cl1("bacc1-l",sec05,anmat1)
      cl1("sg",sec05,anmat1)
      cl1("sv",sec05,anmat1)
      cl1("se",sec05,anmat1)
      cl1("lh",sec05,anmat1)
  
  sss={'anrec':anr}
  return render(request,'app1/directeur/newcodemat.html',sss)

def cl1(cl02,se02,anm02):
   cl=cl02;se=se02;anm=anm02
   clmat(cl,se,anm,"math")
   clmat(cl,se,anm,"physique")
   clmat(cl,se,anm,"chimie")
   clmat(cl,se,anm,"bio")
   clmat(cl,se,anm,"arab1")
   clmat(cl,se,anm,"arab2")
   clmat(cl,se,anm,"arab3")
   clmat(cl,se,anm,"francais1")
   clmat(cl,se,anm,"francais2")
   clmat(cl,se,anm,"francais3")
   clmat(cl,se,anm,"eng")
   clmat(cl,se,anm,"civisme")
   clmat(cl,se,anm,"historique")
   clmat(cl,se,anm,"geographie")
   clmat(cl,se,anm,"economie")
   clmat(cl,se,anm,"socialite")
   clmat(cl,se,anm,"philosophie")
   clmat(cl,se,anm,"informatique")
   clmat(cl,se,anm,"art")
   clmat(cl,se,anm,"religieu")
   clmat(cl,se,anm,"sport")
   clmat(cl,se,anm,"pass1")
   clmat(cl,se,anm,"matiere1")
   clmat(cl,se,anm,"matiere2")
   clmat(cl,se,anm,"matiere3")
   clmat(cl,se,anm,"matiere4")
   clmat(cl,se,anm,"matiere5")
   clmat(cl,se,anm,"matiere6")
   clmat(cl,se,anm,"matiere7")
   

def clmat(cl,se,anm,mati):
  data=matiere(code="xxxabbas",nommatiere="xxxabbas",classe="xxxabbas",section="xxxabbas",score=0)
  data.save()
  data=matiere.objects.get(code="xxxabbas",nommatiere="xxxabbas")
  iii=data.id
  nfc="";nfc1="";nfc2="";nfc3=""
  if mati ==  "math": code001="ma"+str(iii);nfc="رياضيات"
  if mati ==  "physique": code001="py"+str(iii);nfc="فيزياء"
  if mati ==  "chimie": code001="ch"+str(iii);nfc="كيمياء"
  if mati ==  "bio": code001="bi"+str(iii);nfc="علوم"
  if mati ==  "arab1": code001="a1"+str(iii);nfc="اللغة العربية";nfc1="تواصل شفهي"
  if mati ==  "arab2": code001="a2"+str(iii);nfc="اللغة العربية";nfc1="تواصل كتابي"
  if mati ==  "arab3": code001="a3"+str(iii);nfc="اللغة العربية";nfc1="قواعد واملاء"

  if mati ==  "francais1": code001="f1"+str(iii);nfc="La Langue";nfc1="Francaise";nfc2="communication";nfc3="orale"
  if mati ==  "francais2": code001="f2"+str(iii);nfc="La Langue";nfc1="Francaise";nfc2="communication";nfc3="ecrite"
  if mati ==  "francais3": code001="f3"+str(iii);nfc="La Langue";nfc1="Francaise";nfc2="grammaire";nfc3="dictee"
  if mati ==  "eng": code001="en"+str(iii);nfc="English"
  if mati ==  "civisme": code001="ci"+str(iii);nfc="تربية مدنية"
  if mati ==  "historique": code001="hi"+str(iii);nfc="تاريخ"
  if mati ==  "geographie": code001="ge"+str(iii);nfc="جغرافيا"
  if mati ==  "economie": code001="ec"+str(iii);nfc="اقتصاد"
  if mati ==  "socialite": code001="so"+str(iii);nfc="اجتماع"
  if mati ==  "philosophie": code001="ph"+str(iii);nfc="فلسفة"
  if mati ==  "informatique": code001="in"+str(iii);nfc="كمبيوتر"
  if mati ==  "art": code001="ar"+str(iii);nfc="فنون"
  if mati ==  "religieu": code001="re"+str(iii);nfc="تربية دينية"
  if mati ==  "sport": code001="sp"+str(iii);nfc="رياضة"
  if mati ==  "pass1": code001="pa"+str(iii);nfc=""
  if mati ==  "matiere1": code001="m1"+str(iii);nfc="مادة1"
  if mati ==  "matiere2": code001="m2a"+str(iii);nfc="مادة2"
  if mati ==  "matiere3": code001="m3s"+str(iii);nfc="مادة3"
  if mati ==  "matiere4": code001="m4d"+str(iii);nfc="مادة4"
  if mati ==  "matiere5": code001="m5c"+str(iii);nfc="مادة5"
  if mati ==  "matiere6": code001="m6y"+str(iii);nfc="مادة6"
  if mati ==  "matiere7": code001="m7v"+str(iii);nfc="مادة7"




  data.nommatiere=mati
  data.code=code001
  data.classe=cl
  data.section=se
  data.anne=anm
  data.nomforcarnet=nfc
  data.sousnom1=nfc1;data.sousnom2=nfc2;data.sousnom3=nfc3
  data.save()



################################################################################33
######################################
 
#####  عرض الصور والفيديوهات للاهل
def insertimagepare(request):
 x=request.POST.get('monthi')
 y=request.POST.get('annei')
 if x==None: x=""
 if y==None: y=""
 
 rr=mediaschool.objects.filter(dat__month__contains=x,dat__year__contains=y)
 ss={'rec':rr}
 return render(request,'app1/directeur/insertimagepare.html',ss)


def insertvideopare(request):
 x=request.POST.get('monthi')
 y=request.POST.get('annei')
 if x==None: x=""
 if y==None: y=""
 
 rr=videoschool.objects.filter(dat__month__contains=x,dat__year__contains=y)
 ss={'rec':rr}
 return render(request,'app1/directeur/insertvideopare.html',ss)


##########

def insertimage(request):
 x=request.POST.get('monthi')
 y=request.POST.get('annei')
 if x==None: x=""
 if y==None: y=""
 
 rr=mediaschool.objects.filter(dat__month__contains=x,dat__year__contains=y)
 ss={'rec':rr}
 return render(request,'app1/directeur/insertimage.html',ss)
 
def addimage1(request):
 x=request.POST.get('date01')
 y=request.POST.get('pht')
 w=""
 t=""
 h=""
 if x!=None  and y!=None :
    data=mediaschool(dat=x,image=y,rem1=w,rem2=t,rem3=h)
    data.save()
 return render(request,'app1/directeur/addimage.html')
 
def delimage1(request, cc):
 aaa=mediaschool.objects.get(id=cc)
 aaa.delete()

 return HttpResponseRedirect(reverse('image001'))

#### video

def insertvideo(request):
 x=request.POST.get('monthi')
 y=request.POST.get('annei')
 if x==None: x=""
 if y==None: y=""
 
 rr=videoschool.objects.filter(dat__month__contains=x,dat__year__contains=y)
 ss={'rec':rr}
 return render(request,'app1/directeur/insertvideo.html',ss)
 
def addvideo1(request):
 x=request.POST.get('date01')
 y=request.POST.get('pht')
 w=""
 t=""
 h=""
 if x!=None  and y!=None :
    data=videoschool(dat=x,video=y,rem1=w,rem2=t,rem3=h)
    data.save()
 
 
 
 return render(request,'app1/directeur/addvideo.html')
 
def delvideo1(request, cc):
 aaa=videoschool.objects.get(id=cc)
 aaa.delete()
 return HttpResponseRedirect(reverse('video001'))

### end video

def passdirect(request):
 x=request.POST.get('x001')   
 dd=stok.objects.get(id=1)
 ccc={'xwnn':x}
 if dd.user==x:
    return render(request,'app1/direct.html',ccc)
 print(x)
 return render(request,'app1/direct1.html',ccc)

def passmaitre(request):
  x=request.POST.get('x001')   
  pa0s="no"
  dd=stok.objects.all()
  for ddm in dd:
    if ddm.user == x  and ddm.passmod!="oui":
      pa0s="oui"
  
  ccc={'xwnn':x}
  
  if pa0s=="oui":
     return render(request,'app1/directmaitre.html',ccc)
  print(x)
  return render(request,'app1/maitre001.html',ccc)





def direct(request):
   return render(request,'app1/direct.html')
def maitres(request):
   return render(request,'app1/directmaitre.html')

def index(request):
   return render(request,'app1/direct.html')

def about (request):
   return HttpResponse('الاعطال')

def bord (request):
   return render(request,'app1/index.html')

def photo (request):
   return render(request,'app1/men1.html')

def sendvar(request):
   return render(request,'app1/var.html',{'name':'abba','age':25555555555555555} )


def form0001 (request):
  
  x=request.POST.get('username') 
  y=request.POST.get('password')
  
  data=login11(username=x,password=y)
  
  if y!=None and x!=None :
         data.save()
 
  return render(request,'form01.html',{'lf':loginform})
  
def abbas():
   print("hi")
def form0003 (request):
  
  x=request.POST.get('username') 
  y=request.POST.get('password')
  
  data=login11(username=x,password=y)
  
  if y!=None and x!=None :
         data.save()
 
  return render(request,'form03.html',{'rec':login11.objects.all()})

def form0004 (request):
  
  x=request.POST.get('code') 
  y=request.POST.get('nommatiere')
  z=request.POST.get('classe')
  w=request.POST.get('section')
  a=request.POST.get('anne')
  data=matiere(code=x, nommatiere=y, classe=z, section=w, anne=a)
  
  if y!=None and x!=None and z!=None and w!=None:
         data.save()
 
  return render(request,'app1/directeur/formmatiere.html')



def matiereupdate (request):
  
  
  return render(request,'app1/directeur/editmatiere.html')

def addstudent (request):
  
  x=request.POST.get('code') 
  y=request.POST.get('nom')
  z=request.POST.get('pere')
  w=request.POST.get('famille')
  a=request.POST.get('mere')
  b=request.POST.get('city')
  c=request.POST.get('tel')
  d=request.POST.get('dat')   
  e=request.POST.get('quit')
  x1=request.POST.get('lieu1')
  x2=request.POST.get('segel1')
  x3=request.POST.get('rem11')
  x4=request.POST.get('rem21')
  x5=request.POST.get('num11')
  x6=request.POST.get('num21')





  if x!=None:
    data=student101(code=x, nom=y, pere=z, famille=w, mere=a, city=b, tel=c, dat=d, quit=e, lieu=x1, segel=x2, rem1= x3, rem2=x4, num1=x5, num2=x6)
    
    data.save()
    data1=student101.objects.get(code=x)
    cc1=data1.code+str(data.id)
   
    data1.code=cc1
    data1.nom=y
    data1.pere=z
    data1.famille=w
    data1.mere=a
    data1.city=b
    data1.tel=c
    data1.dat=d
    data1.quit=e
    data1.lieu=x1
    data1.segel=x2
    data1.rem1=x3
    data1.rem2=x4
    data1.num1=x5
    data1.num2=x6
    data1.save()
 
 
  return render(request,'app1/directeur/formeleveadd.html')



  

def editstudent (request):
  
  x01=request.POST.get('code1')
  x=request.POST.get('code') 
  y=request.POST.get('nom')
  z=request.POST.get('pere')
  w=request.POST.get('famille')
  a=request.POST.get('mere')
  b=request.POST.get('city')
  c=request.POST.get('tel')
  d=request.POST.get('dat')   
  e=request.POST.get('quit')
  x1=request.POST.get('lieu1')
  x2=request.POST.get('segel1')
  x3=request.POST.get('rem11')
  x4=request.POST.get('rem21')
  x5=request.POST.get('num11')
  x6=request.POST.get('num21')

  
  
  print(x01)
  if x01!=None:
   data=student101.objects.get(code=x01)
   data.nom=y
   data.pere=z
   data.famille=w
   data.mere=a
   data.city=b
   data.tel=c
   data.dat=d
   data.quit=e
   data.lieu=x1
   data.segel=x2
   data.rem1=x3
   data.rem2=x4
   data.num1=x5
   data.num2=x6

   print(x)
  
  if y!=None and x01!=None and z!=None and w!=None and a!=None  and b!=None and c!=None and d!=None and e!=None:
         data.save()
  return render(request,'app1/directeur/editeleve.html',{'rec':student101.objects.all().filter(code=x01)})



def listeleve (request):
  anw=anne.objects.all()
  xann=("A")
  if xann!=None:
    getclasec=regeleve.objects.filter(anne1=xann)
    
  x001=request.POST.get('nom1')
  print(x001)
  
  ff=student101.objects.filter(nom="x")
  sss={'rec': ff,'annn' : anw}
  if xann!=None:
    sss={'rec': ff,'annn' : anw,'getcs': getclasec}

  if x001!=None and x001 !="":
   ff= student101.objects.all()
   sss={'rec': ff.filter(nom__contains=x001),'annn' : anw}
   if xann!=None:
    sss={'rec': ff.filter(nom__contains=x001),'annn' : anw,'getcs': getclasec}
    

    
  if x001=="?":
   sss={'rec': ff,'annn' : anw}
   if xann!=None:
    sss={'rec': ff,'annn' : anw,'getcs': getclasec}

  if x001=="":
    fff=student101.objects.filter(code="x")
    sss={'rec': ff,'annn' : anw}
  print("oui")
  if x001==None:
    fff=student101.objects.filter(code="x")
    sss={'rec': ff,'annn' : anw}
  
  return render(request,'app1/directeur/listeleve.html',sss)

def update1 (request, cod):
 cc=str(cod)
 menber1=student101.objects.all()
 print(cc)
 return render(request,'app1/directeur/formeleve.html', {'menber': student101.objects.get(code=cc)})

def updaterecord(request,coood):
 ttc=request.POST['code']
 nn=request.POST['nom']
 pp=request.POST['pere']
 mm=request.POST['mere']
 ff=request.POST['famille']
 cc=request.POST['city']
 tt=request.POST['tel']
 dd=request.POST['daten']
 reec=request.POST['quit']
 x1=request.POST.get('lieu1')
 x2=request.POST.get('segel1')
 x3=request.POST.get('rem11')
 x4=request.POST.get('rem21')
 x5=request.POST.get('num11')
 x6=request.POST.get('num21')

  
 d=student101.objects.get(code=coood)
 d.code=ttc+str(d.id)
 d.nom=nn
 tem=ttc+str(d.id)
 d.pere=pp
 d.mere=mm
 d.famille=ff
 d.city=cc
 d.dat=dd
 d.quit=reec
 d.tel=tt
 d.lieu=x1
 d.segel=x2
 d.rem1=x3
 d.rem2=x4
 d.num1=x5
 d.num2=x6

 
 d.save()
 #######  update code in file of notes "regeleve"
 
 r=regeleve.objects.filter(code1=coood)
 for ri in r :
   ru=regeleve.objects.get(id=ri.id)
   ru.code1=tem
   ru.nom1=nn
   ru.pere1=pp
   ru.famille1=ff
   ru.save()
 
 
 r=regeleveps.objects.filter(code1=coood)
 for ri in r :
   ru=regeleveps.objects.get(id=ri.id)
   ru.code1=tem
   ru.nom1=nn
   ru.pere1=pp
   ru.famille1=ff
   ru.save()






 return HttpResponseRedirect(reverse('form10033'))



def dele(request, cod01):
 d=student101.objects.get(code=cod01)
 d.delete()
 return HttpResponseRedirect(reverse('form10033'))

 
def updateliste(request, cod008):
 xann=request.POST.get('anne2002')
 xann1=request.POST.get('anne2002')
 xcla1=request.POST.get('classe2002')
 xsection1=request.POST.get('section2002')
 print(xann1)
 print(cod008)
 r=regeleve.objects.filter(code1=cod008, anne1=xann1)
 for ri in r :
   ru=regeleve.objects.get(id=ri.id)
   ru.classe1=xcla1
   ru.section1=xsection1
   ru.save()

 return HttpResponseRedirect(reverse('form10033'))

def chanannemat(request,):
  x=request.POST.get('anne2031')
  y=request.POST.get('anne2033')

  ans=anne.objects.all()
  x001=request.POST.get('nom1')
  pa1="oui";pa2="oui"

  if x!=None and y!=None and x!=""  and y!="":
    sm=ps123note.objects.filter(anne=x)  
    for i in sm:
      pa1=i.anne
    
    dm=ps123note.objects.filter(anne=y)
    for j in dm:
      pa2=j.anne
  
    if pa1 != "oui" and pa2 == "oui":
     sm=ps123note.objects.filter(anne=x) 
     for u in sm:
      d=ps123note(anne=y,classe=u.classe,groupe=u.groupe,champ=u.champ,souschamp=u.souschamp,rem1=u.rem1,rem2=u.rem2,rem3=u.rem3,num1=u.num1,num2=u.num2)
      d.save()
  
  ss={'anrec':ans}
  return render(request,'app1/directeur/channemat.html',ss)
  



def listematiere (request):
  cx=request.POST.get('classe08')
  sx=request.POST.get('section08')
  
  anw=request.POST.get('anne2031')
  x=request.POST.get('anne2031')
  y=request.POST.get('anne2033')

  if x!=None and y!=None:
    sss=matiere.objects.filter(anne=x)
    for ii in sss:
      ii.anne=y
  ##############    ii.save()
   
  ans=anne.objects.all()
  x001=request.POST.get('nom1')
  print(x001)
  
  ff=matiere.objects.filter(anne=anw)
  sss={'rec': ff,'anrec': ans}
  if x001!=None:
   ff= matiere.objects.all()
   sss={'rec': ff.filter(nommatiere__contains=x001),'anrec': ans}
  if x001=="?":
   sss={'rec': ff,'anrec': ans}
  if anw!=None:
   ff= matiere.objects.all()
   sss={'rec': ff.filter(anne=anw,classe=cx,section=sx,nommatiere__contains=x001),'anrec': ans,'c':cx,'s':sx,'a':anw,'m':x001}
  
  return render(request,'app1/directeur/listematiere.html',sss)
####### نفس ما قبلها مباشرة ولكن لاح>دف ولا اضافة فقط للعرض اي فقط للسماح لاستاد المادة بالادخال



def listematierein (request):
  cx=request.POST.get('classe08')
  sx=request.POST.get('section08')
  
  anw=request.POST.get('anne2031')
  x=request.POST.get('anne2031')
  y=request.POST.get('anne2033')

  if x!=None and y!=None:
    sss=matiere.objects.filter(anne=x)
    for ii in sss:
      ii.anne=y
  ##############    ii.save()
   
  ans=anne.objects.all()
  x001=request.POST.get('nom1')
  print(x001)
  
  ff=matiere.objects.filter(anne=anw)
  sss={'rec': ff,'anrec': ans}
  if x001!=None:
   ff= matiere.objects.all()
   sss={'rec': ff.filter(nommatiere__contains=x001),'anrec': ans}
  if x001=="?":
   sss={'rec': ff,'anrec': ans}
  if anw!=None and anw != "":
   ff= matiere.objects.all()
   sss={'rec': ff.filter(anne=anw,classe=cx,section=sx,nommatiere__contains=x001),'anrec': ans,'c':cx,'s':sx,'a':anw,'m':x001}
  
  return render(request,'app1/directeur/listematierein.html',sss)





















#########################################
def updatematiere001 (request, cod):
 cc=str(cod)
 menber1=matiere.objects.all()
 sana=anne.objects.all()
 print(cc)
 return render(request,'app1/directeur/formmatiere.html', {'menber': matiere.objects.get(code=cc),'recsana':sana})

def updaterecordmatiere(request,coood):
 nn=request.POST['code']
 pp=request.POST['nommatiere1']
 mm=request.POST['classe']
 ff=request.POST['section']
 cc=request.POST['anne']
 sc=request.POST['score1']
 d=matiere.objects.get(code=coood)
 d.code=nn+str(d.id)
 d.nommatiere=pp
 d.classe=mm
 d.section=ff
 d.anne=cc
 d.score=sc
 d.save()
 return HttpResponseRedirect(reverse('form10033m'))


def rescore(request, nn1):
  x1=request.POST.get('sc0021')
  s0001=request.POST.get('q1')
  s2=request.POST.get('q2')
  s3=request.POST.get('q3')
  s4=request.POST.get('q4')
  s05=request.POST.get('nfc')
  s06=request.POST.get('nfc1')
  s07=request.POST.get('nfc2')
  s08=request.POST.get('nfc3')
  y=matiere.objects.get(code=nn1)
  c1=y.classe
  s1=y.section
  a1=y.anne
  n1=""
  dd=matiere.objects.get(code=nn1)
  dd.score=x1
  dd.sem1=s0001;dd.exa1=s2;dd.sem2=s3;dd.exa2=s4;dd.nomforcarnet=s05;dd.sousnom1=s06
  dd.sousnom2=s07;dd.sousnom3=s08
  if x1 != None:
    dd.save()


  cx=c1
  sx=s1
  
  anw=a1
  ans=anne.objects.all()
  x001=n1
  print(x001)
  
  ff=matiere.objects.all()
  sss={'rec': ff,'anrec': ans}
  if x001!=None:
   ff= matiere.objects.all()
   sss={'rec': ff.filter(nommatiere__contains=x001),'anrec': ans}
  if x001=="?":
   sss={'rec': ff,'anrec': ans}
  if anw!=None:
   ff= matiere.objects.all()
   sss={'rec': ff.filter(anne=anw,classe=cx,section=sx,nommatiere__contains=x001),'anrec': ans,'c':cx,'s':sx,'a':anw,'m':x001}
  
  return render(request,'app1/directeur/listematiere.html',sss)

##### return HttpResponseRedirect(reverse('form10033m'))

def rescorein(request, nn1):
  x1=request.POST.get('sc0021')
  s0001=request.POST.get('q1')
  s2=request.POST.get('q2')
  s3=request.POST.get('q3')
  s4=request.POST.get('q4')
  y=matiere.objects.get(code=nn1)
  c1=y.classe
  s1=y.section
  a1=y.anne
  n1=""
  dd=matiere.objects.get(code=nn1)
  #dd.score=x1
  dd.sem1=s0001;dd.exa1=s2;dd.sem2=s3;dd.exa2=s4
  #if x1 != None:
  dd.save()


  cx=c1
  sx=s1
  
  anw=a1
  ans=anne.objects.all()
  x001=n1
  print(x001)
  
  ff=matiere.objects.all()
  sss={'rec': ff,'anrec': ans}
  if x001!=None:
   ff= matiere.objects.all()
   sss={'rec': ff.filter(nommatiere__contains=x001),'anrec': ans}
  if x001=="?":
   sss={'rec': ff,'anrec': ans}
  if anw!=None:
   ff= matiere.objects.all()
   sss={'rec': ff.filter(anne=anw,classe=cx,section=sx,nommatiere__contains=x001),'anrec': ans,'c':cx,'s':sx,'a':anw,'m':x001}
  
  return render(request,'app1/directeur/listematierein.html',sss)




 
def addmatiere0024 (request):
  sana=anne.objects.all()
  x=request.POST.get('code') 
  y=request.POST.get('nommatiere1')
  z=request.POST.get('classe')
  w=request.POST.get('section')
  a=request.POST.get('anne')
  sc=request.POST.get('score1')
  if y!=None and x!=None and z!=None and w!=None and a!=None:
    data=matiere(code=x, nommatiere=y, classe=z, section=w, anne=a,score=sc)
    data.save()
    ssmat=matiere.objects.get(code=x)
    ssw=ssmat.code+str(ssmat.id)
    ssmat.code=ssw
    ssmat.nommatiere=y
    ssmat.classe=z
    ssmat.section=w
    ssmat.anne=a
    ssmat.score=sc
    ssmat.save()
  return render(request,'app1/directeur/formematiereadd.html',{'rec':sana})



def dele_m(request, cod01):
 d=matiere.objects.get(code=cod01)
 d.delete()
 return HttpResponseRedirect(reverse('form10033m'))


def listanne (request):
  x001=request.POST.get('anne')
  print(x001)
  
  ff=anne.objects.all()
  sss={'rec': ff}
  if x001!=None:
   ff= anne.objects.all()
   sss={'rec': ff.filter(anne__contains=x001)}
  if x001=="?":
   sss={'rec': ff}
  return render(request,'app1/directeur/listanne.html',sss)

def updatanne (request, cod):
 cc=str(cod)
 menber1=anne.objects.all()
 
 print(cc)
 return render(request,'app1/directeur/formanne.html', {'menber': anne.objects.get(ida=cc)})



def updaterecordanne(request,coood):
 
 pp=request.POST['anne']
 pp1=request.POST['vsem11']
 pp2=request.POST['vexa11']
 pp3=request.POST['vsem21']
 pp4=request.POST['vexa21']
 
 
 
 d=anne.objects.get(ida=coood)
 
 d.anne=pp
 d.vsem1=pp1
 d.vexa1=pp2
 d.vsem2=pp3
 d.vexa2=pp4
 d.save()
 return HttpResponseRedirect(reverse('form10033anne'))


def addanne (request):
  
  x=request.POST.get('ida') 
  y=request.POST.get('anne')
  z=request.POST.get('vsem11')
  t=request.POST.get('vexa11')
  m=request.POST.get('vsem21')
  n=request.POST.get('vexa21')

  if y!=None and x!=None :
    data=anne(ida=x, anne=y, vsem1=z, vexa1=t, vsem2=m, vexa2=n)
    data.save()
 
  return render(request,'app1/directeur/addanne.html')



def dela(request, cod01):
 d=anne.objects.get(ida=cod01)
 d.delete()
 return HttpResponseRedirect(reverse('form10033anne'))





def openaneleve (request):

 sss=anne.objects.all()
 for yty in sss:
   ddd=yty.anne
   
   print(ddd)
 
 pp=request.POST.get('anne2')
 car=structurecarnet.objects.filter(anne=pp)
 
 if pp!=None:
   eleves=student101.objects.all()
   for x in eleves:
       ww=x.code
       mm=ww
       print(ww)
       print(pp)
       ee="oui"
       int=0.0
       print (int)
       if x.quit=="ترك":
         ee="no"
       cc=regeleve.objects.all()
       for zz in cc :
          if zz.code1==mm and zz.anne1==pp :
           ee="no"
       print("e")
       print(ee)
       print(cc)


       



       if ee=='oui' and mm!='None':
           print('HI')
           for gir in car:
               data=regeleve(code1=x.code,nom1=x.nom, pere1=x.pere, famille1=x.famille,anne1=pp,
 
               anne=gir.anne,
               mois=gir.mois,
               code=gir.code,
               nombremy=gir.nombremy,
               code01=gir.code1,
               code2=gir.code2,
               code3=gir.code3,
               code4=gir.code4,
               code5=gir.code5,
               code6=gir.code6,
               code7=gir.code7,
               code8=gir.code8,
               code9=gir.code9,
               code10=gir.code10,
               code11=gir.code11,
               code12=gir.code12,
               rem1="x",
               rem2="y",
               math=0,
               physique=0,
               chimie=0,
               bio=0,
                arab1=0,    
               arab2=0,
               arab3=0,
                francais1=0,
               francais2=0,
               francais3=0 ,
               eng=0,
               civisme=0,
               historique=0,
               geographie=0 ,
               economie=0,
               socialite=0,
               philosophie=0,
               informatique=0,
               religieu=0,
               art=0,
               sport=0,
               pass1=0,matiere1=0,matiere2=0,matiere3=0,matiere4=0,matiere5=0,matiere6=0,matiere7=0,
               som1=0,
               som2=0
               )
               data.save()       
 
 mon=mony.objects.all()
 e1="oui"
 for m1 in mon:
   if m1.anne==pp:
     e1="no" 
 
 if e1=="oui" and pp!=None:
   mmm=mony(classe="ps1",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="ps2",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="ps3",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb1",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb2",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb3",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb4",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb5",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb6",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb7",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb8",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb9",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="sec-sc",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="bacc1-sc",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="bacc1-l",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="sg",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="sv",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="se",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="lh",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   
   
 return render(request,'app1/directeur/openaneleve.html',{'rec':sss})






def listenote(request):

 x001=request.POST.get('codema')
 print(x001)
 if x001!=None:  
   mm=matiere.objects.get(code=x001)
    
   browser3=regeleve.objects.filter(anne1=mm.anne,classe=mm.classe,section=mm.section)
 
 if x001==None:
   mm="a" 
   browser3="a"  
 return render(request,'app1/directeur/listenote.html',{'rec':browser3 ,'mk':mm})

  
 
##########################################
def listelevemat (request):
  anw=anne.objects.all()
  xann1=request.POST.get('anne2002')
  asaz=stok.objects.get(id=1)      
  asaz.f1=xann1
  asaz.f2=xann1
  
  ttt=""
  
  print(xann1)
  if xann1!=None:
   asaz.save()
  ttot=stok.objects.filter(id=1)
  for ww in ttot:
   xann=ww.f1
  if xann1 != None and xann1 != "":
   getclasec=regeleve.objects.filter(anne1=xann1, code=1)
  else :
    getclasec="" 
  
  x001=request.POST.get('nom1001')
  sss={'rec': getclasec,'annn' : anw, 'rt':xann}
  if x001!=None:
   sss={'rec': getclasec.filter(nom1__contains=x001),'annn' : anw, 'rt':xann}
  
  if x001=="?":
   sss={'rec': getclasec,'annn' : anw, 'rt':xann}
  
  return render(request,'app1/directeur/listelevemat.html',sss)




 
def updateliste(request, cod008, ann2002):
 #  هما نقوم بتحديد الصف لكل طالب روضة او غيره ةلكن اذا حددت الصف والشعبة تستطيع تغيير الشعبة فقط ويتم تغييرها في العلامة
 # اما اذا حددت الصف والشعبة وقمت بتغيير الصف ستمحى علامة الطالب لهذا العام
 xcla1=request.POST.get('classe2002')
 xsection1=request.POST.get('section2002')
 sssa=ann2002
 print(cod008)
 print(xcla1)
 print(xsection1)
 print(ann2002)
 ttt=""
 
 capter="no"
 rd=regeleve.objects.filter(code1=cod008, anne1=ann2002,code=1)
 for h in rd:
   if h.classe1 != "" and h.code == 1 and h.section1 != "":
      if h.section1 == xsection1 and h.classe1 != xcla1 :
       capter="oui"   
 print(capter)
 r=regeleve.objects.filter(code1=cod008, anne1=ann2002)
 for ri in r :
   if capter == "oui":
     ri.code1="fordelete"
   ri.classe1=xcla1
   ri.section1=xsection1
   if xcla1!=None and xsection1!=None: 
     ri.save()
 
 r=regeleve.objects.filter(code1="fordelete", anne1=ann2002)
 for i in r:
   d=regeleve.objects.get(id=i.id)
   d.delete()
 
 p=regeleveps.objects.filter(code1=cod008, anne1=ann2002)

 r=regeleveps.objects.filter(code1=cod008, anne1=ann2002)
 for ri in r :
   if capter == "oui":
     ri.code1="fordelete"
   ri.classe1=xcla1
   ri.section1=xsection1
   if xcla1!=None and xsection1!=None: 
     ri.save()
 
 r=regeleveps.objects.filter(code1="fordelete", anne1=ann2002)
 for i in r:
   d=regeleveps.objects.get(id=i.id)
   d.delete()
   
 rd1=regeleve.objects.filter(anne1=ann2002,code=1)

  
  
 sss={'rec': rd1,'annn' : sssa, 'rt':sssa}
  
 return render(request,'app1/directeur/listelevemat.html',sss)

###################################################################
def listenotemaitre (request):   
  b1=""
  b2=""
  b3=""
  c001=""
  m001=""
  reg=""  
  xmonth=0
  #pass01=request.POST.get('passw')
  codema=request.POST.get('codematie')
  xmonth=request.POST.get('month')
  if xmonth == None: xmonth=0
  if codema == None : codema="X"
  if codema == "" : codema="X"
  sx85score=0
  e1=0;e2=0;e3=0;e4=0
  sx85nom=""
  sx85anne=""
  sx85classe=""
  sx85section=""
  sx85score=0 ;mx=""

#############################################
  n1="";n2="";n3="";n4=""
  mast=matiere.objects.filter(code=codema)
  for mas1 in mast:
     sx85nom=mas1.nommatiere
     sx85anne=mas1.anne
     sx85classe=mas1.classe
     sx85section=mas1.section
     sx85score=mas1.score ;n1=mas1.nomforcarnet;n2=mas1.sousnom1;n3=mas1.sousnom2;n4=mas1.sousnom3 
############################################
  st=structurecarnet.objects.filter(anne=sx85anne)
  sts=structurecarnet.objects.filter(anne=sx85anne,code=xmonth)
  for m in sts:
    mx=m.mois

############################################  
  record=regeleve.objects.filter(anne1=sx85anne ,classe1=sx85classe ,section1=sx85section,code=xmonth)
 ###  للسماح او عدم السماح لمعلمي الصف بادخال عامة صف لشهر محدد
  for i in record:
    if i.rem1 == "oui" : record=""
############################################
  sss={'scorem':sx85score,'n1':n1,'n2':n2,'n3':n3,'n4':n4,'nomat':sx85nom,'mx':mx,'st':st,'sx85anne':sx85anne,'codema':codema,'reco':record,'st':st,'xmonth':xmonth}
  print(xmonth,codema)
  return render(request,'app1/directeur/notemaitreinsert.html',sss)




 
def updatenotemaitre(request, code008, nomat,xw01 ,xw02, xw03):

  # code008=id,nomat=nommatiere,xw01=nothink,xw02=codematiere,xw03=code month(0-1-2-...)
 dfdf=code008
 reg="تم الحفظ"
 note=request.POST.get('notexxl')
 k=regeleve.objects.get(id=code008)
 if nomat == "math" : k.math=note
 if nomat == "physique" :k.physique=note
 if nomat == "chimie" :k.chimie=note
 if nomat == "bio":k.bio=note
 if nomat == "arab1": k.arab1=note
 if nomat == "arab2" :k.arab2=note
 if nomat == "arab3" :k.arab3=note
 if nomat == "francais1": k.francais1=note
 if nomat == "francais2": k.francais2=note
 if nomat == "francais3":k.francais3=note
 if nomat == "eng":k.eng=note
 if nomat == "civisme":k.civisme=note
 if nomat == "historique":k.historique=note
 if nomat == "geographie":k.geographie=note
 if nomat == "economie":k.economie=note
 if nomat == "socialite": k.socialite=note
 if nomat == "philosophie":k.philosophie=note
 if nomat == "informatique": k.informatique=note
 if nomat == "art":k.art=note
 if nomat == "religieu":k.religieu=note
 if nomat == "sport":k.sport=note
 if nomat == "matiere1":k.matiere1=note
 if nomat == "matiere2":k.matiere2=note
 if nomat == "matiere3":k.matiere3=note
 if nomat == "matiere4":k.matiere4=note
 if nomat == "matiere5":k.matiere5=note
 if nomat == "matiere6":k.matiere6=note
 if nomat == "matiere7":k.matiere7=note
 
 message="non"
 if note!=None:
   try:
     k.save()   
   except: message="oui"   
 


 print("hi")
 print(note)
 swswk=regeleve.objects.filter(id=code008)
 cw1=""
 cw2=""
 cw3=""
 for swsw in swswk:
  ssss1t=swsw.math+swsw.physique+swsw.chimie+swsw.bio+swsw.arab1+swsw.arab2+swsw.arab3+swsw.francais1+swsw.francais2+swsw.francais3+swsw.philosophie+swsw.eng+swsw.civisme+swsw.historique+swsw.geographie+swsw.economie+swsw.socialite+swsw.informatique+swsw.religieu+swsw.sport+swsw.art+swsw.matiere1+swsw.matiere2+swsw.matiere3+swsw.matiere4+swsw.matiere5+swsw.matiere6+swsw.matiere7
  tratrata=swsw.code1
  
 print(ssss1t)
 cw1=swsw.classe1
 cw2=swsw.section1
 cw3=swsw.anne1
 mmtr=matiere.objects.filter(classe=cw1,section=cw2,anne=cw3)
 sbw=0
 for het in mmtr:
   sbw=sbw+het.score
 
 eswk=regeleve.objects.get(id=code008)
 eswk.som1=ssss1t
 eswk.som2=(20*ssss1t)/sbw
 eswk.save()
 
 
 ##   ##    ##
 
 c001=xw02
 m001=xw03
 pass01=xw01
  
 sx85nom=""
 sx85anne=""
 sx85classe=""
 sx85section=""
 sx85score=0  
  

 mast=matiere.objects.filter(code=xw02)
 for mas1 in mast:
   sx85nom=mas1.nommatiere
   sx85anne=mas1.anne
   sx85classe=mas1.classe
   sx85section=mas1.section
   sx85score=mas1.score  
  
 
 
 
 b1=""
 b2=""
 b3=""
 c001=""
 m001=""
 reg=""  
 xmonth=0
 #pass01=request.POST.get('passw')
 codema=request.POST.get('codematie')
 xmonth=request.POST.get('month')
 if xmonth == None: xmonth=0
 if codema == None : codema="X"
 if codema == "" : codema="X"
 sx85score=0
 e1=0;e2=0;e3=0;e4=0
 sx85nom=""
 sx85anne=""
 sx85classe=""
 sx85section=""
 sx85score=0 ;mx=""
#############################################
 n1="";n2="";n3="";n4="";codema=xw02
 mast=matiere.objects.filter(code=codema)
 for mas1 in mast:
    sx85nom=mas1.nommatiere
    sx85anne=mas1.anne
    sx85classe=mas1.classe
    sx85section=mas1.section
    sx85score=mas1.score ;n1=mas1.nomforcarnet;n2=mas1.sousnom1;n3=mas1.sousnom2;n4=mas1.sousnom3 
###########################################
 st=structurecarnet.objects.filter(anne=sx85anne)
 sts=structurecarnet.objects.filter(anne=sx85anne,code=xw03)
 for m in sts:
   mx=m.mois
############################################  
 record=regeleve.objects.filter(anne1=sx85anne ,classe1=sx85classe ,section1=sx85section,code=xw03)
###########################################
 sss={'message': message,'ii': dfdf,'scorem':sx85score,'n1':n1,'n2':n2,'n3':n3,'n4':n4,'nomat':sx85nom,'mx':mx,'st':st,'sx85anne':sx85anne,'codema':codema,'reco':record,'st':st,'xmonth':xw03}
  
 
 
 
 return render(request,'app1/directeur/notemaitreinsert.html',sss)

###################################################
############################
##   كود المعلمين - الكود لكل استاذ 
#########################################################

def listeusermaitre (request):
  x001=request.POST.get('nom1')
  
  ff=stok.objects.all()
  sss={'rec': ff}
  
  if x001!=None:
   ff= stok.objects.all()
   sss={'rec': ff.filter(name__contains=x001)}
    
    
  if x001=="?":
   sss={'rec': ff}
   
  
  
  
  return render(request,'app1/directeur/listeusermaitre.html',sss)



def delmaitreuser(request, cod01):
 d=stok.objects.get(user=cod01)
 d.delete()
 return HttpResponseRedirect(reverse('form100959'))



def updtusermaitre (request, cod):
 
 menber01=stok.objects.all()
 
 return render(request,'app1/directeur/formeusermaitre.html', {'rec': stok.objects.get(user=cod)})



def updaterecordusermaitre(request,coood):
 
 pp=request.POST['user1']
 nn=request.POST['nom']
 ss=stok.objects.filter(user=coood)
 ffg=request.POST['pasmd']


 for aa in ss:
   wq=aa.id
 d=stok.objects.get(user=coood)
 
 d.user=pp+str(wq)
 d.name=nn
 d.passmod=ffg
 d.save()
 return HttpResponseRedirect(reverse('form100959'))


def addusermaitre(request):
  
  x=request.POST.get('user') 
  y=request.POST.get('nom')
  z=request.POST.get('pasmd')
  if y!=None and x!=None :
    data=stok(user=x, name=y,passmod=z)
    data.save()
    dd=stok.objects.filter(user=x)
    for t in dd:
      sd=t.id
    data=stok.objects.get(id=sd)    
    data.user=x+str(sd)
    data.save()
    
  return render(request,'app1/directeur/addusermaitre.html')
######################################################################################
#  insert notes  by directeur
#########################################################


def listenotedirect (request):   
 and1=anne.objects.all()
 
 xx1=request.POST.get('anne2002')
 xx2=request.POST.get('classe2002')
 xx3=request.POST.get('section2002')
 xx4=request.POST.get('month')
 
 xsd=xx4
 
 subvf=stok11.objects.filter(id=1)
 for ssyy in subvf:
  tssyy4=ssyy.temp
  tssyy3=ssyy.anne
  tssyy1=ssyy.classe
  tssyy2=ssyy.section
  
 
 
 xx1=tssyy3
 xx2=tssyy1
 xx3=tssyy2
 
 xx4=tssyy4
 print(xx4)
 print(xx2)
 print(xx3)
 print(xx1)
 
 if xx4=="all":
  and1="all"
  sata=regeleve.objects.filter(anne1=xx1,classe1=xx2,section1=xx3).order_by('-som1')
 else:
  sata=regeleve.objects.filter(anne1=xx1,classe1=xx2,section1=xx3,mois=xx4).order_by('-som1')
 print(sata)
 #get score
 scmat=0 ;scphy=0 ;scchi=0;scbio=0;scara1=0;scara2=0;scara3=0;scfra1=0
 scfra2=0;scfra3=0; sceng=0; scciv=0;schis=0;scgeo=0;sceco=0;scsoc=0;scphi=0;scinf=0;scart=0
 screl=0;scspo=0;scpas=0
 score1=matiere.objects.filter(classe=xx2 ,section=xx3 , anne=xx1)
 sctotale=0
 for sc1 in score1:
   if sc1.nommatiere=='math':
     scmat=sc1.score
   if sc1.nommatiere=='physique':
     scphy=sc1.score
   if sc1.nommatiere=='chimie':
     scchi=sc1.score
   if sc1.nommatiere=='bio':
     scbio=sc1.score
   if sc1.nommatiere=='arab1':
     scara1=sc1.score
   if sc1.nommatiere=='arab2':
     scara2=sc1.score
   if sc1.nommatiere=='arab3':
     scara3=sc1.score
   if sc1.nommatiere=='francais1':
     scfra1=sc1.score
   if sc1.nommatiere=='francais2':
     scfra2=sc1.score
   if sc1.nommatiere=='francais3':
     scfra3=sc1.score
   if sc1.nommatiere=='eng':
     sceng=sc1.score
   if sc1.nommatiere=='civisme':
     scciv=sc1.score
   if sc1.nommatiere=='historique':
     schis=sc1.score
   if sc1.nommatiere=='geographie':
     scgeo=sc1.score
   if sc1.nommatiere=='economie':
     sceco=sc1.score
   if sc1.nommatiere=='socialite':
     scsoc=sc1.score
   if sc1.nommatiere=='philosophie':
     scphi=sc1.score
   if sc1.nommatiere=='informatique':
     scinf=sc1.score
   if sc1.nommatiere=='art':
     scart=sc1.score
   if sc1.nommatiere=='religieu':
     screl=sc1.score
   if sc1.nommatiere=='sport':
     scspo=sc1.score
   if sc1.nommatiere=='pass1':
     scpas=sc1.score
     
     
   sctotale=sctotale+sc1.score 
 if xx1!=None and xx2!=None and xx3!=None and xx4!=None :
   sss={'somt': sctotale,'root4': tssyy4,'root1': tssyy1,'root2':tssyy2,'root3':tssyy3, 'x1':xx1,'x2':xx2,'x3':xx3,'x4':xsd,'annn':and1,'month001':xsd, 'lss':xsd,'reco': sata, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas}
 if xx1==None or xx2==None or xx3==None or xx4==None:
   sss={'somt': sctotale,'root4': tssyy4,'root1': tssyy1,'root2':tssyy2,'root3':tssyy3, 'x1':None,'x2':None,'x3':None,'x4':None,'annn':and1,'month001':None, 'lss':None, 'reco': sata, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas}
     
 
 return render(request,'app1/directeur/notedirectinsert.html',sss)




 
def updatenotedirect(request, somtxx, idsa, codea1, anne2025,classe2025,section2025,month2025):
  sdia=idsa
  x1=request.POST.get('math1') 
  x2=request.POST.get('physique1')
  x3=request.POST.get('chimie1') 
  x4=request.POST.get('bio1') 
  x5=request.POST.get('arab11') 
  x6=request.POST.get('arab21') 
  x7=request.POST.get('arab31') 
  x8=request.POST.get('francais11') 
  x9=request.POST.get('francais21') 
  x10=request.POST.get('francais31') 
  x010=request.POST.get('english1')
  x11=request.POST.get('philosophie1') 
  x12=request.POST.get('economie1') 
  x13=request.POST.get('socialite1') 
  x14=request.POST.get('historique1') 
  x15=request.POST.get('geographie1') 
  x16=request.POST.get('civisme1') 
  x17=request.POST.get('art1') 
  x18=request.POST.get('religieu1') 
  x19=request.POST.get('informatique1') 
  x20=request.POST.get('sport1')
  dwq=regeleve.objects.get(id=sdia)
  div=somtxx
  s=0
  if x1!=None:
   dwq.math=x1 
   s=s+Decimal(x1)
  else: 
   dwq.math=0 
   
  if x2!=None:
   dwq.physique=x2
   s=s+Decimal(x2)
  else:
    dwq.physique=0
     
  if x3!=None: 
   dwq.chimie=x3
   s=s+Decimal(x3)
  else:
    dwq.chimie=0
  
  if x4!=None: 
   dwq.bio=x4
   s=s+Decimal(x4)
  else:
    dwq.bio=0
  
  if x5!=None: 
   dwq.arab1=x5
   s=s+Decimal(x5)
  else:
    dwq.arab1=0
  
  if x6!=None: 
   dwq.arab2=x6
   s=s+Decimal(x6)
  else:
    dwq.arab2=0
  
  if x7!=None: 
   dwq.arab3=x7
   s=s+Decimal(x7)
  else:
    dwq.arab3=0
  
  if x8!=None: 
   dwq.francais1=x8
   s=s+Decimal(x8)
  else:
    dwq.francais1=0
  
  if x9!=None: 
   dwq.francais2=x9
   s=s+Decimal(x9)
  else:
    dwq.francais2=0
  
  if x10!=None: 
   dwq.francais3=x10
   s=s+Decimal(x10)
  else:
    dwq.francais3=0
  
  if x010!=None: 
   dwq.eng=x010
   s=s+Decimal(x010)
  else:
    dwq.eng=0
  
  
  if x11!=None: 
   dwq.philosophie=x11
   s=s+Decimal(x11)
  else:
    dwq.philosophie=0
  
  if x12!=None: 
   dwq.economie=x12
   s=s+Decimal(x12)
  else:
    dwq.economie=0
  
  if x13!=None: 
   dwq.socialite=x13
   s=s+Decimal(x13)
  else:
    dwq.socialite=0
  
  if x14!=None: 
   
   dwq. historique=x14
   s=s+Decimal(x14)
  else:
    dwq.historique=0
  
  if x15!=None: 
   dwq.geographie=x15
   s=s+Decimal(x15)
  else:
    dwq.geographie=0
  
  if x16!=None: 
   dwq.civisme=x16
   s=s+Decimal(x16)
  else:
    dwq.civisme=0
  
  if x17!=None: 
   dwq.art=x17
   s=s+Decimal(x17)
  else:
    dwq.art=0
  
  if x18!=None: 
   dwq.religieu=x18
   s=s+Decimal(x18)
  else:
    dwq.religieu=0
  
  if x19!=None: 
   dwq.informatique=x19
   s=s+Decimal(x19)
  else:
    dwq.informatique=0
  
  if x20!=None: 
   dwq.sport=x20
   s=s+Decimal(x20)
  else:
    dwq.sport=0
  
  print(s)
  freq=round((20*s)/div,2)
  print(freq)
  dwq.som1=Decimal(s)
  dwq.som2=freq
  dwq.pass1=0.0
  dwq.save()
          #        حساب المعدلاتcodeleve, anne2025,classe2025,section2025 
             # نهاية حساب المعدلات
  xx1=anne2025
  xx2=classe2025
  xx3=section2025
  xx4=month2025
 
  xsd=xx4
 
  if xx4=="all":
   sata=regeleve.objects.filter(anne1=xx1,classe1=xx2,section1=xx3)
  else:
   sata=regeleve.objects.filter(id=sdia)
  #get score
  scmat=0 ;scphy=0 ;scchi=0;scbio=0;scara1=0;scara2=0;scara3=0;scfra1=0
  scfra2=0;scfra3=0; sceng=0; scciv=0;schis=0;scgeo=0;sceco=0;scsoc=0;scphi=0;scinf=0;scart=0
  screl=0;scspo=0;scpas=0
  score1=matiere.objects.filter(classe=xx2 ,section=xx3 , anne=xx1)
  for sc1 in score1:
    if sc1.nommatiere=='math':
      scmat=sc1.score
    if sc1.nommatiere=='physique':
      scphy=sc1.score
    if sc1.nommatiere=='chimie':
      scchi=sc1.score
    if sc1.nommatiere=='bio':
      scbio=sc1.score
    if sc1.nommatiere=='arab1':
      scara1=sc1.score
    if sc1.nommatiere=='arab2':
      scara2=sc1.score
    if sc1.nommatiere=='arab3':
      scara3=sc1.score
    if sc1.nommatiere=='francais1':
      scfra1=sc1.score
    if sc1.nommatiere=='francais2':
      scfra2=sc1.score
    if sc1.nommatiere=='francais3':
      scfra3=sc1.score
    if sc1.nommatiere=='eng':
      sceng=sc1.score
    if sc1.nommatiere=='civisme':
      scciv=sc1.score
    if sc1.nommatiere=='historique':
      schis=sc1.score
    if sc1.nommatiere=='geographie':
      scgeo=sc1.score
    if sc1.nommatiere=='economie':
      sceco=sc1.score
    if sc1.nommatiere=='socialite':
      scsoc=sc1.score
    if sc1.nommatiere=='philosophie':
      scphi=sc1.score
    if sc1.nommatiere=='informatique':
      scinf=sc1.score
    if sc1.nommatiere=='art':
      scart=sc1.score
    if sc1.nommatiere=='religieu':
      screl=sc1.score
    if sc1.nommatiere=='sport':
      scspo=sc1.score
    if sc1.nommatiere=='pass1':
      scpas=sc1.score
 
 
  subvf=stok11.objects.filter(id=1)
  for ssyy in subvf:
    tssyy=ssyy.temp
  
  ttssyy=tssyy


  print(xx1,xx2,xx3,xx4)
  if xx1!=None and xx2!=None and xx3!=None and xx4!=None :
     sss={'somt': somtxx,'root4':ttssyy ,'x1':xx1,'x2':xx2,'x3':xx3,'x4':xsd,'annn':xx1,'month001':xsd, 'lss':xsd,'reco': sata, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas}
  if xx1==None or xx2==None or xx3==None or xx4==None:
     sss={'somt': somtxx, 'root4':ttssyy,'x1':None,'x2':None,'x3':None,'x4':None,'annn':xx1,'month001':None, 'lss':None, 'reco': sata, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas}
  


  return render(request,'app1/directeur/notedirectinsert.html',sss)

###############################################
##    تسجيل الدخول الى العلامات
def regcarnet(request):
  rec=anne.objects.all()
  x1=request.POST.get('anne2030') 
  x2=request.POST.get('classe2030')
  x3=request.POST.get('section2030') 
  x4=request.POST.get('month2030')
  x5= request.POST.get('user2030')
  test=stok.objects.filter(user=x5)
  note= "  لم يتم التسجيل كلمة السر خطأ"
  for k in test:
    if k.user ==  x5:
      note= "  تم التسجيل كلمة السر صحيحة"
      tratra=stok11.objects.get(id=1)
      tratra.temp=x4
      tratra.anne=x1
      tratra.classe=x2
      tratra.section=x3
      tratra.save()
  sss={'rec0' :rec ,'rem' :note}    
  return render(request,'app1/directeur/registreforcarnet.html',sss)
################################################
def fasel(div001,code001 ,anne001 ,classe001, section001, mois1, mois2, result):
       ### 1ere semestre
        saw1=code001
        saw2=anne001
        saw3=classe001
        saw4=section001
        satanew1=regeleve.objects.filter(code1=saw1,anne1=saw2,classe1=saw3,section1=saw4,mois=mois1)
        for st1 in satanew1:
         x1=st1.math
         x2=st1.physique;x3=st1.chimie
         x4=st1.bio;x5=st1.arab1;x6=st1.arab2;x7=st1.arab3;x8=st1.francais1
         x9=st1.francais2;x10=st1.francais3;x11=st1.eng;x12=st1.philosophie
         x13=st1.economie;x14=st1.civisme;x15=st1.geographie
         x16=st1.historique;x17=st1.art;x18=st1.religieu;x19=st1.informatique;x20=st1.sport;x21=st1.socialite
        satanew2=regeleve.objects.filter(code1=saw1,anne1=saw2,classe1=saw3,section1=saw4,mois=mois2)
        for st2 in satanew2:
         y1=st2.math;y2=st2.physique;y3=st2.chimie;y4=st2.bio;y5=st2.arab1;y6=st2.arab2;y7=st2.arab3;y8=st2.francais1
         y9=st2.francais2;y10=st2.francais3;y11=st2.eng;y12=st2.philosophie;y13=st2.economie;y14=st2.civisme;y15=st2.geographie
         y16=st2.historique;y17=st2.art;y18=st2.religieu;y19=st2.informatique;y20=st2.sport;y21=st2.socialite
        
              
        satanewm1=regeleve.objects.get(code1=saw1,anne1=saw2,classe1=saw3,section1=saw4,mois=result)
        satanewm1.math=round((x1+y1)/2,2)    
        satanewm1.physique=round((x2+y2)/2,2)
        satanewm1.chimie=round((x3+y3)/2,2)
        satanewm1.bio=round((x4+y4)/2,2)
        satanewm1.arab1=round((x5+y5)/2,2)
        satanewm1.arab2=round((x6+y6)/2,2)
        satanewm1.arab3=round((x7+y7)/2,2)
        satanewm1.francais1=round((x8+y8)/2,2)
        satanewm1.francais2=round((x9+y9)/2,2)
        satanewm1.francais3=round((x10+y10)/2,2)
        satanewm1.eng=round((x11+y11)/2,2)
        satanewm1.philosophie=round((x12+y12)/2,2)
        satanewm1.economie=round((x13+y13)/2,2)
        satanewm1.civisme=round((x14+y14)/2,2)
        satanewm1.geographie=round((x15+y15)/2,2)
        satanewm1.historique=round((x16+y16)/2,2)
        satanewm1.art=round((x17+y17)/2,2)
        satanewm1.religieu=round((x18+y18)/2,2)
        satanewm1.informatique=round((x19+y19)/2,2)
        satanewm1.sport=round((x20+y20)/2,2)
        satanewm1.socialite=round((x21+y21)/2,2)
        satanewm1.som1=round((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15+x16+x17+x18+x19+x20+x21+y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21)/2,2)
        s=(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15+x16+x17+x18+x19+x20+x21+y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21)/2
        freq=round((20*s)/div001,2)
        satanewm1.som2=freq
   
        satanewm1.save()
 
###############
#  وضع الدرجات

def daragate(xw01,xw02,xw03,coded):
  
  daraga=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=coded)
  for  gg in daraga:
    gg.pass1=0
    gg.save()
  
  
  dar=1
  daraga=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=coded)
  perio=len(daraga)
  sxsom1=0
  sxcode=0
  for i in daraga:
   if i.som1 > sxsom1: sxsom1=i.som1; sxcode=i.code1

  print(perio)
  print(sxsom1,sxcode)


  daraga1=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=coded,som1=sxsom1)
  for j in daraga1: 
    dsds=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code=coded,id=j.id)
    dsds.pass1=dar
    dsds.save()
  
  dar=dar+1
  for ccc in range(perio):
   daraga=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=coded,pass1=0)
   sxsom1=0
   sxcode=0
   ccc=0
   for i in daraga:
      if i.som1 > sxsom1: sxsom1=i.som1; sxcode=i.code1

   daraga1=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=coded,som1=sxsom1,pass1=0)
   for j in daraga1: 
      dsds=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code=coded,id=j.id)
      dsds.pass1=dar
      ccc=1
      dsds.save()
   
   if ccc==1 : dar=dar+1
    

#####   نهاية وضع الدرجات
##############################








##################################
###############################################
##    تسجيل الدخول الى العلامات
def rasmicarnet(request):
  rec=anne.objects.all()
  xw01=request.POST.get('anne2030') 
  xw02=request.POST.get('classe2030')
  xw03=request.POST.get('section2030') 
  xw05= request.POST.get('user2030')
  test=stok.objects.filter(user=xw05)
  note= "  لم يتم الاصدار كلمة السر خطأ"
  for k in test:
    if k.user ==  xw05:
      note= "  تم الاصدار كلمة السر صحيحة"
 
 ###############حساب مجموع العام لمواد الصف
#get score
  scmat=0 ;scphy=0 ;scchi=0;scbio=0;scara1=0;scara2=0;scara3=0;scfra1=0
  scfra2=0;scfra3=0; sceng=0; scciv=0;schis=0;scgeo=0;sceco=0;scsoc=0;scphi=0;scinf=0;scart=0
  screl=0;scspo=0;scpas=0;sctotale=0;scm1=0;scm2=0;scm3=0;scm4=0;scm5=0;scm6=0;scm7=0
  sctotale=0
  score1=matiere.objects.filter(classe=xw02 ,section=xw03 , anne=xw01)
  for sc1 in score1:
    if sc1.nommatiere=='math':
      scmat=sc1.score
    if sc1.nommatiere=='physique':
      scphy=sc1.score
    if sc1.nommatiere=='chimie':
      scchi=sc1.score
    if sc1.nommatiere=='bio':
      scbio=sc1.score
    if sc1.nommatiere=='arab1':
      scara1=sc1.score
    if sc1.nommatiere=='arab2':
      scara2=sc1.score
    if sc1.nommatiere=='arab3':
      scara3=sc1.score
    if sc1.nommatiere=='francais1':
      scfra1=sc1.score
    if sc1.nommatiere=='francais2':
      scfra2=sc1.score
    if sc1.nommatiere=='francais3':
      scfra3=sc1.score
    if sc1.nommatiere=='eng':
      sceng=sc1.score
    if sc1.nommatiere=='civisme':
      scciv=sc1.score
    if sc1.nommatiere=='historique':
      schis=sc1.score
    if sc1.nommatiere=='geographie':
      scgeo=sc1.score
    if sc1.nommatiere=='economie':
      sceco=sc1.score
    if sc1.nommatiere=='socialite':
      scsoc=sc1.score
    if sc1.nommatiere=='philosophie':
      scphi=sc1.score
    if sc1.nommatiere=='informatique':
      scinf=sc1.score
    if sc1.nommatiere=='art':
      scart=sc1.score
    if sc1.nommatiere=='religieu':
      screl=sc1.score
    if sc1.nommatiere=='sport':
      scspo=sc1.score
    if sc1.nommatiere=='pass1':
      scpas=sc1.score
    if sc1.nommatiere=='matiere1':
      scm1=sc1.score
    if sc1.nommatiere=='matiere2':
       scm2=sc1.score
    if sc1.nommatiere=='matiere3':
       scm3=sc1.score
    if sc1.nommatiere=='matiere4':
       scm4=sc1.score
    if sc1.nommatiere=='matiere5':
       scm5=sc1.score
    if sc1.nommatiere=='matiere6':
       scm6=sc1.score
    if sc1.nommatiere=='matiere7':
       scm7=sc1.score

    sctotale=sctotale+sc1.score   
  
  print(sctotale)  
 ###############################  حساب المعدلات   
  princ=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03) 
  div=sctotale
  for pr1 in princ:
       if pr1.nombremy > 1: 
            pr1.math=0;pr1.physique=0;pr1.chimie=0;pr1.bio=0;pr1.arab1=0;pr1.arab2=0;pr1.arab3=0
            pr1.francais1=0;pr1.francais2=0;pr1.francais3=0;pr1.eng=0;pr1.philosophie=0;pr1.economie=0
            pr1.civisme=0;pr1.geographie=0;pr1.historique=0;pr1.art=0;pr1.religieu=0
            pr1.informatique=0;pr1.sport=0;pr1.socialite=0
            pr1.matiere1=0;pr1.matiere2=0;pr1.matiere3=0;pr1.matiere4=0;pr1.matiere5=0;pr1.matiere6=0
            pr1.matiere7=0
            pr1.save()
 
 
 
 
 
  princ=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03) .order_by('code1').order_by('code')
  div=sctotale
  for pr1 in princ:
       if pr1.nombremy > 1: 
          codeleve=pr1.code1;    
          if pr1.code01 != 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code01)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code2 != 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code2)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
          if pr1.code3 != 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code3)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code4 != 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code4)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code5 != 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code5)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code6 != 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code6)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code7 > 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code7)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code8 > 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code8)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code9 > 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code9)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code10 > 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code10)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code11 > 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code11)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
       
          if pr1.code12 > 0:
       
            taw=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code1=codeleve,code=pr1.code12)
            x=pr1.math;y=taw.math;  pr1.math=x+y     
            x=pr1.physique;y=taw.physique;  pr1.physique=x+y
            x=pr1.chimie;y=taw.chimie;  pr1.chimie=x+y
            x=pr1.bio;y=taw.bio;  pr1.bio=x+y
            x=pr1.arab1;y=taw.arab1;  pr1.arab1=x+y;x=pr1.arab2;y=taw.arab2;  pr1.arab2=x+y;x=pr1.arab3;y=taw.arab3;  pr1.arab3=x+y
            x=pr1.francais1;y=taw.francais1;pr1.francais1=x+y;x=pr1.francais2;y=taw.francais2;pr1.francais2=x+y
            x=pr1.francais3;y=taw.francais3;pr1.francais3=x+y
            x=pr1.eng;y=taw.eng;pr1.eng=x+y;x=pr1.philosophie;y=taw.philosophie;pr1.philosophie=x+y
            x=pr1.economie;y=taw.economie;pr1.economie=x+y;x=pr1.civisme;y=taw.civisme;pr1.civisme=x+y
            x=pr1.geographie;y=taw.geographie;pr1.geographie=x+y
            x=pr1.historique;y=taw.historique;pr1.historique=x+y
            x=pr1.art;y=taw.art;pr1.art=x+y;x=pr1.religieu;y=taw.religieu;pr1.religieu=x+y
            x=pr1.informatique;y=taw.informatique;pr1.informatique=x+y
            x=pr1.sport;y=taw.sport;pr1.sport=x+y;x=pr1.socialite;y=taw.socialite;pr1.socialite=x+y
            x=pr1.matiere1;y=taw.matiere1;pr1.matiere1=x+y
            x=pr1.matiere2;y=taw.matiere2;pr1.matiere2=x+y
            x=pr1.matiere3;y=taw.matiere3;pr1.matiere3=x+y
            x=pr1.matiere4;y=taw.matiere4;pr1.matiere4=x+y
            x=pr1.matiere5;y=taw.matiere5;pr1.matiere5=x+y
            x=pr1.matiere6;y=taw.matiere6;pr1.matiere6=x+y
            x=pr1.matiere7;y=taw.matiere7;pr1.matiere7=x+y
            pr1.save()
          princ22=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=pr1.code,code1=pr1.code1) 
          div=sctotale
          for pr1 in princ22:
                if pr1.nombremy > 1: 
                     pr1.math=round(pr1.math/pr1.nombremy,2)
                     pr1.physique=round((pr1.physique)/pr1.nombremy,2)
                     pr1.chimie=round((pr1.chimie)/pr1.nombremy,2)
                     pr1.bio=round((pr1.bio)/pr1.nombremy,2)
                     pr1.arab1=round((pr1.arab1)/pr1.nombremy,2)
                     pr1.arab2=round((pr1.arab2)/pr1.nombremy,2)
                     pr1.arab3=round((pr1.arab3)/pr1.nombremy,2)
                     pr1.francais1=round((pr1.francais1)/pr1.nombremy,2)
                     pr1.francais2=round((pr1.francais2)/pr1.nombremy,2)
                     pr1.francais3=round((pr1.francais3)/pr1.nombremy,2)
                     pr1.eng=round((pr1.eng)/pr1.nombremy,2)
                     pr1.socialite=round((pr1.socialite)/pr1.nombremy,2)
                     pr1.economie=round((pr1.economie)/pr1.nombremy,2)
                     pr1.philosophie=round((pr1.philosophie)/pr1.nombremy,2)
                     pr1.art=round((pr1.art)/pr1.nombremy,2)
                     pr1.religieu=round((pr1.religieu)/pr1.nombremy,2)
                     pr1.sport=round((pr1.sport)/pr1.nombremy,2)
                     pr1.informatique=round((pr1.informatique)/pr1.nombremy,2)
                     pr1.matiere1=round((pr1.matiere1)/pr1.nombremy,2)
                     pr1.matiere2=round((pr1.matiere2)/pr1.nombremy,2)
                     pr1.matiere3=round((pr1.matiere3)/pr1.nombremy,2)
                     pr1.matiere4=round((pr1.matiere4)/pr1.nombremy,2)
                     pr1.matiere5=round((pr1.matiere5)/pr1.nombremy,2)
                     pr1.matiere6=round((pr1.matiere6)/pr1.nombremy,2)
                     pr1.matiere7=round((pr1.matiere7)/pr1.nombremy,2)
                     pr1.civisme=round((pr1.civisme)/pr1.nombremy,2)
                     pr1.historique=round((pr1.historique)/pr1.nombremy,2)
                     pr1.geographie=round((pr1.geographie)/pr1.nombremy,2)
                     pr1.save()
      
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        
  princ=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03) 
  div=sctotale
  for st1 in princ:
         x1=st1.math
         x2=st1.physique;x3=st1.chimie
         x4=st1.bio;x5=st1.arab1;x6=st1.arab2;x7=st1.arab3;x8=st1.francais1
         x9=st1.francais2;x10=st1.francais3;x11=st1.eng;x12=st1.philosophie
         x13=st1.economie;x14=st1.civisme;x15=st1.geographie
         x16=st1.historique;x17=st1.art;x18=st1.religieu;x19=st1.informatique;x20=st1.sport;x21=st1.socialite
         x22=st1.matiere1;x23=st1.matiere2;x24=st1.matiere3;x25=st1.matiere4;x26=st1.matiere5;x27=st1.matiere6
         x28=st1.matiere7
         totays=x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15+x16+x17+x18+x19+x20+x21+x22+x23+x24+x25+x26+x27+x28
         st1.som1=round(totays,2)
         st1.som2=round((20*totays)/div,2)
         st1.save()
         
#######################         
#####   وضع الدرجات       
  xw01=request.POST.get('anne2030') 
  xw02=request.POST.get('classe2030')
  xw03=request.POST.get('section2030') 
  xw05= request.POST.get('user2030')
  
  daraga=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=1)
  for  gg in daraga:
    gg.pass1=0
    gg.save()
  
  
  dar=1
  daraga=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=1)
  perio=len(daraga)
  sxsom1=0
  sxcode=0
  for i in daraga:
   if i.som1 > sxsom1: sxsom1=i.som1; sxcode=i.code1

  print(perio)
  print(sxsom1,sxcode)


  daraga1=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=1,som1=sxsom1)
  for j in daraga1: 
    dsds=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code=1,id=j.id)
    dsds.pass1=dar
    dsds.save()
  
  dar=dar+1
  for ccc in range(perio):
   daraga=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=1,pass1=0)
   sxsom1=0
   sxcode=0
   ccc=0
   for i in daraga:
      if i.som1 > sxsom1: sxsom1=i.som1; sxcode=i.code1

   daraga1=regeleve.objects.filter(anne1=xw01,classe1=xw02,section1=xw03,code=1,som1=sxsom1,pass1=0)
   for j in daraga1: 
      dsds=regeleve.objects.get(anne1=xw01,classe1=xw02,section1=xw03,code=1,id=j.id)
      dsds.pass1=dar
      ccc=1
      dsds.save()
   
   if ccc==1 : dar=dar+1
  jhgf=structurecarnet.objects.filter(anne=xw01)  
  for u in jhgf:
   daragate(xw01,xw02,xw03,u.code)
  
  print("hi")
  print(sctotale)      


#####   نهاية وضع الدرجات
##############################

 ############################################### نهاية حساب المعدلات للصف المذكور
  sss={'rec0' :rec ,'rem' :note}    
  return render(request,'app1/directeur/moyenrasmi.html',sss)
  
   
##############################################اصدار بطاقات العلامات لصف كامل  


def exportcarnets (request):   
 and1=anne.objects.all()
 tnom=request.POST.get('nom2030')
 xx1=request.POST.get('anne2030')
 xx2=request.POST.get('classe2030')
 xx3=request.POST.get('section2030')
 xx4="all"
 
 xsd=xx4
 
 
 recans=anne.objects.all()
 
 
 imm="x"
 tssyy1=xx1
 tssyy2=xx2
 tssyy3=xx3
 tssyy4=xx4
 and1="all"
 iii=school.objects.filter(id=1)
 for xsxs in iii:
  imm=xsxs.imag
 
 if tnom!=None:
   sata=regeleve.objects.filter(anne1=xx1,classe1=xx2,section1=xx3,nom1__contains=tnom).order_by('code1').order_by('id')
 else:
   sata=regeleve.objects.filter(anne1=xx1,classe1=xx2,section1=xx3).order_by('code1').order_by('id')
  #get score
 scmat=0 ;scphy=0 ;scchi=0;scbio=0;scara1=0;scara2=0;scara3=0;scfra1=0
 scfra2=0;scfra3=0; sceng=0; scciv=0;schis=0;scgeo=0;sceco=0;scsoc=0;scphi=0;scinf=0;scart=0
 screl=0;scspo=0;scpas=0;scm1=0;scm2=0;scm3=0;scm4=0;scm5=0;scm6=0;scm7=0
 score1=matiere.objects.filter(classe=xx2 ,section=xx3 , anne=xx1)
 sctotale=0
 for sc1 in score1:
   if sc1.nommatiere=='math':
     scmat=sc1.score
   if sc1.nommatiere=='physique':
     scphy=sc1.score
   if sc1.nommatiere=='chimie':
     scchi=sc1.score
   if sc1.nommatiere=='bio':
     scbio=sc1.score
   if sc1.nommatiere=='arab1':
     scara1=sc1.score
   if sc1.nommatiere=='arab2':
     scara2=sc1.score
   if sc1.nommatiere=='arab3':
     scara3=sc1.score
   if sc1.nommatiere=='francais1':
     scfra1=sc1.score
   if sc1.nommatiere=='francais2':
     scfra2=sc1.score
   if sc1.nommatiere=='francais3':
     scfra3=sc1.score
   if sc1.nommatiere=='eng':
     sceng=sc1.score
   if sc1.nommatiere=='civisme':
     scciv=sc1.score
   if sc1.nommatiere=='historique':
     schis=sc1.score
   if sc1.nommatiere=='geographie':
     scgeo=sc1.score
   if sc1.nommatiere=='economie':
     sceco=sc1.score
   if sc1.nommatiere=='socialite':
     scsoc=sc1.score
   if sc1.nommatiere=='philosophie':
     scphi=sc1.score
   if sc1.nommatiere=='informatique':
     scinf=sc1.score
   if sc1.nommatiere=='art':
     scart=sc1.score
   if sc1.nommatiere=='religieu':
     screl=sc1.score
   if sc1.nommatiere=='sport':
     scspo=sc1.score
   if sc1.nommatiere=='pass1':
     scpas=sc1.score
   if sc1.nommatiere=='matiere1':
     scm1=sc1.score 
   if sc1.nommatiere=='matiere2':
     scm2=sc1.score 
     
   if sc1.nommatiere=='matiere3':
     scm3=sc1.score 
     
   if sc1.nommatiere=='matiere4':
     scm4=sc1.score 
     
   if sc1.nommatiere=='matiere5':
     scm5=sc1.score 
     
   if sc1.nommatiere=='matiere6':
     scm6=sc1.score 
     
   if sc1.nommatiere=='matiere7':
     scm7=sc1.score 
     
     
   sctotale=sctotale+sc1.score 


 nms=structurecarnet.objects.filter(anne=tssyy1).order_by('code')  
 if xx1!=None and xx2!=None and xx3!=None and xx4!=None :
   sss={'score1': score1,'nms':nms,'ims': imm,'recann': recans, 'somt': sctotale,'root4': tssyy4,'root1': tssyy1,'root2':tssyy2,'root3':tssyy3, 'x1':xx1,'x2':xx2,'x3':xx3,'x4':xsd,'annn':and1,'month001':xsd, 'lss':xsd,'reco': sata, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas,'ascm1':scm1,'ascm2':scm2,'ascm3':scm3,'ascm4':scm4,'ascm5':scm5,'ascm6':scm6,'ascm7':scm7}
 if xx1==None or xx2==None or xx3==None or xx4==None:
   sss={'score1': score1,'nms':nms,'ims': imm,'recann': recans,'somt': sctotale,'root4': tssyy4,'root1': tssyy1,'root2':tssyy2,'root3':tssyy3, 'x1':None,'x2':None,'x3':None,'x4':None,'annn':and1,'month001':None, 'lss':None, 'reco': sata, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas,'ascm1':scm1,'ascm2':scm2,'ascm3':scm3,'ascm4':scm4,'ascm5':scm5,'ascm6':scm6,'ascm7':scm7}
     
 
 return render(request,'app1/directeur/exportcarnets.html',sss)
#############################################################################
### carnet d'un seul eleve



def carnetuneleve (request):   
 and1=anne.objects.all()
 xx1=request.POST.get('anne2030')
 xx2=request.POST.get('code2030')
 xmoisx=structurecarnet.objects.filter(anne=xx1)
 
 xx4="all"
 xsd=xx4
 recans=anne.objects.all()
 tssyy1=xx1
 tssyy2=xx2
 tssyy4=xx4
 and1="all"
 if tssyy1 != None and tssyy2!=None:
    sata=regeleve.objects.filter(anne1=tssyy1,code1=tssyy2).order_by('code').order_by('code1')
 else:
   sata=regeleve.objects.filter(anne1="2002-2003",code1="a0a0")  
  #get score
 scmat=0 ;scphy=0 ;scchi=0;scbio=0;scara1=0;scara2=0;scara3=0;scfra1=0
 scfra2=0;scfra3=0; sceng=0; scciv=0;schis=0;scgeo=0;sceco=0;scsoc=0;scphi=0;scinf=0;scart=0
 screl=0;scspo=0;scpas=0;scm1=0;scm2=0;scm3=0;scm4=0;scm5=0;scm6=0;scm7=0
 tyty="AQWQQ"
 cycy="cllslslslsll"
 for iii in sata:
   tyty=iii.section1
   cycy=iii.classe1
 print(xx2)
 print(tyty)
 print(xx1)
 score1=matiere.objects.filter(classe=cycy ,section=tyty, anne=xx1)
 sctotale=0
 for sc1 in score1:
   if sc1.nommatiere=='math':
     scmat=sc1.score
   if sc1.nommatiere=='physique':
     scphy=sc1.score
   if sc1.nommatiere=='chimie':
     scchi=sc1.score
   if sc1.nommatiere=='bio':
     scbio=sc1.score
   if sc1.nommatiere=='arab1':
     scara1=sc1.score
   if sc1.nommatiere=='arab2':
     scara2=sc1.score
   if sc1.nommatiere=='arab3':
     scara3=sc1.score
   if sc1.nommatiere=='francais1':
     scfra1=sc1.score
   if sc1.nommatiere=='francais2':
     scfra2=sc1.score
   if sc1.nommatiere=='francais3':
     scfra3=sc1.score
   if sc1.nommatiere=='eng':
     sceng=sc1.score
   if sc1.nommatiere=='civisme':
     scciv=sc1.score
   if sc1.nommatiere=='historique':
     schis=sc1.score
   if sc1.nommatiere=='geographie':
     scgeo=sc1.score
   if sc1.nommatiere=='economie':
     sceco=sc1.score
   if sc1.nommatiere=='socialite':
     scsoc=sc1.score
   if sc1.nommatiere=='philosophie':
     scphi=sc1.score
   if sc1.nommatiere=='informatique':
     scinf=sc1.score
   if sc1.nommatiere=='art':
     scart=sc1.score
   if sc1.nommatiere=='religieu':
     screl=sc1.score
   if sc1.nommatiere=='sport':
     scspo=sc1.score
   if sc1.nommatiere=='pass1':
     scpas=sc1.score
   if sc1.nommatiere=='matiere1':
     scm1=sc1.score
   if sc1.nommatiere=='matiere2':
     scm2=sc1.score
   if sc1.nommatiere=='matiere3':
     scm3=sc1.score
   if sc1.nommatiere=='matiere4':
     scm4=sc1.score
   if sc1.nommatiere=='matiere5':
     scm5=sc1.score
   if sc1.nommatiere=='matiere6':
     scm6=sc1.score
   if sc1.nommatiere=='matiere7':
     scm7=sc1.score
     
     
   sctotale=sctotale+sc1.score 

 v1="";v2="";v3="";v4="";mony=""
 visasemexa=anne.objects.filter(anne=xx1)
 if len(visasemexa)!=0:
   for i in visasemexa:
      v1=i.vsem1; v2=i.vexa1; v3=i.vsem2; v4=i.vexa2
 visamon=student101.objects.filter(code=xx2)   
 if len(visamon)!=0:
   for j in visamon:
     mony=j.num1
 
 #####  تحرير اظهار علامة الطالب للاهل من السماح للمعلمين في ادخال الفصول

 v1="non";v2="non";v3="non";v4="non"

 ####################
 
 print(v1)
 ssdta=visamoy.objects.filter(id=1)
 for tr in ssdta:
    vvs=tr.visamoye
 if xx1!=None and xx2!=None  and xx4!=None :
   sss={'matiere':score1,'xmoix':xmoisx,'vv1':v1,'vv2':v2,'vv3':v3,'vv4':v4,'movs': vvs, 'recann': recans, 'somt': sctotale,'root4': tssyy4,'root1': tssyy1,'root2':tssyy2, 'x1':xx1,'x2':xx2,'x4':xsd,'annn':and1,'month001':xsd, 'lss':xsd,'reco': sata, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas,'ascm1':scm1,'ascm2':scm2,'ascm3':scm3,'ascm4':scm4,'ascm5':scm5,'ascm6':scm6,'ascm7':scm7}
 if xx1==None or xx2==None or  xx4==None:
   sss={'matiere':score1,'xmoix':xmoisx,'vv1':v1,'vv2':v2,'vv3':v3,'vv4':v4,'movs': vvs,'recann': recans,'somt': sctotale,'root4': tssyy4,'root1': tssyy1,'root2':tssyy2,'x1':None,'x2':None,'x3':None,'x4':None,'annn':and1,'month001':None, 'lss':None, 'reco': sata, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas,'ascm1':scm1,'ascm2':scm2,'ascm3':scm3,'ascm4':scm4,'ascm5':scm5,'ascm6':scm6,'ascm7':scm7}
     
 parent="yes"
 #if mony == 1972 :sss={'matiere':score1,'xmoix':xmoisx,'parent': "no",'recann': recans,'somt': sctotale,'root4': tssyy4,'root1': tssyy1,'root2':tssyy2,'x1':None,'x2':None,'x3':None,'x4':None,'annn':and1,'month001':None, 'lss':None, 'reco': None, 'ascmat':scmat ,'ascphy':scphy ,'ascchi':scchi,'ascbio':scbio,'ascara1':scara1,'ascara2':scara2,'ascara3':scara3,'ascfra1':scfra1 ,'ascfra2':scfra2,'ascfra3':scfra3, 'asceng':sceng, 'ascciv':scciv,'aschis':schis,'ascgeo':scgeo,'asceco':sceco,'ascsoc':scsoc,'ascphi':scphi,'ascinf':scinf,'ascart':scart ,'ascrel':screl,'ascspo':scspo,'ascpas':scpas,'ascm1':scm1,'ascm2':scm2,'ascm3':scm3,'ascm4':scm4,'ascm5':scm5,'ascm6':scm6,'ascm7':scm7}
 if mony == 1972 :sss={}

 
 return render(request,'app1/directeur/carnetuneleve.html',sss)




def visamoyenne (request):
  xx1=request.POST.get('temp')
  data=visamoy.objects.get(id=1)
  data.visamoye=xx1
  if xx1!=None:
   data.save()
  print(xx1)
  
  return render(request,'app1/directeur/visamoyen.html')
###############################################################################################################
####   اصدار افاادت للجيش وغيره

def ifadah (request):
  anw=anne.objects.all()
   ##########  
    
    
  x001=request.POST.get('nomp1')
  x002=request.POST.get('nomf1')
  ann1=request.POST.get('anne2031')
  ann2=request.POST.get('anne2032')
  ann3=request.POST.get('anne2033')
  print(x001)
  monn=mony.objects.filter(anne=ann1)
  cl1=regeleve.objects.filter(code=1)
  for dd in cl1 :
    print(dd.anne1)  

  if x001!=None or x002!=None :
   ff= student101.objects.all()
   sss={'dl': monn, 'rec': ff.filter(pere__contains=x001,famille__contains=x002),'recann' : anw,'a1':ann1,'a2':ann2,'a3':ann3,'clx':cl1}

  if x001==None or x002==None :
    ff= student101.objects.all()

    sss={'dl': monn,'rec': ff, 'recann' : anw,'a1':ann1,'a2':ann2,'a3':ann3, 'clx': cl1}
    

  return render(request,'app1/directeur/ifadah.html',sss)

###############################################################
##    الاقساط المدرسية
def monylist(request):
  ann=anne.objects.all()
  
    
  a01=request.POST.get('anne2031')
  m=mony.objects.filter(anne=a01)
  
  
  ss={'annx':ann, 'a1': a01, 'monycl': m}
  return render(request,'app1/directeur/monylist.html',ss)

def monyupdate(request, idm, anne009):
  id1=idm 
  a01=anne009
  ann=anne009
  ba111=request.POST.get('k1')
  ba222=request.POST.get('k2')
  spotnik=mony.objects.get(id=id1)
  spotnik.amountll=ba111
  spotnik.amountdd=ba222
  spotnik.tl=num2words(ba111,lang='arab')+ " "+"ليرة لبنانية"
  spotnik.td=num2words(ba222,lang='arab')+" "+"دولار أميريكي"
  if ba111!=None and ba222!=None:
   spotnik.save()
  
  ann=anne.objects.all()
  m=mony.objects.filter(anne=a01)
  ss={'annx':ann, 'a1': a01, 'monycl': m}
 
  return render(request,'app1/directeur/monylist.html',ss)
 
 
def callmony(request, x0, x1, x2, x3, x4, x6, x7, x8):
 ax0=x0
 ax1=x1;ax2=x2;ax3=x3;ax4=x4;ax6=x6;ax7=x7;ax8=x8
 # ax6 السنة الاولى - ax7 : السنة الثانية- ax8: السنة الثالثة
 # كود الطالب ax0
 #########################################
 # جلب صف التلميذ في كل عام 
 if ax7 == None: ax7=""
 if ax8 == None:ax8=""
 ac1=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax6, code=1)
 for iii in we:
   ac1=iii.classe1
  
 ac2=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax7, code=1)
 for iii in we:
   ac2=iii.classe1
 ac3=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax8, code=1)
 for iii in we:
   ac3=iii.classe1
 ##########################################################
 # جلب قسط العام الاول
 ddlls=mony.objects.filter(anne=ax6,classe=ac1)
 ll1=0
 dd1=0
 for st in ddlls:
   ll1=st.amountll
   dd1=st.amountdd
 
 #########################################
 ddd=student101.objects.filter(code=ax0)
 
 for tenten in ddd:
   datx=tenten.dat
   sx=tenten.rem1
   
 schooldata=school.objects.filter(id=1)  
 tafl=num2words(ll1,lang='arab')
 tafd=num2words(dd1,lang='arab')
 sss={'tafl1':tafl,'tafd1':tafd,'scho':schooldata,'w0':ax0, 'w1':ax1,'w2':ax2,'w3':ax3,'w4':ax4,'w6':ax6,'c6':ac1,'ll6':ll1,'dd6':dd1,'w7':ax7,'c7':ac2,'w8':ax8,'c8':ac3,'nais':datx ,'sexe':sx}
 return render(request,'app1/directeur/textmoulhakj.html',sss)
   #################################################
##################################################################################################
 ## تعاونية 
def callmonyt(request, x0, x1, x2, x3, x4, x6, x7, x8):
 ax0=x0
 ax1=x1;ax2=x2;ax3=x3;ax4=x4;ax6=x6;ax7=x7;ax8=x8
 # ax6 السنة الاولى - ax7 : السنة الثانية- ax8: السنة الثالثة
 # كود الطالب ax0
 #########################################
 # جلب صف التلميذ في كل عام 
 
 ac1=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax6, code=1)
 for iii in we:
   ac1=iii.classe1
  
 ac2=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax7, code=1)
 for iii in we:
   ac2=iii.classe1
 ac3=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax8, code=1)
 for iii in we:
   ac3=iii.classe1
 ##########################################################
 # جلب قسط العام الاول
 ddlls=mony.objects.filter(anne=ax6,classe=ac1)
 ll1=0
 dd1=0
 for st in ddlls:
   ll1=st.amountll
   dd1=st.amountdd
 
 #########################################
 ddd=student101.objects.filter(code=ax0)
 
 for tenten in ddd:
   datx=tenten.dat
   sx=tenten.rem1
   
 schooldata=school.objects.filter(id=1)  
 tafl=num2words(ll1,lang='arab')
 tafd=num2words(dd1,lang='arab')
 sss={'tafl1':tafl,'tafd1':tafd,'scho':schooldata,'w0':ax0, 'w1':ax1,'w2':ax2,'w3':ax3,'w4':ax4,'w6':ax6,'c6':ac1,'ll6':ll1,'dd6':dd1,'w7':ax7,'c7':ac2,'w8':ax8,'c8':ac3,'nais':datx ,'sexe':sx}
 return render(request,'app1/directeur/textifadataawnieh.html',sss)


##############################################################################
##  ملحق ز
 
def callmonyz(request, x0, x1, x2, x3, x4, x6, x7, x8):
 ax0=x0
 ax1=x1;ax2=x2;ax3=x3;ax4=x4;ax6=x6;ax7=x7;ax8=x8
 # ax6 السنة الاولى - ax7 : السنة الثانية- ax8: السنة الثالثة
 # كود الطالب ax0
 #########################################
 # جلب صف التلميذ في كل عام 
 ac1=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax6, code=1)
 for iii in we:
   ac1=iii.classe1
  
 ac2=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax7, code=1)
 for iii in we:
   ac2=iii.classe1
 ac3=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax8, code=1)
 for iii in we:
   ac3=iii.classe1
 ##########################################################
 # جلب قسط العام الاول
 ddlls=mony.objects.filter(anne=ax6,classe=ac1)
 ll1=0
 dd1=0
 for st in ddlls:
   ll1=st.amountll
   dd1=st.amountdd
 
 #########################################
 ddd=student101.objects.filter(code=ax0)
 
 for tenten in ddd:
   datx=tenten.dat
   sx=tenten.rem1
   
 schooldata=school.objects.filter(id=1)  
 tafl=num2words(ll1,lang='arab')
 tafd=num2words(dd1,lang='arab')
 sss={'tafl1':tafl,'tafd1':tafd,'scho':schooldata,'w0':ax0, 'w1':ax1,'w2':ax2,'w3':ax3,'w4':ax4,'w6':ax6,'c6':ac1,'ll6':ll1,'dd6':dd1,'w7':ax7,'c7':ac2,'w8':ax8,'c8':ac3,'nais':datx ,'sexe':sx}
 return render(request,'app1/directeur/textmoulhakz.html',sss)

###################################################################################
#####      امن داخلي
 
def callmonyd(request, x001, x0, x1, x2, x3, x4, x6, x7, x8):
 ax0=x0
 ax1=x1;ax2=x2;ax3=x3;ax4=x4;ax6=x6;ax7=x7;ax8=x8
 # ax6 السنة الاولى - ax7 : السنة الثانية- ax8: السنة الثالثة
 # كود الطالب ax0 # x001: كود الاب
 #########################################
 # جلب صف التلميذ في كل عام 
 
 stud=student101.objects.filter(rem2=x001)
 reg=regeleve.objects.filter(anne1=ax6,code=1)
 mdl=mony.objects.filter(anne=ax6)
 sc=school.objects.all()
 
 sss={'scho':sc,'ann':ax6,'st':stud,'re':reg,'monydl':mdl}
 
 return render(request,'app1/directeur/textifadadarak.html',sss)

##################################################################
####       أمن عام
 
def callmonyG(request, x0, x1, x2, x3, x4, x6, x7, x8):
 ax0=x0
 ax1=x1;ax2=x2;ax3=x3;ax4=x4;ax6=x6;ax7=x7;ax8=x8
 # ax6 السنة الاولى - ax7 : السنة الثانية- ax8: السنة الثالثة
 # كود الطالب ax0
 #########################################
 # جلب صف التلميذ في كل عام 
 
 ac1=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax6, code=1)
 for iii in we:
   ac1=iii.classe1
  
 ac2=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax7, code=1)
 for iii in we:
   ac2=iii.classe1
 ac3=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax8, code=1)
 for iii in we:
   ac3=iii.classe1
 ##########################################################
 # جلب قسط العام الاول
 ddlls=mony.objects.filter(anne=ax6,classe=ac1)
 ll1=0
 dd1=0
 for st in ddlls:
   ll1=st.amountll
   dd1=st.amountdd
 
 #########################################
 ddd=student101.objects.filter(code=ax0)
 
 for tenten in ddd:
   datx=tenten.dat
   sx=tenten.rem1
   
 schooldata=school.objects.filter(id=1)  
 tafl=num2words(ll1,lang='arab')
 tafd=num2words(dd1,lang='arab')
 sss={'tafl1':tafl,'tafd1':tafd,'scho':schooldata,'w0':ax0, 'w1':ax1,'w2':ax2,'w3':ax3,'w4':ax4,'w6':ax6,'c6':ac1,'ll6':ll1,'dd6':dd1,'w7':ax7,'c7':ac2,'w8':ax8,'c8':ac3,'nais':datx ,'sexe':sx}
 return render(request,'app1/directeur/textamenam.html',sss)
###################################################################
###    لائحة اقساط لعام محدد
def listaksat(request, x6, x7, x8):
  aksa=mony.objects.filter(anne=x6)  
  sco=school.objects.all() 
   
  sss={'akm':aksa, 'an':x6, 'sc':sco, 'x61':x6}  
  return render(request,'app1/directeur/listeaksate.html',sss)
#  
##################################################################   
######    افادة مدرسية لمؤسسة عام
 
def callmonycha(request, x0, x1, x2, x3, x4, x6, x7, x8):
 ax0=x0
 ax1=x1;ax2=x2;ax3=x3;ax4=x4;ax6=x6;ax7=x7;ax8=x8
 # ax6 السنة الاولى - ax7 : السنة الثانية- ax8: السنة الثالثة
 # كود الطالب ax0
 #########################################
 # جلب صف التلميذ في كل عام 
 if ax6 == "":
      ax6="2020-2021" 
 if ax6 == None:
      ax6="2020-2021"
 
 
 a1n1=ax6[0:4]
 a1n2=ax6[5:9]
 a1i1=int(a1n1)
 a1i2=int(a1n2)
 a0cx1=num2words(a1i1,lang='arab')
 a0cx2=num2words(a1i2,lang='arab')
 
 ac1=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax6, code=1)
 for iii in we:
   ac1=iii.classe1
  
 ac2=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax7, code=1)
 for iii in we:
   ac2=iii.classe1
 ac3=""
 we=regeleve.objects.filter ( code1=ax0, anne1=ax8,code=1)
 for iii in we:
   ac3=iii.classe1
 ##########################################################
 # جلب قسط العام الاول
 ddlls=mony.objects.filter(anne=ax6,classe=ac1)
 ll1=0
 dd1=0
 for st in ddlls:
   ll1=st.amountll
   dd1=st.amountdd
 
 #########################################
 ddd=student101.objects.filter(code=ax0)
 
 for tenten in ddd:
   datx=tenten.dat
   sx=tenten.rem1
   
 schooldata=school.objects.filter(id=1)  
 tafl=num2words(ll1,lang='arab')
 tafd=num2words(dd1,lang='arab')
 yst=datx.year
 iyst=int(yst)
 tiyst=num2words(iyst,lang='arab')
 sss={'tyst':tiyst, 'a1cx1':a0cx1, 'a1cx2': a0cx2, 'tafl1':tafl,'tafd1':tafd,'scho':schooldata,'w0':ax0, 'w1':ax1,'w2':ax2,'w3':ax3,'w4':ax4,'w6':ax6,'c6':ac1,'ll6':ll1,'dd6':dd1,'w7':ax7,'c7':ac2,'w8':ax8,'c8':ac3,'nais':datx ,'sexe':sx}
 return render(request,'app1/directeur/textcha.html',sss)
   #################################################



def expuncarnetps01(request):
  n="0"
  ap=anne.objects.all()
  a=request.POST.get('anne2030')
  c=request.POST.get('classe2030')
  s=request.POST.get('section2030')
  
  recnomviews=regeleve.objects.filter(anne1=a,code="1",classe1=c,section1=s) 
  recoviews=regeleveps.objects.filter(anne1=a,classe1=c,section1=s).order_by('code1').order_by('groupe')
  ss={'recnom':recnomviews,'reco':recoviews,'an':ap,'n0':n}
  return render(request,'app1/directeur/expuncarnetps01.html',ss)










def updateschool(request):
  x1=request.POST.get('name1')
  x2=request.POST.get('numeducation1')
  x3=request.POST.get('directeur1')
  x4=request.POST.get('tasnif1')
  x5=request.POST.get('fax1')
  x6=request.POST.get('tel1')
  x7=request.POST.get('tarhis1')
  x8=request.POST.get('mohafaza1')
  x9=request.POST.get('kadaa1')
  x10=request.POST.get('city1')
  x11=request.POST.get('rem11')
  x12=request.POST.get('rem21')
  x13=request.POST.get('num11')
  x14=request.POST.get('num21')
  x15=request.POST.get('image1')

  data=school.objects.get(id=1)
  data.name=x1;data.numeducation=x2;data.directeur=x3;data.tasnif=x4;data.fax=x5;data.tel=x6;data.tarhis=x7;data.mohafaza=x8
  data.kadaa=x9;data.city=x10;data.rem1=x11;data.rem2=x12;data.num1=x13;data.num2=x14;data.imag=x15
  if x1!=None and x2!=None and x3!=None and x4!=None and x5!=None and x6!=None and x7!=None and x8!=None and x9!=None and x10!=None and x11!=None and x12!=None and x13!=None and x14!=None:
     data.save()
     
  sss=school.objects.filter(id=1)
  ccc={'menber11': sss}
  return render(request,'app1/directeur/school.html',ccc)
 #################################################################
 ###################################################################
 ####################################################################
 ########################################################################
 ############################################################################
 ############   ps1  ps2  ps3
 #########################################################################
 #######################################################################
 
def listmatiereps123 (request):
  
  anw=anne.objects.all()
  xann=request.POST.get('anne1')
  x001=request.POST.get('nom1')
  cc=request.POST.get('classe1')  
  f="False"
  ff=ps123note.objects.filter(anne=xann,classe=cc)
  sss={'ans': xann,'rec': ff,'annn' : anw,'tt': f}
  if xann!=None:
    sss={'ans': xann,'rec': ff.filter(anne=xann),'annn' : anw,'tt':f}
    kkk=ff.filter(anne=xann)
  else:
    sss={'ans': xann,'rec': ff,'annn' : anw,'tt':f}
    kkk=ff
  
  if x001!=None:
    sss={'nn': x001,'ans': xann,'rec': kkk.filter(groupe__contains=x001),'annn' : anw,'tt':f}
    zzz=kkk.filter(groupe__contains=x001)
  else :
    sss={'ans': xann,'rec': kkk,'annn' : anw,'tt':f}
    zzz=kkk
  if cc!=None:
    sss={'xc':cc,'ans': xann,'rec': zzz.filter(classe__contains=cc),'annn' : anw,'tt':f}
  else:
    sss={'ans': xann,'rec': zzz,'annn' : anw,'tt':f}

   
  return render(request,'app1/directeur/matiereps123.html',sss)

def addmatps(request):
  tan=anne.objects.all()
  xan=request.POST.get('anne1')
  xcl=request.POST.get('classe1')
  sss={'xan1': xan, 'xcl1': xcl, 'tantan':tan} 
  x1=request.POST.get('groupe1')
  x2=request.POST.get('champ1')
  x3=request.POST.get('souschamp1')
  x4=request.POST.get('rem11')
  x5=request.POST.get('rem21')
  x6=request.POST.get('rem31')
  x7=request.POST.get('num11')
  x8=request.POST.get('num21')
  if x7==None:
    x7=0
  if x8==None:
    x8=0                             
  data=ps123note(anne=xan, classe=xcl, groupe=x1,champ=x2,souschamp=x3,rem1=x4, rem2=x5, rem3=x6, num1=x7, num2=x8)
  if xan!=None:
   data.save()

  return render(request,'app1/directeur/matiereps123add.html',sss)

#####################  update matiere classe ps

def upps123(request, cod0035,cl0,an0):
  sch=request.POST.get('sch0')
  r1=request.POST.get('r10')
  r2=request.POST.get('r20')
  r3=request.POST.get('r30')
  n1=request.POST.get('n10')
  n2=request.POST.get('n20')
  rec0=ps123note.objects.filter(anne=cl0,classe=an0)
  data=ps123note.objects.get(id=cod0035)
  data.souschamp=sch
  if sch!="" and sch!=None:
   data.save()  
  st="True"
  sss={'xc':an0,'ans':cl0,'tt':st,'rec':rec0}

  return render(request,'app1/directeur/matiereps123.html',sss)




#############################################################

def delps(request, cod01):
  d=ps123note.objects.get(id=cod01)
  d.delete()
  return HttpResponseRedirect(reverse('formpsmatiere'))


 

def updatematps(request, cod0035, s1, s2, s3, s4, s5, s6, s7, s8, ann01, class01):
  w1=request.POST.get('groupe1')
  w2=request.POST.get('champ1')
  w3=request.POST.get('souschamp1')
  w4=request.POST.get('rem11')
  w5=request.POST.get('rem21')
  w6=request.POST.get('rem31')
  w7=request.POST.get('num11')
  w8=request.POST.get('num21')
  
  
  
  print("hiaaa")
  print(s1)
  print(w1)
  #remarque w1=s1
  print(cod0035)  
  print(s2)
  data=ps123note.objects.get(id=cod0035)
  
  data.souschamp=w3
  data.rem1=w4
  data.rem2=w5
  data.rem3=w6
  data.num1=w7
  data.num2=w8
  
  data.save()  
  
  
  
  
  anw=anne.objects.all()
  xann=ann01
  x001=""
  cc=class01  

  ff=ps123note.objects.all()
  sss={'ans': xann,'rec': ff,'annn' : anw,'tt':True}
  if xann!=None:
    sss={'ans': xann,'rec': ff.filter(anne=xann),'annn' : anw,'tt':True}
    kkk=ff.filter(anne=xann)
  else:
    sss={'ans': xann,'rec': ff,'annn' : anw,'tt':True}
    kkk=ff
  
  if x001!=None:
    sss={'nn': x001,'ans': xann,'rec': kkk.filter(groupe__contains=x001),'annn' : anw,'tt':True}
    zzz=kkk.filter(groupe__contains=x001)
  else :
    sss={'ans': xann,'rec': kkk,'annn' : anw,'tt':True}
    zzz=kkk
  if cc!=None:
    sss={'xc':cc,'ans': xann,'rec': zzz.filter(classe__contains=cc),'annn' : anw ,'tt':True}
  else:
    sss={'ans': xann,'rec': zzz,'annn' : anw,'tt':True}

   
  return render(request,'app1/directeur/matiereps123.html',sss)

  
  ##################################################################
  #################################################################
  ########## فتح عام دراسي وانشاء بطاقات العلامات للروضات
  
  
def openaps (request):

 sss=anne.objects.all()
 for yty in sss:
   ddd=yty.anne
   
   print(ddd)
 
 pp=request.POST.get('anne2')
 csps=""
 if pp!=None:
   eleves=student101.objects.all()
   for x in eleves:
       ww=x.code
       mm=ww
       print(ww)
       print(pp)
       ps1="non";ps2="non";ps3="non"
       ee="oui"
       int=0.0
       print (int)
       if x.quit=="ترك":
         ee="no"
       cc=regeleve.objects.all()
       for zz in cc :
          if zz.code1==mm and zz.anne1==pp and zz.classe1=="ps1":
           ps1="oui";csps=zz.section1
          if zz.code1==mm and zz.anne1==pp and zz.classe1=="ps2":
           ps2="oui";csps=zz.section1
          if zz.code1==mm and zz.anne1==pp and zz.classe1=="ps3":
           ps3="oui";csps=zz.section1
       
       pps=regeleveps.objects.all()
       for ps123 in pps:
         if ps123.code1==mm and ps123.anne1==pp:
           ee="no"
       
       print("e")
       print(ee)
      
       #######################################################   هنا العمل
       ###  mm=كود التلميذ    pp=العام
       if ee=="oui" and ps1=="oui":
           ccps=ps123note.objects.filter(classe="ps1",anne=pp)
           for iii in ccps:
             data=regeleveps(anne1=pp,classe1="ps1",code1=mm,nom1=x.nom,pere1=x.pere,famille1=x.famille,groupe=iii.groupe,champ=iii.champ,souschamp=iii.souschamp,
                            rem11=iii.rem1,rem21=iii.rem2,rem31=iii.rem3,num11=iii.num1,num21=iii.num2,sem1="",sem2="",sem3="",
                            sem4="",sem5="",sem6="",sem7="",section1=csps) 
             data.save()
                           
       if ee=="oui" and ps2=="oui":
           ccps=ps123note.objects.filter(classe="ps2",anne=pp)
           for iii in ccps:
             data=regeleveps(anne1=pp,classe1="ps2",code1=mm,nom1=x.nom,pere1=x.pere,famille1=x.famille,groupe=iii.groupe,champ=iii.champ,souschamp=iii.souschamp,
                            rem11=iii.rem1,rem21=iii.rem2,rem31=iii.rem3,num11=iii.num1,num21=iii.num2,sem1="",sem2="",sem3="",
                            sem4="",sem5="",sem6="",sem7="",section1=csps) 
             data.save()
       if ee=="oui" and ps3=="oui":
           ccps=ps123note.objects.filter(classe="ps3",anne=pp)
           for iii in ccps:
             data=regeleveps(anne1=pp,classe1="ps3",code1=mm,nom1=x.nom,pere1=x.pere,famille1=x.famille,groupe=iii.groupe,champ=iii.champ,souschamp=iii.souschamp,
                            rem11=iii.rem1,rem21=iii.rem2,rem31=iii.rem3,num11=iii.num1,num21=iii.num2,sem1="",sem2="",sem3="",
                            sem4="",sem5="",sem6="",sem7="",section1=csps) 
             data.save()





 ####################################################################
 mon=mony.objects.all()
 e1="oui"
 for m1 in mon:
   if m1.anne==pp:
     e1="no" 
 
 if e1=="oui" and pp!=None:
   mmm=mony(classe="ps1",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="ps2",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="ps3",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb1",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb2",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb3",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb4",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb5",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb6",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb7",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb8",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="eb9",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="sec-sc",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="bacc1-sc",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="bacc1-l",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="sg",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="sv",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="se",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   mmm=mony(classe="lh",amountll=0.0, amountdd=0.0, anne=pp)
   mmm.save()
   
   
 return render(request,'app1/directeur/openaneps.html',{'rec':sss})
###################################################################################
#####    ادخال لعامات الروضات من قبل المدير
def expcarnetps(request):
  a=request.POST.get('anne2030')
  c=request.POST.get('classe2030')
  s=request.POST.get('section2030')
  n=request.POST.get('nom2030')
  f=request.POST.get('f2030')
  bla=request.POST.get('ard2030')
  if bla == "all" : n="";f=""
  anps=anne.objects.all()
  # mois = sem1  وذلك لناخذ سجل واحد فقط لتلميذ محدد ونظهر علامته مرة
  if n!= None :
   recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,nom1__contains=n,famille1__contains=f,mois="sem1") 
  if n==None:
    recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,mois="sem1") 
  recoviews=regeleveps.objects.filter(anne1=a,classe1=c,section1=s)
  ss={'recnom':recnomviews,'reco':recoviews,'an':anps,'n0':n,'f15':f}
  return render(request,'app1/directeur/expcarnetps.html',ss)
#

def savenoteps(request,cod,a,c,s,n,f0):
  f=f0
  nnn=n
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  print ("s1")
  print(s1)
  dat=regeleveps.objects.get(id=cod)
  dat.sem1=s1
  dat.sem2=s2
  dat.sem3=s3
  if s1 != None and s2 != None and s3 != None:
   dat.save()
  
  anps=anne.objects.all()
  # mois = sem1  وذلك لناخذ سجل واحد فقط لتلميذ محدد ونظهر علامته مرة
 
  bla=request.POST.get('ard2030')
  if bla == "all" : n="";f="";nnn=""

 
  if n!= None:
   recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,nom1__contains=n,famille1__contains=f,mois="sem1") 
  if n==None:
    recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,mois="sem1") 
  recoviews=regeleveps.objects.filter(anne1=a,classe1=c,section1=s)
  ss={'recnom':recnomviews,'reco':recoviews,'an':anps,'x3':s,'xc':c,'xa':a,'n0':nnn,'f15':f}
  return render(request,'app1/directeur/expcarnetps.html',ss)
#
###################################################################################
##### ادخال لعامات الروضات من قبل  الاستاذ 
def Aexpcarnetps(request):
  cmt=request.POST.get('codmat')
  a=request.POST.get('anne2030')
  c=request.POST.get('classe2030')
  s=request.POST.get('section2030')
  n=request.POST.get('nom2030')
  f=request.POST.get('f2030')
  selection="no"
  
  
  
  x1=1;x2=1;x3=1;x4=1
  
  matc=matiere.objects.filter(classe=c,anne=a,section=s)
  for t in matc:
    if t.code==cmt: selection="oui";x1=t.sem1;x2=t.exa1;x3=t.sem2;x4=t.exa2
    
  
  
    
  
  
  bla=request.POST.get('ard2030')
  if bla == "all" : n="";f=""
  anps=anne.objects.all()
  # mois = sem1  وذلك لناخذ سجل واحد فقط لتلميذ محدد ونظهر علامته مرة
  if n!= None :
   recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,nom1__contains=n,famille1__contains=f,mois="sem1") 
  if n==None:
    recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,mois="sem1") 
  recoviews=regeleveps.objects.filter(anne1=a,classe1=c,section1=s)
  ss={'s001':x1,'s002':x2,'s003':x3,'e2':x4,'sel':selection,'recnom':recnomviews,'reco':recoviews,'an':anps,'n0':n,'f15':f}
  return render(request,'app1/directeur/Mexpcarpsmaitre.html',ss)
#

def Asavenoteps(request,cod,a,c,s,n,f0):
  selection="oui"
  f=f0
  nnn=n
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  print ("s1")
  print(s1)
  
  
  v1="";v2="";v3="";v4="";mony=""
  visasemexa=anne.objects.filter(anne=a)
  if len(visasemexa)!=0:
    for i in visasemexa:
       v1=i.vsem1; v2=i.vexa1; v3=i.vsem2; v4=i.vexa2
 
    
  dat=regeleveps.objects.get(id=cod)
  kdkd=dat.code1
  
  x001=1;x002=1;x003=1;x004=1
  cc=dat.classe1;aa=dat.anne1;ss=dat.section1;nm=dat.groupe
  saw=matiere.objects.filter(anne=aa,classe=cc,section=ss,nommatiere="arab1")
  for t in saw:
    x001=t.sem1;x002=t.exa1;x003=t.sem2
  
  
  
  dat=regeleveps.objects.get(id=cod)
  if s1 != None:
    dat.sem1=s1
  if s2 != None:
   dat.sem2=s2
  if s3 != None:
    dat.sem3=s3
  
  dat.save()
 
  anps=anne.objects.all()
  # mois = sem1  وذلك لناخذ سجل واحد فقط لتلميذ محدد ونظهر علامته مرة
 
  bla=request.POST.get('ard2030')
  if bla == "all" : n="";f="";nnn=""

 
  if n!= None:
   recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,nom1__contains=n,famille1__contains=f,mois="sem1") 
  if n==None:
    recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,mois="sem1") 
  recoviews=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,code1=kdkd)
  ss={'s001':x001,'s002':x002,'s003':x003,'e2':x004,'sel':selection,'recnom':recnomviews,'reco':recoviews,'an':anps,'x3':s,'xc':c,'xa':a,'n0':nnn,'f15':f}
  print("abbas")
  print(x002)
  
  return render(request,'app1/directeur/Mexpcarpsmaitre.html',ss)
#########################################
###   francaise


def FAexpcarnetps(request):
  
  cmt=request.POST.get('codmat')
  a=request.POST.get('anne2030')
  c=request.POST.get('classe2030')
  s=request.POST.get('section2030')
  n=request.POST.get('nom2030')
  f=request.POST.get('f2030')
  selection="no"
  
  x1=1;x2=1;x3=1;x4=1
  
  matc=matiere.objects.filter(classe=c,anne=a,section=s)
  for t in matc:
    if t.code==cmt: selection="oui";x1=t.sem1;x2=t.exa1;x3=t.sem2;x4=t.exa2
    
  
  
  
  bla=request.POST.get('ard2030')
  if bla == "all" : n="";f=""
  anps=anne.objects.all()
  # mois = sem1  وذلك لناخذ سجل واحد فقط لتلميذ محدد ونظهر علامته مرة
  if n!= None :
   recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,nom1__contains=n,famille1__contains=f,mois="sem1") 
  if n==None:
    recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,mois="sem1") 
  recoviews=regeleveps.objects.filter(anne1=a,classe1=c,section1=s)
  ss={'s001':x1,'s002':x2,'s003':x3,'e2':x4,'sel':selection,'recnom':recnomviews,'reco':recoviews,'an':anps,'n0':n,'f15':f}
  print("abbas")
  print(x1)
  print(x2)
  return render(request,'app1/directeur/FMexpcarpsmaitre.html',ss)
#

def FAsavenoteps(request,cod,a,c,s,n,f0):
  selection="oui"
  f=f0
  nnn=n
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  print ("s1")
  print(s1)
  
  
  v1="";v2="";v3="";v4="";mony=""
  visasemexa=anne.objects.filter(anne=a)
  if len(visasemexa)!=0:
    for i in visasemexa:
       v1=i.vsem1; v2=i.vexa1; v3=i.vsem2; v4=i.vexa2

  
  dat=regeleveps.objects.get(id=cod)
  kdkd=dat.code1
  
  
  
  x001=1;x002=1;x003=1;x004=1
  cc=dat.classe1;aa=dat.anne1;ss=dat.section1;nm=dat.groupe
  saw=matiere.objects.filter(anne=aa,classe=cc,section=ss,nommatiere="francais1")
  for t in saw:
    x001=t.sem1;x002=t.exa1;x003=t.sem2
  




  
  dat=regeleveps.objects.get(id=cod)
  if s1 != None:
    dat.sem1=s1
  if s2 != None:
   dat.sem2=s2
  if s3 != None:
    dat.sem3=s3
  
  dat.save()
 
  anps=anne.objects.all()
  # mois = sem1  وذلك لناخذ سجل واحد فقط لتلميذ محدد ونظهر علامته مرة
 
  bla=request.POST.get('ard2030')
  if bla == "all" : n="";f="";nnn=""

 
  if n!= None:
   recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,nom1__contains=n,famille1__contains=f,mois="sem1") 
  if n==None:
    recnomviews=regeleve.objects.filter(anne1=a,classe1=c,section1=s,mois="sem1") 
  recoviews=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,code1=kdkd)
  ss={'s001':x001,'s002':x002,'s003':x003,'e2':x004,'sel':selection,'recnom':recnomviews,'reco':recoviews,'an':anps,'x3':s,'xc':c,'xa':a,'n0':nnn,'f15':f}
  return render(request,'app1/directeur/FMexpcarpsmaitre.html',ss)
################################################################
#  اظهار علامة تلميذ روضة للأهل   
def expuncarnetps(request):
  ap=anne.objects.all()
  a=request.POST.get('anne2030')
  n=request.POST.get('cod2030')
  visamon=student101.objects.filter(code=n)   
  mony=1
  if len(visamon)!=0:
    for j in visamon:
      mony=j.num1
  
  if mony==1972: n="000"
  recnomviews=regeleve.objects.filter(anne1=a,code1=n,mois="sem1") 
  recoviews=regeleveps.objects.filter(anne1=a,code1=n)
  ss={'recnom':recnomviews,'reco':recoviews,'an':ap,'n0':n}
  return render(request,'app1/directeur/expuncarnetps.html',ss)
#


##########  news
def listelevenews (request):
  kkk="" 
  x00a="";x00m=""
  x001=request.POST.get('date1001')
  x002=request.POST.get('pnews')
  x00m=request.POST.get('m1001')
  x00a=request.POST.get('a1001')
  
  if x00m == None:
    x00m=""
  if x00a == None:
    x00a=""  
  if x002 == None:
    x002=""  
  
  
  if x001 !="" and x001 != None and x001 != "YYYY-mm-dd":
    kkk=newsschool.objects.filter(dat=x001,news1__contains=x002)
  
  
  if x001 == "" and x00m != ""  and x00a != "":
     kkk=newsschool.objects.filter(news1__contains=x002,dat__month__contains=x00m,dat__year__contains=x00a)
  
  if x001 == None and x00m != "" and x00a != "": 
     kkk=newsschool.objects.filter(news1__contains=x002,dat__month__contains=x00m,dat__year__contains=x00a)
  
  if x001 == "YYYY-mm-dd"  and x00m != ""  and x00a != "":
    kkk=newsschool.objects.filter(news1__contains=x002,dat__month__contains=x00m,dat__year__contains=x00a)
  
  if x001 == None and x00a == ""  and x00m == "" :
      kkk=newsschool.objects.filter(news1__contains=x002)

  if x001 == "" and x00a == ""  and x00m == "" :
      kkk=newsschool.objects.filter(news1__contains=x002)
  if x001 == "YYYY-mm-dd" and x00a == ""  and x00m == "" :
      kkk=newsschool.objects.filter(news1__contains=x002)
 
  sss={'reco':kkk}
   
  return render(request,'app1/directeur/listenews.html',sss)

def delnews(request, idd):
  sss=newsschool.objects.get(id=idd)
  sss.delete()
  return HttpResponseRedirect(reverse('form10033news'))

def addnews(request):
 x001=request.POST.get('dat1')
 x002=request.POST.get('news1')
 x003=request.POST.get('rem11')
 x004=request.POST.get('rem21')
 if x001 != None and x002 != None :
   data=newsschool(dat=x001,news1=x002,rem1=x003,rem2=x004)
   data.save()
 return render(request,'app1/directeur/addnews.html')


def updatelistenews(request, cod):
 x01=request.POST.get('news11')
 x02=request.POST.get('rem11')
 x03=request.POST.get('rem21')
 data=newsschool.objects.get(id=cod)
 data.news1=x01
 data.rem1=x02
 data.rem2=x03
 data.save()
 print(cod)
 print(x01)
 return HttpResponseRedirect(reverse('form10033news'))

#########################################################################
#####   حجب واظهار علامة طالب محدد عن الاهل

def afficar(request,cod017):
  caraff=student101.objects.get(code=cod017)
  caraff.num1=1
  caraff.save()
  return HttpResponseRedirect(reverse('form10033'))


def hidecar(request,cod016):
  caraff=student101.objects.get(code=cod016)
  caraff.num1=1972
  caraff.save()

  return HttpResponseRedirect(reverse('form10033'))
########################################
##   سماح وعدم سماح للاستاد بالعمل
def workst(request,co1):
  ssse=stok.objects.get(user=co1)
  ssse.passmod="oui"
  ssse.save()
  return HttpResponseRedirect(reverse('form100959'))


def work(request,co2):
  ssse=stok.objects.get(user=co2)
  ssse.passmod="non"
  ssse.save()

  return HttpResponseRedirect(reverse('form100959'))



def passtou(request):
  a=request.POST.get('anne08')
  c=request.POST.get('classe08')
  s=request.POST.get('section08')
  af=request.POST.get('aff')
  aaa=anne.objects.all()
  dd=regeleve.objects.filter(anne1=a,classe1=c,section1=s)
  for i in dd:
    eleve=student101.objects.get(code=i.code1)
    if af=="حجب علامة":
      eleve.num1=1972
    if af=="اظهار علامة":
     eleve.num1=1 
    eleve.save()


  


  ssss={'anrec':aaa,'a':a,'c':c,'s':s,'af':af,'rec':dd}

  return render(request,'app1/directeur/passtoucarnets.html',ssss)

def hidetou(request):
  ddd=student101.objects.all()
  for i in ddd:
   i.num1=1972
   i.save()
  
  a=request.POST.get('anne08')
  c=request.POST.get('classe08')
  s=request.POST.get('section08')
  af=request.POST.get('aff')
  aaa=anne.objects.all()
  dd=regeleve.objects.filter(anne1=a,classe1=c,section1=s,mois="sem1")
  for i in dd:
    eleve=student101.objects.get(code=i.code1)
    if af=="حجب علامة":
      eleve.num1=1972
    if af=="اظهار علامة":
     eleve.num1=1 
    eleve.save()


  ssss={'anrec':aaa,'a':a,'c':c,'s':s,'af':af,'rec':dd}
  
  return render(request,'app1/directeur/passtoucarnets.html',ssss)

def afftou(request):
  ddd=student101.objects.all()
  for i in ddd:
   i.num1=0
   i.save()


  a=request.POST.get('anne08')
  c=request.POST.get('classe08')
  s=request.POST.get('section08')
  af=request.POST.get('aff')
  aaa=anne.objects.all()
  dd=regeleve.objects.filter(anne1=a,classe1=c,section1=s,mois="sem1")
  for i in dd:
    eleve=student101.objects.get(code=i.code1)
    if af=="حجب علامة":
      eleve.num1=1972
    if af=="اظهار علامة":
     eleve.num1=1 
    eleve.save()


  ssss={'anrec':aaa,'a':a,'c':c,'s':s,'af':af,'rec':dd}


  return render(request,'app1/directeur/passtoucarnets.html',ssss)



def passtoumss(request):
  mss=0;mfirst=""
  a=request.POST.get('anne08ms')
  c=request.POST.get('classe08ms')
  s=request.POST.get('section08ms')
  af=request.POST.get('affms')
  afa=request.POST.get('affmsa')

  mss=request.POST.get('mois01')
  if mss == None: mss=0
  if mss == "" : mss=0
  aaa=anne.objects.all()
  msss08=structurecarnet.objects.filter(anne=a)
  #############################
  if c != "ALL" and s != "ALL" and mss != "1900":
     dd=regeleve.objects.filter(anne1=a,classe1=c,section1=s,code=mss)
     print("by1")
  if c == "ALL" and s == "ALL" and mss == "1900":
     print("yai"),print(a),print(mss)
     dd=regeleve.objects.filter(anne1=a)
  
  if (c == "ALL") and (s == "ALL") and (mss!="1900"):
     dd=regeleve.objects.filter(anne1=a,code=mss)
     print("by2")
  if c == "ALL" and  mss == "1900" and s!= "ALL":
     dd=regeleve.objects.filter(anne1=a,section1=s)
     print("by3")
  if  s == "ALL" and mss == "1900" and c!= "ALL":
     dd=regeleve.objects.filter(anne1=a,classe1=c)
     print("by4")
  if  s == "ALL" and mss != "1900" and c!= "ALL":
     dd=regeleve.objects.filter(anne1=a,classe1=c,code=mss)
     print("by5")
  if  s != "ALL" and mss == "1900" and c!= "ALL":
     dd=regeleve.objects.filter(anne1=a,classe1=c,section1=s)
     print("by6")
  if  s != "ALL" and mss != "1900" and c == "ALL":
     dd=regeleve.objects.filter(anne1=a,code=mss,section1=s)
     print("by7")
 
  print("hi",mss,a,dd)
  ##################################
  for i in dd:
    
    if af == "حجب":
      i.rem1="oui"
    if af == "اظهار":
     i.rem1="non"
    
    i.save()
  
  if c != "ALL" and s != "ALL" and mss != "1900":
     dd=regeleve.objects.filter(anne1=a,classe1=c,section1=s,code=mss)
     print("by1")
  if c == "ALL" and s == "ALL" and mss == "1900":
     print("yai"),print(a),print(mss)
     dd=regeleve.objects.filter(anne1=a)
  
  if (c == "ALL") and (s == "ALL") and (mss!="1900"):
     dd=regeleve.objects.filter(anne1=a,code=mss)
     print("by2")
  if c == "ALL" and  mss == "1900" and s!= "ALL":
     dd=regeleve.objects.filter(anne1=a,section1=s)
     print("by3")
  if  s == "ALL" and mss == "1900" and c!= "ALL":
     dd=regeleve.objects.filter(anne1=a,classe1=c)
     print("by4")
  if  s == "ALL" and mss != "1900" and c!= "ALL":
     dd=regeleve.objects.filter(anne1=a,classe1=c,code=mss)
     print("by5")
  if  s != "ALL" and mss == "1900" and c!= "ALL":
     dd=regeleve.objects.filter(anne1=a,classe1=c,section1=s)
     print("by6")
  if  s != "ALL" and mss != "1900" and c == "ALL":
     dd=regeleve.objects.filter(anne1=a,code=mss,section1=s)
     print("by7")
 

  for i in dd:
    
    if afa == "حجب":
      i.rem2="oui"
    if afa == "اظهار":
     i.rem2="non"
    
    i.save()
  
  
  jasmin=regeleve.objects.filter(anne=a,classe1=c,section1=s,code=mss)
  
  for jj in jasmin:
    mfirst=jj.mois
  
  print(mss)
  print(af)
  print(a)
  print(c)
  print(s)
  ssss={'mss':mss,'jasmin':jasmin,'msss08':msss08,'anrec':aaa,'a':a,'c':c,'s':s,'af':af,'rec':dd,'afa':afa,'mfirst':mfirst}
  return render(request,'app1/directeur/passtoucarnetsma.html',ssss)





def test(request):
 x=0
 z1zmat=matiere.objects.all()
 for i in z1zmat:
   i.delete()
   x=x+1
   print(x)

 y=50000
 #for i in range(y):
  #  print(y)
 return render(request,'app1/directeur/test.html')


#########################   
def notepssA(request):
  nee="";nff=""
  sata=""
  nm=request.POST.get('nommat')
  gar=matiere.objects.filter(code=nm,nommatiere="arab1")
  #temp
  
  #
  a=request.POST.get('anne2032')
  c=request.POST.get('classe2030')
  s=request.POST.get('section2030')
  nee="";nff=""
  nee=request.POST.get('ne')
  nff=request.POST.get('nf')
  if nee == None: nee=""
  if nff== None: nff=""
  
  
  aaa=anne.objects.all()
  if len(gar) !=0:
    if nee != "" and nee != None and nff != ""  and nff != None:
      sata=regeleveps.objects.filter(anne1=a,nom1__contains=nee,famille1__contains=nff,classe1=c,section1=s,groupe="اللغة العربية")
    else:
      sata=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,groupe="اللغة العربية")

  ssss={'anrec':aaa,'rec':sata,'nm':nm,'a':a,'c':c,'s':s,'nee':nee,'nff':nff}
  print(nm)
  print(gar)
  print(a)
  return render(request,'app1/directeur/listps123.html',ssss)



def Asavenoteps01(request,icode,a,n,f,c,s):
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  fdfd=icode  
  dat=regeleveps.objects.get(id=icode)
  if s1 != None:
    dat.sem1=s1
  if s2 != None:
   dat.sem2=s2
  if s3 != None:
    dat.sem3=s3
  
  dat.save()
  aaa=anne.objects.all()
  sata=regeleveps.objects.filter(anne1=a,nom1__contains=n,famille1__contains=f,classe1=c,section1=s,groupe="اللغة العربية")

  n="";f=""
  ssss={'ii':fdfd,'anrec':aaa,'rec':sata,'a':a,'c':c,'s':s,'nee':n,'nff':f}
  return render(request,'app1/directeur/listps123.html',ssss)

#####

def notepssAF(request):
  nee="";nff=""
  sata=""
  nm=request.POST.get('nommat')
  gar=matiere.objects.filter(code=nm,nommatiere="francais1")
  
  a=request.POST.get('anne2032')
  c=request.POST.get('classe2030')
  s=request.POST.get('section2030')
  nee="";nff=""
  nee=request.POST.get('ne')
  nff=request.POST.get('nf')
  if nee == None: nee=""
  if nff== None: nff=""
  
  
  aaa=anne.objects.all()
  if len(gar) !=0:
    if nee != "" and nee != None and nff != ""  and nff != None:
      sata=regeleveps.objects.filter(anne1=a,nom1__contains=nee,famille1__contains=nff,classe1=c,section1=s,groupe="La langue francaise")
    else:
      sata=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,groupe="La langue francaise")

  ssss={'anrec':aaa,'rec':sata,'nm':nm,'a':a,'c':c,'s':s,'nee':nee,'nff':nff}
  print(nm)
  print(gar)
  print(a)
  return render(request,'app1/directeur/listps123F.html',ssss)



def Asavenoteps01F(request,icode,a,n,f,c,s):
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  dfdf=icode
  dat=regeleveps.objects.get(id=icode)
  if s1 != None:
    dat.sem1=s1
  if s2 != None:
   dat.sem2=s2
  if s3 != None:
    dat.sem3=s3
  
  dat.save()
  aaa=anne.objects.all()
  sata=regeleveps.objects.filter(anne1=a,nom1__contains=n,famille1__contains=f,classe1=c,section1=s,groupe="La langue francaise")

  n="";f=""
  ssss={'ii':dfdf,'anrec':aaa,'rec':sata,'a':a,'c':c,'s':s,'nee':n,'nff':f}
  return render(request,'app1/directeur/listps123F.html',ssss)

  ##########AAAAAAAAAAAAAAAA


def notepssAA(request):
  nee="";nff=""
  sata=""
  nm=request.POST.get('nommat')
  gar=matiere.objects.filter(code=nm,nommatiere="arab1")
  #temp
  
  #
  a=request.POST.get('anne2032')
  c=request.POST.get('classe2030')
  s=request.POST.get('section2030')
  nee="";nff=""
  nee=request.POST.get('ne')
  nff=request.POST.get('nf')
  if nee == None: nee=""
  if nff== None: nff=""
  
  
  aaa=anne.objects.all()
  if len(gar) !=0:
    if nee != "" and nee != None and nff != ""  and nff != None:
      sata=regeleveps.objects.filter(anne1=a,nom1__contains=nee,famille1__contains=nff,classe1=c,section1=s,groupe="اللغة العربية")
    else:
      sata=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,groupe="اللغة العربية")

  ssss={'anrec':aaa,'rec':sata,'nm':nm,'a':a,'c':c,'s':s,'nee':nee,'nff':nff}
  print(nm)
  print(gar)
  print(a)
  return render(request,'app1/directeur/listps123A.html',ssss)



def Asavenoteps01A(request,icode,a,n,f,c,s):
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  
  dat=regeleveps.objects.get(id=icode)
  if s1 != None:
    dat.sem1=s1
  if s2 != None:
   dat.sem2=s2
  if s3 != None:
    dat.sem3=s3
  
  dat.save()
  aaa=anne.objects.all()
  sata=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,groupe="اللغة العربية")

  n="";f=""
  ssss={'anrec':aaa,'rec':sata,'a':a,'c':c,'s':s,'nee':n,'nff':f}
  return render(request,'app1/directeur/listps123A.html',ssss)
############FFFFFFFFFFFFFFF



def notepssAFF(request):
  nee="";nff=""
  sata=""
  nm=request.POST.get('nommat')
  gar=matiere.objects.filter(code=nm,nommatiere="francais1")
  
  a=request.POST.get('anne2032')
  c=request.POST.get('classe2030')
  s=request.POST.get('section2030')
  nee="";nff=""
  nee=request.POST.get('ne')
  nff=request.POST.get('nf')
  if nee == None: nee=""
  if nff== None: nff=""
  
  
  aaa=anne.objects.all()
  if len(gar) !=0:
    if nee != "" and nee != None and nff != ""  and nff != None:
      sata=regeleveps.objects.filter(anne1=a,nom1__contains=nee,famille1__contains=nff,classe1=c,section1=s,groupe="La langue francaise")
    else:
      sata=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,groupe="La langue francaise")

  ssss={'anrec':aaa,'rec':sata,'nm':nm,'a':a,'c':c,'s':s,'nee':nee,'nff':nff}
  print(nm)
  print(gar)
  print(a)
  return render(request,'app1/directeur/listps123FF.html',ssss)



def Asavenoteps01FF(request,icode,a,n,f,c,s):
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  
  dat=regeleveps.objects.get(id=icode)
  if s1 != None:
    dat.sem1=s1
  if s2 != None:
   dat.sem2=s2
  if s3 != None:
    dat.sem3=s3
  
  dat.save()
  aaa=anne.objects.all()
  sata=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,groupe="La langue francaise")

  n="";f=""
  ssss={'anrec':aaa,'rec':sata,'a':a,'c':c,'s':s,'nee':n,'nff':f}
  return render(request,'app1/directeur/listps123FF.html',ssss)
######fils

def Asavenoteps01Afils(request,icode,a,n,f,c,s):
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  
  dat=regeleveps.objects.get(id=icode)
  if s1 != None:
    dat.sem1=s1
  if s2 != None:
   dat.sem2=s2
  if s3 != None:
    dat.sem3=s3
  
  dat.save()
  aaa=anne.objects.all()
  sata=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,groupe="اللغة العربية")

  n="";f=""
  ssss={'anrec':aaa,'rec':sata,'a':a,'c':c,'s':s,'nee':n,'nff':f}
  return render(request,'app1/directeur/listps123.html',ssss)
def Asavenoteps01Afilsf(request,icode,a,n,f,c,s):
  s1=request.POST.get('sem1')
  s2=request.POST.get('sem2')
  s3=request.POST.get('sem3')
  
  dat=regeleveps.objects.get(id=icode)
  if s1 != None:
    dat.sem1=s1
  if s2 != None:
   dat.sem2=s2
  if s3 != None:
    dat.sem3=s3
  
  dat.save()
  aaa=anne.objects.all()
  sata=regeleveps.objects.filter(anne1=a,classe1=c,section1=s,groupe="La langue francaise")

  n="";f=""
  ssss={'anrec':aaa,'rec':sata,'a':a,'c':c,'s':s,'nee':n,'nff':f}
  return render(request,'app1/directeur/listps123F.html',ssss)
##################################################################################
##################################################################################
###  structurecarnet



def strucar (request):
  anw=anne.objects.all()
  xann=("A")
  x001=request.POST.get('ann1')

  
  
  ff=structurecarnet.objects.filter(anne=x001)
    
    
  sss={'rec': ff,'annn' : anw,'an':x001}
  
  return render(request,'app1/directeur/structurecarnet.html',sss)

def delelmoiscar(request, cod01,asw):
 d=structurecarnet.objects.get(id=cod01)
 d.delete()
 
 xann=asw
 
 ff=structurecarnet.objects.filter(anne=xann)
    
    
 sss={'rec': ff,'annn' : xann,'an':xann}
  
 return render(request,'app1/directeur/structurecarnet.html',sss)

 
 
def addmoiscarnet(request, asw):
 xann=asw
 r=structurecarnet(anne=xann,mois="",code=0,nombremy=0,code1=0,code2=0,code3=0,code4=0,code5=0,code6=0,code7=0,code8=0,code9=0,code10=0,code11=0,code12=0,rem1="",rem2="")
 r.save()

 ff=structurecarnet.objects.filter(anne=xann)
    
    
 sss={'rec': ff,'annn' : xann,'an':xann}
  
 return render(request,'app1/directeur/structurecarnet.html',sss)




def updmoiscar(request,cod01,asss):
  iii=cod01
  asw=asss
  c0=request.POST.get('c')
  m=""
  c100=request.POST.get('c1')
  ny00=request.POST.get('ny')
  c200=request.POST.get('c2')
  c300=request.POST.get('c3')
  c400=request.POST.get('c4')
  c500=request.POST.get('c5')
  c600=request.POST.get('c6')
  c700=request.POST.get('c7')
  c800=request.POST.get('c8')
  c900=request.POST.get('c9')
  c1000=request.POST.get('c10')
  c1100=request.POST.get('c11')
  c1200=request.POST.get('c12')
  m=request.POST.get('mois01')
  print("hi")
  print(m)  
  print("hi")
  print(m)  
  print("hi")
  print(m)  
  print("hi")
  print(m)  
  z="x"
  w="y"
  d=structurecarnet.objects.get(id=iii)
  d.code=c0;d.nombremy=ny00;d.code1=c100;d.code2=c200;d.code3=c300;d.code4=c400;d.code5=c500
  d.code6=c600;d.code7=c700;d.code8=c800;d.code9=c900;d.code10=c1000
  d.code11=c1100;d.code12=c1200;d.rem2=z;d.rem1=w;d.mois=m;
  d.save()


  xann=asw
 
  ff=structurecarnet.objects.filter(anne=xann)
    
    
  sss={'rec': ff,'annn' : xann,'an':xann}
  
  return render(request,'app1/directeur/structurecarnet.html',sss)

def addmoiscarnetun(request):
  azn=request.POST.get('an1')
  m=request.POST.get('mois11')
  c0=request.POST.get('c')
  c100=request.POST.get('c1')
  ny00=request.POST.get('ny')
  c200=request.POST.get('c2')
  c300=request.POST.get('c3')
  c400=request.POST.get('c4')
  c500=request.POST.get('c5')
  c600=request.POST.get('c6')
  c700=request.POST.get('c7')
  c800=request.POST.get('c8')
  c900=request.POST.get('c9')
  c1000=request.POST.get('c10')
  c1100=request.POST.get('c11')
  c1200=request.POST.get('c12')
  z="x";w="y"
  d=structurecarnet(anne=azn,mois=m,code=c0,nombremy=ny00,code1=c100,code2=c200,code3=c300,code4=c400,code5=c500,
  code6=c600,code7=c700,code8=c800,code9=c900,code10=c1000,
  code11=c1100,code12=c1200,rem2="oui",rem1="oui")
  if m !=None and m !="" :
      d.save()
  
  
  asw=anne.objects.all()

  xann=asw
 
  ff=structurecarnet.objects.filter(anne=xann)
    
    
  sss={'rec': ff,'annn' : xann,'an':xann}
  
  return render(request,'app1/directeur/structurecarnetun.html',sss)
