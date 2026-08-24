# InfraKit

O **InfraKit** é uma ferramenta modular de infraestrutura desenvolvida em Python e executada através do terminal.

O projeto tem como objetivo estudar, na prática, conceitos de **Python, automação, redes, infraestrutura, arquitetura modular e desenvolvimento baseado em plugins**.

---

## 🚧 Status

**Em desenvolvimento — versão inicial**

Atualmente, o InfraKit possui:

* Interface CLI
* Sistema modular de plugins
* Descoberta automática de plugins
* Engine para gerenciamento e execução dos plugins
* `PluginResult` para padronização dos resultados
* `ScanResult` para organização de um scan completo
* Logger com data e hora
* Histórico de scans
* Plugin de Ping
* Plugin HTTP
* Plugin DNS
* Plugin de PortScan
* Verificação de portas TCP através de `socket`
* Execução de comandos do sistema através de `subprocess`

---

## 📂 Estrutura

```text
InfraKit/
│
├── core/
│   ├── engine.py
│   ├── plugin.py
│   ├── result.py
│   ├── scan.py
│   └── logger.py
│
├── plugins/
│   └── network/
│       ├── ping.py
│       ├── dns.py
│       ├── http.py
│       └── portscan.py
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

---

## ⚙️ Arquitetura

O InfraKit utiliza uma arquitetura baseada em plugins.

```text
                    main.py
                       │
                       ▼
                     Engine
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        Ping          HTTP         DNS
          │            │            │
          └────────────┼────────────┘
                       ▼
                    PortScan
                       │
                       ▼
                 PluginResult
                       │
                       ▼
                  ScanResult
                       │
              ┌────────┴────────┐
              ▼                 ▼
           Logger             CLI
```

### Engine

O `Engine` é responsável por:

* descobrir plugins automaticamente;
* carregar os módulos;
* identificar classes que herdam de `Plugin`;
* executar os plugins;
* organizar os resultados;
* registrar os resultados no log;
* criar o `ScanResult`.

### Plugin

Cada funcionalidade do InfraKit é implementada como um plugin independente.

Todos os plugins seguem o mesmo padrão:

```text
Plugin
  │
  └── run(target)
          │
          ▼
    PluginResult
```

Isso permite adicionar novas funcionalidades sem precisar modificar o funcionamento principal do Engine.

---

## 📦 Resultados

O InfraKit possui duas classes para organização dos resultados.

### PluginResult

Representa o resultado de um único plugin.

Possui:

```text
nome
status
resultado
```

Exemplo:

```text
PING
Status: SUCESSO!
Resultado:
PING google.com ...
```

### ScanResult

Representa o resultado completo de um scan.

Ele contém:

```text
target
resultados
```

onde `resultados` é uma coleção de `PluginResult`.

---

## 🔌 Plugins

### Ping

Realiza um teste de conectividade utilizando o comando `ping`.

Exemplo:

```text
PING
Status: SUCESSO!
Resultado:
2 packets transmitted, 2 received, 0% packet loss
```

---

### HTTP

Realiza uma requisição HTTP ao alvo e verifica o código de resposta.

Exemplo:

```text
HTTP
Status: SUCESSO!
Resultado:
Requisição realizada com sucesso! código HTTP: 200
```

---

### DNS

Realiza a resolução DNS do domínio.

Exemplo:

```text
DNS
Status: SUCESSO!
Resultado:
142.250.219.238
```

---

### PortScan

Realiza uma verificação de portas TCP comuns utilizando o módulo `socket` do Python.

Atualmente são verificadas:

| Porta | Serviço |
| ----: | ------- |
|    22 | SSH     |
|    53 | DNS     |
|    80 | HTTP    |
|   443 | HTTPS   |
|  8080 | HTTP    |

Exemplo:

```text
PortScan
Status: SUCESSO!
Resultado:
   22 | SSH   | FECHADA
   53 | DNS   | FECHADA
   80 | HTTP  | FECHADA
  443 | HTTPS | FECHADA
 8080 | HTTP  | ABERTA
