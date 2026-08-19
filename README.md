# InfraKit

InfraKit é uma ferramenta modular de infraestrutura desenvolvida em Python e executada pelo terminal.

O projeto foi criado com foco em **aprendizado de Python, automação, infraestrutura, arquitetura modular de plugins e organização de software**.

## 🚧 Status

**Em desenvolvimento — versão inicial**

Atualmente, o InfraKit possui:

* Interface CLI
* Sistema modular de plugins
* Descoberta automática de plugins
* Engine para gerenciamento e execução dos plugins
* Sistema padronizado de resultados com `PluginResult`
* Plugin de Ping
* Plugin HTTP
* Plugin DNS
* Execução de comandos do sistema através do `subprocess`
* Requisições HTTP através do `requests`
* Sistema de logs
* Registro automático de data e hora
* Registro do alvo, plugin e status da execução
* Histórico de scans através do terminal
* Criação automática da pasta de logs

## 📂 Estrutura

```text
InfraKit/
│
├── core/
│   ├── engine.py
│   ├── plugin.py
│   ├── result.py
│   └── logger.py
│
├── plugins/
│   └── network/
│       ├── ping.py
│       ├── http.py
│       └── dns.py
│
├── cli/
│   └── menu.py
│
├── logs/
│   └── infrakit.log
│
├── main.py
├── .gitignore
└── README.md
```

## ⚙️ Arquitetura

O InfraKit utiliza uma arquitetura baseada em plugins:

```text
                         ┌─────────────┐
                         │   main.py   │
                         └──────┬──────┘
                                │
                                ▼
                         ┌─────────────┐
                         │    Engine   │
                         └──────┬──────┘
                                │
                   ┌────────────┼────────────┐
                   ▼            ▼            ▼
                PING           HTTP          DNS
                   │            │            │
                   └────────────┼────────────┘
                                ▼
                         PluginResult
                                │
                                ▼
                             Logger
                                │
                                ▼
                       logs/infrakit.log
```

### `main.py`

Responsável pela interface principal do programa e pelo controle do menu.

### `Engine`

Responsável por:

* Descobrir automaticamente os plugins;
* Carregar os plugins;
* Executar os plugins;
* Padronizar os resultados;
* Encaminhar os resultados para o sistema de logs.

### `Plugin`

Define a estrutura básica que os plugins devem seguir.

Novos plugins podem herdar dessa classe e implementar suas próprias funcionalidades.

### `PluginResult`

Responsável por organizar o resultado de cada plugin:

```text
Nome
Status
Resultado
```

Isso permite que o Engine trabalhe com os resultados de maneira padronizada.

### `Logger`

Responsável pelo sistema de logs do InfraKit.

O Logger registra:

* Data e hora;
* Alvo do scan;
* Plugin executado;
* Status da execução.

Os registros são armazenados em:

```text
logs/infrakit.log
```

A pasta `logs` é criada automaticamente caso não exista.

## ▶️ Como executar

Execute o programa pela raiz do projeto:

```bash
python3 main.py
```

O InfraKit apresenta o menu:

```text
╔══════════════════════════╗
║        InfraKit          ║
╠══════════════════════════╣
║  1. Scan                 ║
║  2. Plugins              ║
║  3. Histórico            ║
║  0. Sair                 ║
╚══════════════════════════╝
```

## 🔎 Scan

A opção `1` executa todos os plugins disponíveis contra o alvo informado.

Exemplo:

```text
Digite o domínio do scan: google.com
```

O InfraKit executará os plugins disponíveis e exibirá seus resultados.

Também são aceitos alvos com protocolo:

```text
google.com
http://google.com
https://google.com
```

## 🧩 Plugins

### PING

Realiza um teste de conectividade com o alvo utilizando o comando `ping` do sistema.

Exemplo de resultado:

```text
PING
Status: SUCESSO!
Resultado: PING google.com ...
```

### HTTP

Realiza uma requisição HTTP/HTTPS utilizando a biblioteca `requests`.

O plugin identifica códigos HTTP e apresenta informações básicas sobre a requisição.

