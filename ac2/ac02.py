# Kaique Silva Grangeiro Ra:1903564
def calcular_salario(dicionario, funcionario):
    try:
        funcionario = dicionario[funcionario]

    except KeyError:
        raise KeyError  

    cargo = funcionario[2]
    salario = float(funcionario[1])
    if(cargo == 'DESENVOLVEDOR'):
        if(salario >= 2000):
            return salario-salario*0.15
          
        else:
            return salario-salario*0.05
   
    if(cargo == 'ANALISTA'):
        if(salario >= 3500):
            return salario-salario * 0.2
        else:
            return salario-salario * 0.1
   
    if(cargo == 'GERENTE'):
        if(salario >= 4000):
            return salario-salario * 0.25
        else:
            return salario-salario * 0.15
    else:
        raise TypeError