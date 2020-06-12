import requests
from pandas import json_normalize

Handle = 'ElProfesor._.'
url = 'https://codeforces.com/api/user.rating?handle=' + Handle

r = requests.get(url)
dictr = r.json()

# print(dictr)

if(dictr['status'] == "OK"):
    tdict = json_normalize(dictr['result'])
    print(tdict.keys())

    result = {}
    result['NoOfContests'] = len(tdict)

    delta = []
    rank = []

    diff = tdict['newRating'][0] - 1500
    delta.append((diff, int(tdict['contestId'][0])))

    rank.append((tdict['rank'][0], int(tdict['contestId'][0])))

    for i in range(1, len(tdict)):
        diff = tdict['newRating'][i] - tdict['oldRating'][i]
        delta.append( (diff, int(tdict['contestId'][i])))

        rank.append((tdict['rank'][i], int(tdict['contestId'][i])))

    delta.sort()
    rank.sort()

    result['MaxUp'] = delta[len(delta) - 1]
    result['MaxDown'] = delta[0]

    result['BestRank'] = rank[0]
    result['WorstRank'] = rank[len(rank) - 1]

    print(result)