Exemplo:

```text
HTTP
Status: SUCESSO!
Resultado: Requisição realizada com sucesso! código HTTP: 200
```

### DNS

Realiza a resolução DNS do domínio e retorna o endereço IP encontrado.

Exemplo:

```text
DNS
Status: SUCESSO!
Resultado: 142.250.219.238
```

## 📋 Lista de plugins

| Plugin | Função                              |
| ------ | ----------------------------------- |
| PING   | Teste de conectividade              |
| HTTP   | Requisição e verificação HTTP/HTTPS |
| DNS    | Resolução DNS                       |

O sistema foi desenvolvido para permitir a adição de novos plugins sem precisar alterar a estrutura principal do Engine.

## 📝 Sistema de Logs

Após a execução dos plugins, o InfraKit registra automaticamente os resultados.

Exemplo:

```text
14/08/2026 - 18:58:58 | google.com | PING | SUCESSO!
14/08/2026 - 18:58:59 | google.com | HTTP | SUCESSO!
14/08/2026 - 18:58:59 | google.com | DNS | SUCESSO!
14/08/2026 - 18:59:07 | exemplo.com | PING | ERRO!
14/08/2026 - 18:59:07 | exemplo.com | HTTP | ERRO!
14/08/2026 - 18:59:07 | exemplo.com | DNS | ERRO!
```

Os logs são armazenados em:

```text
logs/infrakit.log
```

A pasta é criada automaticamente pelo `Logger`.

## 📚 Histórico

A opção `3` do menu permite consultar os logs diretamente pelo terminal.

Exemplo:

```text
╔═══════════════════════════╗
║         HISTÓRICO         ║
╚═══════════════════════════╝

14/08/2026 - 18:58:58 | google.com | PING | SUCESSO!
14/08/2026 - 18:58:59 | google.com | HTTP | SUCESSO!
14/08/2026 - 18:58:59 | google.com | DNS | SUCESSO!
```

Isso permite consultar execuções anteriores sem precisar abrir o arquivo de log manualmente.

## 🛠️ Tecnologias

* Python
* Git
* GitHub
* `subprocess`
* `requests`
* `os`
* `importlib`
* `datetime`
* CLI

## 🔐 Conceito de uso

O InfraKit foi desenvolvido como uma ferramenta de aprendizado e experimentação em infraestrutura e segurança.

Os plugins devem ser utilizados apenas em sistemas, domínios e ambientes nos quais o usuário tenha autorização para realizar testes.

## 🗺️ Próximos passos

Funcionalidades planejadas:

* [ ] Melhorar a apresentação dos resultados
* [ ] Melhorar o sistema de logs
* [ ] Separar os logs por scan
* [ ] Sistema para limpar o histórico
* [ ] Histórico com filtros
* [ ] Persistência de resultados utilizando SQLite
* [ ] Histórico estruturado de scans
* [ ] Novos plugins de infraestrutura
* [ ] Sistema de descoberta e gerenciamento de plugins mais avançado
* [ ] Ferramentas de análise de rede
* [ ] Ferramentas de OSINT
* [ ] Novos módulos de análise
* [ ] Melhor tratamento de exceções
* [ ] Configurações personalizáveis

> As funcionalidades listadas acima são planos futuros e ainda não estão implementadas.

## 📖 Objetivo

O InfraKit também funciona como um projeto prático de aprendizado.

Durante seu desenvolvimento são estudados conceitos como:

* Programação em Python;
* Programação orientada a objetos;
* Herança;
* Arquitetura modular;
* Sistemas de plugins;
* Manipulação de arquivos;
* Logs;
* CLI;
* Redes;
* DNS;
* HTTP;
* Infraestrutura;
* Organização de projetos;
* Git e GitHub.

A ideia é evoluir o InfraKit gradualmente, adicionando funcionalidades enquanto a arquitetura do projeto também é aprimorada.

## 👨‍💻 Desenvolvimento

O projeto está em desenvolvimento contínuo e novas funcionalidades serão adicionadas conforme a arquitetura evoluir.
