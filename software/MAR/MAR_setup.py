import os
import json
import shutil
import sys
import subprocess
import platform
import urllib.request
import zipfile
from pathlib import Path

# =========================
# URLs
# =========================
AVR_GCC_URL = "https://ww1.microchip.com/downloads/aemDocuments/documents/DEV/ProductDocuments/SoftwareTools/avr8-gnu-toolchain-4.0.0.52-win32.any.x86_64.zip"
AVRDUDE_URL = "https://github.com/avrdudes/avrdude/releases/download/v8.1/avrdude-v8.1-windows-x64.zip"

INSTALL_AVR_DIR = r"C:\avr"
INSTALL_AVRDUDE_DIR = r"C:\avrdude"

# =========================
# OS DETECTION
# =========================

def is_windows():
    return platform.system().lower().startswith("win")


def is_linux():
    return platform.system().lower().startswith("linux")

# =========================
# SAFE SUBPROCESS
# =========================

def safe_run(cmd):
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT, timeout=3).strip()
    except:
        return ""

# =========================
# PYTHON DEPENDENCY CHECK
# =========================

def ensure_pyserial():
    try:
        import serial
        version = getattr(serial, "__version__", None)
        if version == "3.5":
            print("pyserial 3.5 already installed")
            return
        else:
            print(f"pyserial version found: {version}, enforcing 3.5")
    except ImportError:
        print("pyserial not found")

    subprocess.run([sys.executable, "-m", "pip", "install", "pyserial==3.5"])
    print("pyserial==3.5 installed")

# =========================
# TOOL DETECTION
# =========================

def has_avr_gcc():
    return shutil.which("avr-gcc") is not None


def has_avrdude():
    return shutil.which("avrdude") is not None

# =========================
# DOWNLOAD & EXTRACT
# =========================

def download_zip(url, out_path):
    print(f"Downloading {url}")
    urllib.request.urlretrieve(url, out_path)
    print("Download complete")


def extract_zip(zip_path, dest):
    print(f"Extracting {zip_path} -> {dest}")
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(dest)
    print("Extract complete")

# =========================
# WINDOWS INSTALL
# =========================

def install_windows_tools():
    os.makedirs(INSTALL_AVR_DIR, exist_ok=True)
    os.makedirs(INSTALL_AVRDUDE_DIR, exist_ok=True)

    avr_zip = os.path.join(INSTALL_AVR_DIR, "avr.zip")
    avrdude_zip = os.path.join(INSTALL_AVRDUDE_DIR, "avrdude.zip")

    if not has_avr_gcc():
        download_zip(AVR_GCC_URL, avr_zip)
        extract_zip(avr_zip, INSTALL_AVR_DIR)

    if not has_avrdude():
        download_zip(AVRDUDE_URL, avrdude_zip)
        extract_zip(avrdude_zip, INSTALL_AVRDUDE_DIR)

    add_to_path_windows(INSTALL_AVR_DIR + "\\bin")
    add_to_path_windows(INSTALL_AVRDUDE_DIR)

# =========================
# PATH WINDOWS
# =========================

def add_to_path_windows(new_path):
    try:
        current = os.environ.get("PATH", "")
        if new_path not in current:
            subprocess.run(f'setx PATH "%PATH%;{new_path}"', shell=True)
            print(f"Added to PATH: {new_path}")
    except Exception as e:
        print("Failed to update PATH:", e)

# =========================
# LINUX INSTALL
# =========================

def install_linux_tools():
    print("Installing AVR tools via apt...")
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "-y", "avr-gcc", "avr-libc", "avrdude"])

    bashrc = os.path.expanduser("~/.bashrc")
    path_line = 'export PATH=$PATH:/usr/bin'

    with open(bashrc, "a") as f:
        f.write("\n# AVR tools\n")
        f.write(path_line + "\n")

# =========================
# MAIN INSTALLER
# =========================

def ensure_tools():
    if is_windows():
        install_windows_tools()
    elif is_linux():
        install_linux_tools()
    else:
        print("Unsupported OS")

# =========================
# ORIGINAL FUNCTIONS (unchanged core)
# =========================

WORKSPACE = os.getcwd()
CONFIG_DIR = os.path.join(WORKSPACE, ".vscode")
COMPILE_DB = os.path.join(CONFIG_DIR, "compile_commands.json")
VSCODE_CONFIG = os.path.join(CONFIG_DIR, "c_cpp_properties.json")


def find_avr_gcc():
    gcc = shutil.which("avr-gcc")
    if gcc:
        return gcc
    raise Exception("avr-gcc not found")


def find_avr_include(gcc):
    sysroot = safe_run([gcc, "-print-sysroot"])
    if sysroot:
        candidate = os.path.join(sysroot, "avr", "include")
        if os.path.exists(os.path.join(candidate, "avr", "io.h")):
            return candidate
    return ""


def find_sources():
    sources = []
    for root, _, files in os.walk(WORKSPACE):
        if ".vscode" in root:
            continue
        for f in files:
            if f.endswith(".c"):
                sources.append(os.path.join(root, f))
    return sources


def generate_compile_commands():
    gcc = find_avr_gcc()
    include_path = find_avr_include(gcc)

    os.makedirs(CONFIG_DIR, exist_ok=True)
    data = []

    for src in find_sources():
        cmd = f'"{gcc}" -mmcu=attiny13a '
        if include_path:
            cmd += f'-I"{include_path}" '
        cmd += f'-c "{src}" -o "{src}.o"'

        data.append({
            "directory": WORKSPACE,
            "command": cmd,
            "file": src
        })

    with open(COMPILE_DB, "w") as f:
        json.dump(data, f, indent=4)

    print("compile_commands.json generated")


def write_vscode_config():
    gcc = find_avr_gcc()
    include_path = find_avr_include(gcc)

    config = {
        "version": 4,
        "configurations": [{
            "name": "AVR",
            "compilerPath": gcc,
            "compileCommands": "${workspaceFolder}/.vscode/compile_commands.json",
            "includePath": [include_path, "${workspaceFolder}/**"] if include_path else ["${workspaceFolder}/**"],
            "browse": {"path": [include_path] if include_path else []},
            "defines": ["__AVR_ATtiny13A__"],
            "intelliSenseMode": "gcc-x64",
            "cStandard": "c11"
        }]
    }

    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(VSCODE_CONFIG, "w") as f:
        json.dump(config, f, indent=4)

# =========================
# MAIN
# =========================

def main():
    print("=== AVR AUTO SETUP ===")

    ensure_pyserial()
    ensure_tools()

    generate_compile_commands()
    write_vscode_config()

    print("DONE ✔")


if __name__ == "__main__":
    main()
