import requests
from pandas import json_normalize

def about(handle):

    Handle = handle
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

        if 'firstName' not in temp.keys():
            temp['firstName'] = 'NA'

        if 'lastName' not in temp.keys():
            temp['lastName'] = 'NA'
        
        if 'city' not in temp.keys():
            temp['city'] = 'NA'

        if 'country' not in temp.keys():
            temp['country'] = 'NA'
        
        if 'organization' not in temp.keys():
            temp['organization'] = 'NA'
        
        if 'rank' not in temp.keys():
            temp['rank'] = 'NA'

        if 'maxRank' not in temp.keys():
            temp['maxRank'] = 'NA'

        if 'rating' not in temp.keys():
            temp['rating'] = 'NA'

        if 'maxRating' not in temp.keys():
            temp['maxRating'] = 'NA'
        
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

        return result