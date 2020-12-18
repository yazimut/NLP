import unittest
from AddressNERHypothesis import AddressNERHypothesis


class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = AddressNERHypothesis()

    def test_shkolnaya(self):
        testing_address = 'санкт-петербург школьная 20'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('санкт-петербург', None), res.city)
        self.assertEqual(('школьная', None), res.street)
        self.assertEqual(('20', None, None), res.building)

    def test_full_gagarina(self):
        testing_address = 'санкт-петербург юрия гагарина 22 к2'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('санкт-петербург', None), res.city)
        self.assertEqual(('юрия гагарина', None), res.street)
        self.assertEqual(('22', '2', None), res.building)

    def test_short_gagarina(self):
        testing_address = 'питер гагарина 22 к2'
        res = self.NERInstance.predict(testing_address)
        #self.assertEqual(('санкт-петербург', None), res.city)
        self.assertEqual(('гагарина', None), res.street)
        self.assertEqual(('22', '2', None), res.building)

    def test_untolovsky(self):
        testing_address = "санкт-петербург;юнтоловский 43 корпус 1"
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('санкт-петербург', None), res.city)
        self.assertEqual(('юнтоловский', None), res.street)
        self.assertEqual(('43', '1', None), res.building)


    def test_untolovsky_str(self):
        testing_address = "санкт-петербург;юнтоловский 43 строение 1"
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('санкт-петербург', None), res.city)
        self.assertEqual(('юнтоловский', None), res.street)
        self.assertEqual(('43',  None, '1'), res.building)

    def test_untolovsky_str(self):
        testing_address = "юнтоловский 43 ст 1"
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('юнтоловский', None), res.street)
        self.assertEqual(('43',  None, '1'), res.building)

if __name__ == '__main__':
    unittest.main()
