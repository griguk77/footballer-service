import requests


def test_get_all_footballer(url: str):
    res = requests.get(url).json()
    assert (res == [{'clubs_id': 1, 'name': 'Killian', 'surname': 'Mbappe', 'age': 24, 'goals': 86},
                    {'clubs_id': 2, 'name': 'Cristiano', 'surname': 'Ronaldo', 'age': 31, 'goals': 837}])


def test_get_footballer_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {'clubs_id': 1, 'name': 'Killian', 'surname': 'Mbappe', 'age': 24, 'goals': 86})
    print("3")


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/footballers/'
    test_get_footballer_by_id(URL + '1')
    test_get_all_footballer(URL)
