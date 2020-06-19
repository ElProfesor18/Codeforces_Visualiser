from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from Cf_API_Interaction.About import *
from Cf_API_Interaction.Contest_Stats import *
from Cf_API_Interaction.Problem_Stats import *

from .forms import search_handle

from collections import OrderedDict

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .import fusioncharts
from .auxilliary import *
from .TimeTable import *

# Create your views here.

def is_valid(handle):
    Handle = handle
    url = 'https://codeforces.com/api/user.info?handles=' + Handle

    r = requests.get(url)
    dictr = r.json()

    # print(dictr)

    return dictr['status'] == "OK"

def search(request):
    if request.method == 'POST':
        form = search_handle(request.POST)

        if form.is_valid():
            handle = form.cleaned_data['name']

            if not is_valid(handle):
                return render(request, 'invalid_handle_search.html')

            return HttpResponseRedirect('/search/%s' %handle)

    else:
        form = search_handle()
        
    return render(request, 'visualise/search.html', {'form' : form})

def show(request, handle):
    print(handle) 
    content = {}
    content['about'] = about(handle)
    content['contest_stats'] = contest_stats(handle)
    content['problem_stats'] = problem_stats(handle)

    # print(content['problem_stats'])

    content['output_levels'] = get_levels(content, handle).render()
    content['output_problem_ratings'] = get_problem_rating(content, handle).render()
    content['output_languages'] = get_languages(content, handle).render()
    content['output_verdicts'] = get_verdicts(content, handle).render()
    content['output_tags'] = get_tags(content, handle).render()

    return render(request, 'visualise/show.html', content) 

def time_table(request):
    fcd = fetch_time_table()
    
    print(fcd)

    return render(request, "visualise/timetable.html", {"cols" : fcd})

     





