from input_data import Ct, ml

Moles = {
    'Mixture': 1,
    'N2': 0.7212,
    'O2': 0.0959,
    'CO2': 0.0668,
    'H2O': 0.1161,
}


def get_properties(Moles, T):
    T = (T - 273.15) / 1000
    #  Мольные доли
    r0 = {}
    r0['N2'] = Moles['N2'] / Moles['Mixture']
    r0['O2'] = Moles['O2'] / Moles['Mixture']
    r0['CO2'] = Moles['CO2'] / Moles['Mixture']
    r0['H2O'] = Moles['H2O'] / Moles['Mixture']
    # Молярная масса смеси
    ml_mix = r0['N2'] * ml['N2'] + r0['O2'] * ml['O2'] + r0['CO2'] * ml['CO2'] + r0['H2O'] * ml['H2O']
    # Теплоемкость
    N2 = sum([Ct['N2'][k] * T ** k for k in range(0, 6)]) * ml['N2']
    O2 = sum([Ct['O2'][k] * T ** k for k in range(0, 6)]) * ml['O2']
    CO2 = sum([Ct['CO2'][k] * T ** k for k in range(0, 6)]) * ml['CO2']
    H2O = sum([Ct['H2O'][k] * T ** k for k in range(0, 6)]) * ml['H2O']
    Cv = N2 * r0['N2'] + O2 * r0['O2'] + CO2 * r0['CO2'] + H2O * r0['H2O']

    return Cv, ml_mix
