import requests


class BookingAPI:
    """класс с методами для тестирования брони"""
    def __init__(self):
        self.site_url = 'https://restful-booker.herokuapp.com/'
        self.headers = {"Cookie": None,
                "Accept": "application/json",
                "Content-Type": "application/json"}

    def auth(self, username, password):
        """авторизация н сайте"""
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(self.site_url + 'auth', data)
        assert response.status_code == 200, 'Ошибка авторизации'
        self.headers['Cookie'] = 'token=' + response.json()['token']

    def create_booking(self, **kwargs):
        """создание брони"""
        data = {
            "firstname": kwargs.get('firstname'),
            "lastname": kwargs.get('lastname'),
            "totalprice": 109,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2022-07-11",
                "checkout": "2022-07-18"
            },
            "additionalneeds": "Dinner"
        }

        response = requests.post(self.site_url + 'booking', json=data, headers=self.headers)
        assert response.status_code == 200, 'Ошибка запроса'
        return response.json()['bookingid']

    def get_booking_ids(self):
        """получение id всех броней"""
        booking_ids = requests.get(self.site_url + 'booking')
        assert booking_ids.status_code == 200, 'Ошибка запроса'
        return booking_ids.json()

    def refresh_booking(self, id, **kwargs):
        """изменение имени, фамилии и цены в готовой брони"""
        data = {
            "firstname": kwargs.get('firstname'),
            "lastname": kwargs.get('lastname'),
            "totalprice": kwargs.get('totalprice'),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2022-07-11",
                "checkout": "2022-07-18"
            },
            "additionalneeds": "Dinner"
        }

        refr = requests.put(self.site_url +  'booking/' + id, json=data, headers=self.headers)
        assert refr.status_code == 200, 'Ошибка запроса'

    def get_booking(self, id):
        """получение информакии о существующей брони по id"""
        return requests.get(self.site_url + 'booking/' + id).json()

    def make_id_list(self, results):
        """создание списка из id всех существующих броней"""
        id_list = []
        for i in results:
            id_list.append(str(i['bookingid']))
        return id_list     





