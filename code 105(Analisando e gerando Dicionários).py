def notas(*n, sit=False):
    f = dict()
    f['total'] = len(n)
    f['maior'] = max(n)
    f['menor'] = min(n)
    f['media'] = sum(n)/len(n)
    if sit:
        if f['media'] >= 7:
            f['situação'] = 'boa'
        elif f['media'] >= 5:
            f['situação'] = 'razoavel'
        else:
            f['situação'] = 'bom'
    return f


#programa principal
resp = notas(5, 8, 9, sit=True)
print(resp)
