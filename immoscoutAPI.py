import requests

_headers = {
    'authority': 'rest-api.immoscout24.ch',
    'accept': 'text/plain, application/json, text/json',
    'accept-language': 'en-US,en;q=0.6',
    'is24-meta-pagesize': '20',
    'origin': 'https://www.immoscout24.ch',
    'referer': 'https://www.immoscout24.ch/',
    'sec-ch-ua': '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'is24-meta-pagenumber': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-originalclientip': '64.252.144.138',
    'x-originalurl': 'http%3A%2F%2Fwww.immoscout24.ch%2Fde',
}

_params = {
    's': '1',
    't': '1',
    'l': '5220',
}

def _get_immoscout_location_id(zip_code = 2502):
    params = {}
    params['term'] = zip_code
    id_request = requests.get('https://rest-api.immoscout24.ch/v4/de/locations', params=params, headers=_headers).json()
    if len(id_request)>0:
        return id_request[0]['id']


def get_number_of_listings(zip_code = 2501, offer_type='RENT'):
    immoscout_location_id = _get_immoscout_location_id(zip_code)
    if immoscout_location_id is not None:
        params = {}
        params['s']=1
        params['t']=1 if offer_type=='RENT' else 2
        params['l']=immoscout_location_id
        return requests.get('https://rest-api.immoscout24.ch/v4/de/serpsearchfilters', params=params, headers=_headers).json()['searchMetaData']['totalMatches']
    else: return 0
        

def get_listings(zip_code = 2501, offer_type='RENT'):
    immoscout_location_id = _get_immoscout_location_id(zip_code)
    if immoscout_location_id is not None:
        params = {}
        params['s']=1
        params['t']=1 if offer_type=='RENT' else 2
        params['l']=immoscout_location_id
        params['inp']=1
    results = requests.get('https://rest-api.immoscout24.ch/v4/de/properties', params=params, headers=_headers).json()
    _is24_meta_pagenumber = 1
    while (_is24_meta_pagenumber <= results['pagingInfo']['totalPages']):
        _is24_meta_pagenumber +=1
        _headers['is24-meta-pagenumber'] = str(_is24_meta_pagenumber)
        _res = requests.get('https://rest-api.immoscout24.ch/v4/de/properties', params=params, headers=_headers).json()
        results['properties'].extend(_res['properties'])
    return results['properties']