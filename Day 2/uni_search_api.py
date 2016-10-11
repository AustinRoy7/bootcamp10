

#Program that searches for  universities in a country and returns the country, name and domain of the university utilising the hipolabs university API

import urllib2
import json

def uni_search(query):
    url = 'http://universities.hipolabs.com/search?country='
    country = query.replace(' ', '%20')
    final_url = url + country
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    
    for item in data['objects']:
        print item['country'], item['name'],item['domain']