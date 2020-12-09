import unittest

from NER.engine.AddressNERHypothesis import AddressNERHypothesis
from NER.engine.NERModel import NERModel


class TestCity(unittest.TestCase):
    def setUp(self):
        self.NERInstance = NERModel()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, (None, None))

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, ('липецк', 'город'))


    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, ('сургут', None))

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, ('липецк', 'город'))

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, (None, None))

    def test_6(self):
        testing_address = 'сургут югорская 30/2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, ('сургут', None))

    def test_7(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, (None, None))

    def test_8(self):
        testing_address = 'ты сургут улица 30 лет победы'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, ('сургут', None))

    def test_9(self):
        testing_address = 'надо 50% город нальчик горького 1257'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, ('нальчик', 'город'))

    def test_10(self):
        testing_address = 'null'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, (None, None))

    def test_11(self):
        testing_address = '60 мегабит я'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, (None, None))

    def test_12(self):
        testing_address = 'сургут крылова 53/4'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, ('сургут', None))

    def test_13(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, ('москва', None))

    def test_14(self):
        testing_address = 'мое 3 парковая'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, (None, None))

    def test_15(self):
        testing_address = 'Пришвина 17'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, (None, None))

    def test_16(self):
        testing_address = 'Старый Гай 1 корпус 2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.city, (None, None))


if __name__ == '__main__':
    unittest.main()

    list_of_addresses = ['город липецк улица катукова 36 a',
                         'проспект комсомольский 50',
                         'сургут улица рабочая дом 31а',
                         'город липецк доватора 18',
                         'ну бехтеева 9 квартира 310',
                         'улица меркулова дом 24',
                         'октябрьская 48 частный дом город сургут',
                         'московская 34б',
                         'краснопресненская 47',
                         'улица минина дом 1',
                         'улица горького дом 5',
                         'сколько улица 30 лет победы 50 46',
                         'тюменский тракт 10',
                         'береговая 43 береговая 43 сургут',
                         'сургут югорская 30/2',
                         'индекс 12 мне вот этого не надо',
                         'город сургут улица фармана салманова 4',
                         'ты сургут улица 30 лет победы',
                         'проезд мунарева 2',
                         'старый оскол микрорайон олимпийский дом 23 квартира 105',
                         'домашний адрес где я живу',
                         'сосновая 9 город чебоксары',
                         'артема 32 квартира 8',
                         'город липецк полиграфическая дом 4',
                         'знаете знаете у меня дорогая девочка у меня уже все есть и менять из из одного переходить на другой я не хочу поэтому какой город квартира какой ничего я вам сообщать не хочу поэтому до свидания я ничего не',
                         'так город москва улица ключевая дом 20',
                         'москва мусы джалиля 38 корпус 2',
                         'надо 50% город нальчик горького 1257',
                         'москва улица нагорная дом 7 корпус 5',
                         'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1',
                         'город иркутск улица ленина дом 7',
                         'зеленые аллеи город видное дом 8',
                         'дмитрия ульянова 17 корпус 1 москва',
                         'люберцы октябрьский проспект 10 корпус 1',
                         '60 мегабит я',
                         'null',
                         'москва смольная 44 корпус 1',
                         'стол вы знаете москва алтуфьевское 78',
                         'фортунатовская 17 квартира 52',
                         'бульвар миттова 24',
                         'а зачем',
                         'не надо там на обед когда вниистром 200 есть у меня хороший тарифный на метросеть поэтому спасибо за предложение',
                         'я говорю у меня съемная квартира я не смогу ничего туда подключать',
                         'ну вы сказали до 50% но вы не сказали стоимость',
                         'а у меня интернет 1 гб',
                         'сургут крылова 53/4',
                         'ну допустим первомайская 17',
                         'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения',
                         'тормозите хорошей пудры для политика вас не слышал я вам скажу по моему адресу вас нет подключения я живу в городе сургуте по республике 81 убедиться в этом я вас жду ваш ответ',
                         'липецк мичурина 8',
                         'микрорайон дом 17 квартира 2',
                         'город сургут 30 лет победы 1',
                         'город сургут улица семена билецкого 1',
                         '4/1',
                         '1 месяц сколько это все будет',
                         'вы знаете у нас здесь дома на ростелеком подключенный и мы когда переносились она нам сказали больше никакой связи нет только ростелеком',
                         'я же назвал сударыня давайте не будем 50% скидки на сколько месяцев',
                         'москва дмитровское шоссе дом 90',
                         'ну мне 50 не устраивает у меня же то зачем мне 2 раза меньше я же объясняю',
                         'москва профсоюзная 58 корпус 4',
                         'не спасибо я вам понял у меня есть дома есть',
                         'микрорайон кутузовский дом 1 корпус 1',
                         'марша захарова 12 маршала захарова дом 12',
                         'Кавказский 16',
                         'у меня нет мегафона на доме',
                         'Новая 14',
                         'дом 67 квартира 12 улица ленина',
                         'Ореховый 35 корпус 1',
                         'Рязанский 27',
                         'нет нас есть подключение и по нашему по нашему дому',
                         'улица пионерская 109',
                         'Мусы Джалиля 29 корпус 1',
                         'немножко у меня нет у меня нет домашнего телефона и я смартфон потерял у меня простой кнопочный',
                         'мое 3 парковая',
                         'не подождите ели 5 сколько стоимость пустой',
                         'ну я бы удовольствием живу арендованном квартире не зачем хозяйка там есть все есть пусть они',
                         'улица лермонтова дом 10 корпус 3',
                         'улица 3 почтовое отделение дом 62',
                         'сейчас 1 секунду',
                         'Кусковская 19 корпус 1',
                         'и сколько там получается ладно я узнаю когда тогда будем просто сейчас не дома мы на отдыхе',
                         'москва на 8',
                         'Пришвина 17',
                         'Старый Гай 1 корпус 2',
                         'улица космонавтов дом 10',
                         'меня тоже самое подключено толк все в билайне еще привязан 3 телефона вся семья на 1 моем телефоне как говорится',
                         'Новгородская 30',
                         'меня в ближайшее время интересовал хотел мне домитру мобильный интересует безлимитный у меня не домашний именно мобильный',
                         'нас дома телевизор тоже нет не пользуемся телефон',
                         'город москва марьинский парк дом 25 корпус 2',
                         'москва щелковское шоссе 35',
                         'новогиреевская 34',
                         'зелинского улица зелинского дом 2',
                         'я сейчас не дома',
                         'нет спасибо меня не интересует до свидания и не звоните по этому вопросу уже 3 раз зад',
                         'я хотел бы сначала услышать условия прежде чем называть улица номер дома'
                         ]
    print("AMOUNT of ADDRESSES: ", len(list_of_addresses))
