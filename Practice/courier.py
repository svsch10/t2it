from math import floor, ceil, trunc
flat = int(input('№ квартири: '))
flat_numbers = int(input('Кількість квартир на поверсі: '))
floors = int(input('Кількість поверхів у будинку: '))

def courier(flat, flat_numbers, floors):
    total_flats = flat_numbers*floors
    entrance = flat/total_flats
    if floor(entrance) == ceil(entrance):
        etage = floors
    else:
        etage = (floors * (entrance-trunc(entrance)))
    return(ceil(entrance), ceil(etage))

print(courier(flat, flat_numbers, floors))