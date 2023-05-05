d = 0
v = 0
t = 0

MRD = {
   "d" : f"{v}*{t}",
   "v" : f"{d}/{t}",
   "t" : f"{d}/{v}",

}

vari = {"v" : 12, "t":10}


def calculo(variables, formula):
   for v in variables:
      
      formulaCon = formula.format
      
      print(v)
   
   
    
    
    
#print the first formule
print(MRD.get("d"))
calculo(vari, MRD.get(1))


