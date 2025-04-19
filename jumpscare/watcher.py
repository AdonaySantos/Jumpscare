import platform, subprocess, pkg_resources
from pathlib import Path
from typing import override
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from jumpscare.utils import open_file

class WatchFiles(FileSystemEventHandler):
    @override
    def on_modified(self, event: FileSystemEvent):
        if not event.is_directory and isinstance(event.src_path, str) and event.src_path.endswith((".py",)):
            print(f"[WATCHED] File changed: {event.src_path}")
            self.handle_change(event.src_path)
    
    def handle_change(self, filepath: str):
        result = subprocess.run(
            ["python", filepath],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("[SUCESS] se livrou dessa vez..")
        else:
             self.jumpscare()

    def jumpscare(self):
        system = platform.system()

        try:
            image_path: Path = Path(pkg_resources.resource_filename('jumpscare', "releases/jumpscare-image.jpg"))
            audio_path: Path = Path(pkg_resources.resource_filename('jumpscare', "releases/never.mp3"))

            match system:
                case "Windows":
                    open_file(["cmd", "/c", "start", image_path], "image")
                    open_file(["cmd", "/c", "start", audio_path], "audio")

                case "Linux":
                    open_file(["gio", "open", image_path], "image")
                    open_file(["gio", "open", audio_path], "audio")

                case _:
                    pass
        except Exception as e:
            print(f"Failed to trigger jumpscare: {e}")


def start_watcher(watch_path: str = "."):
    observer = Observer()
    handler = WatchFiles()
    _ = observer.schedule(handler, path=watch_path, recursive=True)
    observer.start()

    print("Watching for changes in .py files...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        print("Watcher stopped")

    observer.join()

if __name__ == "__main__":
    start_watcher()
