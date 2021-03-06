class Car(object):
    """ This is the car class """

    def __init__(self, name = 'General', model = 'GM', car_type = 'default'): # default car properties
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0
        self.num_of_wheels = 4
        self.num_of_doors = 4

        if self.name == 'Porshe' or self.name == 'Koenigsegg': # number of doors
            self.num_of_doors = 2
        if self.car_type == 'trailer': # number of wheels
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.num_of_wheels == 4:
            self.car_type = 'saloon'
            return True
        else:
            return False
    
    def drive(self, speed):
        if self.car_type == 'trailer':
            self.speed = 11 * speed
        else:
            self.speed = 10 ** speed
        return self