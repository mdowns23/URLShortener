from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Url mapping for app
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        # Store URL in variable
        url = request.POST['link']

        # Create unique shortened id for url
        uid = str(uuid.uuid4())[:5]

        # Store new url in database
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    # Get Url from database using variable pk
    url_details = Url.objects.get(uuid=pk)
    # Redirect user to website by getting link from database
    return redirect(url_details.link)