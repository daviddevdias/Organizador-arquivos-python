# Organizador de arquivos

Script que organiza os arquivos de uma pasta em categorias de acordo com a extensão.

## 📌 Funcionalidades

- Cria pastas para imagens, documentos, programas, compactados, vídeos e áudios.
- Move arquivos não classificados para Outros.
- Exibe o total de arquivos organizados.

## Tecnologias

Python 3, pathlib e shutil. Não exige pacotes externos.

## 🚀 Como executar

Configure `pasta_alvo` em `organizador.py` e execute:

```bash
git clone https://github.com/daviddevdias/Organizador-arquivos-python.git
cd Organizador-arquivos-python
python organizador.py
```

O script move os arquivos da pasta selecionada. Use primeiro uma pasta de teste com cópias e evite arquivos de mesmo nome no destino.
