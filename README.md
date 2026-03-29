# 📁 Python File Organizer

> **A automação que você precisava pra limpar sua pasta de Downloads em segundos.**

Cansado de ver sua pasta de Downloads virar um "buraco negro" de arquivos perdidos? Eu também. Por isso criei esse script simples em Python que faz a faxina pesada por você, separando tudo por categorias de forma automática.

---

## 🚀 O que ele faz?
O script varre a pasta escolhida, identifica o tipo de cada arquivo e o move para a subpasta correta:

* **📸 Imagens:** `.jpg`, `.png`, `.svg`, `.webp`...
* **📄 Documentos:** `.pdf`, `.docx`, `.xlsx`, `.txt`...
* **⚙️ Programas:** `.exe`, `.msi`, `.bat`
* **📦 Compactados:** `.zip`, `.rar`, `.7z`
* **🎬 Multimídia:** `.mp4`, `.mp3`, `.mov`
* **📂 Outros:** Qualquer extensão que não esteja na lista.

---

## 🛠️ Como usar na sua máquina

### 1. Zero dependências
Como o script usa apenas bibliotecas nativas do Python (`pathlib` e `shutil`), você **não precisa instalar nada via pip**. É só baixar e rodar.

### 2. Configurar o caminho
Abra o arquivo `organizador.py` e ajuste a variável `pasta_alvo` com o caminho da pasta que você quer limpar:

```python
# Exemplo para Windows:
pasta_alvo = Path(r"C:\Users\SeuUsuario\Downloads")
