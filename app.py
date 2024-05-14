import json
import os
import datetime


lata = "6300"


buckingham = input("Decime cuántas pidio el Buckingham: ")
socorro = input("Cuantas pidio el Socorro: ")
sanjose = input("Cuantas pidio el San Jose: ")
sanalfonso = input("Cuantas pidio el San Alfonso: ")
chaparral = input("Cuantas pidio el Chaparral: ")
profesorado = input("Cuantas pidio el profesorado: ")
lourdes = input("Cuantas pidio el Lourdes: ")
unq = input("Cuantas pidio la UNQUI: ")
dominico = input("Cuantas pidio el Dominico: ")
costo_dia = input("Cuanto gastamos por dia: ")

# Corregir la definición de resultado
resultado = float(buckingham) + float(socorro) + float(sanjose) + float(sanalfonso) + float(chaparral) + float(profesorado) + float(lourdes) +  float(dominico) + float(unq) 

print("Resultado total de latas: ", resultado)

# Convertir lata a un número
precio_lata = float(lata)

# Calcular ganancia total
ganancia = resultado * precio_lata

# Costo dia a numero
costo_fijo = float(costo_dia)

# Restar costo fijo a la ganancia total
g_total = ganancia - costo_fijo

pedido =  {
                "Precio x lata actual":lata,
                "buckingham":buckingham,
                "socorro":socorro,
                "sanjose":sanjose,
                "sanalfonso":sanalfonso,
                "chaparral":chaparral,
                "profesorado":profesorado,
                "lourdes":lourdes,
                "unq":unq,
                "dominico":dominico,
                "costo_dia":costo_dia,
                "fecha":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ganancia":ganancia,
                "costo_fijo":costo_fijo,
                "g_total":g_total
}

print("Ganancia total después de restar costo fijo: ", g_total)


if os.path.exists("./semana.json"):
    with open("./semana.json", "r") as f:
        try: 
            format_file = json.load(f)
            format_file["Pedidos"].append(pedido)
            with open("./semana.json", "w+") as f:
                f.write(json.dumps(format_file, indent=4))
        except Exception as e:
            print("La cagué", e)
else:
    with open("./semana.json", "w+") as f:
        f.write(json.dumps({
            "Pedidos": [
                    pedido
            ]
        }, indent=4))
        
