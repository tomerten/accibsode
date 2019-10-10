"""Load and rename physical constants to shorter names"""

from scipy import constants as const

# required for calculation of classical particle radius
ELECTRON_AATOM = const.physical_constants['electron mass energy equivalent in MeV'][0] / \
                    const.physical_constants['proton mass energy equivalent in MeV'][0]

ELECTRON_ENERGYEV = const.physical_constants['electron mass energy equivalent in MeV'][0] * 1.0e6
ELECTRON_ENERGYMEV = const.physical_constants['electron mass energy equivalent in MeV'][0]
ELECTRON_ENERGYGEV = const.physical_constants['electron mass energy equivalent in MeV'][0] * 1.0e-3
