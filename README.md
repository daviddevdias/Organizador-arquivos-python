# 📁 Organizador Automático de Downloads

Script em Python pra acabar com a bagunça da pasta de Downloads. 

Ele lê todos os arquivos soltos na pasta, checa a extensão de cada um e joga automaticamente pras subpastas certas (Imagens, Documentos, Programas, etc.). 

Fiz isso porque minha pasta de Downloads tava virando um buraco negro de arquivos perdidos.

---

## ⚙️ Como funciona
O script usa as bibliotecas nativas `pathlib` e `shutil` do Python. Você não precisa instalar nada de fora (nenhum `pip install` é necessário).

Ele já vem configurado pra organizar essas extensões:
* **Imagens:** `.jpg`, `.png`, `.svg`, etc.
* **Documentos:** `.pdf`, `.docx`, `.xlsx`, etc.
* **Programas:** `.exe`, `.msi`
* **Compactados:** `.zip`, `.rar`, `.7z`
* **Vídeos e Áudios:** `.mp4`, `.mp3`, etc.
* *Qualquer outra extensão:* Vai para uma pasta "Outros".

---

## 🛠️ Como usar na sua máquina

### 1. Ajuste o caminho da pasta
Abre o script `.py` no seu editor e altera a variável `pasta_alvo` na linha 6 para o caminho da sua pasta de Downloads. 

Por exemplo:
```python
pasta_alvo = Path(r"C:\Users\SeuUsuario\Downloads")