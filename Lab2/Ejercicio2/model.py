class Model:
    
    numDecimals = 3
    
    def __init__(self):
        self.mass = 0.0
        self.distance = 0.0
        self.time = 0.0
        self.initial_velocity = 0.0
        self.final_velocity = 0.0
        self.force = 0.0
        self.acceleration = 0.0

    def calculate_force(self):
        self.calculate_acceleration()
        self.force = self.mass * self.acceleration
        # redondeamos a 3 decimales
        self.force = round(self.force, self.numDecimals)
        return self.force

    # formula de la aceleracion (vf - vi) / t
    def calculate_acceleration(self):
        velocity_change = self.final_velocity - self.initial_velocity
        self.acceleration = velocity_change / self.time
        
        self.acceleration = round(self.acceleration, self.numDecimals)
        return self.acceleration
