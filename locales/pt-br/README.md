# Simulador de Detecção SIEM

**Bottom line:** gera eventos de log sintéticos, claramente identificados,
no formato de técnicas de ataque específicas — usado pra validar lógica
de detecção do Splunk (busca SPL, regra de correlação) antes de apontar
pra telemetria real. Nenhum script aqui executa ataque, conexão de rede
ou chamada de sistema real.

*Read this in: [English](./README.md)*

## Por que existe

Construir uma busca de detecção contra tráfego de ataque real significa
ou rodar algo genuinamente arriscado, ou esperar o evento real acontecer
sozinho. Esse repositório escreve linha de log no formato exato que um
evento real produziria, pra que a lógica de uma detecção — extração de
campo, correlação, limiar — possa ser testada e refinada rápido,
independente de um cenário de ataque ao vivo estar rodando.

Detecção validada assim ainda precisa ser confirmada contra telemetria
real antes de ser confiável — veja
[splunk-alert-response-pipeline](https://github.com/Kanetahk/splunk-alert-response-pipeline)
e [soc-lab](https://github.com/Kanetahk/soc-lab) pra onde isso acontece.

## Project structure
```
siem-detection-simulator/
├── locales/
│   └── pt-br/
│       └── README.md
├── src/
│   ├── gui/
│   │   └── __init__.py
│   └── logsgenerator/
│       ├── __init__.py
│       └── beaconing/
│           ├── __init__.py
│           └── beaconing.py
├── tests/
│   └── tkinter
│       └── test-app.py
│
├── .gitignore
├── app.py
└── README.md
```

## Geradores

| Script | Simula | MITRE ATT&CK |
|---|---|---|
| `src/logsgenerator/beaconing/beaconing.py` | Beaconing C2: conexão de saída em intervalo regular | T1071 (Command and Control) |

## Uso

`app.py` é o ponto de entrada. Execute-o a partir da raiz do projeto
para abrir a interface tkinter:

```bash
python app.py
```

Escolha um gerador na lista, confira a descrição e um exemplo da linha
de log que ele produz, e então clique no botão de gerar para escrever o
arquivo de log daquele gerador.

Cada gerador escreve seu próprio arquivo de log, ao lado do script, no
formato documentado no próprio cabeçalho dele.

## Projetos relacionados

- [soc-lab](https://github.com/Kanetahk/soc-lab) - engenharia de detecção no Splunk, consome esses logs
- [splunk-alert-response-pipeline](https://github.com/Kanetahk/splunk-alert-response-pipeline) - o pipeline de automação que essas detecções alimentam.