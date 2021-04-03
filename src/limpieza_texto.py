import numpy as np
import re


def clean_shark_species(x):
    rgx = r'[A-Za-z]'
    species = re.findall(rgx, x)
    if species:
        return species
    else:
        return np.nan


def clean_age(age):
    try:
        age = int(age)
    except:
        age = 0
    if (age > 0 and age <= 100):
        return age
    else:
        return np.nan


def filter_countries_by_attack_number(x):
    if len(x) > 100:
        return True
    else:
        return False


def clean_fatal(x):
    if x == 'N' or x == 'Y':
        return x
    else:
        return np.nan


def clean_sex(x):  # Maybe rename this function it sounds weird
    if x == 'M' or x == 'F':
        return x
    else:
        return np.nan
