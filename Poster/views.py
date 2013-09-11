from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect, Http404 #Http403
from django.shortcuts import render_to_response
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User

from Poster.models import *

#from NaN.forms import *

def homepage(request):
    return render_to_response('homepageTemplate.html')

def ajaxBlocksHome(request):
    return render_to_response('ajaxBlocksHome.html')

def ajaxBlocksSearch(request, searchString):
    #if request.user.is_superuser:
        #raise PermissionDenied
    
    color = searchString
    found = True 
    results = Blocks.objects.filter(color=color)
    if not results:
        results = Blocks.objects.all()
        found = False
    #return render_to_response('ajaxBlocksRender.html', {
    return render_to_response('ajaxBlocksRender.html', {
                                "results": results,
                                "found": found,
                                "color": color,
                                })