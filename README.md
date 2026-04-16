# Morning: ingest new notes you wrote
```
python run.py ingest raw/papers/my_notes/
```

# Check if anything is broken
```
python run.py lint
```


# Rebuild graph after new ingestions
```
python run.py graph
```

# Open Gemini CLI to explore and query interactively
```
cd /path/to/llm-wiki-agent
gemini
```