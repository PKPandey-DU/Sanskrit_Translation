import pandas as pd
from pathlib import Path

def read_csv(path: Path):
    return pd.read_csv(path)

def write_csv(df, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

def read_text(path: Path, encoding="utf-8"):
    return Path(path).read_text(encoding=encoding)

def write_text(text: str, path: Path, encoding="utf-8"):
    path.parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(text, encoding=encoding)
