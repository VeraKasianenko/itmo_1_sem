'''
Напишите программу по следующему описанию: двум переменным присваиваются числовые значения; если значение первой
переменной больше второй, то найти разницу значений переменных (вычесть из первой вторую), результат связать с
третьей переменной; если первая переменная имеет меньшее значение, чем вторая, то третью переменную связать с
результатом суммы значений двух первых переменных; во всех остальных случаях, присвоить третьей переменной значение
первой переменной; вывести значение третьей переменной на экран.
'''

n1 = 64
n2 = 23

if n1 > n2:
    n3 = n1 - n2
elif n1 < n2:
    n3 = n1 + n2
else:
    n3 = n1

print(n3)