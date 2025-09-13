import os
import shutil
import datetime

# Data e hora atual
data_atual = datetime.datetime.now()

# Caminhos principais
pasta_origem = r"/home/valcann/backupsFrom"
pasta_destino = r"/home/valcann/backupsTo"
log_origem = r"/home/valcann/backupsFrom.log"
log_destino = r"/home/valcann/backupsTo.log"

# Abrindo os arquivos de log
with open(log_origem, "w", encoding="utf-8") as log_from, open(log_destino, "w", encoding="utf-8") as log_to:
    log_from.write("Relatório de arquivos em backupsFrom\n\n")
    log_to.write("Arquivos com data de criação menor ou igual a 3 dias\n\n")

    # Listando os arquivos na pasta de origem
    for nome_arquivo in os.listdir(pasta_origem):
        caminho_completo = os.path.join(pasta_origem, nome_arquivo)

        # Verifica se é um arquivo
        if os.path.isfile(caminho_completo):
            tamanho = os.path.getsize(caminho_completo) / 1024  # em KB
            data_criacao = datetime.datetime.fromtimestamp(os.path.getctime(caminho_completo))
            data_modificacao = datetime.datetime.fromtimestamp(os.path.getmtime(caminho_completo))
            dias_desde_criacao = (data_atual - data_criacao).days

            # Escreve no log de origem
            log_from.write(f"Arquivo: {nome_arquivo}\n")
            log_from.write(f"Tamanho: {tamanho:.2f} KB\n")
            log_from.write(f"Criado em: {data_criacao}\n")
            log_from.write(f"Modificado em: {data_modificacao}\n\n")

            if dias_desde_criacao > 3:
                os.remove(caminho_completo)
                print(f"Arquivo removido: {nome_arquivo} (Criado há {dias_desde_criacao} dias)")
            else:
                # Copia o arquivo para backupsTo
                caminho_destino = os.path.join(pasta_destino, nome_arquivo)
                shutil.copy2(caminho_completo, caminho_destino)

                # Escreve no log de destino
                log_to.write(f"Arquivo: {nome_arquivo}\n")
                log_to.write(f"Tamanho: {tamanho:.2f} KB\n")
                log_to.write(f"Criado em: {data_criacao}\n")
                log_to.write(f"Modificado em: {data_modificacao}\n")
                log_to.write(f"Copiado para: {caminho_destino}\n\n")

                print(f"📁 Arquivo copiado: {nome_arquivo}")