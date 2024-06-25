
import fake_math as f_m
import true_math as t_m

result1 = f_m.divide(69, 3)
result2 = f_m.divide(3, 0)
result3 = t_m.divide(49, 7)
result4 = t_m.divide(15, 0)













#fake_math:
# def divide(first, second):
#     if second == 0:
#         print('Ошибка')
#         return
#     result = first / second
#     print(result)
#
#
# true_math:
# def divide(first, second):
#     if second == 0:
#         from math import inf
#         print(inf)
#         return inf
#     result = first / second
#     print(result)

