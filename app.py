from user import User
from credential import Credential


def emptyChecker(*args):
    '''
    '''
    results = all([item!='' for item in args])
    return results

