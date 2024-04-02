def tif(condition: bool, true, false):
    """ use this for non-lazy 
    """
    return true if condition else false


def tlif(condition: bool, true: callable, false: callable):
    """ use this for lazy
    """
    return true() if condition else false()
