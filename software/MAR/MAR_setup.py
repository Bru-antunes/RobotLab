import os
import zipfile
import sys
import subprocess
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LIBS_DIR = os.path.join(BASE_DIR, "libs")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
REQUIREMENTS_FILE = os.path.join(LIBS_DIR, "requirements.txt")


# =========================
# Utils
# =========================

def run(cmd):
    print(f"\n🔧 {cmd}")
    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        print("❌ Command failed / Comando falhou")
        sys.exit()


def extract(zip_path, destination):
    print(f"\n📦 Extracting / Extraindo: {zip_path}")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination)

    print("✅ Extraction completed / Extração concluída.")


def check_file(path):
    if not os.path.exists(path):
        print(f"❌ File not found / Arquivo não encontrado: {path}")
        sys.exit()


def install_python_deps():
    print("\n🐍 Installing Python dependencies / Instalando dependências Python...")

    if not os.path.exists(REQUIREMENTS_FILE):
        print("❌ requirements.txt not found / requirements.txt não encontrado")
        sys.exit()

    run(f"{sys.executable} -m pip install -r {REQUIREMENTS_FILE}")

    print("✅ Python dependencies installed / Dependências Python instaladas.")


def add_to_path(path):
    print(f"➕ Adding to PATH / Adicionando ao PATH: {path}")
    os.environ["PATH"] += os.pathsep + path


# =========================
# Windows Setup
# =========================

def setup_windows():
    print("\n🪟 Windows detected / Windows detectado")

    os.makedirs(TOOLS_DIR, exist_ok=True)

    gcc_zip = os.path.join(LIBS_DIR, "avr8-gnu-toolchain-4.0.0.52-win32.any.x86_64.zip")
    avrdude_zip = os.path.join(LIBS_DIR, "avrdude-v8.1-windows-x64.zip")

    check_file(gcc_zip)
    check_file(avrdude_zip)

    extract(gcc_zip, TOOLS_DIR)
    extract(avrdude_zip, TOOLS_DIR)

    # Add to PATH
    for root, dirs, files in os.walk(TOOLS_DIR):
        if "bin" in root.lower():
            add_to_path(root)

        if "avrdude" in root.lower() and root.endswith("bin"):
            add_to_path(root)

    print("✅ Windows setup complete / Setup Windows concluído")


# =========================
# Linux Setup
# =========================

def setup_linux():
    print("\n🐧 Linux detected / Linux detectado")

    print("\n⚠️ This requires sudo privileges / Necessário sudo")

    run("sudo apt-get update")
    run("sudo apt-get install -y avrdude gcc-avr avr-libc")

    print("✅ Linux setup complete / Setup Linux concluído")


# =========================
# MAIN
# =========================

def main():
    print("\n===== AVR MULTI-PLATFORM SETUP =====")
    print("===== CONFIGURAÇÃO MULTIPLATAFORMA AVR =====\n")

    # 1. Python deps
    install_python_deps()

    sistema = platform.system()

    if sistema == "Windows":
        setup_windows()

    elif sistema == "Linux":
        setup_linux()

    else:
        print(f"❌ Unsupported system / Sistema não suportado: {sistema}")
        sys.exit()

    print("\n🎉 Setup completed / Configuração concluída!")
    print("👉 You can now run the main script / Agora você pode rodar o script principal.")


if __name__ == "__main__":
    main()