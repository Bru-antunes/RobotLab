import subprocess
import serial.tools.list_ports
import sys
import os
import time

# =========================
# CONFIG
# =========================

ARDUINO_ISP_HEX = os.path.join("libs", "ArduinoISP.ino.hex")

# =========================
# Helper functions / Funções auxiliares
# =========================

def listar_coms():
    portas = list(serial.tools.list_ports.comports())
    return [p.device for p in portas]


def escolher_com():
    portas = listar_coms()

    if not portas:
        print("❌ No COM ports found / Nenhuma porta COM encontrada.")
        sys.exit()

    print("Available ports / Portas disponíveis:")
    for i, p in enumerate(portas):
        print(f"{i}: {p}")

    com_sugerida = portas[0]
    print(f"\n👉 Suggested port / Porta sugerida: {com_sugerida}")

    confirm = input("Is this correct? / Essa é a porta correta? (y/n): ").strip().lower()

    if confirm in ['y', 's']:
        return com_sugerida
    else:
        try:
            idx = int(input("Enter index / Digite o índice: "))
            return portas[idx]
        except:
            print("❌ Invalid input / Entrada inválida.")
            sys.exit()


def rodar_comando(cmd, erro_msg):
    print(f"\n🔧 Running / Executando: {cmd}")

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    saida = result.stdout + result.stderr

    if result.returncode != 0:
        print("❌ ERROR / ERRO:")
        print(saida)
        print(f"\n🚨 {erro_msg}")
        sys.exit()
    else:
        print("✅ OK")


def verificar_arquivo(nome):
    if not os.path.exists(nome):
        print(f"❌ File not found / Arquivo não encontrado: {nome}")
        sys.exit()


# =========================
# Check if Arduino is ISP
# =========================

def arduino_ja_e_isp(com):
    print("\n🔎 Checking if Arduino is already ISP / Verificando se Arduino já é ISP...")

    cmd = f"avrdude -c arduino -p t13 -P {com} -b 19200"

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    saida = (result.stdout + result.stderr).lower()

    if "device signature" in saida:
        print("✅ Arduino already running ArduinoISP / Arduino já está como ISP!")
        return True
    else:
        print("⚠️ Arduino is NOT ISP / Arduino NÃO está como ISP.")
        return False


# =========================
# Upload ArduinoISP
# =========================

def gravar_arduino_isp(com):
    print("\n⚙️ Uploading ArduinoISP / Gravando ArduinoISP...")

    verificar_arquivo(ARDUINO_ISP_HEX)

    # First attempt
    cmd = f"avrdude -c arduino -p m328p -P {com} -b 115200 -U flash:w:{ARDUINO_ISP_HEX}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print("⚠️ Failed at 115200, trying 57600 / Falha em 115200, tentando 57600...")

        cmd = f"avrdude -c arduino -p m328p -P {com} -b 57600 -U flash:w:{ARDUINO_ISP_HEX}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            print("❌ Error uploading ArduinoISP / Erro ao gravar ArduinoISP:")
            print(result.stdout + result.stderr)
            sys.exit()

    print("✅ ArduinoISP uploaded successfully / ArduinoISP gravado com sucesso!")

    time.sleep(2)


# =========================
# Test ATTINY
# =========================

def testar_attiny(com):
    print("\n🔎 Testing ATTINY communication / Testando comunicação com ATTINY...")

    cmd = f"avrdude -c arduino -p t13 -P {com} -b 19200"

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    saida = (result.stdout + result.stderr).lower()

    if "device signature" not in saida:
        print("❌ ATTINY not detected / ATTINY não identificado!")
        print("👉 Check / Verifique:")
        print("- Wiring / Conexões")
        print("- Clip contact / Contato da garra")
        print("- Power supply / Alimentação")
        print("- Arduino ISP setup")
        sys.exit()
    else:
        print("✅ ATTINY detected successfully / ATTINY detectado com sucesso!")


# =========================
# MAIN
# =========================

def main():

    print("\n===== MAR PROGRAMMER – ATTINY13A =====\n")

    verificar_arquivo("MAR.c")
    verificar_arquivo(ARDUINO_ISP_HEX)

    com = escolher_com()

    print("""
🔌 IMPORTANT / IMPORTANTE:
Connect ATTINY to Arduino ISP before continuing
Conecte o ATTINY ao Arduino antes de continuar
""")

    input("Press ENTER to continue / Pressione ENTER para continuar...")

    # Check ISP
    if not arduino_ja_e_isp(com):
        gravar_arduino_isp(com)
    else:
        print("👉 Skipping ArduinoISP upload / Pulando gravação do ArduinoISP.")

    # Test ATTINY
    testar_attiny(com)

    # Fuse
    rodar_comando(
        f"avrdude -c arduino -p t13 -P {com} -b 19200 -U lfuse:w:0x7A:m",
        "Fuse configuration error / Erro ao configurar fuse"
    )

    # Compile
    rodar_comando(
        "avr-gcc -mmcu=attiny13 -Os -DF_CPU=9600000UL -o MAR.elf MAR.c",
        "Compilation error / Erro na compilação"
    )

    # HEX
    rodar_comando(
        "avr-objcopy -O ihex MAR.elf MAR.hex",
        "HEX generation error / Erro ao gerar HEX"
    )

    # Upload
    rodar_comando(
        f"avrdude -c arduino -p t13 -P {com} -b 19200 -B 10 -U flash:w:MAR.hex",
        "Upload error / Erro ao gravar no ATTINY"
    )

    print("\n🎉 Done successfully / Processo finalizado com sucesso!\n")


if __name__ == "__main__":
    main()
