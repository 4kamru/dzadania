# Методы Юнит-тестирования
import unittest
import runner as rn

class TournamentTest(unittest.TestCase):
    # создается словарь для хранения результатов тестов
    @classmethod
    def setUpClass(cls):
        cls.list_ = []
        cls.all_results = {}

    # создаем объекты участников соревнований
    def setUp(self):
        self.rn_0 = rn.Runner('Усэйн', 10)
        self.rn_1 = rn.Runner('Андрей', 9)
        self.rn_2 = rn.Runner('Ник', 3)


    # Действие в конце - в данном случае вывод результата всех тестов
    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'Тест {key}')
            for key, value in value.items():
                print(f'{key}: {value.name}')

    # Тесты КТО БЫСТРЕЕ
    def test_kto_bystree_1(self):
        t_obj_1 = rn.Tournament(90, self.rn_0, self.rn_2)
        finishers = t_obj_1.start()
        max_key = max(finishers)
        # Ник у нас самый медленный - должен быть последним
        self.assertTrue(finishers[max_key] == 'Ник', 'Неправильный результат!')
        self.all_results['test_kto_bystree_1'] = finishers

    def test_kto_bystree_2(self):
        t_obj_2 = rn.Tournament(90, self.rn_1, self.rn_2)
        finishers = t_obj_2.start()
        max_key = max(finishers)
        # Ник у нас самый медленный - должен быть последним
        self.assertTrue(finishers[max_key] == 'Ник', 'Неправильный результат!')
        self.all_results['test_kto_bystree_2'] = finishers

    def test_kto_bystree_3(self):
        t_obj_3 = rn.Tournament(90, self.rn_0, self.rn_1, self.rn_2)
        finishers = t_obj_3.start()
        max_key = max(finishers)
        # Ник у нас самый медленный - должен быть последним
        self.assertTrue(finishers[max_key] == 'Ник', 'Неправильный результат!')
        self.all_results['test_kto_bystree_3'] = finishers

    # Проверим, на какой дистанции возможны ошибки. Знаем, что при 90 тест проходит нормально
    def test_uncorrect_run(self):
        # Зададим начальную дистанцию
        dist = 90
        res = True
        while dist > 0:
            t_obj = rn.Tournament(dist, self.rn_0, self.rn_1, self.rn_2)
            finishers = t_obj.start()
            max_key = max(finishers)
            try:
                self.assertTrue(finishers[max_key] == 'Ник', 'Неправильный результат!')
            except AssertionError as E:
                print(f' при dist ={dist} ошибка {E}')
                res = dist
            else:
                res = 0
            finally:
                key = str(f'test_uncorrect_run_{dist}')
                self.all_results[key] = finishers
                dist -= 1


if __name__ == '__main__':
        unittest.main()

