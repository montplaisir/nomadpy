
class Double:
    _defined = False
    _value = 0.0

    def __init__(self, d=None):
        if d is not None:
            self._defined = True
            self._value = d

    def display(self):
        if (self._defined):
            return(self._value)
        else:
            return("Undefined value")


