import os
import shutil
from pathlib import Path



pasta_alvo = Path(r"C:\Users\Dias\Downloads")



if not pasta_alvo.exists():
    print("Pasta não encontrada. Verifica o caminho aí.")
    exit()



categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Programas": [".exe", ".msi", ".bat"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audios": [".mp3", ".wav", ".ogg"]
}


movidos = 0

print(f"Organizando arquivos em: {pasta_alvo}...\n")

for arquivo in pasta_alvo.iterdir():
    if arquivo.is_file():
        ext = arquivo.suffix.lower()
        destino = None

        for cat, extensoes in categorias.items():
            if ext in extensoes:
                destino = pasta_alvo / cat
                break
        
        if not destino:
            destino = pasta_alvo / "Outros"

        destino.mkdir(exist_ok=True)
        
        try:
            shutil.move(str(arquivo), str(destino / arquivo.name))
            nome_cat = cat if destino.name != 'Outros' else 'Outros'
            print(f"[{nome_cat}] {arquivo.name}")
            movidos += 1
        except Exception as e:
            print(f"Erro ao mover {arquivo.name}: {e}")


if movidos == 0:
    print("Nenhum arquivo solto pra organizar.")
else:
    print(f"\nPronto! {movidos} arquivos movidos com sucesso.")