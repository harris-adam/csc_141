def make_car(manufacturer, model, **options):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(options)
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)