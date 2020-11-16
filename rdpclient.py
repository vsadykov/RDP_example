"""
__author__ = "Viacheslav M Sadykov"
__version__ = 1.0.1
__status__ = "Released"
"""


import requests


def apiget_flights_all():
    url = 'https://solarflare.njit.edu/RDP/ARMAS_API/apiget_flights_all.php'
    request = requests.get(url, timeout=20)
    data = request.json()
    return data


def apiget_flights_selected(flightID = 'none', start_time = 'none', end_time = 'none'):
    warningmessage = 'Specify either flightID or the pair of start_time and end_time variables'
    if ((flightID == 'none') and (start_time == 'none')):
        print (warningmessage)
        return
    if ((flightID == 'none') and (end_time == 'none')):
        print (warningmessage)
        return
    if (flightID == 'none'):
        url = 'https://solarflare.njit.edu/RDP/ARMAS_API/apiget_flights_selected.php'
        url += '?start_time='+start_time+'&end_time='+end_time
        request = requests.get(url, timeout=20)
        data = request.json()
        return data
    else:
        url = 'https://solarflare.njit.edu/RDP/ARMAS_API/apiget_flights_selected.php'
        url += '?flightID='+flightID
        request = requests.get(url, timeout=20)
        data = request.json()
        return data


def apiget_flightmeasurements_byID(flightID = 'none'):
    warningmessage = 'Specify the flightID'
    if (flightID == 'none'):
        print (warningmessage)
        return
    url = 'http://localhost/RDP/ARMAS_API/apiget_flightmeasurements_byID.php'
    url += '?flightID='+flightID
    request = requests.get(url, timeout=20)
    data = request.json()
    return data
