# merge-pdf-files
A simple tools to merge multiple pdf files

# Setup

1. Install all depandacies
```bash
  poetry install
  poetry shell
```

# Using
1. Put all files to merge at ``pdf-files`` folder. If you want to sort files, you can prefix each file name with priority level number.
for example:
  - 00-filename.pdf
  - 01-filename.pdf
  - 03-filename.pdf

2. Launch merging
  ```bash
    python start.py
  ```
    
