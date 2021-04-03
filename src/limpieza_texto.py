import numpy as np


def clean_shark_species(x):
    print(x)
    return str(x)


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
