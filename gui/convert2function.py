import numpy as np
import matplotlib.pyplot as plt

# there should be a better way using regex
replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    '^': '**',
}

# think of more security hazards here
forbidden_words = [
    'import',
    'shutil',
    'sys',
    'subprocess',
]

def string2func(string):
    ''' evaluates the string and returns a function of x '''
    for word in forbidden_words:
        if word in string:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    def func(x):
        return eval(string)

    return func