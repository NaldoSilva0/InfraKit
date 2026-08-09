# InfraKit

Ferramenta de diagnóstico de infraestrutura desenvolvida em Python, com arquitetura baseada em plugins.

O objetivo do InfraKit é permitir a execução de diferentes testes de rede através de uma estrutura modular e extensível.

## Funcionalidades

* **Ping** — testa a conectividade com o alvo.
* **DNS** — resolve o domínio e obtém seu endereço IP.
* **Sistema de plugins** — plugins são descobertos e carregados automaticamente pelo Engine.
* **Status e resultados** — cada plugin retorna seu status e o resultado da execução.

## Uso

Para visualizar os plugins disponíveis:

```bash
python3 main.py plugins
```

Para executar um scan:

```bash
python3 main.py scan <alvo>
```

Exemplo:

```bash
python3 main.py scan google.com
```

## Estrutura

```text
InfraKit/
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
└── README.md
```

## Arquitetura

O InfraKit utiliza uma arquitetura baseada em plugins.

O `Engine` procura automaticamente por arquivos Python dentro do diretório de plugins, identifica classes que herdam da classe base `Plugin`, cria suas instâncias e adiciona os plugins ao sistema.

Isso permite adicionar novos plugins sem precisar cadastrá-los manualmente no `Engine`.

### Exemplo de fluxo

```text
Engine
  ↓
Procura os plugins
  ↓
Encontra os módulos
  ↓
Identifica classes Plugin
  ↓
Cria as instâncias
  ↓
Executa os plugins
  ↓
Retorna status + resultado
```

## Criando um plugin

Um novo plugin deve herdar da classe base `Plugin` e implementar o método `run()`.

Exemplo:

```python
from core.plugin import Plugin

class MeuPlugin(Plugin):

    def __init__(self):
        super().__init__("MeuPlugin", "Descrição do plugin")

    def run(self, target):
        # lógica do plugin
        return ["SUCESSO", "Resultado"]
```

Depois de colocado no diretório apropriado de plugins, o InfraKit poderá encontrá-lo automaticamente.

## Tecnologias

* Python 3
* `socket`
* `subprocess`
* `importlib`
* `os`

## Status do projeto

🚧 Em desenvolvimento.

O projeto está sendo desenvolvido gradualmente, com foco em uma arquitetura modular que permita adicionar novas ferramentas de diagnóstico através de plugins.
