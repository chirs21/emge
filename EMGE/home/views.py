from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import MenApparel

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "home/home.html")
    else:
        return redirect(reverse('login'))

def partner(request):
    return render(request,'home/partner.html')

def about(request):
    return render(request,'home/aboutus.html')

def companyprofile(request):
    return render(request,'home/company_profile.html')

def dashboard(request):
    return render(request,'home/dashboard.html')

def terms(request):
    return render(request,'home/terms.html')

def menapparel(request):

	apparels = MenApparel.objects.all()
	search_term=''

	if 'name' in request.GET:
		apparels = apparels.order_by('id')
	
	if 'search' in request.GET:
		
		search_term= request.GET['search']
		apparels = apparels.filter(product_name__icontains=search_term)
		#print(doctors)

	context = {'apparels' : apparels,'search_term' : search_term}
	return render(request, 'home/men.html', context)
