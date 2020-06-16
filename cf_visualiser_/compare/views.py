from django.shortcuts import render
from .forms import compare_handles
from django.http import HttpResponseRedirect

from Cf_API_Interaction.Compare import *

# Create your views here.
def compare(request):
    
    if request.method == 'POST':
        form = compare_handles(request.POST)

        if form.is_valid():
            handle1 = form.cleaned_data['name1']
            handle2 = form.cleaned_data['name2']

            print(handle1)
            print(handle2)

            para = handle1 + '&' + handle2
            print(para)

            return HttpResponseRedirect('/compare/%s' %para)

    else:
        form = compare_handles()
        
    return render(request, 'compare/compare_handles.html', {'form' : form})

def compute(request, handles):

    handles = handles.split('&')
    handle1 = handles[0]
    handle2 = handles[1]

    print(handle1)
    print(handle2)

    return render(request, 'compare/compute.html')