import schedule
import subprocess
import time

# Função para executar o script automacao.py
def executar():
    print("Executando gitrun.py...")    
    subprocess.run(["python", "gitrun.py", "-m", "Commit via agenda"], shell=True)

if __name__ == "__main__":
    print("Agendador de tarefas iniciado...")
    # Agendar as tarefas
    schedule.every().minute.do(executar)

    # Loop para manter o agendador rodando
    while True:
        schedule.run_pending()  # Executa tarefas agendadas
        time.sleep(10)  # Pausa para evitar alto consumo de CPU
