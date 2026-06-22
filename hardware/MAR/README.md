# MAR – Remote Activation Module [EN]
Para a versão em Português, [clique aqui](#pt)

---

## 📚 Reference, Motivation and Adaptation

This project is based on:

> **Antunes et al. (2025)** – *Development of a Low-Cost Remote Activation System for Competitive Sumo Robots*
> Available at: https://www.sba.org.br/open_journal_systems/index.php/sbai/article/view/5371

The original work presents a low-cost remote activation system for sumo robots using infrared communication based on the SIRC protocol at 38 kHz. Its main motivation is to ensure reliable, standardized, and interference-resistant activation during competitions.

**When referring to this project, please cite the paper above.**

Based on this work, the present project introduces adaptations focused on **modularity, ease of use, and hardware simplification**, aiming to create a portable and easily replicable solution.

Main adaptations:

* Modular hardware design
* Migration to ATTINY13A (size and cost reduction)
* Firmware rewritten from ATMEGA328P
* Timer and interrupt reconfiguration
* Falling-edge-only signal processing
* Noise filtering via timing constraints
* Full automation via scripts

---

## 🔗 Project Links

- 💻 Software: [RobotLab/software/MAR](https://github.com/Bru-antunes/RobotLab/tree/main/software/MAR)  
- 🔧 Hardware: [RobotLab/hardware/MAR](https://github.com/Bru-antunes/RobotLab/tree/main/hardware/MAR)
- 📚 Documentation: [RobotLab/docs/MAR](https://github.com/Bru-antunes/RobotLab/tree/main/docs/MAR)
- 🔖 References: [RobotLab/docs/References](https://github.com/Bru-antunes/RobotLab/tree/main/docs/References)

---

## 📐 Board Overview

The MAR (Remote Activation Module) hardware was designed to be **compact, lightweight, and easy to integrate** into competitive robotics platforms.

**Board dimensions:**  

📏 **15 mm x 14 mm** 

**Component size standard:**  

📦 SMD **0603**

---

## 🖼️ Schematic

<p align="center">

  <img src="../../docs/images/MAR/schematic_MAR.png" width="800">

</p>

---

## 📷 PCB

<p align="center">

  <!-- INSERT PCB PHOTO HERE -->

  <img src="../../docs/images/MAR/pcb_MAR.png" width="600">

</p>

---

## 🔩 Bill of Materials (BOM)


| Reference | Value       | Description |
|-----------|------------|------------|
| R1        | 7.5 kΩ     | Pull-up resistor |
| R2        | 100 Ω      | TSOP auxiliary resistor |
| R3        | 220 Ω      | LED resistor |
| R4        | 220 Ω      | LED resistor |
| C1        | 100 nF     | Decoupling capacitor |
| C2        | 4.7 µF     | TSOP auxiliary capacitor |
| IC1       | ATTINY13A  | Microcontroller |
| TSOP      | TSOP4838   | Infrared receiver |
| LEDB      | Blue LED   | Status indicator |
| LEDR      | Red LED    | Status indicator |
| Pinhead   | 3 pins     | Power and signal connector |


---

## ⚙️ Circuit Description

### 🔹 TSOP4838

Infrared receiver module responsible for detecting **modulated IR signals at 38 kHz**.  

It includes internal filtering that rejects continuous light and environmental noise, ensuring reliable communication even in competitive environments.

---

### 🔹 ATTINY13A (IC1)

Microcontroller responsible for:

- Decoding the IR signal received from the TSOP  

- Interpreting the SIRC protocol  

- Controlling system outputs and status LEDs  

---

### 🔹 C1 – Decoupling Capacitor (100 nF)

Placed close to the microcontroller power pins.  

Its function is to:

- Filter high-frequency noise  

- Stabilize the supply voltage  

---

### 🔹 R1 – Pull-up Resistor (7.5 kΩ)

Connected to the RESET pin of the ATTINY13A.  

Ensures:

- Stable operation  

- Prevents unintended resets  

---

### 🔹 R2 and C2 – TSOP Auxiliary Network

These components follow the **datasheet recommendation** for the TSOP module.

They help:

- Improve noise immunity  

- Stabilize signal reception  

- Reduce false triggering  

---

### 🔹 R3 and R4 – LED Current Limiting

Resistors used to protect the LEDs by limiting current.

---

### 🔹 LEDB (Blue) and LEDR (Red)

Two programmable LEDs used for **visual feedback** of the system state:

- 🔵 Blue LED → activation / status indication   

- 🔴 Red LED → idle / standby / armed states 

These LEDs are essential for:

- Debugging  

- Competition readiness feedback  

---

### 🔹 Pinhead (3-pin header)

Provides connection for:

- Power (VCC)  

- Ground (GND)  

- Signal / output  

Designed for easy integration with robot systems.

---

## 🔌 Design Considerations

- Compact layout for small robots  

- Noise-resistant IR reception  

- Minimal component count  

- Easy soldering (0603 standard)  

- Modular integration via pin header  

---

## 🚀 Integration

The MAR hardware was designed to work seamlessly with the software tools:

- **MAR_setup** → environment configuration  

- **MAR_programmer** → firmware upload  

This ensures a **fast and reliable deployment pipeline** from hardware to operation.

---

# MAR – Módulo de Ativação Remota [PT]
<a name="pt"> </a>

---

## 📚 Referência, Motivação e Adaptação

Este projeto é baseado em:

> **Antunes et al. (2025)** – *Desenvolvimento de um Sistema de Ativação Remota de Baixo Custo para Robôs de Sumô Competitivos*  
> Disponível em: https://www.sba.org.br/open_journal_systems/index.php/sbai/article/view/5371

O trabalho original apresenta um sistema de ativação remota de baixo custo para robôs de sumô utilizando comunicação infravermelha baseada no protocolo SIRC a 38 kHz. Sua principal motivação é garantir uma ativação confiável, padronizada e resistente a interferências durante competições.

**Ao se referir a este projeto, por favor cite o artigo acima.**

Com base nesse trabalho, o presente projeto introduz adaptações focadas em **modularidade, facilidade de uso e simplificação de hardware**, com o objetivo de criar uma solução portátil e facilmente replicável.

Principais adaptações:

* Design de hardware modular  
* Migração para ATTINY13A (redução de tamanho e custo)  
* Firmware reescrito a partir do ATMEGA328P  
* Reconfiguração de timers e interrupções  
* Processamento apenas de borda de descida  
* Filtragem de ruído via restrições de tempo  
* Automação completa via scripts  

---

## 🔗 Links do Projeto

- 💻 Software: [RobotLab/software/MAR](https://github.com/Bru-antunes/RobotLab/tree/main/software/MAR)  
- 🔧 Hardware: [RobotLab/hardware/MAR](https://github.com/Bru-antunes/RobotLab/tree/main/hardware/MAR)  
- 📚 Documentação: [RobotLab/docs/MAR](https://github.com/Bru-antunes/RobotLab/tree/main/docs/MAR)
- 🔖 Referências: [RobotLab/docs/References](https://github.com/Bru-antunes/RobotLab/tree/main/docs/References)


---

## 📐 Visão Geral da Placa

O hardware do MAR (Módulo de Ativação Remota) foi projetado para ser **compacto, leve e de fácil integração** em plataformas de robótica competitiva.

**Dimensões da placa:**  

📏 **15 mm x 14 mm** 

**Padrão de componentes:**  

📦 SMD **0603**

---

## 🖼️ Esquemático

<p align="center">

  <img src="../../docs/images/MAR/schematic_MAR.png" width="800">

</p>

---

## 📷 PCB

<p align="center">

  <!-- INSERIR FOTO DO PCB AQUI -->

  <img src="../../docs/images/MAR/pcb_MAR.png" width="600">

</p>

---

## 🔩 Lista de Materiais (BOM)

| Referência | Valor       | Descrição |
|-----------|------------|------------|
| R1        | 7,5 kΩ     | Resistor de pull-up |
| R2        | 100 Ω      | Resistor auxiliar do TSOP |
| R3        | 220 Ω      | Resistor do LED |
| R4        | 220 Ω      | Resistor do LED |
| C1        | 100 nF     | Capacitor de desacoplamento |
| C2        | 4,7 µF     | Capacitor auxiliar do TSOP |
| IC1       | ATTINY13A  | Microcontrolador |
| TSOP      | TSOP4838   | Receptor infravermelho |
| LEDB      | LED azul   | Indicador de status |
| LEDR      | LED vermelho | Indicador de status |
| Pinhead   | 3 pinos    | Conector de alimentação e sinal |

---

## ⚙️ Descrição do Circuito

### 🔹 TSOP4838

Módulo receptor infravermelho responsável por detectar **sinais IR modulados a 38 kHz**.

Ele inclui filtragem interna que rejeita luz contínua e ruídos ambientais, garantindo comunicação confiável mesmo em ambientes competitivos.

---

### 🔹 ATTINY13A (IC1)

Microcontrolador responsável por:

- Decodificar o sinal infravermelho recebido pelo TSOP  
- Interpretar o protocolo SIRC  
- Controlar as saídas do sistema e os LEDs de status  

---

### 🔹 C1 – Capacitor de Desacoplamento (100 nF)

Posicionado próximo aos pinos de alimentação do microcontrolador.

Sua função é:

- Filtrar ruídos de alta frequência  
- Estabilizar a tensão de alimentação  

---

### 🔹 R1 – Resistor de Pull-up (7,5 kΩ)

Conectado ao pino RESET do ATTINY13A.

Garante:

- Operação estável do microcontrolador  
- Prevenção de resets indesejados  

---

### 🔹 R2 e C2 – Rede Auxiliar do TSOP

Esses componentes seguem a **recomendação do datasheet** do módulo TSOP.

Eles ajudam a:

- Melhorar imunidade a ruídos  
- Estabilizar a recepção do sinal  
- Reduzir falsos disparos  

---

### 🔹 R3 e R4 – Limitação de Corrente dos LEDs

Resistores utilizados para proteger os LEDs, limitando a corrente elétrica.

---

### 🔹 LEDB (Azul) e LEDR (Vermelho)

Dois LEDs programáveis usados para **feedback visual do estado do sistema**:

- 🔵 LED azul → ativação / indicação de estado 
- 🔴 LED vermelho → estado ocioso / standby / pronto 

Esses LEDs são essenciais para:

- Depuração  
- Feedback durante competições  

---

### 🔹 Pinhead (conector de 3 pinos)

Permite conexão de:

- Alimentação (VCC)  
- Terra (GND)  
- Sinal / saída  

Projetado para facilitar integração com sistemas robóticos.

---

## 🔌 Considerações de Projeto

- Layout compacto para robôs pequenos  
- Recepção IR resistente a ruído  
- Baixo número de componentes  
- Facilidade de soldagem (padrão 0603)  
- Integração modular via conector  

---

## 🚀 Integração

O hardware MAR foi projetado para funcionar perfeitamente com as ferramentas de software:

- **MAR_setup** → configuração do ambiente  
- **MAR_programmer** → gravação de firmware  

Isso garante um pipeline de implantação **rápido e confiável**, do hardware à operação.
