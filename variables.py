count_of_completed_dz = 12
count_of_hours_spent = 1.5
name_of_course = "Python"
time_for_one_task = count_of_hours_spent / count_of_completed_dz
# старый вариант строки вывода
# print("Курс: ",name_of_course, ", всего задач:",count_of_completed_dz,", затрачено часов: ",count_of_hours_spent,", среднее время выполнения ",time_for_one_task," часа")
# вариант от 2024-08-13
print(f"{"Курс:"} {name_of_course},{" всего задач:"}"
      f"{count_of_completed_dz},{" затрачено часов:"}"
      f" {count_of_hours_spent},{" среднее время выполнения "}"
      f"{time_for_one_task} {" часа."}")
