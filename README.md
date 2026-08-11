# InfraKit

InfraKit é uma ferramenta modular de infraestrutura desenvolvida em Python e executada pelo terminal.

O projeto utiliza uma arquitetura baseada em **plugins**, permitindo adicionar novas funcionalidades sem precisar alterar diretamente o Engine.

O InfraKit também funciona como um projeto prático de aprendizado, com foco em Python, automação, infraestrutura, CLI e arquitetura modular.

## 🚧 Status

**Em desenvolvimento — versão inicial**

Atualmente, o InfraKit possui:

* Interface CLI interativa
* Menu principal
* Sistema de plugins
* Descoberta automática de plugins
* Engine para gerenciamento e execução dos plugins
* Plugin de Ping
* Plugin de DNS
* Execução de comandos do sistema através do `subprocess`
* Sistema padronizado de status e resultados
* Tratamento básico de erros
* Execução de scans através do menu

## 📂 Estrutura

```text
InfraKit/
│
├── cli/
│   └── menu.py
│
├── core/
│   ├── engine.py
│   └── plugin.py
│
├── plugins/
│   └── network/
│       ├── ping.py
│       └── dns.py
│
├── main.py
├── .gitignore
└── README.md
```

## ⚙️ Arquitetura

O InfraKit utiliza uma arquitetura modular baseada em plugins:

```text
                 main.py
                    │
                    ▼
             Menu / CLI
                    │
                    ▼
             Menu Control
                    │
                    ▼
                 Engine
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      PingPlugin          DNSPlugin
          │                   │
          └─────────┬─────────┘
                    ▼
               Resultados
```

O `main.py` é responsável pelo ponto de entrada do programa e pelo controle do fluxo do menu.

O `cli/menu.py` contém a interface do menu e retorna a opção escolhida pelo usuário.

O `Engine` é responsável por carregar e executar os plugins.

Cada plugin possui uma função específica e retorna seu próprio status e resultado.

## 🧩 Sistema de Plugins

O InfraKit possui um sistema de descoberta automática de plugins.

O Engine procura arquivos Python dentro dos diretórios de plugins, importa os módulos e identifica classes que herdam da classe base `Plugin`.

Isso permite adicionar novos plugins sem precisar registrá-los manualmente no Engine.

Atualmente:

| Plugin | Categoria | Função                                |
| ------ | --------- | ------------------------------------- |
| Ping   | Network   | Teste de conectividade com um alvo    |
| DNS    | Network   | Resolução de domínio para endereço IP |

### Exemplo de fluxo

```text
plugins/network/ping.py
        │
        ▼
Engine encontra o arquivo
        │
        ▼
Importa o módulo
        │
        ▼
Identifica PingPlugin
        │
        ▼
Cria uma instância
        │
        ▼
Adiciona aos plugins disponíveis
```

## 🖥️ Menu

O InfraKit possui um menu interativo para facilitar a utilização:

```text
╔══════════════════════════╗
║        InfraKit          ║
╠══════════════════════════╣
║  1. Scan                 ║
║  2. Plugins              ║
║  0. Sair                 ║
╚══════════════════════════╝
```

### Scan

Ao selecionar `Scan`, o programa solicita o alvo:

```text
Digite o domínio do scan: google.com
```

O Engine executa os plugins disponíveis e apresenta os resultados:

```text
Ping

Status: SUCESSO!

Resultado: ...

DNS

Status: Sucesso

Resultado: 172.xxx.xxx.xxx
```

### Plugins

A opção `Plugins` mostra os plugins atualmente carregados pelo Engine, incluindo seus nomes e descrições.

## ▶️ Execução

Para executar o InfraKit:

```bash
python3 main.py
```

O programa abrirá o menu interativo.

A partir dele é possível selecionar as funções disponíveis.

## 🛠️ Tecnologias

* Python
* Git
* GitHub
* `subprocess`
* `importlib`
* CLI
* Arquitetura modular de plugins

## 🗺️ Próximos passos

As funcionalidades abaixo fazem parte do planejamento futuro do projeto e ainda não estão implementadas:

### Arquitetura

* [ ] Melhorar o sistema de descoberta de plugins
* [ ] Organização dos plugins por categorias
* [ ] Melhorar o sistema de resultados
* [ ] Melhorar o tratamento de erros
* [ ] Sistema de configuração

### Network

* [ ] Plugin HTTP
* [ ] Traceroute
* [ ] Novas ferramentas de análise de rede

### System

* [ ] Informações do sistema
* [ ] Informações de CPU
* [ ] Informações de memória
* [ ] Informações de armazenamento
* [ ] Informações das interfaces de rede

### Persistência

* [ ] Persistência de resultados com SQLite
* [ ] Histórico de scans
* [ ] Visualização de scans anteriores
* [ ] Exportação de resultados

### Identidade e sincronização

Planejamento para uma etapa mais avançada do projeto:

* [ ] Sistema de identidade baseado em token
* [ ] Modo de utilização sem conta
* [ ] Histórico associado à identidade do usuário
* [ ] API do InfraKit
* [ ] Sincronização de histórico

> Esses recursos são apenas planos futuros e não fazem parte da versão atual.

## 📚 Objetivo

O InfraKit é desenvolvido como um projeto prático para estudar e aplicar conceitos de:

* Programação em Python
* Programação orientada a objetos
* Arquitetura modular
* Desenvolvimento de CLI
* Automação
* Gerenciamento de processos
* Redes
* Persistência de dados
* Arquitetura de software

O projeto será desenvolvido gradualmente, adicionando novas funcionalidades conforme a arquitetura evolui.
