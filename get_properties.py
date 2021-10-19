#Moles={ 'N2':  0.0652828008625491,
#        'O2':  0.0173536559254877,
#        'CO2': 0,
#        'H2O': 0,
#        'Mixture': 0.0826364567880368
#}
#T=373

def get_properties(Moles, T):
    T = (T - 273.15) / 1000
    #  коэффициенты степенного полинома
    Ct = {
        'N2': [739.285131, -22.471670, 227.207844, -185.894180, 70.004916, -12.379265, 0.769710],
        'O2': [654.562116, 68.439046, 264.346543, -393.574630, 246.484449, -73.329697, 8.469622],
        'CO2': [623.417107, 642.051281, -894.274220, 1184.176523, -917.659359, 348.918593, -50.600189],
        'H2O': [1397.282949, 116.902172, 349.689382, -269.541130, 112.473429, -27.731548, 3.047700]
    }
    #  молярные массы
    ml = {
        'N2': 0.028,
        'O2': 0.032,
        'CO2': 0.044,
        'H2O': 0.018
    }
    # Теплоемкость
    N2 = sum([Ct['N2'][k] * T ** k for k in range(0, 6)]) * ml['N2']
    O2 = sum([Ct['O2'][k] * T ** k for k in range(0, 6)]) * ml['O2']
    CO2 = sum([Ct['CO2'][k] * T ** k for k in range(0, 6)]) * ml['CO2']
    H2O = sum([Ct['H2O'][k] * T ** k for k in range(0, 6)]) * ml['H2O']
    Cv = (N2 * Moles['N2'] + O2 * Moles['O2'] + CO2 * Moles['CO2'] + H2O * Moles['H2O'])/Moles['Mixture']
    return Cv

if __name__ == '__main__':
    get_properties()
