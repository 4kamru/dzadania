#Простые Юнит-Тесты
import unittest
import runner as rn
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        # self.name = 'Vasya'
        rn_ = rn.Runner('Vasya')
        for i in range(10):
            rn_.walk()
        self.assertEqual(rn_.distance, 50, 'Тест walk на равенство дистанций')
        # self.assertEqual(rn_.distance, 49,'Тест walk на равенство дистанций')


    def test_run(self):
        rn_ = rn.Runner('Fedya')
        for i in range(10):
            rn_.run()
        self.assertEqual(rn_.distance,100,'Тест run на равенство дистанций')
        # self.assertEqual(rn_.distance, 99, 'Тест run на равенство дистанций')

    def test_challenge(self):
        rn1 = rn.Runner('Alex')
        rn2 = rn.Runner('Boris')
        for i in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance,rn2.distance,'Тест на разницу дистанций')



if __name__ == '__main__':
        unittest.main()

# Если ничего не менять, тест проходит с такими сообщениями:
# Launching unittests with arguments python -m unittest D:\Python\М12\pythonProject1\tests_12_1.py in D:\Python\М12\pythonProject1
# Ran 3 tests in 0.002s
# OK

# При вводе 49 в методе  test_walk получается такой ответ
# Launching unittests with arguments python -m unittest D:\Python\М12\pythonProject1\tests_12_1.py in D:\Python\М12\pythonProject1
#
#
# Ran 3 tests in 0.006s
#
# FAILED (failures=1)
#
# Тест walk на равенство дистанций
# 49 != 50
#
# Expected :50
# Actual   :49
# <Click to see difference>
#
# Traceback (most recent call last):
#   File "D:\Python\М12\pythonProject1\tests_12_1.py", line 11, in test_walk
#     self.assertEqual(rn_.distance, 49,'Тест walk на равенство дистанций')
# AssertionError: 50 != 49 : Тест walk на равенство дистанций