import subprocess
from pathlib import Path

def open_file(command: list[str | Path], file_type: str):
    try:
        _ = subprocess.run(command)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Fail to open {file_type}. Return code: {e.returncode}")
    except FileNotFoundError:
        print(f"[ERRO] Command not found while trying to open {file_type}.")
    except Exception as e:
        print(f"[ERRO] Unexpected error while opening {file_type}: {e}")
