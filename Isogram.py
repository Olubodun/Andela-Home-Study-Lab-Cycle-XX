#This program checks if a string of word is without a repeating letter.
def is_isogram(string):
    if isinstance(string, str) and len(string) != 0:
        string = string.lower()
        return string, len(string) == len(set(string))
    if not string:
        return string, False;
    raise TypeError('Argument should be a string')
