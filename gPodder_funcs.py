import requests
import base64
import json

def headers_generator(username,password):
    loginStr = username +":"+ password
    loginStr_encoded = base64.b64encode(loginStr.encode())
    loginStr_encoded=str(loginStr_encoded)[2:-1]
    headers = {'Authorization':'Basic '+ loginStr_encoded}
    return headers
def user_subscriptions(username,password):
    getSubs_URL = "https://gpodder.net/subscriptions/"+username+".json"
    Subs_response = requests.get(getSubs_URL, headers = headers_generator(username, password))
    Subs_response  = Subs_response.json()
    subs_list = []
    for item in Subs_response:
        subs_list.append({"title":str(item['title']), "subscribers":str(item['subscribers']),"description":str(item['description'])})
    return subs_list
def basic_search(searched_term):
    basicSearch_URL ="https://gpodder.net/search.json?q="+searched_term
    basicSearch_response = requests.get(url=basicSearch_URL)
    basicSearch_response = basicSearch_response.json()
    bs_list = []
    for item in basicSearch_response:
        bs_list.append({"title":str(item['title']), "subscribers":str(item['subscribers']),"description":str(item['description'])})
    return bs_list
def genre_search(searched_genre):
    genreSearch_URL ="https://gpodder.net/api/2/tag/"+searched_genre+"/50.json"
    genreSearch_response = requests.get(url=genreSearch_URL)
    genreSearch_response = genreSearch_response.json()
    gs_list = []
    for item in genreSearch_response:
        gs_list.append({"title":str(item['title']), "subscribers":str(item['subscribers']),"description":str(item['description'])})
    return gs_list
def popularity_search(topPodcast_Range):
    topPodcast_Range= str(topPodcast_Range)
    popularitySearch_URL = "https://gpodder.net/toplist/"+topPodcast_Range+".json"
    popularitySearch_response = requests.get(popularitySearch_URL)
    popularitySearch_response = popularitySearch_response.json()
    ps_list = []
    for item in popularitySearch_response:
        ps_list.append({"title":str(item['title']), "subscribers":str(item['subscribers']),"description":str(item['description'])})
    return ps_list
def user_suggestions(username,password):
    suggestions_URL = "https://gpodder.net/suggestions/10.json"
    suggestions_response = requests.get(suggestions_URL, headers = headers_generator(username, password))
    suggestions_response = suggestions_response.json()
    sr_list = []
    for item in suggestions_response:
        sr_list.append({"title":str(item['title']), "subscribers":str(item['subscribers']),"description":str(item['description'])})
    return sr_list
