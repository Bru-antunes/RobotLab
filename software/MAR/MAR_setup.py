import os
import json
import shutil

# =========================
# FIND PROJECT ROOT
# =========================

def find_project_root():
    current = os.getcwd()

    while True:
        if os.path.exists(os.path.join(current, ".git")):
            return current

        parent = os.path.dirname(current)
        if parent == current:
            break

        current = parent

    return os.getcwd()


WORKSPACE_ROOT = find_project_root()

PROJECT_DIR = os.path.join(WORKSPACE_ROOT, "software", "MAR")
CONFIG_DIR = os.path.join(WORKSPACE_ROOT, ".vscode")

COMPILE_DB = os.path.join(CONFIG_DIR, "compile_commands.json")
VSCODE_CONFIG = os.path.join(CONFIG_DIR, "c_cpp_properties.json")


# =========================
# FIND AVR-GCC
# =========================

def find_avr_gcc():
    path = shutil.which("avr-gcc")
    if path:
        return path

    possible = [
        r"C:\avr\bin\avr-gcc.exe",
        r"C:\avr\avr\bin\avr-gcc.exe"
    ]

    for p in possible:
        if os.path.exists(p):
            return p

    raise Exception("avr-gcc not found")


# =========================
# FIND AVR INCLUDE (FIX REAL)
# =========================

def find_avr_include():
    candidates = [
        r"C:\avr\avr\include",
        r"C:\avr\include"
    ]

    for c in candidates:
        if os.path.exists(c):
            return c

    return ""


# =========================
# COMPILE COMMANDS
# =========================

def generate_compile_commands():
    gcc = find_avr_gcc()
    avr_include = find_avr_include()

    sources = []

    for root, _, files in os.walk(PROJECT_DIR):
        for f in files:
            if f.endswith(".c"):
                sources.append(os.path.join(root, f))

    data = []

    for src in sources:
        cmd = f'"{gcc}" -mmcu=attiny13a'

        if avr_include:
            cmd += f' -I"{avr_include}"'

        cmd += f' -c "{src}" -o "{src}.o"'

        data.append({
            "directory": PROJECT_DIR,
            "command": cmd,
            "file": src
        })

    os.makedirs(CONFIG_DIR, exist_ok=True)

    with open(COMPILE_DB, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("✔ compile_commands.json gerado")


# =========================
# VS CODE CONFIG (FIX REAL)
# =========================

def write_vscode_config():
    gcc = find_avr_gcc()
    avr_include = find_avr_include()

    os.makedirs(CONFIG_DIR, exist_ok=True)

    config = {
        "version": 4,
        "configurations": [
            {
                "name": "AVR",

                # 🔥 essencial (corrige 80% dos erros)
                "compilerPath": gcc,

                # 🔥 usa compile_commands
                "compileCommands": "${workspaceFolder}/.vscode/compile_commands.json",

                # 🔥 include global do AVR
                "includePath": [
                    "${workspaceFolder}/**",
                    avr_include
                ] if avr_include else [
                    "${workspaceFolder}/**"
                ],

                # 🔥 ajuda o IntelliSense a resolver headers
                "browse": {
                    "path": [
                        avr_include
                    ] if avr_include else []
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

    print("✔ VS Code configurado corretamente")


# =========================
# MAIN
# =========================

def main():
    print("=== AVR SETUP FINAL PRO FIX ===")
    print(f"ROOT: {WORKSPACE_ROOT}")
    print(f"PROJECT: {PROJECT_DIR}")
    print(f"CONFIG: {CONFIG_DIR}")

    generate_compile_commands()
    write_vscode_config()

    print("DONE ✔")


if __name__ == "__main__":
    main()