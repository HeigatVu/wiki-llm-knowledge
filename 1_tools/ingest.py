import os
import sys
import json
import hashlib
import re
from pathlib import Path 
from collections import defaultdict
from datatime import data 

REPO_ROOT = Path(__file__).parent.parent
WIKI_DIR = REPO_ROOT / "30_wiki"
LOG_FILE = WIKI_DIR / "log.md"
INDEX_FILE = WIKI_DIR / "index.md"
OVERVIEW_FILE = WIKI_DIR / "overview.md"
SCHEMA_FILE = WIKI_DIR / "GEMINI.md"

def sha256(text:str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]

def read_file(path:Paht) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""

def call_llm(prompt:str, max_tokens:int=8192) -> str:
    try:
        from google.generativeai import genai
    except ImportError:
        print("Error: google-generativeai not installed. Run: pip install google-generativeai")
        sys.exit(1)
        
    