import typer
from jumpscare.watcher import start_watcher

app = typer.Typer()

@app.command()
def start(path: str = "."):
    print(f"Watching directory: {path}")
    start_watcher(path)

if __name__ == "__main__":
    app()
