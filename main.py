''' Operators '''

REGISTRED_MEMBERS = ['mariano', 'jose']

def certify(func):
    """certify if name exists in registred names
    Args:
        func (function): recive a name
    """
    def wrapper(*arg):
        if arg[0] in REGISTRED_MEMBERS:
            return func(*arg)
        return arg[0] + ' is not registred'
    return wrapper


@certify
def test_register(arg: str) -> str:
    """test operators
    Args:
        arg (str): name for sujeit
    Returns:
        str: sujeit is camarada now
    """
    return arg + ' is registred!'

if __name__ == '__main__':
    NAMES_TEST = ['marcos', 'mariano', 'roberto', 'jose']

    for name in NAMES_TEST:
        print(test_register(name))
