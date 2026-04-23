import os
import zipfile
import sys
import subprocess
import platform
import urllib.request

# =========================
# PATHS
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LIBS_DIR = os.path.join(BASE_DIR, "libs")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
REQUIREMENTS_FILE = os.path.join(LIBS_DIR, "requirements.txt")

# =========================
# DOWNLOAD LINKS
# =========================

AVR_GCC_URL = "https://ww1.microchip.com/downloads/aemDocuments/documents/DEV/ProductDocuments/SoftwareTools/avr8-gnu-toolchain-4.0.0.52-win32.any.x86_64.zip"
AVRDUDE_URL = "https://github.com/avrdudes/avrdude/releases/download/v8.1/avrdude-v8.1-windows-x64.zip"

# =========================
# UTILS
# =========================

def run(cmd):
    print(f"\n🔧 {cmd}")
    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        print("❌ Command failed / Comando falhou")
        sys.exit()


def download(url, dest):
    print(f"\n🌐 Downloading / Baixando:\n{url}")

    try:
        urllib.request.urlretrieve(url, dest)
        print("✅ Download completed / Download concluído")
    except Exception as e:
        print("❌ Download failed / Falha no download")
        print(e)
        sys.exit()


def extract(zip_path, destination):
    print(f"\n📦 Extracting / Extraindo: {zip_path}")

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destination)
    except Exception as e:
        print("❌ Extraction failed / Falha na extração")
        print(e)
        sys.exit()

    print("✅ Extraction completed / Extração concluída.")


def install_python_deps():
    print("\n🐍 Installing Python dependencies / Instalando dependências Python...")

    if not os.path.exists(REQUIREMENTS_FILE):
        print("❌ requirements.txt not found / requirements.txt não encontrado")
        sys.exit()

    run(f"{sys.executable} -m pip install -r \"{REQUIREMENTS_FILE}\"")

    print("✅ Python dependencies installed / Dependências Python instaladas.")


def add_to_path(path):
    print(f"➕ Adding to PATH / Adicionando ao PATH: {path}")
    os.environ["PATH"] += os.pathsep + path


# =========================
# WINDOWS SETUP
# =========================

def setup_windows():
    print("\n🪟 Windows detected / Windows detectado")

    os.makedirs(LIBS_DIR, exist_ok=True)
    os.makedirs(TOOLS_DIR, exist_ok=True)

    gcc_zip = os.path.join(LIBS_DIR, "avr-gcc.zip")
    avrdude_zip = os.path.join(LIBS_DIR, "avrdude.zip")

    # DOWNLOAD AUTOMÁTICO
    if not os.path.exists(gcc_zip):
        download(AVR_GCC_URL, gcc_zip)
    else:
        print("✅ AVR-GCC already downloaded / Já baixado")

    if not os.path.exists(avrdude_zip):
        download(AVRDUDE_URL, avrdude_zip)
    else:
        print("✅ AVRDUDE already downloaded / Já baixado")

    # EXTRAÇÃO
    extract(gcc_zip, TOOLS_DIR)
    extract(avrdude_zip, TOOLS_DIR)

    # CONFIGURAR PATH
    for root, dirs, files in os.walk(TOOLS_DIR):
        if root.lower().endswith("bin"):
            add_to_path(root)

    print("\n✅ Windows setup complete / Setup Windows concluído")


# =========================
# LINUX SETUP
# =========================

def setup_linux():
    print("\n🐧 Linux detected / Linux detectado")
    print("⚠️ Requires sudo privileges / Necessário sudo")

    run("sudo apt-get update")
    run("sudo apt-get install -y avrdude gcc-avr avr-libc")

    print("\n✅ Linux setup complete / Setup Linux concluído")


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
    print("👉 You can now run the programmer script / Agora você pode rodar o programmer.")


if __name__ == "__main__":
    main()