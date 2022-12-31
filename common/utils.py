from pathlib import Path


def create_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)
