# esta funcion esta pensada para que resiba una lista con valores y me calcule cuantos de estos
# y que valores se salen de el rango ''NORMAL'' de los datos

def detect_otliers(x):
    Q3 = Datos[x].quantile(0.75)
    Q1 = Datos[x].quantile(0.25)
    IQR = Q3 - Q1
    superior = Q3 + (1.5 * IQR)
    inferior = Q1 - (1.5 * IQR)
    out_sup = Datos[Datos[x] > superior].index
    out_inf = Datos[Datos[x] < inferior].index
    outliers = []
    for i in out_sup:
        outliers.append(i)
        for j in out_inf:
            outliers.append(j)
    
    size = len(outliers)
        
    return (f'Hay {size} valores atípicos en la variable {x}, y corresponden a los índices: {outliers}')