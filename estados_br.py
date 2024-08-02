# fazer um programa com os estados

estados =  ['Acre', 'Alagoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara', 'Distrito Federal', 'Espirito Santto', 'Goias', 'Maranhão', 'Mato Grosso', 'Mato Grosso Do sul', 'Minas Gerais', 'Pará', 'Paraiba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'rio Grande do Norte', 'Rio Grande do Sul', 'Rodonia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantis' ]

#saida de dados

print(f'Quantidades de Estados: {len(estados)}.\n')
print('modo 1:\n')

for estado in estados:
    print(estado)

print('\nModo 2:\n')

for i in range(len(estados)):
    print(f'{i + 1}º estado: {estados[i]}.')

