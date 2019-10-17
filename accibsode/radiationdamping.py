"""Module dealing with radiation damping calculations"""

import numexpr as ne

MADX_KEYMAP = {
    'angle': 'ANGLE',
    'alphax': 'ALFX',
    'alphay': 'ALFY',
    'betx': 'BETX',
    'bety': 'BETY',
    'dx': 'DX',
    'dy': 'DY',
    'dpx': 'DPX',
    'dpy': 'DPY',
    'k1l': 'K1L',
    'k1sl': 'K1SL',
    'length': 'L'
}


def radiation_integrals_from_lattice(_dict, keymap=MADX_KEYMAP):
    """
    Method to calculate the standard
    radiation integrals from element
    by element Twiss data.
    :param _dict: dict of numpy arrays containing the twiss data
    :param keymap:
    :return:
    """
