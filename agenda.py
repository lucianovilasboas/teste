import schedule
import subprocess
import time
from datetime import datetime

# Função para executar o script gitrun.py
def executar():
    # Obtendo o horário atual
    horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Mensagem de commit com o horário de execução
    mensagem_commit = f"Commit via agenda em {horario_atual}"
    
    # print(f"Executando gitrun.py com a mensagem: {mensagem_commit}") 
    
    # Executando o script gitrun.py com a mensagem de commit
    subprocess.run(["python", "gitrun.py", "-m", mensagem_commit], shell=True)

if __name__ == "__main__":
    print("Agendador de tarefas iniciado...")
    
    # Agendar as tarefas
    schedule.every().minute.do(executar)

    # Loop para manter o agendador rodando
    while True:
        schedule.run_pending()  # Executa tarefas agendadas
        time.sleep(10)  # Pausa para evitar alto consumo de CPU
