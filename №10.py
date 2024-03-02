distance_m = float(input('Расстояние в метрах: '))
distance_ml = distance_m / 1609.34
print(f'Полных миль пробежала: {int(distance_ml // 1)}')
