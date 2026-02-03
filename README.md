# Vetografia-
Projeto de linguagem nativa de IA com Interface para humanos.

## Teste
Este repositório contém uma proposta inicial de interface para análises vetográficas,
incluindo métricas como:

- Bits ativos e padding.
- Entropia global e entropia local por janela.
- Distribuição por camadas e distância de Hamming.

Esta seção serve como ponto de partida para futuras descrições detalhadas e exemplos
visuais do projeto.

## Experimento Vetografia + HDC
O script `vetografia_hdc.py` reproduz o experimento de vetores semânticos com
operações de HDC para os conceitos "amor", "amizade" e "verdade". Ele gera
vetores com densidades distintas, combina-os por soma e aplica multiplicação
circular (XOR sobre projeções inteiras), imprimindo os 10 primeiros valores de
cada resultado.

### Como executar
```bash
python vetografia_hdc.py
```
