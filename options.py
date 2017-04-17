#!/usr/bin/env python3
#coding utf-8

class options():
    def __init__(self, systemName):
        self.multip = 10
        self.radius = 10
        if systemName == '5x20':
            self.delta = 1560
            self.fname = '/home/anton/DataExamples/5x20.data'
            self.polymer_len = 382
            self.polymer_chains = 45
            self.chains_per_cell = 5
            self.systemsize = 3470
            self.masses = [
                26.9815,
                24.305,
                28.0855,
                15.9994,
                15.9994,
                15.9994,
                15.9994,
                1.00797,
                14.0067,
                12.0112,
                12.0112,
                1.00797,
                1.00797,
                12.0112,
                15.9994,
                14.0067,
                14.0067
            ]
            self.bounds = [
                2.1013845707998023e+01,
                1.1441491466831698e+02,
                -1.3761236108570003e+00,
                7.8865558143111798e+01,
                -6.8295859362781655e+01,
                -2.7234316256227014e+01
            ]
        if systemName == '10x20':
            self.delta = 1560
            self.fname = '/home/anton/DataExamples/10x20.data'
            self.polymer_len = 382
            self.polymer_chains = 90
            self.chains_per_cell = 10
            self.systemsize = 1560 + 382 * 10
            self.masses = [
                26.9815,
                24.305,
                28.0855,
                15.9994,
                15.9994,
                15.9994,
                15.9994,
                1.00797,
                14.0067,
                12.0112,
                12.0112,
                1.00797,
                1.00797,
                12.0112,
                15.9994,
                14.0067,
                14.0067
            ]
            self.bounds = [
                1.5014225762971904e+01,
                1.0843139970748176e+02,
                -2.9446803612962640e+00,
                7.7342048367274359e+01,
                -7.1726842351346498e+00,
                5.5560723506846024e+01
            ]
        if systemName == '1x100':
            self.delta = 720 * 9
            self.fname = '/home/anton/DataExamples/long.data'
            self.polymer_len = 1902
            self.polymer_chains = 9
            self.chains_per_cell = 9
            self.systemsize = 1560*9 + 1902 * 9
            self.masses = [
                26.9815,
                24.305,
                28.0855,
                15.9994,
                15.9994,
                15.9994,
                15.9994,
                1.00797,
                14.0067,
                12.0112,
                12.0112,
                1.00797,
                1.00797,
                12.0112,
                15.9994,
                14.0067,
                14.0067
            ]
            self.bounds = [
                -5.4595297322462102e+00,
                8.7949513866223157e+01,
                6.6070426756816047e+00,
                8.6873041223869592e+01,
                2.1637070295754972e+02,
                2.5722952612437177e+02
            ]
        if systemName == 'pa6x20':
            self.delta = 720 * 9
            self.fname = ('/media/anton/Seagate Expansion Drive/Article-MMT/' +
                          'Cluster calculations for article/BiggerSystems/' +                         'PA6x20/1930764/co.7500000.data')
            self.polymer_len = 382
            self.polymer_chains = 144
            self.chains_per_cell = 144
            self.systemsize = 55008
            self.masses = [
                1.00797,
                12.0112,
                1.00797,
                12.0112,
                15.9994,
                14.0067,
                14.0067,
                12.0112
            ]
            self.bounds = [
                1.3226992600000000e+00,
                8.5752099259999994e+01,
                1.0452857058545163e+01,
                8.6111077616706069e+01,
                -3.9074032933933722e+00,
                8.7932663426553233e+01
            ]
#--------------------------------
        if systemName == 'mixed':
            self.delta = 1560
            self.fname = '/home/anton/DataExamples/mixed.data'
            self.polymer_len = 192
            self.polymer_chains = 90
            self.chains_per_cell = 10
            self.systemsize = 1560 + 192 * 10
            self.masses = [
                26.9815,
                24.305,
                28.0855,
                15.9994,
                15.9994,
                15.9994,
                15.9994,
                1.00797,
                14.0067,
                12.0112,
                12.0112,
                1.00797,
                1.00797,
                12.0112,
                15.9994,
                14.0067,
                14.0067
            ]
            self.bounds = [
                3.4988705925833030e-01,
                9.3782994515896377e+01,
                -1.7361352807099948e+00,
                7.8552542784986954e+01,
                4.8146256827637224e+00,
                4.6059252594555446e+01
            ]
#--------------------------------
        if systemName == 'segregated':
            self.delta = 1560
            self.fname = '/home/anton/DataExamples/segregated.data'
            self.polymer_len = 192
            self.polymer_chains = 90
            self.chains_per_cell = 10
            self.systemsize = 1560 + 192 * 10
            self.masses = [
                26.9815,
                24.305,
                28.0855,
                15.9994,
                15.9994,
                15.9994,
                15.9994,
                1.00797,
                14.0067,
                12.0112,
                12.0112,
                1.00797,
                1.00797,
                12.0112,
                15.9994,
                14.0067,
                14.0067
            ]
            self.bounds = [
                8.7397656345222585e-01,
                9.4295503111445754e+01,
                -9.3640753602093696e-01,
                7.9317886582194518e+01,
                5.1960075046373376e+01,
                9.3074634839230029e+01
            ]
#--------------------------------
        if systemName == 'poly65856':
            self.delta = 0
            self.fname = '/home/anton/DataExamples/poly65856.data'
            self.polymer_len = 192
            self.polymer_chains = 343
            self.chains_per_cell = 343
            self.systemsize = 343 * 192
            self.masses = [
                1.00797,
                12.0112,
                1.00797,
                12.0112,
                15.9994,
                14.0067,
                14.0067,
                12.0112
            ]
            self.bounds = [
                4.4755155371005870e+01,
                1.3444138637203960e+02,
                5.8102071464311827e+01,
                1.4360418141260860e+02,
                6.1444793649615214e+01,
                1.4340717578331314e+02
            ]
