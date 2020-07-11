from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from .models import Company, Contact,Post 
from home.forms import ContactForm,Profile,PostForm 
from Magenta.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.db.models import Q

# Create your views here.
global s

def home(request):
    #if request.user.is_authenticated:
    return render(request, "home/home.html")
    #else:
        #return redirect(reverse("home"))

def partner(request):
	if request.method == 'POST':
		form2 = ContactForm(request.POST, request.FILES or None)
		print(form2.errors)
		if form2.is_valid():
			
			form2.save()
			#return redirect('partner')
			subject= form2.cleaned_data.get('subject')
			message=form2.cleaned_data.get('mssg')
			recepient=form2.cleaned_data.get('email')
			send_mail(subject, 
				message, recepient, [ EMAIL_HOST_USER], fail_silently = False)	
			return render(request, 'home/success.html', {'recepient': recepient})
	else:
		form2 = ContactForm()

	context = {'form2' : form2}
	return render(request,'home/partner.html',context)

def about(request):
    return render(request,'home/aboutus.html')


def dashboard(request):
    return render(request,'home/dashboard1.html')

def terms(request):
    return render(request,'home/terms.html')

def profile(request):
	#info = Post.objects.filter(id=inf_id)
	companies = Company.objects.get(id__exact=4)
	posts=Post.objects.get(Industry_id__exact=3)
		
	if request.method == 'POST':
		#print("apppppple")
		form3 = Profile(request.POST, request.FILES or None )
		print(form3.errors)
		
		if form3.is_valid():
			print(form3.errors)
			form3.save()
			return redirect('home')
	else:
		form3 = Profile()

	context = {'media_url':settings.MEDIA_URL,'form3':form3,'companies':companies,'posts' : posts}
	
	return render(request,'home/profile.html', context)

"""
def search(request):

	posts = Post.objects.all()
	companies = Company.objects.all()
	group = []
	
	
	search_term=''

	if 'name' in request.GET:
		posts = posts.order_by('id')
	
	if 'search' in request.GET:
		search_term= request.GET['search']
		mylist = search_term.split(',')
		c=len(mylist)
		k=0
		group=[]
		res=[]

		print(mylist)
		for j in mylist:
			if k<c:
				k+=1
				print("hi")
				group.append(posts.filter(Q(Locations__icontains=j) | Q(Brand__icontains=j )))	
				
				
				
		#companies=companies.filter(id == posts.industry)
	res = list(set(i for j in group for i in j))

	
	context = {'res' : res,'media_url':settings.MEDIA_URL,'companies':companies}
	return render(request, 'home/search1.html', context)
"""

def search(request):
	posts = Post.objects.all()
	companies = Company.objects.all()
	
	search_term=''

	if 'name' in request.GET:
		posts = posts.order_by('id')
	
	
	if 'search' in request.GET:
		search_term= request.GET['search']
		res = posts.filter(Q(pro1__icontains=search_term) | Q(Brand__icontains=search_term ) | Q(Industry__organisation__icontains=search_term))
		
		#companies=companies.filter(id == posts.industry)
	
	context = {'res' : res,'search_term' : search_term,'media_url':settings.MEDIA_URL,'companies':companies}
	return render(request, 'home/search1.html', context)

def filter_it(request,search_term):
	posts = Post.objects.all()
	companies = Company.objects.all()
	term=''
	#search_term=search_term[1]
	res= posts.filter(Q(pro1__icontains=search_term) | Q(Brand__icontains=search_term ) | Q(Industry__organisation__icontains=search_term))
	print(search_term)
	
	if 'name' in request.GET:
		posts = posts.order_by('id')
	
	if 'search' in request.GET:
		res = posts.filter(Q(Locations__icontains=search_term) | Q(Brand__icontains=search_term ) | Q(Industry__organisation__icontains=search_term))
		term= request.GET['search']
		mylist = term.split(',')
		c=len(mylist)
		k=0
		group=[]
		
		#print(type(Res))
		print(mylist)
		for j in mylist:
			if k<c:
				k+=1
				group.append(res.filter(Q(Locations__icontains=j) | Q(Brand__icontains=j )))	
			
				
		#companies=companies.filter(id == posts.industry)
		res = list(set(i for j in group for i in j))

	context = {'res' : res,'media_url':settings.MEDIA_URL,'search_term' : search_term,'companies':companies}
	
	return render(request, 'home/search1.html', context)

def companyprofile(request, inf_id):
	info = Post.objects.filter(id=inf_id)
	#companies = Company.objects.all()
	context = {'info' : info}
	
	return render(request,'home/company_profile.html', context)

def post(request):
	
	companies = Company.objects.get(id__exact=4)
	posts=Post.objects.get(Industry_id__exact=3)
	
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES or None)
		print(form.errors)
		if form.is_valid():
			
			form.save()
			return redirect('home')
	else:
		form = PostForm()

	context = {'form' : form,'posts':posts,'companies':companies}
	return render(request,'home/contactform.html',context)