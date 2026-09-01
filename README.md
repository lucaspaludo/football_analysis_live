<div align="center">

# ⚽ Football Computer Vision Analysis

### Transformando um vídeo comum de futebol em dados de laboratório — ao vivo, do zero.

**Sem colete GPS. Sem sensor no atleta. Sem estádio equipado.**
Só o vídeo que o clube já grava.

<br>

[![Live no YouTube](https://img.shields.io/badge/▶_Assista_às_lives-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/live/scwTUaPM91M)
[![Slides](https://img.shields.io/badge/📊_Slides_da_aula-F2B23E?style=for-the-badge&logoColor=black)](https://claude.ai/code/artifact/822d837a-e11b-4ff8-bb28-c06ee126f1c4)

<br>

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-gerenciador-DE5FE9?style=flat-square&logo=astral&logoColor=white)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO26-0B2E4F?style=flat-square)
![PyTorch](https://img.shields.io/badge/PyTorch-cu118-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5.0-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/status-em_construção_ao_vivo-49B26B?style=flat-square)

</div>

---

## 🎯 O que é este projeto

Uma **série de lives** construindo, do zero e em público, um sistema de visão computacional que assiste a uma partida de futebol e devolve números:

<div align="center">

| O que entra | | O que sai |
|:---:|:---:|:---:|
| 🎥 **Um vídeo** | ➜ | 📏 **8.412 m** percorridos |
| Uma câmera aberta | ➜ | ⚡ **31,4 km/h** de pico |
| Nada no atleta | ➜ | 🗺️ Mapa de calor, posse, sprints |

</div>

O pipeline é **geral** — futebol é só o domínio. Troque o conjunto de exemplos e as mesmas etapas contam pessoas numa loja, carros numa avenida, peças numa esteira ou gado no pasto.

---

## 📺 As lives

> Cada live tem uma página própria com **o conteúdo destrinchado**, o código daquele dia e o que rodar para reproduzir.

<table>
<thead>
<tr>
<th width="60">#</th>
<th width="380">Tema</th>
<th>O que você sai sabendo</th>
<th width="130">Material</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><b>01</b></td>
<td>
  <a href="docs/lives/live-01-como-a-maquina-enxerga.md"><b>👁️ Como a Máquina Enxerga</b></a><br>
  <sub>Aula zero · conceitos + primeira detecção</sub>
</td>
<td>
  Pixel, frame, FPS, dataset, treino × inferência, bounding box, confiança, NMS, tracking, fine-tuning, CPU × GPU — e a <b>primeira inferência YOLO rodando</b>.
</td>
<td>
  <a href="https://www.youtube.com/live/scwTUaPM91M">▶ Vídeo</a><br>
  <a href="https://claude.ai/code/artifact/822d837a-e11b-4ff8-bb28-c06ee126f1c4">📊 Slides</a><br>
  <a href="docs/lives/live-01-como-a-maquina-enxerga.md">📄 Notas</a>
</td>
</tr>
</tbody>
</table>

<div align="center">

<img src="docs/assets/deteccao.gif" width="100%" alt="Detecção do YOLO rodando sobre a partida — resultado da Live 01">

<sub>▲ <b>O resultado da Live 01</b> — a primeira inferência rodando sobre <code>input_videos/cobaia.mp4</code></sub>

</div>

<table>
<tr>
<td width="50%" align="center"><b>Entrada</b> — <code>input_videos/cobaia.mp4</code></td>
<td width="50%" align="center"><b>Saída</b> — <code>runs/detect/predict/cobaia.avi</code></td>
</tr>
<tr>
<td><img src="docs/assets/frame-antes.jpg" alt="Frame original da partida"></td>
<td><img src="docs/assets/frame-depois.jpg" alt="Mesmo frame com as detecções do YOLO"></td>
</tr>
</table>

> [!NOTE]
> **Esse resultado ainda está errado de propósito** — e é justamente daí que sai o roteiro das próximas lives:
> todo mundo é `person` (falta ajuste fino), a bola aparece com `0.33` de confiança (falta calibrar o corte),
> há caixas duplicadas e ninguém tem um número fixo (falta rastreamento).
> A [página da Live 01](docs/lives/live-01-como-a-maquina-enxerga.md#-lendo-o-resultado-o-que-deu-errado-de-propósito) destrincha cada um desses erros.

---

## ⚡ Rodando em 4 comandos

<details open>
<summary><b>Pré-requisitos</b></summary>

- **Python 3.13** (fixado em [`.python-version`](.python-version))
- **[uv](https://docs.astral.sh/uv/)** — gerenciador de ambiente e dependências
- **GPU NVIDIA é opcional.** Sem placa dedicada tudo funciona igual — só é preciso paciência e vídeos mais curtos nos testes.

</details>

```bash
# 1. clone
git clone https://github.com/lucaspaludo/football_analysis_live.git
cd football_analysis_live

# 2. ambiente + dependências (uv resolve tudo pelo uv.lock)
uv sync

# 3. coloque um vídeo de partida em input_videos/cobaia.mp4
#    (30 s, 1920x1080, 25 fps é o formato usado nas lives)

# 4. primeira inferência — baixa o yolo26x.pt na primeira execução
uv run yolo_inference.py
```

O resultado sai anotado em **`runs/detect/predict/cobaia.avi`**.

---

## 🧰 Stack

| Ferramenta | Papel |
|---|---|
| **[uv](https://docs.astral.sh/uv/)** | Ambiente e dependências reprodutíveis via `uv.lock` |
| **[Ultralytics YOLO26](https://docs.ultralytics.com/)** | Detecção de objetos — jogadores, bola, juiz |
| **[PyTorch](https://pytorch.org/) (cu118)** | Motor de inferência, com aceleração CUDA |
| **[OpenCV](https://opencv.org/)** | Leitura, escrita e manipulação de frames |
| **[Supervision](https://supervision.roboflow.com/)** | Anotação, rastreamento e utilitários de CV |
| **[scikit-learn](https://scikit-learn.org/)** | Agrupamento de cores para separar os times |
| **[pandas](https://pandas.pydata.org/)** | Séries temporais das métricas por jogador |

---

<div align="center">

### 🤝 Acompanhe

As lives são abertas e o código nasce em tempo real, com erro, tentativa e refação incluídos.

[![YouTube](https://img.shields.io/badge/YouTube-assistir_ao_vivo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/live/scwTUaPM91M)

<sub>Feito por <b><a href="https://github.com/lucaspaludo">Lucas Paludo</a></b> · construído em público, uma live por vez.</sub>

</div>
