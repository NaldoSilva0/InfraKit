# InfraKit

**InfraKit** é uma ferramenta modular de infraestrutura desenvolvida em Python para execução de tarefas de diagnóstico, análise de rede, coleta de informações e inspeção do sistema através de uma interface de linha de comando (CLI).

O projeto foi desenvolvido com foco em **aprendizado prático de Python, Linux, redes, automação e arquitetura modular baseada em plugins**.

---

## 🚧 Status

**Versão inicial — projeto em desenvolvimento**

O InfraKit já possui uma estrutura funcional de plugins, execução de scans, armazenamento de resultados em SQLite, histórico de execuções e ferramentas para análise de rede, sistema e informações públicas.

---

## ✨ Funcionalidades

### 🌐 Network

* **Ping** — testa a conectividade com um alvo.
* **DNS** — consulta registros DNS do domínio.
* **HTTP** — coleta informações básicas da resposta HTTP.
* **PortScan** — verifica o estado de portas específicas do alvo.

### 🔎 OSINT

* **Username** — verifica a presença de um nome de usuário em diferentes plataformas públicas.

### 💻 Computer

* **HardConfig** — coleta informações de hardware e configuração do computador.

### 📊 Sistema

* Interface de linha de comando.
* Arquitetura modular baseada em plugins.
* Execução centralizada através de uma Engine.
* Resultados estruturados por plugin.
* Persistência dos resultados utilizando SQLite.
* Histórico de scans.
* Sistema de logs.

---

## 🏗️ Arquitetura

O InfraKit utiliza uma arquitetura modular, onde cada funcionalidade é implementada como um plugin independente.

```text
                    InfraKit
                       │
                       ▼
                     CLI
                       │
                       ▼
                    Engine
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Network          OSINT         Computer
        │              │              │
   ┌────┼────┐         │              │
   ▼    ▼    ▼         ▼              ▼
 Ping  DNS  HTTP    Username      HardConfig
          │
          ▼
       PortScan
                       │
                       ▼
                  PluginResult
                       │
                       ▼
                    SQLite
```

A separação das responsabilidades permite adicionar novos plugins sem precisar modificar toda a estrutura da aplicação.

---

## 📂 Estrutura do projeto

```text
InfraKit/
│
├── cli/
│   └── menu.py
│
├── core/
│   ├── database.py
│   ├── engine.py
│   ├── logger.py
│   ├── plugin.py
│   ├── result.py
│   └── scan.py
│
├── plugins/
│   ├── computer/
│   │   └── hardconfig.py
│   │
│   ├── network/
│   │   ├── dns.py
│   │   ├── http.py
│   │   ├── ping.py
│   │   └── portscan.py
│   │
│   └── osint/
│       └── username.py
│
├── logs/
│
├── main.py
├── .gitignore
└── README.md
```

---

## ⚙️ Tecnologias

* **Python**
* **Linux**
* **SQLite**
* **Git**
* **GitHub**
* `subprocess`
* `socket`
* `requests`
* CLI

---

## ▶️ Instalação

Clone o repositório:

```bash
git clone https://github.com/NaldoSilva0/InfraKit.git
```

Entre no diretório:

```bash
cd InfraKit
```

Recomenda-se utilizar um ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Instale as dependências do projeto, caso estejam definidas em um arquivo de requisitos:

```bash
pip install -r requirements.txt
```

---

## 🚀 Execução

Execute o programa com:

```bash
python3 main.py
```

O InfraKit apresenta uma interface de menu através da qual é possível acessar as funcionalidades disponíveis.

---

## 🧩 Sistema de Plugins

O principal conceito arquitetural do InfraKit é o sistema de plugins.

Cada plugin possui uma responsabilidade específica e segue uma estrutura comum baseada na classe `Plugin`.

Exemplo conceitual:

```text
Plugin
  │
  ├── Ping
  ├── DNS
  ├── HTTP
  ├── PortScan
  ├── Username
  └── HardConfig
```

A `Engine` é responsável por coordenar e executar os plugins, enquanto o sistema de resultados organiza as informações produzidas por cada ferramenta.

Essa abordagem facilita a manutenção e permite que novas funcionalidades sejam adicionadas de maneira independente.

---

## 🗄️ Persistência e histórico

O InfraKit utiliza **SQLite** para armazenar informações relacionadas aos scans.

Os resultados podem ser associados a uma sessão de scan, permitindo consultar posteriormente:

* ID da execução;
* alvo analisado;
* plugin utilizado;
* status da execução;
* resultado obtido.

Isso permite manter um histórico das análises realizadas pelo programa.

---

## 📝 Exemplo de resultado

Um resultado pode ser apresentado de forma estruturada:

```text
[2] HTTP

Status: SUCESSO!

Resultado:

Processo     | Resultado
-------------------------------
HTTP         | 200
Server       | gws
Content-Type | text/html; charset=ISO-8859-1
HSTS         | Não encontrado
```

Resultados de diferentes plugins possuem formatos próprios de acordo com as informações coletadas.

---

## 🔐 Uso responsável

O InfraKit foi desenvolvido para **aprendizado, diagnóstico e análise de sistemas e redes em ambientes autorizados**.

As funcionalidades de rede e OSINT devem ser utilizadas somente em alvos sobre os quais você possui autorização para realizar análises.

O projeto não deve ser utilizado para acessar, interferir ou tentar explorar sistemas de terceiros sem permissão.

---

## 🗺️ Possíveis melhorias futuras

Algumas ideias que podem ser exploradas em versões futuras:

* [ ] Sistema automático de descoberta de plugins
* [ ] Melhorias na interface CLI
* [ ] Novos plugins de infraestrutura
* [ ] Melhor organização dos resultados
* [ ] Exportação dos resultados
* [ ] Melhor gerenciamento de logs
* [ ] Novos módulos de OSINT
* [ ] Novas ferramentas de análise de rede

> Essas funcionalidades são ideias para futuras versões e não fazem parte da implementação atual.

---

## 🎯 Objetivo do projeto

O InfraKit nasceu como um projeto prático para estudar e aplicar conceitos de:

* programação em Python;
* programação orientada a objetos;
* arquitetura modular;
* desenvolvimento de CLI;
* sistemas Linux;
* redes de computadores;
* automação;
* persistência de dados;
* organização de software.

Além de ser uma ferramenta experimental, o projeto representa uma etapa prática de aprendizado e evolução na área de tecnologia.

---

## 👤 Autor

**NaldoSilva0**

Projeto desenvolvido para fins de aprendizado e experimentação com Python, Linux, redes e desenvolvimento de software.

---

## 📄 Licença

Este projeto ainda não possui uma licença definida.
