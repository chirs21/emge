from django.shortcuts import render, get_object_or_404, redirect, reverse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect(reverse('login'))
