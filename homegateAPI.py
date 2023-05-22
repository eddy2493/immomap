import requests

_headers = {
    'authority': 'api.homegate.ch',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://www.homegate.ch',
    'referer': 'https://www.homegate.ch/',
    'sec-ch-ua': '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

_json_data = {
    'query': {
        'offerType': 'RENT',
        'categories': [
            'APARTMENT',
            'MAISONETTE',
            'DUPLEX',
            'ATTIC_FLAT',
            'ROOF_FLAT',
            'STUDIO',
            'SINGLE_ROOM',
            'TERRACE_FLAT',
            'BACHELOR_FLAT',
            'LOFT',
            'ATTIC',
            'HOUSE',
            'ROW_HOUSE',
            'BIFAMILIAR_HOUSE',
            'TERRACE_HOUSE',
            'VILLA',
            'FARM_HOUSE',
            'CAVE_HOUSE',
            'CASTLE',
            'GRANNY_FLAT',
            'CHALET',
            'RUSTICO',
            'SINGLE_HOUSE',
            'HOBBY_ROOM',
            'CELLAR_COMPARTMENT',
            'ATTIC_COMPARTMENT',
        ],
        'excludeCategories': [
            'FURNISHED_FLAT',
        ],
        'location': {
            'geoTags': [
                'geo-zipcode-2501',
            ],
        },
    },
    'sortBy': 'listingType',
    'sortDirection': 'desc',
    'from': 0,
    'size': 0,
    'trackTotalHits': True,
    'fieldset': 'srp-list'
}

def _json_data_customizer(zip_code = 2501, offer_type='RENT', _size = 0, _from = 0):
    _json_data['query']['offerType'] = offer_type
    _json_data['query']['location']['geoTags'] = ['geo-zipcode-'+str(zip_code)]
    _json_data['size']=_size
    _json_data['from']=_from
    return _json_data

def get_number_of_listings(zip_code = 2501, offer_type='RENT'):
    return requests.post('https://api.homegate.ch/search/listings', headers=_headers, json=_json_data_customizer(zip_code, offer_type)).json()['total']

def get_listings(zip_code = 2501, offer_type='RENT'):
    _from = 0
    results = requests.post('https://api.homegate.ch/search/listings', headers=_headers, json=_json_data_customizer(zip_code, offer_type, 100, _from)).json()
    properties = results['results']
    while (_from < results['total']):
        _from += 100
        results = requests.post('https://api.homegate.ch/search/listings', headers=_headers, json=_json_data_customizer(zip_code, offer_type, 100, _from)).json()
        properties.extend(results['results'])
    return properties
    
