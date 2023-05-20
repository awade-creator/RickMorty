import requests

BASE = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

def api_request(BASE, endpoint, n_page):
    response = requests.get(BASE + endpoint + f'?page={n_page}')
    return response.json()



def get_pages(response):
    """
        Keys are indexed to gather pages and information values
    """
    pages = response['info']['pages']
    return pages


def json_parse(response):
    """
        dictionary created from the response.
        names and episodes are extracted from the response.
        returning the dictionary with appended names and episodes
    """
    personaList = [] 
    
    for item in response['results']:
        personas = {
            'name': item['name'],
            'number_of_episodes': len(item['episode']),
        }
        
        personaList.append(personas)
    return personaList


json_data = api_request(BASE, endpoint, 0)
for n_page in range(1, get_pages(json_data) + 1):
    print(n_page)
    api_request(BASE, endpoint, n_page)


#print(json_parse(json_data))








