
# Геометрические параметры двигателя
D= 0.102
S = 0.122
eps = 18
lamb = 0.264
n = 2400
alpha = 2.007
# Н.У.
Fi_ovt = 0
# Клапана
Fi_ovik = 360 - 64
Fi_zvik = 540 + 18
Fi_ovk = 540 - 10
Fi_zvk = 42
muf_int = 0.0027
muf_exh = 0.0027
# Параметры на впуске
Tk = 352
Pk = 2.53 * 10 ** 5
Tog = 862
Pog = 1.78 * 10 ** 5
# Коэффициенты для теплоемкостей
Ct = {
    'N2': [739.285131, -22.471670, 227.207844, -185.894180, 70.004916, -12.379265, 0.769710],
    'O2': [654.562116, 68.439046, 264.346543, -393.574630, 246.484449, -73.329697, 8.469622],
    'CO2': [623.417107, 642.051281, -894.274220, 1184.176523, -917.659359, 348.918593, -50.600189],
    'H2O': [1397.282949, 116.902172, 349.689382, -269.541130, 112.473429, -27.731548, 3.047700]
}
ml = {
    'N2': 0.028,
    'O2': 0.032,
    'CO2': 0.044,
    'H2O': 0.018
}

# Газ на входе
# rin=struct('N2',0.79,'O2',0.21,'CO2',0,'H2O',0,'Mixture', 1)
# ml_in=rin.N2*ml.N2+rin.O2*ml.O2+rin.CO2*ml.CO2+rin.H2O*ml.H2O
# Газ на выходе
# rout=struct('N2',0.7212,'O2',0.0959,'CO2',0.0668,'H2O',0.1161,'Mixture', 1)
# ml_out=rout.N2*ml.N2+rout.O2*ml.O2+rout.CO2*ml.CO2+rout.H2O*ml.H2O
