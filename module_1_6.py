my_dict = {'А.Н.Толстой': 1883,'А.П.Чехов': 1860,'Агния Барто': 1906}
print('Dict: ',my_dict)
print('Existing value: ',my_dict["А.П.Чехов"])
# my_dict['С.Михалков'] = 1913
print('Not existing value: ',my_dict.get('С.Михалков','Нет такого ключа'))
my_dict['М.Булгаков'] = 1891
my_dict['М.Шолохов'] = 1905
a = my_dict.pop('Агния Барто')
print('Deleted value: ',a)
print('Modified dictionary: ',my_dict)
print('')
my_set = {10,11,12,False,'строка1','строка2',False,11,12,'строка2'}
print('Set: ',my_set)
my_set.add('новая_строка')
my_set.add(True)
# print('контроль множества после добавления и до удаления', my_set)
my_set.remove('строка2')
print('Modified set: ',my_set)