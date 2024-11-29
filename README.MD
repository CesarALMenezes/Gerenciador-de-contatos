Gerenciador de Contatos

Um sistema para gerenciar contatos pessoais e profissionais. Permite o cadastro, listagem, atualização, exclusão e busca de contatos, com suporte a informações adicionais.

Funcionalidades 

Criar Contato
Adicione informações detalhadas sobre cada contato:

Nome
Telefone
E-mail
Empresa (informação adicional)
Aniversário (informação adicional)

Listar Contatos 

Visualize todos os contatos registrados.
Exibição formatada dos contatos para facilitar a leitura.

Atualizar Contato

Altere qualquer informação de um contato existente.

Deletar Contato

Remova contatos do sistema com opção de confirmação para evitar exclusões acidentais.

Buscar Contatos (Funcionalidade Extra)
Encontre contatos por:

Nome
Empresa

Encerrar

Encerre o programa.

Detalhes Técnicos
Estrutura de Arquivo

Os contatos são armazenados em um arquivo CSV chamado dados/contatos.csv.
Estrutura do arquivo:

Nome
Telefone
E-mail
Empresa
Aniversário

Implementação
Foi utilizada a biblioteca csv para leitura, escrita e manipulação do arquivo de dados.

A estrutura do código foi modularizada em:

Controladores: para gerenciar as interações do menu com as funcionalidades.
Funcionalidades: para manipulação lógica de cada operação.
Serviços: para operações de leitura e escrita no arquivo CSV.
Menu Principal
O menu principal apresenta as seguintes opções:

Criar Contato
Listar Contatos
Atualizar Contato
Deletar Contato
Buscar Contato
Encerrar

