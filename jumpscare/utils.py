import subprocess

def open_file(command, kind):
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"Failed to open {kind}: {e}")