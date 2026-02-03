from pathlib import Path
from typing import List, Tuple
from langchain_text_splitters import RecursiveCharacterTextSplitter

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_policies() -> Tuple[List[str], List[str]]:
    

    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Data folder not found at: {DATA_DIR}")
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,      
        chunk_overlap=80     
    )
    documents, sources = [], []

    for file in DATA_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8").strip()
        if text:
            chunks = splitter.split_text(text)
            for chunk in chunks:
                documents.append(text)
                sources.append(file.name)

    if not documents:
        raise ValueError("No policy documents found in data folder.")

    print(f"Loaded {len(documents)} policy files from {DATA_DIR}")
    return documents, sources
