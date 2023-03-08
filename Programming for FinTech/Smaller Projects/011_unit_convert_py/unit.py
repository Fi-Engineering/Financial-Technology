unit = ['Kilogram', 'Pound', 'Stone', 'Jin', 'Seer', 'Gram', 'Oka']
amount = [1.0, 0.453592, 6.35029, 0.5, 1.25, .001, 1.2829]


def convert_mass(value, current, target):
    """Converts a value for a given unit of mass into the value for a target unit of mass,
       using a nested dictionary as a lookup table."""
       


    x = 0
    y = 0
    
    for i in unit:
        if i == current:
            x = value * amount[unit.index(i)]
            for j in unit:
                if j == target:
                    y = x / amount[unit.index(j)]            
                       
    return y
    
    