from collections import OrderedDict
# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .import fusioncharts

def get_tags(content, handle):
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Tags of " + handle
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    for item in content['problem_stats']['ProblemTags']:
        chartData[item] = int(content['problem_stats']['ProblemTags'][item])


    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        if(key == 'OK'):
            key = 'AC'
        data["label"] = str(key)
        data["value"] = str(value)
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    doughnut2d = fusioncharts.FusionCharts("doughnut2d", "Tags Chart", "800", "700", "tags_chart", "json", dataSource)

    return doughnut2d

def get_verdicts(content, handle):
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Verdicts of " + handle
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    for item in content['problem_stats']['Problem_Verdicts']:
        chartData[item] = int(content['problem_stats']['Problem_Verdicts'][item])


    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        if(key == 'OK'):
            key = 'AC'
        data["label"] = str(key)
        data["value"] = str(value)
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    pie2D = fusioncharts.FusionCharts("pie2d", "Verdicts Chart", "800", "700", "verdicts_chart", "json", dataSource)

    return pie2D

def get_languages(content, handle):
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Languages of " + handle
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    for item in content['problem_stats']['Languages']:
        chartData[item] = int(content['problem_stats']['Languages'][item])


    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = str(key)
        data["value"] = str(value)
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    pie2D = fusioncharts.FusionCharts("pie2d", "Languages Chart", "700", "500", "languages_chart", "json", dataSource)

    return pie2D

def get_problem_rating(content, handle):
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Problem Ratings of " + handle
    chartConfig["xAxisName"] = "Rating"
    chartConfig["yAxisName"] = "Number of Problems"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    ratings = []
    for item in content['problem_stats']['ProblemRatings']:
        ratings.append(int(item))

    ratings.sort()
    ratings.reverse()
    for item in ratings:
        chartData[int(item)] = int(content['problem_stats']['ProblemRatings'][item])


    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = str(key)
        data["value"] = str(value)
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = fusioncharts.FusionCharts("column2d", "Problem Ratings Chart", "700", "500", "problem_ratings_chart", "json", dataSource)

    return column2D

def get_levels(content, handle):
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Levels of " + handle
    chartConfig["xAxisName"] = "Rating"
    chartConfig["yAxisName"] = "Number of Problems"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    levels = []
    for item in content['problem_stats']['ProblemIndex']:
        levels.append(str(item))

    levels.sort()
    levels.reverse()
    for item in levels:
        chartData[item] = int(content['problem_stats']['ProblemIndex'][str(item)])

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = str(value)
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = fusioncharts.FusionCharts("column2d", "Levels Chart", "700", "500", "levels_chart", "json", dataSource)

    return column2D