import random, math, statistics
data = [random.randint(1, 100) for x in range(100)]
print('Среднее: ', statistics.mean(data))
print('Медиана: ', statistics.median(data))
print('Стандартное отклонение: ', statistics.stdev(data))
print('Корень из суммы: ', math.sqrt(math.fsum(data)))