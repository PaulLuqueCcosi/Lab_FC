import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class View:
    
  
    
    def calculate(self):
        
        # create a dicc with the values of the entries
        dicc = {
            'mass': {
                "value": self.mass_entry.get(),
                "unit": self.mass_unit_var.get()
            },
            'distance': {
                "value": self.distance_entry.get(),
                "unit": self.distance_unit_var.get()
            },
            'time': {
                "value": self.time_entry.get(),
                "unit": self.time_unit_var.get()
            },
            'initial_velocity': {
                "value": self.initial_velocity_entry.get(),
                "unit": self.initial_velocity_unit_var.get()
            },
            'final_velocity': {
                "value": self.final_velocity_entry.get(),
                "unit": self.final_velocity_unit_var.get()
            }
        }
        
        # # convertimos a SI y a numero
        # dicc = self.convertToSIAndNumber(dicc)
        
        
        # self.controller.set_model_data(
        #     dicc['mass']['value'], dicc['mass']['unit'],
        #     dicc['distance']['value'], dicc['distance']['unit'],
        #     dicc['time']['value'], dicc['time']['unit'],
        #     dicc['initial_velocity']['value'], dicc['initial_velocity']['unit'],
        #     dicc['final_velocity']['value'], dicc['final_velocity']['unit']
        # )
        
        self.controller.set_model_data(dicc)
        force, acceleration = self.controller.calculate()
        
        text=f"Aceleracion: {acceleration} m/s^2\nFuerza: {force} N"
        label = tk.Label(self.window, text=text, font=("Arial", 14, "bold"))
        label.pack()
        
        messagebox.showinfo("Information",text)
        
        self.controller.plot_graph()

    def run(self):
        self.window.mainloop()

    def initComponenMasa(self):
        self.mass_label = tk.Label(self.window, text="Masa:", font=("Times New Roman", 12, "bold"))
        self.mass_label.pack()

        self.mass_entry = tk.Entry(self.window)
        self.mass_entry.pack()

        self.mass_unit_label = tk.Label(self.window, text="Unidad:", font=("Times New Roman", 12))
        self.mass_unit_label.pack()

        self.mass_unit_var = tk.StringVar(value="kg")
        self.mass_unit_kg_radio = tk.Radiobutton(self.window, text="kg", variable=self.mass_unit_var, value="kg")
        self.mass_unit_kg_radio.pack()
        self.mass_unit_g_radio = tk.Radiobutton(self.window, text="g", variable=self.mass_unit_var, value="g")
        self.mass_unit_g_radio.pack()
        
    def initComponentsDistancia(self):
        self.distance_label = tk.Label(self.window, text="Distancia:", font=("Times New Roman", 12, "bold"))
        self.distance_label.pack()
        self.distance_entry = tk.Entry(self.window)
        self.distance_entry.pack()

        self.distance_unit_label = tk.Label(self.window, text="Unidad:", font=("Times New Roman", 12))
        self.distance_unit_label.pack()

        self.distance_unit_var = tk.StringVar(value="m")
        self.distance_unit_m_radio = tk.Radiobutton(self.window, text="m", variable=self.distance_unit_var, value="m")
        self.distance_unit_m_radio.pack()
        self.distance_unit_cm_radio = tk.Radiobutton(self.window, text="cm", variable=self.distance_unit_var, value="cm")
        self.distance_unit_cm_radio.pack()
        self.distance_unit_km_radio = tk.Radiobutton(self.window, text="km", variable=self.distance_unit_var, value="km")
        self.distance_unit_km_radio.pack()
        
    def initComponentTiempo(self):
        self.time_label = tk.Label(self.window, text="Tiempo:", font=("Times New Roman", 12, "bold"))
        self.time_label.pack()
        self.time_entry = tk.Entry(self.window)
        self.time_entry.pack()

        self.time_unit_label = tk.Label(self.window, text="Unidad:", font=("Times New Roman", 12))
        self.time_unit_label.pack()

        self.time_unit_var = tk.StringVar(value="s")
        self.time_unit_s_radio = tk.Radiobutton(self.window, text="s", variable=self.time_unit_var, value="s")
        self.time_unit_s_radio.pack()
        self.time_unit_min_radio = tk.Radiobutton(self.window, text="min", variable=self.time_unit_var, value="min")
        self.time_unit_min_radio.pack()
        self.time_unit_h_radio = tk.Radiobutton(self.window, text="h", variable=self.time_unit_var, value="h")
        self.time_unit_h_radio.pack()
        
    def initComponentsVelocidadInicial(self):
        self.initial_velocity_label = tk.Label(self.window, text="Velocidad inicial:", font=("Times New Roman", 12, "bold"))
        self.initial_velocity_label.pack()
        self.initial_velocity_entry = tk.Entry(self.window)
        self.initial_velocity_entry.pack()

        self.initial_velocity_unit_label = tk.Label(self.window, text="Unidad:", font=("Times New Roman", 12))
        self.initial_velocity_unit_label.pack()

        self.initial_velocity_unit_var = tk.StringVar(value="m/s")
        self.initial_velocity_unit_mps_radio = tk.Radiobutton(
            self.window, text="m/s", variable=self.initial_velocity_unit_var, value="m/s"
        )
        self.initial_velocity_unit_mps_radio.pack()
        self.initial_velocity_unit_kmph_radio = tk.Radiobutton(
            self.window, text="km/h", variable=self.initial_velocity_unit_var, value="km/h"
        )
        self.initial_velocity_unit_kmph_radio.pack()   

    def initComponentsVelocidadFinal(self):        
        self.final_velocity_label = tk.Label(self.window, text="Velocidad final:", font=("Times New Roman", 12, "bold"))
        self.final_velocity_label.pack()
        self.final_velocity_entry = tk.Entry(self.window)
        self.final_velocity_entry.pack()

        self.final_velocity_unit_label = tk.Label(self.window, text="Unidad:", font=("Times New Roman", 12))
        self.final_velocity_unit_label.pack()

        self.final_velocity_unit_var = tk.StringVar(value="m/s")
        self.final_velocity_unit_mps_radio = tk.Radiobutton(
            self.window, text="m/s", variable=self.final_velocity_unit_var, value="m/s"
        )
        self.final_velocity_unit_mps_radio.pack()
        self.final_velocity_unit_kmph_radio = tk.Radiobutton(
            self.window, text="km/h", variable=self.final_velocity_unit_var, value="km/h"
        )
        self.final_velocity_unit_kmph_radio.pack()

    def initComponentsCalcularButton(self):
        self.calculate_button = tk.Button(self.window, text="Calcular", command=self.calculate)
        self.calculate_button.pack() 
        
    def initComponentsLimpiarButton(self):
        pass
        
    
    def initComponents(self):
        self.window = tk.Tk()
        self.window.title("Cálculo de Fuerza y Gráfica")
        self.window.geometry("650x1000")
        
        label = tk.Label(self.window, text="Calculo de ACELERACION Y FUERZA con GRAFICA", font=("Arial", 14, "bold"))
        label.pack()
        
        separator = ttk.Separator(self.window, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=10)
        
        self.initComponenMasa()
        
        separator = ttk.Separator(self.window, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=10)
        
        self.initComponentsDistancia()
        
        separator = ttk.Separator(self.window, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=10)
        
        self.initComponentTiempo()
        
        separator = ttk.Separator(self.window, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=10)
        
        self.initComponentsVelocidadInicial()
        
        separator = ttk.Separator(self.window, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=10)
        
        self.initComponentsVelocidadFinal()
        
        separator = ttk.Separator(self.window, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=10)
        
        self.initComponentsCalcularButton()
        
        self.initComponentsLimpiarButton()
    
    def __init__(self, controller):
        self.controller = controller
        self.initComponents()
        
