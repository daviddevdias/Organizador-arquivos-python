# 📁 Organizador de Downloads

Fiz esse script pra resolver o problema da minha pasta de Downloads, que sempre virava uma bagunça. Ele varre a pasta, identifica o tipo do arquivo pela extensão e move cada um pra sua subpasta automática (Imagens, Docs, etc).

---

## 🛠️ O que ele faz
O script separa os arquivos nessas categorias:

* **Imagens:** .jpg, .png, .svg, .webp
* **Documentos:** .pdf, .docx, .xlsx, .txt
* **Programas:** .exe, .msi, .bat
* **Compactados:** .zip, .rar, .7z
* **Vídeos/Áudio:** .mp4, .mp3, .mov
* **Outros:** Tudo que não estiver mapeado acima vai pra uma pasta separada.

---

## 🚀 Como rodar

### 1. Sem instalação
O código usa apenas bibliotecas nativas do Python (`pathlib` e `shutil`). Não precisa dar `pip install` em nada.

### 2. Configuração
No arquivo `organizador.py`, altere o caminho da pasta que você quer organizar na variável `pasta_alvo`:

```python
# Só mudar o caminho aqui:
pasta_alvo = Path(r"C:\Users\Dias\Downloads")
