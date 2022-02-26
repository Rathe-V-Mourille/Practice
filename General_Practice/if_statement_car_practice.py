# simple example w/ added concepts
cars = ['audi', 'bmw', 'subaru', 'toyota']

cars.append('gm')

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'gm':
        print(car.upper())
    else:
        print(car.title())

