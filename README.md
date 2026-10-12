# Organizador de arquivos com Python

Automação que organiza os arquivos de uma pasta em subpastas conforme a extensão. Usa somente a biblioteca padrão do Python.

## 📁 Categorias

- Imagens: .jpg, .jpeg, .png, .gif, .svg, .webp.
- Documentos: .pdf, .docx, .txt, .xlsx, .pptx, .csv.
- Programas: .exe, .msi, .bat.
- Compactados: .zip, .rar, .7z, .tar, .gz.
- Videos: .mp4, .mkv, .avi, .mov.
- Audios: .mp3, .wav, .ogg.
- Outros: Extensões não mapeadas.

## 🚀 Executar

Requisito: Python 3.

```bash
git clone https://github.com/daviddevdias/Organizador-arquivos-python.git
cd Organizador-arquivos-python
```

Em `organizador.py`, configure `pasta_alvo` com o caminho da pasta desejada:

```python
pasta_alvo = Path(r"C:\caminho\para\pasta-de-teste")
```

Execute a partir da raiz do repositório:

```bash
python organizador.py
```

No Windows, você também pode usar `py organizador.py`.

## Comportamento e limites

O script cria as categorias necessárias, move apenas os arquivos diretamente na pasta escolhida e mostra o total de arquivos movidos. Subpastas existentes não são percorridas.

**Teste primeiro em uma pasta com cópias:** a execução move arquivos de verdade. Não existe simulação ou desfazer. O código não trata colisões de nomes explicitamente; um arquivo existente no destino pode ser substituído ou provocar erro, conforme o sistema.

## 📌 Próximos passos

Receber o caminho por argumento, adicionar simulação, tratar nomes repetidos e testar a organização com arquivos temporários.
