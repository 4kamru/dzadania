immutable_var = ("dog", "cat", 1, 2, True)
print(immutable_var)
#immutable_var[2] = 6 # это приводит к ошибке, т.к. я пытаюсь изменить 3-й элемент. ЗАКОММЕНТИРОВАЛ, ЧТОБЫ НЕ РУГАЛСЯ ПИТОН
print("Immutable tuple: ",immutable_var)

mutable_list = ["dog", "cat", 1, 2, True]
mutable_list[0] = "good_dog"
mutable_list[1] = ("bad_cat")
mutable_list[2] = 10
mutable_list[3] = 22
mutable_list[4] = 'stringgggg'  # даже изменение типа с bool на string не вызывает ошибку
print("Mutable list:",mutable_list)
