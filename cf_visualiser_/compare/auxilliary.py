from Cf_API_Interaction.Compare import *
from Cf_API_Interaction.About import *
from Cf_API_Interaction.Contest_Stats import *
from Cf_API_Interaction.Problem_Stats import *

from collections import OrderedDict
# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .import fusioncharts

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def get_contests(handle1, handle2):
    my_dict1 = contest_stats(handle1)
    my_dict2 = contest_stats(handle2)
    
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Contests"
    chartConfig["xAxisName"] = "Handles"
    chartConfig["yAxisName"] = "Number of Contests"
    chartConfig["theme"] = "fusion"

    result = {}
    result[handle1] = my_dict1['NoOfContests']
    result[handle2] = my_dict2['NoOfContests']

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()

    for item in result.keys():
        chartData[item] = int(result[str(item)])

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    cnt=0
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = str(value)
    
        if cnt==1:
            data["color"] = "#5ad1a7"
        dataSource["data"].append(data)
        cnt += 1


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = fusioncharts.FusionCharts("column2d", "Contests Chart", "700", "500", "contests_chart", "json", dataSource)

    return column2D

def get_unsolved(handle1, handle2, my_dict1, my_dict2):
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Unsolved"
    chartConfig["xAxisName"] = "Rating"
    chartConfig["yAxisName"] = "Number of Unsolved Problems"
    chartConfig["theme"] = "fusion"

    result = {}
    result[handle1] = len(my_dict1['Unsolved'])
    result[handle2] = len(my_dict2['Unsolved'])

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()

    for item in result.keys():
        chartData[item] = int(result[str(item)])

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    cnt=0
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = str(value)
    
        if cnt==1:
            data["color"] = "#5ad1a7"
        dataSource["data"].append(data)
        cnt += 1
        


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = fusioncharts.FusionCharts("column2d", "Unsolved Chart", "700", "500", "unsolved_chart", "json", dataSource)

    return column2D

def get_max_submission(handle1, handle2, my_dict1, my_dict2):
    my_dict1 = problem_stats(handle1)
    my_dict2 = problem_stats(handle2)
    
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Max Submission"
    chartConfig["xAxisName"] = "Handles"
    chartConfig["yAxisName"] = "Number of Submissions"
    chartConfig["theme"] = "fusion"

    result = {}
    result[handle1] = my_dict1['Max_Attempts'][1]
    result[handle2] = my_dict2['Max_Attempts'][1]

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()

    for item in result.keys():
        chartData[item] = int(result[str(item)])

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    cnt=0
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = str(value)
    
        if cnt==1:
            data["color"] = "#5ad1a7"
        dataSource["data"].append(data)
        cnt += 1


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = fusioncharts.FusionCharts("column2d", "Max Submission Chart", "700", "500", "max_submission_chart", "json", dataSource)

    return column2D

def get_max_ac(handle1, handle2, my_dict1, my_dict2):
    my_dict1 = problem_stats(handle1)
    my_dict2 = problem_stats(handle2)
    
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Max AC"
    chartConfig["xAxisName"] = "Handles"
    chartConfig["yAxisName"] = "Number of Submissions"
    chartConfig["theme"] = "fusion"

    result = {}
    result[handle1] = my_dict1['Max_AC'][1]
    result[handle2] = my_dict2['Max_AC'][1]

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()

    for item in result.keys():
        chartData[item] = int(result[str(item)])

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    cnt=0
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = str(value)
    
        if cnt==1:
            data["color"] = "#5ad1a7"
        dataSource["data"].append(data)
        cnt += 1


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = fusioncharts.FusionCharts("column2d", "Max AC Chart", "700", "500", "max_ac_chart", "json", dataSource)

    return column2D

def get_common_contests(handle1, handle2):
    url = 'https://codeforces.com/api/user.rating?handle='

    r1 = requests.get(url+handle1)
    dictr1 = r1.json()

    r2 = requests.get(url+handle2)
    dictr2 = r2.json()

    res = []
    mydict1 = {}
    mydict2 = {}

    contests_id1 = []
    contests_id2 = []

    if(dictr1['status'] == "OK"):
        tdict1 = json_normalize(dictr1['result'])

        cnt = 0
        for i in tdict1['contestId']:
            contests_id1.append(i)
            mydict1[i] = ((tdict1['contestName'][cnt], tdict1['rank'][cnt]))
            cnt += 1


    if(dictr2['status'] == "OK"):
        tdict2 = json_normalize(dictr2['result'])

        cnt = 0
        for i in tdict2['contestId']:
            contests_id2.append(i)
            mydict2[i] = ((tdict2['contestName'][cnt], tdict2['rank'][cnt]))
            cnt += 1

    common_contests = intersection(contests_id1, contests_id2)

    for i in common_contests:
        res.append((i, mydict1[i][0], mydict1[i][1], mydict2[i][1]))
    
    return res

def get_rating_stats(handle1, handle2):
    url = 'https://codeforces.com/api/user.rating?handle='

    r1 = requests.get(url+handle1)
    dictr1 = r1.json()

    r2 = requests.get(url+handle2)
    dictr2 = r2.json()

    my_dict1 = {}
    my_dict2 = {}

    rating_id1 = []
    rating_id2 = []

    if(dictr1['status'] == "OK"):
        tdict1 = json_normalize(dictr1['result'])

        for i in tdict1['newRating']:
            rating_id1.append(i)


    if(dictr2['status'] == "OK"):
        tdict2 = json_normalize(dictr2['result'])

        for i in tdict2['newRating']:
            rating_id2.append(i)
    
    my_dict1['CurrRating'] = rating_id1[(len(rating_id1)-1)]
    my_dict2['CurrRating'] = rating_id2[(len(rating_id2)-1)]

    rating_id1.sort()
    rating_id2.sort()

    my_dict1['MinRating'] = rating_id1[0]
    my_dict1['MaxRating'] = rating_id1[len(rating_id1)-1]


    my_dict2['MinRating'] = rating_id2[0]
    my_dict2['MaxRating'] = rating_id2[len(rating_id2)-1]  

    print(my_dict1)
    print(my_dict2)  

    # We need to work on this.