from django.shortcuts import render
from .forms import compare_handles
from django.http import HttpResponseRedirect

from Cf_API_Interaction.Compare import *
from Cf_API_Interaction.About import *
from Cf_API_Interaction.Contest_Stats import *
from Cf_API_Interaction.Problem_Stats import *

from .auxilliary import *

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

    content = {}

    content['output_contests'] = get_contests(handle1, handle2).render()

    my_dict1 = problem_stats(handle1)
    my_dict2 = problem_stats(handle2)
    
    content['output_unsolved'] = get_unsolved(handle1, handle2, my_dict1, my_dict2).render()
    content['output_max_submission'] = get_max_submission(handle1, handle2, my_dict1, my_dict2).render()
    content['output_max_ac'] = get_max_ac(handle1, handle2, my_dict1, my_dict2).render()

    res = get_common_contests(handle1, handle2)

    my_dict3, my_dict4 = get_rating_stats(handle1, handle2)
    
    result = []
    for i in res:
        tlist = []

        for j in range(4): 
            tlist.append(i[j])

        tlist.append(abs(tlist[3]-tlist[2]))
        result.append(tlist)

    content['result'] = result
    content['handle1'] = handle1
    content['handle2'] = handle2

    content['my_dict3'] = my_dict3
    content['my_dict4'] = my_dict4

    content['output_rating_stats'] = get_rating_chart(handle1, handle2, my_dict3, my_dict4).render()

    content['output_tags'] = get_tags_chart(handle1, handle2, my_dict1, my_dict2).render()
    
    content['output_levels'] = get_levels_chart(handle1, handle2, my_dict1, my_dict2).render()

    content['output_problem_ratings'] = get_problem_ratings_chart(handle1, handle2, my_dict1, my_dict2).render()

    content['common_problems_solved'] = get_common_problems(handle1, handle2)

    return render(request, 'compare/compute.html', content) 