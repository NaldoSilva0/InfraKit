# 🔧 InfraKit

Ferramenta modular de infraestrutura desenvolvida em **Python**, executada através do terminal.

O InfraKit foi criado como um projeto prático para estudar **Python, Linux, automação, redes, OSINT e arquitetura modular baseada em plugins**.

> 🚧 **Projeto em desenvolvimento**

---

## 📌 Sobre o projeto

O InfraKit reúne diferentes ferramentas de diagnóstico e análise em uma única interface de terminal.

A aplicação utiliza uma arquitetura baseada em **plugins**, permitindo adicionar novas funcionalidades sem precisar concentrar toda a lógica em um único arquivo.

Atualmente, o projeto possui módulos para:

* 🌐 Análise de rede
* 🔎 Consultas DNS
* 👤 Verificação de usernames em plataformas públicas
* 💻 Monitoramento básico do computador
* 📜 Histórico de scans
* 🧩 Descoberta automática de plugins

---

## 🏗️ Arquitetura

O funcionamento básico do InfraKit segue esta estrutura:

```text
                    ┌──────────────┐
                    │    main.py   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  CLI / Menu  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Engine    │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          Network        OSINT       Computer
              │            │            │
              ▼            ▼            ▼
           Plugins      Plugins       Plugins
              │            │            │
              └────────────┼────────────┘
                           ▼
                    ┌──────────────┐
                    │ PluginResult │
                    └──────────────┘
```

O `Engine` é responsável por carregar e executar os plugins.

Cada plugin possui uma responsabilidade específica e retorna seus resultados através do sistema de resultados do InfraKit.

---

## 📂 Estrutura do projeto

```text
InfraKit/
│
├── cli/
│   └── menu.py
│
├── core/
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
├── teste.py
├── .gitignore
└── README.md
```

---

## ⚙️ Funcionalidades

### 🌐 Network

Plugins relacionados à análise de rede.

| Plugin   | Função                    |
| -------- | ------------------------- |
| Ping     | Teste de conectividade    |
| DNS      | Consulta registros DNS    |
| HTTP     | Consulta informações HTTP |
| PortScan | Verificação de portas     |

---

### 🔎 OSINT

O módulo OSINT permite verificar a presença de um username em plataformas públicas.

Atualmente possui suporte para plataformas como:

* GitHub
* Reddit
* Instagram
* Facebook
* TikTok

Como diferentes plataformas possuem diferentes formas de resposta, o InfraKit pode retornar estados como:

```text
Registrado!
Não registrado!
Não foi possível verificar
Consulta bloqueada pela plataforma
```

O objetivo é evitar tratar uma resposta HTTP genérica como uma confirmação absoluta de existência.

---

### 💻 Hardware Status

O plugin `HardConfig` permite visualizar informações básicas do sistema:

* Uso da RAM
* Uso da CPU
* Armazenamento
* Dados de rede

Exemplo:

```text
╔══════════════════════════════════════════════════════╗
║               HardConfig - System Monitor            ║
╠══════════════════════════════════════════════════════╣
║ RAM                                                  ║
╠══════════════════════════════════════════════════════╣
║ RAM Total:  3.71GB                                   ║
║ RAM Usando:  2.37GB                                  ║
║ RAM Barra: [████████████--------] 63.7%              ║
╠══════════════════════════════════════════════════════╣
║ CPU                                                  ║
╠══════════════════════════════════════════════════════╣
║ CPU Total:  45.9%                                    ║
║ CPU Barra:  [█████████-----------] 45.9%             ║
╠══════════════════════════════════════════════════════╣
║ ARMAZENAMENTO                                        ║
╠══════════════════════════════════════════════════════╣
║ DISCO Total:  194.03GB                               ║
║ DISCO Usando:  80.23GB                               ║
║ DISCO Barra: [████████------------] 41.3%             ║
╠══════════════════════════════════════════════════════╣
║ REDE                                                 ║
╠══════════════════════════════════════════════════════╣
║ BYTES Enviados:  22.79MB                             ║
║ BYTES Recebidos:  43.54MB                            ║
╚══════════════════════════════════════════════════════╝
```

---

## 🧩 Sistema de Plugins

Uma das principais características do InfraKit é o sistema de plugins.

Novos plugins podem ser adicionados dentro da pasta:

```text
plugins/
```

O `Engine` realiza a descoberta dos arquivos e identifica automaticamente as classes que herdam da classe base `Plugin`.

Isso permite adicionar novas funcionalidades sem precisar alterar diretamente o núcleo da aplicação.

Exemplo conceitual:

```python
from core.plugin import Plugin

class MeuPlugin(Plugin):

    def __init__(self):
        super().__init__(
            "MeuPlugin",
            "Descrição do plugin"
        )

    def run(self, target):
        ...
```

---

## 📊 Sistema de resultados

Os plugins utilizam `PluginResult` para padronizar suas respostas.

Um resultado possui:

```text
Nome
Status
Resultado
```

Exemplo:

```text
DNS
Status: SUCESSO!
Resultado:
A:
142.250.xxx.xxx
```

Resultados que possuem múltiplas informações também podem utilizar estruturas como `dict`.

---

## 📜 Histórico e Logs

O InfraKit possui um sistema de registro das execuções através do `Logger`.

Os registros são utilizados para manter informações sobre os plugins executados e seus respectivos status.

Os arquivos de log são ignorados pelo Git através do `.gitignore`.

---

## ▶️ Executando

Clone o repositório:

```bash
git clone https://github.com/NaldoSilva0/InfraKit.git
```

Entre na pasta:

```bash
cd InfraKit
```

Execute:

```bash
python3 main.py
```

---

## 🖥️ Menu

O InfraKit possui uma interface de terminal com opções como:

```text
╔══════════════════════════╗
║        InfraKit          ║
╠══════════════════════════╣
║  1. Scan                 ║
║  2. Plugins              ║
║  3. Histórico            ║
║  4. OSINT                ║
║  5. Hardware Status      ║
║  0. Sair                 ║
╚══════════════════════════╝
```

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Linux**
* **Git / GitHub**
* `requests`
* `psutil`
* `dnspython`
* `subprocess`
* `socket`
* `importlib`

---

## 🗺️ Próximos passos

O projeto ainda está em desenvolvimento.

Algumas ideias para versões futuras:

* [ ] Melhorar o sistema de resultados
* [ ] Melhorar o tratamento de erros
* [ ] Adicionar novos plugins de infraestrutura
* [ ] Adicionar novas plataformas ao OSINT
* [ ] Melhorar o sistema de histórico
* [ ] Persistência de dados com SQLite
* [ ] Melhorar a interface CLI
* [ ] Adicionar testes automatizados
* [ ] Melhorar a documentação dos plugins
* [ ] Criar novos módulos de análise

---

## 🎯 Objetivo

O InfraKit é, acima de tudo, um projeto prático de aprendizado.

A ideia é utilizar o desenvolvimento da ferramenta para estudar e aplicar conceitos de:

```text
Python
   ↓
Linux
   ↓
Redes
   ↓
Automação
   ↓
APIs
   ↓
Arquitetura de software
   ↓
Plugins
   ↓
OSINT
```

O projeto continuará evoluindo conforme novos conceitos forem aprendidos e novas funcionalidades forem implementadas.

---

## ⚠️ Aviso

O InfraKit deve ser utilizado apenas em sistemas, redes e serviços nos quais você tenha autorização para realizar testes e consultas.

O projeto tem finalidade **educacional, de administração de sistemas e análise de informações públicas**.
