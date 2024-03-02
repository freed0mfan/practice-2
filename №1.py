total = float(input('Общая стоимость часов: '))
slvr = 96
gldn = slvr / 16
slvr_price = 48
gldn_price = (total - slvr * slvr_price) / gldn
print(int(gldn_price // 1))
