cadena = 'estoy probando'

def inverso(cadena):
    var = ''
    for h in cadena:
        var = h + var

    return var

print inverso(cadena)