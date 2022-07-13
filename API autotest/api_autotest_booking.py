import unittest
from class_creation import BookingTestClass


class BookingTest(unittest.TestCase):
    name = 'Dadya'
    new_name = 'galya'
    lastname = 'Badya'
    new_lastname = 'otmena'
    username = 'admin'
    password = 'password123'
    new_totalprice = 228


    @classmethod
    def setUpClass(cls):
        cls.booking_class = BookingTestClass()
        cls.booking_class.auth(cls.username, cls.password)

    def test_booking_create(self):
        """тест создания новой брони и ее изменения"""
        #получаем количество всех созданных до нас броней
        start_amount = len(self.booking_class.get_booking_ids())

        #создаем новую бронь и получаем ее id
        new_id = str(self.booking_class.create_booking(firstname=self.name,lastname=self.lastname)) 

        #получаем данные о всех бронях созданных на сайте
        second_booking_results = self.booking_class.get_booking_ids()

        #получаем количество всех броней с учетом нашей собственной
        finish_amount = len(second_booking_results) 

        #получаем список из всех id всех броней
        finish_ids = self.booking_class.make_id_list(second_booking_results)

        #проверяем наличие id созданой нами брони в списке всех существующих
        self.assertTrue(new_id in finish_ids, 'ID не найден')

        #изменяем бронь
        self.booking_class.refresh_booking(new_id, firstname=self.new_name, lastname=self.new_lastname, totalprice = self.new_totalprice)

        #получаем данные измененной записи
        new_data = self.booking_class.get_booking(new_id)

        #проверяем данные измененной записи 
        self.assertEqual(new_data, {
            "firstname": self.new_name,
            "lastname": self.new_lastname,
            "totalprice": self.new_totalprice,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2022-07-11",
                "checkout": "2022-07-18"
            },
            "additionalneeds": "Dinner"
        }, 'неверно записаны данные')

        #проверяем, изменилось ли общее число броней после нашего бронирования
        self.assertEqual(finish_amount, start_amount + 1, 'не сходится количество броней')

if __name__ == '__main__':
    unittest.main()


