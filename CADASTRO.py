#Layout inicial


print('='*50)
print('1 - Cadastrar um funcionário')
print('2 - Alterar um funcionário')
print('3 - Listar (imprimir) todos os funcionários')
print('4 - Excluir um funcionário')
print('5 - Adicionar um aumento de salário')
print('='*50)
escolha=int(input('Digite sua escolha:'))



#Programa Principal


funcionários=[{'código de funcionário':'11','nome':'Neymar','email':'neymarjr@gmail.com',
               'data de admissão':'2011','salário':'R$ 14.000.000'},
              {'código de funcionário':'7','nome':'Cristiano','email':'cristiano@gmail.com',
               'data de admissão':'1997','salário':'R$ 183.000.000'},
            {'código de funcionário':'10','nome':'Messi','email':'messi@gmail.com',
               'data de admissão':'1999','salário':'R$ 123.000.000'}]



#Primeiro IF


if escolha==1:
    código_de_funcionário=int(input('Código de funcionário:'))
    nome=str(input('Digite um nome:'))
    email=str(input('Email:'))
    while True:
        if '@hotmail.com' not in email:
            if '@gmail.com' not in email:
                print('Email inválido. Tente utilizar @hotmail.com ou @gmail.com.')
                email = str(input('Tente novamente:'))
            else:
                break
        else:
            break
    data_de_admissão=int(input('Data de admissão(ano):'))
    salário=int(input('Digite o salário: R$'))
    funcionários.append({'código de funcionário':código_de_funcionário,'nome':nome,'email': email,
               'data de admissão': data_de_admissão,'salário R$': salário})



#Segundo IF


if escolha==2:
    índice=int(input('Digite o índice do funcionário que você deseja alterar:'))
    while True:
        if índice>2:
            print('Índice inválido.')
            índice = int(input('Tente novamente:'))
        if índice<=2:
            del funcionários[índice]
            break
    código_de_funcionário=int(input('Código de funcionário:'))
    nome=str(input('Digite um nome:'))
    email=str(input('Email:'))
    while True:
        if '@hotmail.com' not in email:
            if '@gmail.com' not in email:
                print('Email inválido. Tente utilizar @hotmail.com ou @gmail.com.')
                email = str(input('Tente novamente:'))
            else:
                break
        else:
            break
    data_de_admissão=int(input('Data de admissão(ano):'))
    salário=int(input('Digite o salário: R$'))
    funcionários.insert(índice,{'código de funcionário':código_de_funcionário,'nome':nome,'email': email,
               'data de admissão': data_de_admissão,'salário R$': salário})



#Terceiro IF


if escolha==3:
    print('Funcionários:')
    print(funcionários[0]['nome'])
    print(funcionários[1]['nome'])
    print(funcionários[2]['nome'])



#Quarto IF


if escolha==4:
    demitido=str(input('Digite o nome do funcionário que você deseja excluir:'))
    while True:
        if 'Neymar' in demitido:
            del funcionários[0]
            break
        elif 'Cristiano' in demitido:
            del funcionários[1]
            break
        elif 'Messi' in demitido:
            del funcionários[2]
            break
        else:
            print('Nome não encontrado.')
            demitido = str(input('Tente novamente:'))



#Quinto IF
if escolha==5:
    aumento = int(input('De quanto será o aumento???'))
    funcionário_aumento = str(input('Digite o nome do funcionário que você deseja dar um aumento:'))
    while True:
        if 'Neymar' in funcionário_aumento:
            total=aumento+ 14000000
            del funcionários[0]
            funcionários.insert(0,{'código de funcionário':'11','nome':'Neymar','email':'neymarjr@gmail.com',
               'data de admissão':'2011','salário':total})
            break
        elif 'Cristiano' in funcionário_aumento:
            total=aumento+ 183000000
            del funcionários[1]
            funcionários.insert(1,{'código de funcionário':'7','nome':'Cristiano','email':'cristiano@gmail.com',
               'data de admissão':'1997','salário':total})
            break
        elif 'Messi' in funcionário_aumento:
            total=aumento+ 123000000
            del funcionários[2]
            funcionários.insert(2,{'código de funcionário':'10','nome':'Messi','email':'messi@gmail.com',
               'data de admissão':'1999','salário':total})
            break
        else:
            funcionário_aumento = str(input('Nome inválido. Tente novamente:'))

if escolha!=3:
    print(funcionários)