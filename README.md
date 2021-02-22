# Batch raster mosaic

Script to create a raster mosaic considering files inside of a specific folder.

## Como desenvolver?
- Clone o repositório.
- Crie um virtualenv com Python 3.7
- Ative o virtualenv.
- Instale as dependências.

## Códigos
```
git clone https://github.com/newmarwegner/batchrastermosaic.git
cd batchrastermosaic
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py bits(8 or 16) path_of_folder/
```