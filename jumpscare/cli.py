import typer
from jumpscare.watcher import WatchFiles

app = typer.Typer()

@app.command()
def start(path: str = "."):
    print(f"Watching directory: {path}")
    WatchFiles().start(path)

if __name__ == "__main__":
    app()
