from utils.util import read_config
import requests
from datetime import datetime
LIB_VERSION = 1.2  # library version
MAX_RESULTS = 10000000
API_BASE_URL = "https://swissdox.linguistik.uzh.ch/api"


def get_headers(path):
    api_key, api_secret = read_config(path)
    headers = {
    "X-API-Key": api_key,
    "X-API-Secret": api_secret
    }
    return headers



def submit_query(yaml_string, query_name, query_comment, headers, expirationDate=None):
    API_URL_QUERY = f"{API_BASE_URL}/query"
   
    if expirationDate is not None:
        expiration_datetime = datetime(expirationDate[0], expirationDate[1] , expirationDate[2]).strftime("%Y-%m-%d")
    else:
        expiration_datetime = ''
    print('Expiration date', expiration_datetime)
    data = {
        "query": yaml_string,
        "name": query_name,
        "comment": query_comment,
       "expirationDate": {expiration_datetime}
    }

    r = requests.post(
        API_URL_QUERY,
        headers=headers,
        data=data
    )

    print('Request status code : ', r.status_code)
    return r.json(), yaml_string





def check_status(headers):
    """
    Check the status of all queries
    :return: String in json format
    """
    API_URL_STATUS = f"{API_BASE_URL}/status"

    r = requests.get(
        API_URL_STATUS,
        headers=headers
    )
    return r.json()

def check_status_id(status_id, headers):
    """
    Check the status of a specific query
    :param status_id:
    :return:
    """

    API_URL_STATUS = f"{API_BASE_URL}/status/{status_id}"

    r = requests.get(
        API_URL_STATUS,
        headers=headers
    )
    return r.json()

def download(tsv_uri, output_tsv_file, headers):
    """
    Download a file
    :param: tsv_uri: id of the file to download
    :param output_tsv_file: name of the output file
    """

    r = requests.get(
      tsv_uri,
      headers=headers
    )

    if r.status_code == 200:
        if r.content == 0:
          print('The file is empty!')
        print("Size of file: %.2f KB" % (len(r.content)/1024))
        fp = open(f"./{output_tsv_file}", "wb")
        fp.write(r.content)
        fp.close()
    else:
        print(r.text)


def get_query_id(json_response, query_name, case_sensitive=False):
    for js in json_response:
        if not case_sensitive:
            js_name = js['name'].lower().strip()
            query_name = query_name.lower().strip()
        else:
            js_name = js['name'].strip()
            query_name = query_name.strip()
        if js_name == query_name:
            return js['id']
    return None


def get_output_file(json_response, query_name=None, query_id=None):
    if not query_name and not query_id:
        raise ValueError('query_name and query_id params are both None!')

    if not query_id and query_name:
        id = get_query_id(json_response, query_name)
        if not id: return None
    else:
        id = query_id
    for js in json_response:
        if js['id'] == id:
            return js['downloadUrl']

    return None


def get_all_query_names(json_response, case_sensitive=False):
    names = []
    for js in json_response:
        if not case_sensitive:
            js_name = js['name'].lower().strip()
        else:
            js_name = js['name'].strip()

        names.append(js_name)
    return names