# MAR – Remote Activation Module [EN/PT]

---

## 📚 Reference, Motivation and Adaptation

This project is based on:

> **Antunes et al. (2025)** – *Development of a Low-Cost Remote Activation System for Competitive Sumo Robots*
> Available at: https://www.sba.org.br/open_journal_systems/index.php/sbai/article/view/5371

The original work presents a low-cost remote activation system for sumo robots using infrared communication based on the SIRC protocol at 38 kHz. Its main motivation is to ensure reliable, standardized, and interference-resistant activation during competitions.

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

* Software: **[INSERT SOFTWARE LINK HERE]**
* Hardware: **[INSERT HARDWARE LINK HERE]**

---

## 📁 Project Structure

```
MAR/
├── MAR_setup.py
├── MAR_programmer.py
├── MAR.c
├── libs/
├── tools/
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

   * Extracts `avr-gcc` and `avrdude` from `libs/`
   * Places them inside `tools/`
   * Configures PATH dynamically
4. On Linux:

   * Runs:

     ```bash
     sudo apt-get update
     sudo apt-get install avrdude gcc-avr avr-libc
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
   sudo apt-get install avrdude gcc-avr avr-libc
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
  <img src="images/attiny13a_pinout.png" width="400">
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

---

# MAR – Módulo de Ativação Remota [EN/PT]

---

## 📚 Referência, Motivação e Adaptação

Este projeto foi inspirado no artigo:

> **Antunes et al. (2025)** – *Development of a Low-Cost Remote Activation System for Competitive Sumo Robots*
> Disponível em: https://www.sba.org.br/open_journal_systems/index.php/sbai/article/view/5371

O artigo apresenta um sistema de ativação remota baseado em infravermelho utilizando o protocolo SIRC em 38 kHz, com foco em confiabilidade e padronização em competições.

Este projeto adapta a solução com foco em:

* Modularização
* Redução de custo
* Facilidade de integração
* Miniaturização (ATTINY13A)

Principais modificações:

* Reescrita do firmware
* Alteração de registradores
* Reconfiguração de timers
* Tratamento de interrupções
* Filtragem de ruído por tempo
* Automação completa via scripts

---

## 🔗 Links do Projeto

* Software: **[https://github.com/Bru-antunes/RobotLab/tree/main/software/MAR]**
* Hardware: **[INSIRA LINK DO HARDWARE]**

---

## 📁 Estrutura do Projeto

```
MAR/
├── MAR_setup.py
├── MAR_programmer.py
├── MAR.c
├── libs/
├── tools/
└── README.md
```

---

## ⚙️ Requisitos

* Python 3
* Windows ou Linux

---

# 🚀 SETUP

## 🔹 Setup Automático (Recomendado)

```bash
python MAR_setup.py
```

### O script realiza:

1. Instala dependências Python
2. Detecta o sistema operacional
3. Windows:

   * Extrai avr-gcc e avrdude
   * Configura PATH
4. Linux:

   * Instala via apt-get
5. Prepara ambiente completo

---

## 🔹 Setup Manual (Passo a passo)

### 🪟 Windows

1. Instale Python
2. Rode:

```bash
pip install -r libs/requirements.txt
```

3. Extraia os ZIPs para `tools/`
4. Adicione ao PATH:

   * pasta `bin` do avr-gcc
   * pasta `bin` do avrdude

---

### 🐧 Linux

```bash
sudo apt-get update
sudo apt-get install avrdude gcc-avr avr-libc
pip install -r libs/requirements.txt
```

---

# ▶️ PROGRAMAÇÃO

## 🔹 Automática

```bash
python MAR_programmer.py
```

O script realiza automaticamente:

* Detecção da COM
* Teste de comunicação
* Configuração de fuse
* Compilação
* Geração de HEX
* Upload

---

## 🔹 Manual (Terminal)

```bash
avrdude -c arduino -p t13 -P COMX -b 19200 -U lfuse:w:0x7A:m
avr-gcc -mmcu=attiny13 -Os -DF_CPU=9600000UL -o MAR.elf MAR.c
avr-objcopy -O ihex MAR.elf MAR.hex
avrdude -c arduino -p t13 -P COMX -b 19200 -B 10 -U flash:w:MAR.hex
```

---

## 🔌 Configuração de Programação

Para a programação do ATTINY13A, é **fortemente recomendado** o uso de uma **garra de programação de EEPROM (clip SOIC)**. Essa abordagem permite programar o microcontrolador **diretamente na placa**, sem a necessidade de dessoldagem, tornando o processo mais rápido, seguro e prático.

Neste projeto, foi utilizado um **Arduino Uno configurado como ISP (In-System Programmer)** para realizar a gravação do firmware.

---

### 📷 Pinagem do ATTINY13A

<p align="center">
  <img src="images/attiny13a_pinout.png" width="400">
</p>

---

### 🔗 Conexões (Arduino ISP → ATTINY13A)

A ligação pode ser feita com jumpers conforme abaixo:

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

### ⚠️ Observações Importantes

* Certifique-se de que o Arduino esteja rodando o código **ArduinoISP**
* Verifique todas as conexões antes de energizar
* Mau contato (principalmente na garra) pode impedir a gravação
* Projeto para ATTINY13A
* Necessário programador ISP

---
