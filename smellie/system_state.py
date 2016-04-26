from subprocess import check_output

def get_SHA():
    '''
    Returns the current git SHA of the SMELLIE software
    '''
    return check_output(["git", "describe", "--always", "--tag"]).strip()
