from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .form import ContactForm
from .models import Contact

def project(request):
    return render(request, "project_index.html")

def about(request):
    return render(request, "project_index.html")


def language(request):
    return render(request, "language.html")



def contact(request):
    if request.method == 'POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Comment=request.POST['comments']


        user=Contact.objects.create(name=Name,email=Email,comment=Comment)
        user.save()
        # form = ContactForm(request.POST)
        # if form.is_valid():
        #     form.save()
        return redirect('/')  # Replace 'success_url_name' with the name of the URL to redirect after successful form submission
    else:
        # form = ContactForm()

        return render(request, 'index.html')

