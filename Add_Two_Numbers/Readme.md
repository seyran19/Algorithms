Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа. Цифры хранятся в обратном порядке , и каждый из их узлов содержит одну цифру. Сложите два числа и верните сумму в виде связанного списка.

Вы можете предположить, что эти два числа не содержат ведущих нулей, кроме самого числа 0.

 

Пример 1:


Входные данные: l1 = [2,4,3], l2 = [5,6,4]
 Выходные данные: [7,0,8]
 Объяснение: 342 + 465 = 807.
Пример 2:

Вход: l1 = [0], l2 = [0]
 Выход: [0]
Пример 3:

Ввод: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 Выход: [8,9,9,9,0,0,0,1]
 

Ограничения:

Количество узлов в каждом связанном списке находится в диапазоне [1, 100].
0 <= Node.val <= 9
Гарантируется, что список представляет число, не имеющее ведущих нулей.