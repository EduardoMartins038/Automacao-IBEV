print('Olá, Seja bem-vindo á IBEV! Para realizar o seu cadastro é necessário preencher os seguintes dados:')
nomec=input('Informe por favor seu nome completo:')
cpf=input('Digite seu CPF:')
datanascimento=input('Informe por favor sua data de nascimento:')
endereco=input('Informe por favor seu endereço completo, Exemplo: *Av. Crisantino de Almeida, 590 - Vargem Grande II, Montes Claros - MG, 39403-452* ')
contato=input('Qual o telefone para contato?')
nome=input('Como gostaria de ser chamado?')
confirm=input('Maravilha {}, Agora me confime os dados informados: Seu nome completo é: {}, Seu Cpf: {}, Sua data de nascimento: {}, Seu endereco: {}, Sua naturalidade: {}, Seu telefone para contato: {}'
.format(nome, nomec, cpf, datanascimento, endereco, contato))
print('Glorias a Deus, {}! Seu cadastro foi feito com sucesso.'.format(nome))