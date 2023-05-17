import matplotlib.pyplot as plt
from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    
    def printDicc(self, dicc):
        for key in dicc:
            print(key, dicc[key])
    
    def convertSI(self, value, unit):
        # masa
        if unit == 'g':
            return (value / 1000, 'kg')
        # distancia
        elif unit == 'cm':
            return (value / 100, 'm')
        elif unit == 'km':
            return (value * 1000, 'm')
        # tiempo
        elif unit == 'min':
            return (value * 60, 's')
        elif unit == 'h':
            return (value * 3600, 's')
        # velocidad
        elif unit == 'km/h':
            return (value / 3.6, 'm/s')

        return (value, unit)
    
    def convertToNumber(self, value):
        # change , to .
        value = value.replace(',', '.')
        
        # tratamos de convertir a un float
        try:
            number = float(value)
            return number
        except:
            print("No es un numero")
            
    def convertToSIAndNumber(self, dicc):
        for key in dicc:
            value = dicc[key]['value']
            unit = dicc[key]['unit']
            
            # convertimos a numero 
            value = self.convertToNumber(value)
        
            # convertimos a SI
            value, unit = self.convertSI(value, unit)
            
            # guardamos en el dicc
            dicc[key]['value'] = value
            dicc[key]['unit'] = unit
            
        return dicc
        

    # def set_model_data(self, mass, mass_unit, distance, distance_unit, time, time_unit,
    #                    initial_velocity, initial_velocity_unit, final_velocity, final_velocity_unit):
        
    def set_model_data(self, dicc):
        
        # convertimos a SI y a numero
        dicc = self.convertToSIAndNumber(dicc)
        
        self.printDicc(dicc)
        
        # extraemos los valores
        mass = dicc['mass']['value']
        mass_unit = dicc['mass']['unit']
        
        distance = dicc['distance']['value']
        distance_unit = dicc['distance']['unit']
        
        time = dicc['time']['value']
        time_unit = dicc['time']['unit']
        
        initial_velocity = dicc['initial_velocity']['value']
        initial_velocity_unit = dicc['initial_velocity']['unit']
        
        final_velocity = dicc['final_velocity']['value']
        final_velocity_unit = dicc['final_velocity']['unit']

        # Guardar los valores en el modelo
        
        self.model.mass = mass
        self.model.distance = distance
        self.model.time = time
        self.model.initial_velocity = initial_velocity
        self.model.final_velocity = final_velocity

   

    def calculate(self):
        aceleration = self.model.calculate_acceleration()        
        force = self.model.calculate_force()


        print("Aceleracion:", aceleration, "m/s^2")
        print("Fuerza:", force, "N")
        return force, aceleration

    def plot_graph(self):
        time_values = [0, self.model.time]
        velocity_values = [self.model.initial_velocity, self.model.final_velocity]

        plt.plot(time_values, velocity_values)
        plt.xlabel('Tiempo')
        plt.ylabel('Velocidad')
        plt.title('Cambio de velocidad')
        plt.show()

    def run(self):
        self.view.run()
