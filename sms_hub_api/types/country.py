from . import utils


class Country(utils.Helper):
    RUSSIA = utils.Item(value="0")  # Россия
    UKRAINE = utils.Item(value="1")  # Украина
    KAZAKHSTAN = utils.Item(value="2")  # Казахстан
    CHINA = utils.Item(value="3")  # Китай
    PHILIPPINES = utils.Item(value="4")  # Филиппины
    MYANMAR = utils.Item(value="5")  # Мьянма
    INDONESIA = utils.Item(value="6")  # Индонезия
    MALAYSIA = utils.Item(value="7")  # Малайзия
    KENYA = utils.Item(value="8")  # Кения
    TANZANIA = utils.Item(value="9")  # Танзания
    VIETNAM = utils.Item(value="10")  # Вьетнам
    KYRGYZSTAN = utils.Item(value="11")  # Кыргызстан
    USA = utils.Item(value="12")  # США (виртуальные)
    ISRAEL = utils.Item(value="13")  # Израиль
    HONGKONG = utils.Item(value="14")  # Гонконг
    POLAND = utils.Item(value="15")  # Польша
    ENGLAND = utils.Item(value="16")  # Англия
    DCONGO = utils.Item(value="18")  # Дем.Конго
    NIGERIA = utils.Item(value="19")  # Нигерия
    EGYPT = utils.Item(value="21")  # Египет
    INDIA = utils.Item(value="22")  # Индия
    IRELAND = utils.Item(value="23")  # Ирландия
    CAMBODIA = utils.Item(value="24")  # Камбоджа
    LAOS = utils.Item(value="25")  # Лаос
    HAITI = utils.Item(value="26")  # Гаити
    IVORY = utils.Item(value="27")  # Кот д'Ивуар
    GAMBIA = utils.Item(value="28")  # Гамбия
    SERBIA = utils.Item(value="29")  # Сербия
    YEMEN = utils.Item(value="30")  # Йемен
    SOUTHAFRICA = utils.Item(value="31")  # Южная Африка
    ROMANIA = utils.Item(value="32")  # Румыния
    COLOMBIA = utils.Item(value="33")  # Колумбия
    ESTONIA = utils.Item(value="34")  # Эстония
    CANADA = utils.Item(value="36")  # Канада
    MOROCCO = utils.Item(value="37")  # Марокко
    GHANA = utils.Item(value="38")  # Гана
    ARGENTINA = utils.Item(value="39")  # Аргентина
    UZBEKISTAN = utils.Item(value="40")  # Узбекистан
    CAMEROON = utils.Item(value="41")  # Камерун
    CHAD = utils.Item(value="42")  # Чад
    GERMANY = utils.Item(value="43")  # Германия
    LITHUANIA = utils.Item(value="44")  # Литва
    CROATIA = utils.Item(value="45")  # Хорватия
    SWEDEN = utils.Item(value="46")  # Швеция
    IRAQ = utils.Item(value="47")  # Ирак
    NETHERLANDS = utils.Item(value="48")  # Нидерланды
    LATVIA = utils.Item(value="49")  # Латвия
    AUSTRIA = utils.Item(value="50")  # Австрия
    BELARUS = utils.Item(value="51")  # Беларусь
    THAILAND = utils.Item(value="52")  # Таиланд
    SAUDIARABIA = utils.Item(value="53")  # Сауд. Аравия
    MEXICO = utils.Item(value="54")  # Мексика
    TAIWAN = utils.Item(value="55")  # Тайвань
    SPAIN = utils.Item(value="56")  # Испания
    IRAN = utils.Item(value="57")  # Иран
    ALGERIA = utils.Item(value="58")  # Алжир
    BANGLADESH = utils.Item(value="60")  # Бангладеш
    SENEGAL = utils.Item(value="61")  # Сенегал
    TURKEY = utils.Item(value="62")  # Турция
    CZECH = utils.Item(value="63")  # Чехия
    SRILANKA = utils.Item(value="64")  # Шри-Ланка
    PERU = utils.Item(value="65")  # Перу
    PAKISTAN = utils.Item(value="66")  # Пакистан
    NEWZEALAND = utils.Item(value="67")  # Новая Зеландия
    GUINEA = utils.Item(value="68")  # Гвинея
    MALI = utils.Item(value="69")  # Мали
    VENEZUELA = utils.Item(value="70")  # Венесуэла
    MONGOLIA = utils.Item(value="72")  # Монголия
    BRAZIL = utils.Item(value="73")  # Бразилия
    AFGHANISTAN = utils.Item(value="74")  # Афганистан
    UGANDA = utils.Item(value="75")  # Уганда
    ANGOLA = utils.Item(value="76")  # Ангола
    CYPRUS = utils.Item(value="77")  # Кипр
    FRANCE = utils.Item(value="78")  # Франция
    PAPUA = utils.Item(value="79")  # Папуа-Новая Гвинея
    MOZAMBIQUE = utils.Item(value="80")  # Мозамбик
    NEPAL = utils.Item(value="81")  # Непал
    MOLDOVA = utils.Item(value="85")  # Молдова
    PARAGUAY = utils.Item(value="87")  # Парагвай
    HONDURAS = utils.Item(value="88")  # Гондурас
    TUNISIA = utils.Item(value="89")  # Тунис
    NICARAGUA = utils.Item(value="90")  # Никарагуа
    BOLIVIA = utils.Item(value="92")  # Боливия
    GUATEMALA = utils.Item(value="94")  # Гватемала
    UAE = utils.Item(value="95")  # ОАЭ
    ZIMBABWE = utils.Item(value="96")  # Зимбабве
    SUDAN = utils.Item(value="98")  # Судан
    SALVADOR = utils.Item(value="101")  # Сальвадор
    LIBYAN = utils.Item(value="102")  # Ливия
    JAMAICA = utils.Item(value="103")  # Ямайка
    TRINIDAD = utils.Item(value="104")  # Тринидад и Тобаго
    ECUADOR = utils.Item(value="105")  # Эквадор
    DOMINICAN = utils.Item(value="109")  # Доминиканская Республика
    MAURITANIA = utils.Item(value="114")  # Мавритания
    SIERRALEONE = utils.Item(value="115")  # Сьерра-Леоне
    JORDAN = utils.Item(value="116")  # Иордания
    PORTUGAL = utils.Item(value="117")  # Португалия
    BENIN = utils.Item(value="120")  # Бенин
    BRUNEI = utils.Item(value="121")  # Бруней
    BOTSWANA = utils.Item(value="123")  # Ботсвана
    DOMINICA = utils.Item(value="126")  # Доминика
    GEORGIA = utils.Item(value="128")  # Грузия
    GREECE = utils.Item(value="129")  # Греция
    GUYANA = utils.Item(value="131")  # Гайана
    LIBERIA = utils.Item(value="135")  # Либерия
    SURINAME = utils.Item(value="142")  # Суринам
    TAJIKISTAN = utils.Item(value="143")  # Таджикистан
    REUNION = utils.Item(value="146")  # Реюньон
    ARMENIA = utils.Item(value="148")  # Армения
    CONGO = utils.Item(value="150")  # Конго
    BURKINAFASO = utils.Item(value="152")  # Буркина-Фасо
    LEBANON = utils.Item(value="153")  # Ливан
    GABON = utils.Item(value="154")  # Габон
    MAURITIUS = utils.Item(value="157")  # Маврикий
    BHUTAN = utils.Item(value="158")  # Бутан
    MALDIVES = utils.Item(value="159")  # Мальдивы
    TURKMENISTAN = utils.Item(value="161")  # Туркменистан
    DENMARK = utils.Item(value="172")  # Дания
    ARUBA = utils.Item(value="179")  # Аруба
    JAPAN = utils.Item(value="182")  # Япония
    USAPHYSICAL = utils.Item(value="187")  # США
    FIJI = utils.Item(value="189")  # Фиджи
    SOUTHKOREA = utils.Item(value="190")  # Южная Корея
    BERMUDA = utils.Item(value="195")  # Бермуды
