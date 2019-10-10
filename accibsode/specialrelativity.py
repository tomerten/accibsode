"""Standard special relativity calculations"""

import numpy as np
from scipy import constants as const


def beta_from_gamma(gamma) -> float:
    """
    Get the relativistic beta
    given a relativistic gamma.
    :param gamma: relativistic gamma
    :type gamma: float
    :return: relativistic beta
    """
    if (gamma - 1.0) <= -1.0e-16:
        raise ValueError('Gamma has to be larger than 1')
    return np.sqrt(1 - (1 / gamma ** 2))


def velocity_from_beta(beta: 'v/c') -> {'type': float, 'units': 'm/s'}:
    """
    Calculate the relativistic speed
    given a relativistic beta.
    :param beta: relativistic beta
    :type beta: float
    :return: speed
    """
    if (1.0 - abs(beta)) < -1e-16:
        raise ValueError('Beta can not be larger than 1')
    return beta * const.c


def gamma_from_beta(beta: 'v/c') -> float:
    """
    Calculates the relativistic gamma
    given a relativistic beta.
    :param beta: relativistic beta
    :type beta: float
    :return: relativistic gamma
    """
    if (1.0 - abs(beta)) < 1e-16:
        raise ValueError('Beta can not be larger than or equal to 1')
    return np.sqrt(1 / (1 - beta ** 2))
