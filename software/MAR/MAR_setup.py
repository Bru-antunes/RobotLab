import os
import json
import shutil
import sys
import subprocess

# =========================
# WORKSPACE DETECTION
# =========================

def get_workspace():
    ws = os.environ.get("VSCODE_WORKSPACE_FOLDER")
    if ws:
        return ws

    if len(sys.argv) > 1:
        return sys.argv[1]

    return os.getcwd()


WORKSPACE = get_workspace()

CONFIG_DIR = os.path.join(WORKSPACE, ".vscode")
COMPILE_DB = os.path.join(CONFIG_DIR, "compile_commands.json")
VSCODE_CONFIG = os.path.join(CONFIG_DIR, "c_cpp_properties.json")


# =========================
# SAFE SUBPROCESS
# =========================

def safe_run(cmd):
    try:
        return subprocess.check_output(
            cmd,
            text=True,
            stderr=subprocess.STDOUT,
            timeout=3
        ).strip()
    except:
        return ""


# =========================
# FIND TOOLCHAIN
# =========================

def find_avr_gcc():
    gcc = shutil.which("avr-gcc")
    if gcc:
        return gcc
    raise Exception("avr-gcc not found in PATH")


def find_avr_include(gcc):
    """
    Encontra AVR libc corretamente (avr/io.h)
    """

    # 1. sysroot (melhor caso)
    sysroot = safe_run([gcc, "-print-sysroot"])
    if sysroot:
        candidate = os.path.join(sysroot, "avr", "include")
        if os.path.exists(os.path.join(candidate, "avr", "io.h")):
            return candidate

    # 2. instalação padrão Windows
    fallback = r"C:\avr\avr\include"
    if os.path.exists(os.path.join(fallback, "avr", "io.h")):
        return fallback

    # 3. busca relativa ao gcc
    current = os.path.dirname(gcc)
    for _ in range(6):
        candidate = os.path.join(current, "avr", "include")
        if os.path.exists(os.path.join(candidate, "avr", "io.h")):
            return candidate
        current = os.path.dirname(current)

    return ""


# =========================
# SOURCE DISCOVERY
# =========================

def find_sources():
    sources = []

    for root, _, files in os.walk(WORKSPACE):
        if ".vscode" in root:
            continue

        for f in files:
            if f.endswith(".c"):
                sources.append(os.path.join(root, f))

    return sources


# =========================
# COMPILE COMMANDS
# =========================

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

    with open(COMPILE_DB, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("✔ compile_commands.json generated")


# =========================
# VS CODE CONFIG
# =========================

def write_vscode_config():
    os.makedirs(CONFIG_DIR, exist_ok=True)

    gcc = find_avr_gcc()
    include_path = find_avr_include(gcc)

    config = {
        "version": 4,
        "configurations": [
            {
                "name": "AVR",

                "compilerPath": gcc,

                "compileCommands": "${workspaceFolder}/.vscode/compile_commands.json",

                "includePath": [
                    include_path,
                    "${workspaceFolder}/**"
                ] if include_path else [
                    "${workspaceFolder}/**"
                ],

                "browse": {
                    "path": [include_path] if include_path else [],
                    "limitSymbolsToIncludedHeaders": True
                },

                "defines": [
                    "__AVR_ATtiny13A__"
                ],

                "intelliSenseMode": "gcc-x64",
                "cStandard": "c11"
            }
        ]
    }

    with open(VSCODE_CONFIG, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

    print("✔ c_cpp_properties.json generated")


# =========================
# MAIN
# =========================

def main():
    print("=== AVR SETUP FINAL ===")
    print(f"WORKSPACE: {WORKSPACE}")
    print(f"CONFIG: {CONFIG_DIR}")

    generate_compile_commands()
    write_vscode_config()

    print("DONE ✔")


if __name__ == "__main__":
    main()