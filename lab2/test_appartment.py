import unittest
from AddressNERHypothesis import AddressNERHypothesis


class TestAppartment(unittest.TestCase):
    def setUp(self):
        self.NERInstance = AddressNERHypothesis()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(res.appartment, None)

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(res.appartment, None)

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(res.appartment, None)

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(res.appartment, None)

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(res.appartment, '310')

    def test_6(self):
        testing_address = 'Кусковская 19 корпус 1'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(res.appartment, None)

    def test_7(self):
        testing_address = 'марша захарова 12 маршала захарова дом 12'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(res.appartment, None)

    def test_8(self):
        testing_address = 'null'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(res.appartment, None)


if __name__ == '__main__':
    unittest.main()
