# Web-PyInstaller

PyInstaller é uma biblioteca simples de usar para gerar executáveis a partir de aplicações Python. No entanto, ele não permite cross-compiling nativo entre diferentes sistemas operacionais.

Web-PyInstaller é uma aplicação web open source desenvolvida em Flask que permite converter projetos Python hospedados em repositórios Git em executáveis compatíveis com Linux, Windows e Alpine, de acordo com a plataforma selecionada.

## Como Funciona

A aplicação:

1. Recebe a URL de um repositório Git
2. Clona o projeto
3. Executa um container Docker
4. Usa o PyInstaller dentro do container para gerar o executável

O processo utiliza a imagem Docker `fydeinc/pyinstaller`.

## Requisitos Importantes

Para que a conversão funcione corretamente:

- O arquivo `main.py` deve estar na raiz do repositório
- O projeto deve estar estruturado corretamente
- Você talvez tenha problemas de permissão, o `app/core/methods.py` deleta todos os arquivos de `app/src/`, isso inclui o `.gìt`, sugiro alterar as permições dessa pasta. Tambem pode ser necessário adicionar o seu usuário a permissão de rodar o docker. 

## Ambiente do Container

A imagem `fydeinc/pyinstaller` possui:

- Python 3.9.2
- PyInstaller 4.2

### Limitações

Devido à versão do Python (3.9.2):

- Recursos do Python 3.10 ou superior, como `match/case`, não são suportados
- Algumas bibliotecas mais recentes podem não funcionar corretamente
- A versão do PyInstaller é antiga e pode não suportar todas as opções modernas

Caso utilize recursos do Python 3.10 ou superior, será necessário adaptar o código ou usar uma imagem Docker mais recente.

## Objetivo do Projeto

Web-PyInstaller facilita a geração de executáveis multiplataforma de forma simples e acessível via interface web, eliminando a necessidade de configurar manualmente ambientes de build para cada sistema operacional.

## Licença

MIT License