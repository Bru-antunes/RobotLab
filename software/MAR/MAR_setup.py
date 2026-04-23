import os
import zipfile
import sys
import subprocess
import platform
import urllib.request
import shutil

# =========================
# BASE PATHS
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
# MESSAGES (EN/PT)
# =========================

def msg(en, pt):
    return f"{en} / {pt}"

# =========================
# UTILITIES
# =========================

def run(cmd):
    print(msg(f"Running: {cmd}", f"Executando: {cmd}"))
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(msg("Command failed", "Comando falhou"))
        sys.exit()


def download(url, dest):
    print(msg(f"Downloading {url}", f"Baixando {url}"))
    urllib.request.urlretrieve(url, dest)
    print(msg("Download complete", "Download concluído"))


def extract_zip(zip_path, extract_to):
    print(msg(f"Extracting {zip_path}", f"Extraindo {zip_path}"))

    temp_dir = zip_path + "_temp"

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    os.makedirs(temp_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    # evita poluir tools com 4000 arquivos soltos
    for item in os.listdir(temp_dir):
        src = os.path.join(temp_dir, item)
        dst = os.path.join(extract_to, item)

        if os.path.exists(dst):
            shutil.rmtree(dst)

        shutil.move(src, dst)

    shutil.rmtree(temp_dir)

    print(msg("Extraction done", "Extração concluída"))


def add_to_path(path):
    if path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + path
        print(msg(f"Added to PATH: {path}", f"Adicionado ao PATH: {path}"))


def is_installed(binary):
    return shutil.which(binary) is not None


# =========================
# INSTALL CHECKS
# =========================

def check_tools():
    gcc_ok = is_installed("avr-gcc")
    dude_ok = is_installed("avrdude")

    print(msg(f"avr-gcc installed: {gcc_ok}", f"avr-gcc instalado: {gcc_ok}"))
    print(msg(f"avrdude installed: {dude_ok}", f"avrdude instalado: {dude_ok}"))

    return gcc_ok and dude_ok


# =========================
# WINDOWS SETUP
# =========================

def setup_windows():
    print(msg("Windows detected", "Windows detectado"))

    os.makedirs(LIBS_DIR, exist_ok=True)
    os.makedirs(TOOLS_DIR, exist_ok=True)

    gcc_zip = os.path.join(LIBS_DIR, "avr-gcc.zip")
    avrdude_zip = os.path.join(LIBS_DIR, "avrdude.zip")

    if not check_tools():

        if not os.path.exists(gcc_zip):
            download(AVR_GCC_URL, gcc_zip)

        if not os.path.exists(avrdude_zip):
            download(AVRDUDE_URL, avrdude_zip)

        extract_zip(gcc_zip, TOOLS_DIR)
        extract_zip(avrdude_zip, TOOLS_DIR)

    # add bin folders only
    for root, dirs, files in os.walk(TOOLS_DIR):
        if root.lower().endswith("bin"):
            add_to_path(root)

    print(msg("Windows setup complete", "Setup Windows concluído"))


# =========================
# LINUX SETUP
# =========================

def setup_linux():
    print(msg("Linux detected", "Linux detectado"))

    run("sudo apt-get update")
    run("sudo apt-get install -y avrdude gcc-avr avr-libc")

    print(msg("Linux setup complete", "Setup Linux concluído"))


# =========================
# VS CODE CONFIG (FIXED)
# =========================

def generate_vscode_properties():
    import json

    vscode_dir = os.path.join(BASE_DIR, ".vscode")
    os.makedirs(vscode_dir, exist_ok=True)

    config_path = os.path.join(vscode_dir, "c_cpp_properties.json")

    avr_include_paths = []

    for root, dirs, files in os.walk(TOOLS_DIR):
        if "avr" in root.lower() and "include" in root.lower():
            avr_include_paths.append(root)

    compiler_path = "avr-gcc"

    for root, dirs, files in os.walk(TOOLS_DIR):
        if root.lower().endswith("bin"):
            if any("avr-gcc" in f for f in files):
                compiler_path = os.path.join(root, "avr-gcc.exe")

    config = {
        "configurations": [
            {
                "name": "ATtiny13A",
                "includePath": [
                    "${workspaceFolder}/**",
                    *avr_include_paths
                ],
                "defines": [
                    "__AVR_ATtiny13A__",
                    "__AVR_ATtiny13__"
                ],
                "compilerPath": compiler_path,
                "intelliSenseMode": "gcc-x64",
                "cStandard": "c11"
            }
        ],
        "version": 4
    }

    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)

    print(msg("VS Code configured for ATtiny13A",
              "VS Code configurado para ATtiny13A"))


# =========================
# MAIN
# =========================

def main():
    print("\n===== AVR MULTI PLATFORM SETUP =====")

    if platform.system() == "Windows":
        setup_windows()

    elif platform.system() == "Linux":
        setup_linux()

    else:
        print(msg("Unsupported system", "Sistema não suportado"))
        sys.exit()

    generate_vscode_properties()

    print(msg("Setup completed!", "Configuração concluída!"))


if __name__ == "__main__":
    main()