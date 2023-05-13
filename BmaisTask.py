import psutil
import subprocess
import time
import logging
import socket
import os

f = 0

def get_pc_name():
    try:
        host_name = socket.gethostname()
        return host_name
    except:
        return "[Não foi possível recuperar o nome do PC]"

pc_name = get_pc_name()

log_file = r'\\CC-CAIXA01\Pasta Teste\log.txt'

#Configuração do logger
logger = logging.getLogger('my_logger') #Cria o objeto de log
logger.setLevel(logging.INFO) #Configura o nível de log
handler = logging.FileHandler(log_file) #Cria arquivo handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S') #Define o formato do log
handler.setFormatter(formatter) #Define o formato do log para o handler
logger.addHandler(handler) #Adiciona o handler ao logger

def check_process_running(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

def restart_process(executable_path):
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        if proc.info['exe'] == executable_path:
            return  # Process is already running, no need to restart

    subprocess.Popen([executable_path])

if __name__ == '__main__':
    main_script = 'Bmais.exe'  # Replace with your main executable filename
    main_script_path = 'C:\\Bancamais\\Bmais.exe'  # Replace with the actual path to your main executable

    while True:
        if not check_process_running(main_script):
            restart_process(main_script_path)
            if f == 0:
                f = 1
            else:
                logger.info(f'O PC {pc_name} tentou finalizar o programa mas o mesmo será reiniciado.')
        
        time.sleep(1)
        
        if os.path.exists('C:\\ever1401.txt'):
            time.sleep(3)
            try:
                os.remove('C:\\ever1401.txt')
            except:
                pass
            break
