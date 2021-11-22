Rm = 8.314                                   # универсальная газовая постоянная, Дж/моль/К
# Геометрические параметры двигателя
D = 0.102
S = 0.122
eps = 18
lamb = 0.264
n = 2400
alpha = 2.007
# Клапана
Fi_ovik = 360 - 64
Fi_zvik = 540 + 15
Fi_ovk = 540 - 10
Fi_zvk = 42
muf_int = 0.000850
muf_exh = 0.000809
# Параметры на впуске
Tk = 310
Pk = 1.91 * 10 ** 5
Tog = 777
Pog = 1.9044 * 10 ** 5
# Параметры сгорания
Fi_ovt = 1


# Коэффициенты для теплоемкостей
# Газ на входе
# rin=struct('N2',0.79,'O2',0.21,'CO2',0,'H2O',0,'Mixture', 1)
# ml_in=rin.N2*ml.N2+rin.O2*ml.O2+rin.CO2*ml.CO2+rin.H2O*ml.H2O
# Газ на выходе
# rout=struct('N2',0.7212,'O2',0.0959,'CO2',0.0668,'H2O',0.1161,'Mixture', 1)
# ml_out=rout.N2*ml.N2+rout.O2*ml.O2+rout.CO2*ml.CO2+rout.H2O*ml.H2O
