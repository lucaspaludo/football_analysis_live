<div align="center">

<sub>[⬅ voltar para o índice do projeto](../../README.md)</sub>

# 👁️ Live 01 — Como a Máquina Enxerga

### Os conceitos de visão computacional e IA por trás do projeto — e a primeira detecção rodando.

[![Assistir à live](https://img.shields.io/badge/▶_Assistir_à_live-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/live/scwTUaPM91M)
[![Slides](https://img.shields.io/badge/📊_Slides_(21)-F2B23E?style=for-the-badge&logoColor=black)](https://claude.ai/code/artifact/822d837a-e11b-4ff8-bb28-c06ee126f1c4)

<a href="https://www.youtube.com/live/scwTUaPM91M">
  <img src="https://img.youtube.com/vi/scwTUaPM91M/maxresdefault.jpg" width="70%" alt="Capa da live Como a Máquina Enxerga">
</a>

</div>

---

## 📋 Índice

- [Por que isso importa](#-por-que-isso-importa)
- [Bloco 1 · A imagem](#️-bloco-1--a-imagem)
- [Bloco 2 · O modelo](#-bloco-2--o-modelo)
- [Bloco 3 · A máquina](#️-bloco-3--a-máquina)
- [Mão na massa: o que foi construído](#️-mão-na-massa-o-que-foi-construído)
- [Lendo o resultado: o que deu errado (de propósito)](#-lendo-o-resultado-o-que-deu-errado-de-propósito)
- [Glossário](#-glossário)
- [Para a próxima live](#️-para-a-próxima-live)

---

## 🎯 Por que isso importa

Hoje, distância percorrida e velocidade de pico vêm de **colete GPS e estádio equipado** — coisa de clube grande. A proposta da série é tirar os mesmos números de **um vídeo comum**, o mesmo que o clube já grava.

<div align="center">

| 📥 O que entra | 📤 O que sai |
|:---:|:---:|
| Uma câmera aberta, sem nada no atleta | **8.412 m** percorridos · **31,4 km/h** de pico |

</div>

### Seis usos que já existem hoje

| | Área | Aplicação |
|:---:|---|---|
| 🧠 | **Análise tática** | Onde o time realmente ocupa o campo — não onde o quadro tático diz que ocupa. |
| 🏃 | **Preparação física** | Distância, número de sprints e carga de cada atleta, jogo a jogo. |
| 🔎 | **Observação e scouting** | Avaliar um jogador de qualquer liga tendo apenas o vídeo da partida. |
| 📺 | **Transmissão** | Gráficos ao vivo: posse, velocidade do contra-ataque, mapa de calor. |
| ⚖️ | **Arbitragem** | Revisão de lance com posições medidas em metros, não estimadas no olho. |
| 🌱 | **Base e amador** | Dado de clube grande para quem não tem orçamento de colete GPS. |

### O mesmo motor, outro problema

O pipeline não é sobre futebol — futebol é só o domínio. **Troca-se o conjunto de exemplos e o caminho continua exatamente o mesmo:**

| | | |
|---|---|---|
| 🛒 **Varejo** — fluxo de pessoas, filas e tempo de permanência | 🚗 **Trânsito** — contagem e velocidade de veículos | 🏭 **Indústria** — inspeção na esteira e alerta de área de risco |
| 📦 **Logística** — rastrear volumes e empilhadeiras | 🌾 **Agro** — contagem de animais e lavoura por drone | 🏐 **Esporte amador** — o mesmo relatório para o futsal de quinta |

### E o que isso deixa para quem constrói

> **Um portfólio que se explica sozinho** — trinta segundos de vídeo anotado convencem mais numa entrevista do que dez repositórios de tutorial.
>
> **Conceitos que servem em qualquer vaga** — detecção, rastreamento, agrupamento e geometria são a base de quase toda posição de visão computacional.
>
> **Problema real, não exercício** — câmera que se mexe, jogador escondido atrás de outro, bola que some. Nada aqui vem limpo.
>
> **Da ponta à ponta** — dados, treino, inferência e produto final. O ciclo inteiro, e não só a parte divertida.

---

## 🖼️ Bloco 1 · A imagem

<table><tr><td width="60" align="center"><h3>01</h3></td><td>

### Ele não vê um jogador. Vê uma tabela de números.

O computador **nunca** enxerga o jogo. Ele recebe uma grade de números. Cada célula dessa grade é um **pixel**, e o valor vai de **0 (preto) a 255 (branco)**.

Todo o resto da série é achar padrão nessa tabela.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>02</h3></td><td>

### Cor é a mesma tabela, três vezes

Uma imagem colorida são **três camadas** empilhadas — R, G e B — cada uma guardando de `0` a `255`. Juntas dão 16,7 milhões de cores. **É por elas que vamos separar os times** lá na frente.

> ⚠️ **Pegadinha clássica:** o OpenCV lê vídeo na ordem **BGR** (azul-verde-vermelho), não RGB. Trocar sem querer deixa o time vermelho azul.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>03</h3></td><td>

### Vídeo não existe — é uma pilha de fotos

Vídeo é o caderninho de desenhos folheado rápido. **Frame** é uma foto; **FPS** é quantas fotos passam por segundo.

```
frame 1 → frame 2 → frame 3 → frame 4 → frame 5 → ...
```

A 24 quadros por segundo, um jogo inteiro tem **129.600 fotos**.
**Tudo o que fizermos, faremos uma vez por foto.**

</td></tr></table>

---

## 🤖 Bloco 2 · O modelo

<table><tr><td width="60" align="center"><h3>01</h3></td><td>

### Um modelo é um arquivo que aprendeu

Não é um programa com regras escritas. É **um arquivo cheio de números**.

```
entrada: uma foto  →  [ MODELO ]  →  saída: o quê, onde, e o quanto ele confia
```

Ninguém escreveu `se tem duas pernas então é jogador`.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>02</h3></td><td>

### Alguém desenhou cada caixa à mão

O que quase ninguém conta: **um humano desenhou cada caixa**, uma por uma, em milhares de fotos — `jogador`, `juiz`, `bola`. Isso é o **dataset**, e cada caixa é um **rótulo**.

> 🔑 **Um modelo nunca é melhor que os exemplos que recebeu.** Sem juiz rotulado, não existe juiz reconhecido.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>03</h3></td><td>

### Estudar para a prova × fazer a prova

A confusão mais comum da área:

| | **Treino** | **Inferência** |
|---|---|---|
| **O que faz** | chuta → compara com o gabarito → corrige → repete | entra foto, sai resposta |
| **Quanto custa** | horas de placa de vídeo | milissegundos |
| **Frequência** | uma vez | o tempo todo |
| **Aprende?** | ✅ sim | ❌ **nada é aprendido aqui** |

</td></tr></table>

<table><tr><td width="60" align="center"><h3>04</h3></td><td>

### Do risco na tela até o jogador

As camadas da rede formam uma escada de abstração:

```
bordas  →  texturas  →  partes  →  jogador
```

As primeiras camadas enxergam coisas bobas. As últimas enxergam pessoas.
**Ninguém programou essa progressão — ela nasce sozinha do treino.**

</td></tr></table>

<table><tr><td width="60" align="center"><h3>05</h3></td><td>

### Três perguntas sobre a mesma foto

| Tarefa | Pergunta que responde | Saída |
|---|---|---|
| **Classificação** | *o quê?* | "é futebol" |
| **Detecção** ⬅ *é a nossa* | *o quê + onde?* | caixas com rótulo |
| **Segmentação** | *quais pixels?* | máscara pixel a pixel |

Qual delas responde **"quantos jogadores estão em campo"**? A do meio.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>06</h3></td><td>

### A caixa: dois cantos e um nome

Uma **bounding box** é definida por dois pontos — canto superior esquerdo e canto inferior direito — mais um rótulo e uma confiança:

```python
[x1, y1, x2, y2]   'person'   0.94
```

> ⚽ **Guarde este detalhe:** o **pé** é o que encosta no gramado. É pela base da caixa que vamos medir distância percorrida lá na frente.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>07</h3></td><td>

### Ele nunca tem certeza — tem um palpite medido

Cada detecção vem com uma **confiança** de 0 a 1. Define-se um **corte** (threshold) e o que estiver abaixo é ignorado.

```
0.96  ██████████  ✔
0.88  █████████   ✔
────────────────────  corte em 0.50
0.34  ███         ✘
0.12  █           ✘
```

**Subir o corte faz a bola sumir. Baixar cria bolas onde não há nenhuma.**
Não existe valor certo — escolher o erro que dói menos é trabalho nosso.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>08</h3></td><td>

### Cinco caixas, um jogador só

O modelo propõe **várias caixas quase iguais** para o mesmo jogador. A faxina — **NMS**, *Non-Maximum Suppression* — mantém a mais confiante e joga fora o resto.

É a diferença entre contar **1 jogador** e contar **5**.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>09</h3></td><td>

### Detectar não é acompanhar

> 💡 **O momento "aha" da aula.** O detector é **amnésico**: cada foto nasce do zero.

| Sem identidade | Com identidade |
|---|---|
| `pessoa` `pessoa` `pessoa` | `#7` `#12` `#3` |
| dá para **contar** pessoas | dá para dizer que **UMA delas correu** |

Manter o número fixo entre frames é **rastreamento (tracking)** — e é o tema da Live 02.

</td></tr></table>

<table><tr><td width="60" align="center"><h3>10</h3></td><td>

### Do generalista ao especialista

| Modelo de prateleira | Depois do ajuste fino |
|---|---|
| `pessoa` `pessoa` `pessoa` `?` | `time A` `time B` `juiz` `bola` |

**Fine-tuning** é mostrar algumas centenas de fotos do nosso mundo a um modelo que já sabe ver. É contratar quem já sabe a profissão em vez de ensinar do zero.

</td></tr></table>

---

## 🖥️ Bloco 3 · A máquina

### Poucos gênios em fila, ou um mutirão

| | **CPU** — processador | **GPU** — placa de vídeo |
|---|---|---|
| **Analogia** | poucos gênios, em fila | um mutirão de gente simples |
| **Trabalho** | uma bola de cada vez | todas ao mesmo tempo |
| **Ideal para** | lógica complexa e variada | a mesma conta simples, milhões de vezes |

> ✅ **Sem placa dedicada tudo funciona igual** — só é preciso paciência e vídeos mais curtos nos testes. **Ninguém precisa comprar nada para acompanhar a série.**

---

## 🛠️ Mão na massa: o que foi construído

### 1. O projeto, com `uv`

```bash
uv init football_analysis_live
cd football_analysis_live
uv add ultralytics opencv-python supervision pandas scikit-learn
```

O PyTorch com CUDA 11.8 vem de um índice próprio, declarado no [`pyproject.toml`](../../pyproject.toml):

```toml
[tool.uv.sources]
torch       = { index = "pytorch-cu118" }
torchvision = { index = "pytorch-cu118" }

[[tool.uv.index]]
name     = "pytorch-cu118"
url      = "https://download.pytorch.org/whl/cu118"
explicit = true
```

> 💡 **Por que `uv`?** Ele resolve, instala e trava as versões no `uv.lock` — quem clonar o repositório roda `uv sync` e tem **exatamente** o mesmo ambiente. Sem "na minha máquina funciona".

### 2. A primeira inferência

[`yolo_inference.py`](../../yolo_inference.py) — o arquivo inteiro da live:

```python
from ultralytics import YOLO

MODEL_PATH = 'yolo26x.pt'
VIDEO_PATH = 'input_videos/cobaia.mp4'

model = YOLO(MODEL_PATH)
results = model.predict(VIDEO_PATH, save=True)

print(model.names)                        # o dicionário de classes que o modelo conhece

for box in results[0].boxes:
    print(box.xyxy, box.conf, box.cls)    # onde · o quanto confia · o quê
```

| Linha | O conceito por trás |
|---|---|
| `YOLO(MODEL_PATH)` | Carrega **o arquivo que aprendeu** — ~119 MB de números. Baixa sozinho na primeira execução. |
| `model.predict(...)` | **Inferência.** Nada é aprendido aqui — entra foto, sai resposta. |
| `save=True` | Grava o vídeo anotado em `runs/detect/predict/`. |
| `model.names` | As **classes** que o modelo de prateleira conhece (COCO: `person`, `sports ball`, …). |
| `box.xyxy` | Os **dois cantos** da caixa. |
| `box.conf` | A **confiança** — o palpite medido. |
| `box.cls` | O **índice da classe** detectada. |

### 3. Rodando

```bash
uv run yolo_inference.py
```

<div align="center">

| | Entrada | Saída |
|---|:---:|:---:|
| **Arquivo** | `input_videos/cobaia.mp4` | `runs/detect/predict/cobaia.avi` |
| **Conteúdo** | 30 s · 1920×1080 · 25 fps · 750 frames | os mesmos 750 frames, agora anotados |
| **Tamanho** | ~20 MB | ~128 MB |

</div>

> 750 frames em 30 segundos de vídeo. Um jogo inteiro seriam **129.600**.

---

## 🔬 Lendo o resultado: o que deu errado (de propósito)

<div align="center">
  <img src="../assets/frame-depois.jpg" width="90%" alt="Frame com as detecções do modelo de prateleira">
</div>

Este único frame contém **quatro problemas** — e cada um vira uma live:

| 🔴 O que está errado | Por quê | Onde se resolve |
|---|---|---|
| **Todo mundo é `person`** — jogador, juiz, técnico, gandula e torcedor no fundo | O modelo de prateleira só conhece as classes do COCO. Ele nunca viu um "juiz". | **Fine-tuning** com dataset de futebol |
| **`sports ball 0.33`** — a bola mal passa do corte | Objeto pequeno, rápido e borrado. Subir o corte a faz sumir; baixar cria bola fantasma na torcida. | Modelo especialista + **interpolação** da trajetória |
| **Caixas sobrepostas e rótulos repetidos** | Detecções concorrentes no mesmo alvo, num NMS que não foi calibrado para aglomeração. | Ajuste de **NMS** e do corte de confiança |
| **Ninguém tem número** | O detector é amnésico: cada frame nasce do zero. Dá para contar, não para medir corrida. | **Rastreamento** (Live 02) |

> [!TIP]
> Esse é o valor de começar pelo modelo de prateleira: **o erro dele é o mapa do que falta construir.**

---

## 📖 Glossário

| Termo | Em uma frase |
|---|---|
| **Pixel** | A menor célula da imagem. Um número de 0 a 255 por canal de cor. |
| **Canal (R/G/B)** | Uma das três tabelas que, somadas, formam a cor. O OpenCV usa a ordem **BGR**. |
| **Frame** | Uma foto isolada do vídeo. |
| **FPS** | Quantos frames passam por segundo. |
| **Dataset** | O conjunto de fotos de exemplo, com as caixas desenhadas à mão. |
| **Rótulo (label)** | O nome da coisa dentro da caixa: `jogador`, `juiz`, `bola`. |
| **Treino** | Chutar, comparar com o gabarito, corrigir, repetir. Horas de GPU, uma vez. |
| **Inferência** | Usar o modelo já treinado. Milissegundos, o tempo todo, sem aprender nada. |
| **Bounding box** | Dois cantos `[x1, y1, x2, y2]` que cercam o objeto. |
| **Confiança** | Probabilidade de 0 a 1 de que a detecção está certa. |
| **Threshold (corte)** | O valor mínimo de confiança aceito. Abaixo dele, ignora. |
| **NMS** | A faxina que apaga caixas duplicadas e mantém a mais confiante. |
| **Classificação** | Responde *o quê*. |
| **Detecção** | Responde *o quê + onde*. É a nossa tarefa. |
| **Segmentação** | Responde *quais pixels exatamente*. |
| **Rastreamento (tracking)** | Manter o mesmo número no mesmo jogador ao longo dos frames. |
| **Fine-tuning** | Especializar um modelo pronto com exemplos do nosso domínio. |
| **CPU × GPU** | Poucos gênios em fila × um mutirão fazendo a mesma conta simples. |

---

## ⏭️ Para a próxima live

O caminho completo, do pixel até o número na tela:

<div align="center">

`Pixel` ➜ `Frame` ➜ `Modelo` ➜ `Caixa` ➜ **`Identidade`** ➜ `Métrica`

<sub>a matéria-prima · uma foto do jogo · o que aprendeu · o quê e onde · **sempre o mesmo** · km/h e metros</sub>

</div>

Fechamos a Live 01 na quarta etapa. **A Live 02 ataca a quinta:** dar um número fixo a cada jogador e mantê-lo — porque sem identidade dá para contar pessoas, mas nunca dizer que *uma delas* correu 8.412 metros.

<div align="center">
<br>

[![Assistir à live](https://img.shields.io/badge/▶_Assistir_à_Live_01-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/live/scwTUaPM91M)
[![Slides](https://img.shields.io/badge/📊_Ver_os_slides-F2B23E?style=for-the-badge&logoColor=black)](https://claude.ai/code/artifact/822d837a-e11b-4ff8-bb28-c06ee126f1c4)

<sub>[⬅ voltar para o índice do projeto](../../README.md)</sub>

</div>
