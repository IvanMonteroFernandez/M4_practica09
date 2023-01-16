areas = ['cuina', 7.88, 'menjador', 13.0, 'terrassa', 20.34, 'lavabo', 6.55, 'habitació1', 7.98, 'habitació2', 12, 'rebedor', 4.23]

#Imprimir el segon element
"""
Imprimir l’últim element
Imprimir l’àrea de la terrassa
Imprimir del primer element al tercer element
Imprimir del tercer element a l’últim
Imprimir el total de l'àrea de les dues habitacions
Modificar l’àrea del lavabo i imprimir la nova list area
Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
"""
print(f'Imprimir el segon element {areas[1]}')
print(f'Imprimir ultim element = {areas[-1]}')
print (f'Imprimir area de la terrasa= {areas[5]}')
print (f'Imprimir del primer element al tercer {areas[:3]}')
print(f'Imprimir del tercer elemento al ultim {areas[2:]}')
print(f'Imprimir el total de area de les dues habitacions {areas[9]+areas[11]}')
areas[7] = 4
print(areas)
areas.append('pati interior')
areas.append(2.78)
print(areas)
