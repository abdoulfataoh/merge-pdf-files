# merge-pdf-files
A simple tools to merge multiple pdf files

## Setup

1. Install all depandacies
```bash
  poetry install
  poetry shell
```

## Help

![help](https://github.com/abdoulfataoh/pdfs-merger/blob/master/docs/help.png)

## Examples
1. Merge two pdfs file

```bash
  python main.py -f file_1.pdf file_2.pdf -o merge.pdf
```

2. Merge all pdfs files contains in document folder

```bash
  python main.py -f document/* -o merge.pdf
```

3. Merge all pdfs files contains in document folder sorted by name

```bash
  python main.py -s -f document/* -o merge.pdf
```

4. Merge all pdfs files contains in document folder sorted by name and show verbose

```bash
  python main.py -v -s -f document/* -o merge.pdf
```
 
