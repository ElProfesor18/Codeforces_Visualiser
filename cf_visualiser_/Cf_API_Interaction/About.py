import requests
from pandas import json_normalize

Handle = 'ElProfesor._.'
url = 'https://codeforces.com/api/user.info?handles=' + Handle

r = requests.get(url)
dictr = r.json()

# print(dictr)

if(dictr['status'] == "OK"):
    tdict = json_normalize(dictr['result'])
    # print(temp.keys())

    temp = {}

    for k in tdict.keys():
        if k!= 'organization':
            temp.update({k : str(tdict[k][0]).capitalize()})
        else:
            temp.update({k : str(tdict[k][0])})

    result = {}

    Name = temp['firstName'] + ' ' + temp['lastName']
    Location = temp['city'] + ', ' + temp['country']
    Affiliation = 'From ' + temp['organization']
    rank = temp['rank']
    maxRank = temp['maxRank']
    rating = temp['rating']
    maxRating = temp['maxRating']

    result['rank'] = rank
    result['handle'] = Handle
    result['Name'] = Name
    result['Location'] = Location
    result['Affiliation'] = Affiliation
    result['ContestRating'] = 'Contest Rating: ' + rating + ' (max. ' + maxRank + ', ' + maxRating + ')'

    print(result)