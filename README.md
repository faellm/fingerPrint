# Projeto de Automação Web com Selenium

Este é um projeto de automação web desenvolvido em Python usando a biblioteca Selenium. O objetivo deste projeto é demonstrar como automatizar ações em um navegador web, neste caso, o Firefox, utilizando o Selenium para interagir com elementos da página, realizar ações e personalizar configurações do navegador.

## Funcionalidades

### 1. Geração de Número Inteiro Aleatório

O projeto começa gerando um número inteiro aleatório entre 5 e 20, com passo de 2, usando a biblioteca `random`. Esse número é exibido no console.

### 2. Definição de User-Agent Personalizado

Um novo User-Agent é definido, simulando a identidade do navegador. Isso é feito através das opções do navegador Firefox, onde o User-Agent é sobrescrito para o valor definido.

### 3. Inicialização do Navegador Firefox

O projeto inicia um navegador Firefox usando o WebDriver do Selenium. O serviço do driver do Firefox é configurado usando o WebDriver Manager para instalar automaticamente a versão adequada do driver. As opções de navegador definidas anteriormente são aplicadas.

### 4. Criação de um Novo Usuário

A função `create_new_user()` demonstra como acessar uma página específica para criar um novo perfil de usuário. Ela busca um botão na página e realiza um clique. Depois, a nova janela aberta é tratada, demonstrando como interagir com elementos nessa nova janela.

### 5. Ajuste das Configurações do Firefox

A função `open_config()` acessa a página de configurações do Firefox (`about:config`). Se houver um botão de aceitar riscos, ele é clicado para permitir o acesso às configurações. Em seguida, o botão "Mostrar Tudo" é clicado para exibir todas as configurações disponíveis. Essa parte do projeto serve como exemplo de como acessar e interagir com elementos de configuração do navegador.

### 6. Encerramento do Navegador

O navegador é encerrado usando a função `driver.quit()` ao final do projeto.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- Selenium
- webdriver_manager
- time

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as bibliotecas necessárias usando o comando `pip install selenium webdriver_manager`.
3. Copie o código do projeto para um arquivo `.py`.
4. Execute o arquivo usando o comando `python nome_do_arquivo.py`.

Lembre-se de que este é um projeto de demonstração e você pode adaptá-lo para suas próprias necessidades, expandindo as funcionalidades e ajustando as interações de acordo com as páginas web que deseja automatizar. Certifique-se de entender a ética e as políticas de automação da web ao aplicar esses conceitos em seus próprios projetos.
