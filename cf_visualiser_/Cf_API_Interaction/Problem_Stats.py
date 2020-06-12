import requests
import pandas as pd 
from pandas import json_normalize

Handle = 'ElProfesor._.'
url = 'https://codeforces.com/api/user.status?handle=' + Handle

r = requests.get(url)
dictr = r.json()

def most_frequent(List): 
    dict = {} 
    count, itm = 0, ('', '') 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm, count)

def edit_problem_index(x):
    x = x[0]
    return x 

if(dictr['status'] == "OK"):
    tdict = json_normalize(dictr['result'])
    print(tdict.keys())

    result = {}

    # Set to find unsolved
    Unsolved = set()

    problemsTried = []
    problemsSolved = []
    problemRatings = []
    problemTags = []

    for i in range(len(tdict)):
        key = (tdict['problem.contestId'][i], tdict['problem.index'][i])

        if(tdict['verdict'][i] == 'OK'):
            problemsSolved.append((tdict['problem.contestId'][i], tdict['problem.index'][i]))
            if type(tdict['problem.rating'][i]) != None :
                problemRatings.append((tdict['problem.contestId'][i], tdict['problem.index'][i], tdict['problem.rating'][i]))
            
            if type(tdict['problem.tags'][i]) != None :
                for tag in tdict['problem.tags'][i]:
                    problemTags.append((key, tag))


        problemsTried.append((tdict['problem.contestId'][i], tdict['problem.index'][i]))

    result['Max_AC(s)'] = most_frequent(problemsSolved)
    result['Max_Attempts'] = most_frequent(problemsTried)

    problemsTried = list(set(problemsTried))
    problemsSolved = list(set(problemsSolved))
    problemRatings = list(set(problemRatings))
    problemTags = list(set(problemTags))

    for i in problemsTried:
        Unsolved.add(i)
    
    for i in problemsSolved:
        Unsolved.remove(i)
    
    result['Tried'] = len(problemsTried)
    result['Solved'] = len(problemsSolved)
    result['Unsolved'] = Unsolved

    result['Solved_With_One_Submission'] = '???'
    result['AverageAttempts'] = '???'

    result['Languages'] = dict(tdict['programmingLanguage'].value_counts())
    
    # Counts Problem Indexes A, B, C, D, E, F ...
    df1 = pd.DataFrame(problemsSolved)
    df1[1] = df1[1].apply(edit_problem_index)
    
    result['ProblemIndex'] = dict(df1[1].value_counts())

    # Count Problem Ratings 800, 900, ...
    df2 = pd.DataFrame(problemRatings)    
    result['ProblemRatings'] = dict(df2[2].value_counts())

    # Count Problem Verdicts AC, TLE, ...
    result['Problem_Verdicts'] =  dict(tdict['verdict'].value_counts())

    # Count Problem Tags
    df3 = pd.DataFrame(problemTags)  
    result['ProblemTags'] = dict(df3[1].value_counts())
    
    print(result)