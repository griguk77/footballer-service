import requests


def test_get_all_footballers(url: str):
    res = requests.get(url).json()
    assert (res == [
        {'clubs_id': 1, 'name': 'Mbappe',
         'country': 'France',
         'goals': '50', 'age': '34'},
        {'clubs_id': 2, 'name': 'Ronaldo',
         'country': 'Portugal',
         'goals': '5', 'age': '26'},
        {'clubs_id': 3, 'name': 'Akinfeev',
         'country': 'Russia',
         'goals': '90', 'age': '47'},
        {'clubs_id': 3, 'name': 'Dzagoev',
         'country': 'Russia',
         'goals': '105', 'age': '36'}
    ])


def test_get_footballer_by_id(url: str):
    res = requests.get(url).json()
    assert (res == [{'clubs_id': 3, 'name': 'Akinfeev',
                     'country': 'Russia',
                     'goals': '90', 'age': '47'},
                    {'clubs_id': 3, 'name': 'Dzagoev',
                     'country': 'Russia',
                     'goals': '105', 'age': '36'}])


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/footballers/'
    test_get_footballer_by_id(URL + '3')
    test_get_all_footballers(URL)
