'''
Создайте список (количество чисел не важно) самым простым способом, значения списка любые, например:
a = [1, 20, 3, 10, 15]
Реализуйте изменение значений списка (рекомендуется создать новый результирующий список) по следующему правилу – каждое число:
- меньшее 10 должно быть умножено на 1.13,
- большее 10 – умножить на 0.18,
- равное точно 10 – оставить без изменения.
Значения обоих списков выведите на экран.
'''

spisok_first = [1, 20, 3, 10, 15]

spisok_new = []
a = 1.13
b = 0.18

for i in range(len(spisok_first)):
    if spisok_first[i] < 10:
        c = spisok_first[i] * a
        spisok_new.append(round(c, 2))
    elif spisok_first[i] > 10:
        c = spisok_first[i] * b
        spisok_new.append(round(c, 2))
    else:
        spisok_new.append(spisok_first[i])

print(f'Изначальный список: {spisok_first}\n'
      f'Полученный список: {spisok_new}')