```

O PortScan utiliza `socket` e `connect_ex()` para verificar se uma conexão TCP pode ser estabelecida na porta analisada.

---

## 📝 Logger

O InfraKit possui um sistema de logs para registrar os resultados dos plugins.

Os registros são armazenados em:

```text
logs/infrakit.log
```

Cada registro contém:

```text
data/hora | alvo | plugin | status
```

Exemplo:

```text
24/08/2026 - 16:18:37 | google.com | PING | SUCESSO!
24/08/2026 - 16:18:38 | google.com | HTTP | SUCESSO!
24/08/2026 - 16:18:38 | google.com | PortScan | SUCESSO!
24/08/2026 - 16:18:38 | google.com | DNS | SUCESSO!
```

A pasta `logs` é criada automaticamente quando necessário.

---

## ▶️ Execução

Para iniciar o InfraKit:

```bash
python3 main.py
```

O menu principal apresenta:

```text
╔══════════════════════════╗
║        InfraKit           ║
╠══════════════════════════╣
║  1. Scan                 ║
║  2. Plugins              ║
║  3. Histórico            ║
║  0. Sair                 ║
╚══════════════════════════╝
```

### Scan

A opção `Scan` executa todos os plugins disponíveis contra o alvo informado.

Exemplo:

```text
Digite o domínio do scan: google.com
```

O Engine executará automaticamente os plugins carregados.

### Plugins

Lista os plugins encontrados pelo sistema.

### Histórico

Exibe os registros armazenados pelo Logger.

---

## 🛠️ Tecnologias

* Python
* Git
* GitHub
* CLI
* `subprocess`
* `socket`
* `datetime`
* `os`
* `importlib`

---

## 🧩 Sistema de plugins

O InfraKit possui descoberta automática de plugins.

Para adicionar uma nova funcionalidade, basta criar um novo módulo dentro da pasta `plugins` e implementar uma classe que herde de `Plugin`.

O Engine identifica automaticamente o novo plugin durante a inicialização.

Fluxo:

```text
Novo plugin
     │
     ▼
Herda Plugin
     │
     ▼
Implementa run()
     │
     ▼
Retorna PluginResult
     │
     ▼
Engine detecta automaticamente
```

Isso permite que o projeto cresça de forma modular.

---

## 🗺️ Próximos passos

Funcionalidades planejadas:

* [ ] Melhorar o sistema de resultados
* [ ] Melhorar o PortScan
* [ ] Adicionar identificação de serviços
* [ ] Adicionar novos plugins de infraestrutura
* [ ] Plugin de informações HTTP
* [ ] Plugin WHOIS
* [ ] Sistema automático de descoberta de plugins
* [ ] Persistência de resultados com SQLite
* [ ] Histórico estruturado de scans
* [ ] Ferramentas de OSINT
* [ ] Novos módulos de análise
* [ ] Melhorar tratamento de erros
* [ ] Configuração das portas do PortScan
* [ ] Sistema de configuração do InfraKit

> As funcionalidades listadas acima são planos futuros e ainda não estão implementadas.

---

## 📚 Objetivo do projeto

O InfraKit também funciona como um projeto prático de aprendizado.

Através do desenvolvimento da ferramenta, são estudados conceitos como:

* Programação orientada a objetos;
* Herança;
* Modularização;
* Exceções;
* Manipulação de arquivos;
* Automação;
* Redes;
* Sockets;
* TCP;
* DNS;
* HTTP;
* CLI;
* Arquitetura de software;
* Git e GitHub;
* Desenvolvimento baseado em plugins.

O projeto será desenvolvido gradualmente, adicionando novas funcionalidades enquanto a arquitetura é aprimorada.

---

## ⚠️ Uso

Utilize as funcionalidades de análise de rede somente em sistemas, dispositivos e redes para os quais você possui autorização.

O InfraKit é desenvolvido principalmente para **aprendizado, administração de infraestrutura e testes em ambientes autorizados**.
