from ac02 import calcular_salario 
dicionario = {'marcilio': ['marcilio@email.com', 5000.00, 'DESENVOLVEDOR'],
              'pedro': ['pedro@email.com', 2000.00, 'DESENVOLVEDOR'],
              'carlos': ['carlos@email.com', 1000.00, 'DESENVOLVEDOR'],
              'roberto': ['roberto@email.com', 5000.00, 'ANALISTA'],
              'renata': ['renata@email.com', 3500.00, 'ANALISTA'],
              'angelica': ['angelica@email.com', 1000.00, 'ANALISTA'],
              'amanda': ['amanda@email.com', 8000.00, 'GERENTE'],
              'ricardo': ['ricardo@email.com', 4000.00, 'GERENTE'],
              'fernanda': ['fernanda@email.com', 3000.00, 'GERENTE'],
              'marcos': ['marcos@email.com', 800.00, 'ESTAGIARIO']}
resultado = calcular_salario(dicionario, 'marcos')
print(resultado)