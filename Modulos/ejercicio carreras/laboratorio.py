def compara_tiempos(carrera):
    array_de_scores = []
    for clave, detalles in carrera['participantes'].items():
        if 'score' in detalles:
            array_de_scores.append((clave, detalles['score']))
    return array_de_scores

# Ejemplo de uso
carrera = {
    "participantes": {
        "1": {'Nombre': 'camilo', 'Edad': '54', 'score': 40.0},
        "2": {'Nombre': 'maria', 'Edad': '17', 'score': 10},
        "3": {'Nombre': 'juan', 'Edad': '188', 'score': 150}
    }
}

resultados = compara_tiempos(carrera)
print("Resultados de la carrera:", resultados)
