import math
import geopy
# Definir constantes
K0 =float(input("Ingrese factor de escala : "))
a = float(input("Ingrese Semi eje mayor : "))
e = float(input("Ingrese primera excentricidad  : "))

# Definir valores para Lat1 y Lat2 (en radianes)
Lat1_deg = float(input("Ingrese Latitud 1 en °: "))
Lat2_deg = float(input("Ingrese Latitud 2 en ° : "))
#Transformar a radianes
Lat1 = math.radians(Lat1_deg)
Lat2 = math.radians(Lat2_deg)
#Ingresar valores de coordenadas
este_1 = float(input("Ingrese Coordenada UTM Este 1 : "))
norte_1 = float(input("Ingrese Coordenada UTM Norte 1 : "))
este_2 = float(input("Ingrese Coordenada UTM Este 2 : "))
norte_2 = float(input("Ingrese Coordenada UTM Norte 2 : "))


# Calcular Latm, Dx, x1, x2, x10, x20, y1, y2, Xm
Latm = (Lat1 + Lat2) / 2
x1 = este_1 - 500000
x10 = este_1
y1 = norte_1
x2 = este_2 - 500000
x20 = este_2
y2 = norte_2
Dx = x2 - x1
Xm = (x2 + x1) / 2

# Calcular Rm utilizando la fórmula corregida
Rm= (a * math.sqrt((1 - e**2))) / (1 - e**2 * math.sin(Latm)**2)**1.5


# Calcular Kutm utilizando la fórmula corregida
Kutm = K0 * (1+((Xm**2 )/ (2 * Rm**2 * K0**2))) + (((Dx**2) / (24 * Rm**2 * K0**2)))

# Calcular Dutm
Dutm = math.sqrt((x20 - x10)**2 + (y2 - y1)**2)


# Calcular DAE
DAE = Dutm / Kutm


# Calcular DCE utilizando la fórmula corregida
DCE = (2 * Rm) *  (math.sin(DAE / (2 * Rm)))


# Calcular Distancia Horizontal (DH)
Hm = 476.685
DH = (DCE / Rm) * (Rm + Hm)


# Factor de correción por altura
Kh = (Rm + Hm) / Rm


# Factor de Escala combinado
Fc = Kh * Kutm


# Relación entre las distancias UTM y distancias Horizontales
Dutm = Fc * DH


#Relación de distancias en terreno y PTL
Ds= (Hm*DH)/Rm
DHm= DH+Ds
#Resultados
print("Valor de Radio medio:", Rm)
print("Valor de K utm:", Kutm)
print('Distancia UTM:', Dutm)
print('Distancia Arco Elipsoide:', DAE)
print('Distancia Cuerda de Elipsoide:', DCE)
print('Distancia Horizontal:', DH)
print('Altura media:',Hm)
print('Factor de correción por altura :', Kh)
print('Factor de escala combinado:', Fc)
print('Relación entre las distancias UTM y distancias Horizontales:', Dutm)
print("Delta S",Ds)
print('Realizado por Mauricio Meyer Silva')

