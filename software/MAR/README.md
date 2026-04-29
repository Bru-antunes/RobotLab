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
---

## 📁 Project Structure

```
MAR/
├── MAR_setup.py
├── MAR_programmer.py
├── MAR.c
├── libs/
└── README.md
```

---

## ⚙️ Requirements

* Python 3
* Windows or Linux

---

# 🚀 SETUP

## 🔹 Automatic Setup (Recommended)

Run:

```bash
python MAR_setup.py
```

### What this script does:

1. Installs Python dependencies (`pyserial`)
2. Detects operating system
3. On Windows:

   * Installs `avr-gcc` and `avrdude`
   * Places them inside `tools/`
   * Configures PATH dynamically
4. On Linux:

   * Runs:

     ```bash
     sudo apt-get update
     sudo apt-get install avrdude gcc-avr
     ```
5. Prepares the environment for compilation and upload

---

## 🔹 Manual Setup (Step-by-step)

### 🪟 Windows

1. Install Python 3

2. Install Python dependencies:

   ```bash
   pip install -r libs/requirements.txt
   ```

3. Extract toolchains:

   * Extract `avr8-gnu-toolchain-...zip` into `tools/`
   * Extract `avrdude-...zip` into `tools/`

4. Locate folders:

   * `tools/.../bin` (avr-gcc)
   * `tools/.../bin` (avrdude)

5. Add both paths to system PATH:

   * Open Environment Variables
   * Add paths manually

---

### 🐧 Linux

1. Update system:

   ```bash
   sudo apt-get update
   ```

2. Install AVR tools:

   ```bash
   sudo apt-get install avrdude gcc-avr 
   ```

3. Install Python dependencies:

   ```bash
   pip install -r libs/requirements.txt
   ```

---

# ▶️ PROGRAMMING

## 🔹 Automatic (Recommended)

Run:

```bash
python MAR_programmer.py
```

### This script automatically:

1. Detects serial port (COM)
2. Tests communication with ATTINY13A
3. Sets fuse bits:

   ```bash
   avrdude -U lfuse:w:0x7A:m
   ```
4. Compiles firmware:

   ```bash
   avr-gcc -mmcu=attiny13 -Os -DF_CPU=9600000UL -o MAR.elf MAR.c
   ```
5. Generates HEX:

   ```bash
   avr-objcopy -O ihex MAR.elf MAR.hex
   ```
6. Uploads firmware:

   ```bash
   avrdude -c arduino -p t13 -P COMX -b 19200 -B 10 -U flash:w:MAR.hex
   ```

---

## 🔹 Manual Programming (Terminal)

1. Configure fuse:

```bash
avrdude -c arduino -p t13 -P COMX -b 19200 -U lfuse:w:0x7A:m
```

2. Compile:

```bash
avr-gcc -mmcu=attiny13 -Os -DF_CPU=9600000UL -o MAR.elf MAR.c
```

3. Generate HEX:

```bash
avr-objcopy -O ihex MAR.elf MAR.hex
```

4. Upload:

```bash
avrdude -c arduino -p t13 -P COMX -b 19200 -B 10 -U flash:w:MAR.hex
```

---

## 🔌 Programming Hardware Setup

For programming the ATTINY13A, it is **strongly recommended** to use an **EEPROM test clip (SOIC clip)**. This allows programming the microcontroller **directly on the board**, without the need for desoldering, making the process faster, safer, and more practical.

In this project, an **Arduino Uno configured as ISP (In-System Programmer)** was used to perform the programming.

---

### 📷 ATTINY13A Pinout

<p align="center">
  <img src="../../docs/images/MAR/attiny13a_pinout.png" width="400">
</p>

---

### 🔗 Wiring (Arduino ISP → ATTINY13A)

The connection can be made using jumper wires as follows:

```
Arduino ____________ ATtiny13(A)

5V      ----------------> Pin 8
GND     ----------------> Pin 4
Pin 13  ----------------> Pin 7
Pin 12  ----------------> Pin 6
Pin 11  ----------------> Pin 5
Pin 10  ----------------> Pin 1
```

---

### ⚠️ Important Notes

* Ensure the Arduino is loaded with the **ArduinoISP** sketch before use
* Double-check all connections before powering the system
* Poor contact (especially with clips) may cause programming failure
* Designed for ATTINY13A
* Requires ISP programmer (Arduino as ISP supported)

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

Com base nesse trabalho, o presente projeto introduz adaptações focadas em **modularidade, facilidade de uso e simplificação de hardware**, visando criar uma solução portátil e facilmente replicável.

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

---


