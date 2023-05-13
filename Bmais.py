import requests
import datetime
import win32api
import time
import os
import logging
from plyer import notification
import psutil
import subprocess
import socket

global f
f = 0

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

def get_pc_name():
    try:
        host_name = socket.gethostname()
        return host_name
    except:
        return "[Não foi possível recuperar o nome do PC]"

def antikill():
    global f
    if f == 0:
        if not check_process_running(main_script):
            restart_process(main_script_path)
        f = 1
    else:
        if not check_process_running(main_script):
            restart_process(main_script_path)
            logger.info(f'O PC {pc_name} tentou finalizar o programa mas o mesmo será reiniciado.')
        time.sleep(1)

pc_name = get_pc_name()

tolerance_seconds = 2

notification_title1 = "HORÁRIO BLOQUEADO"
notification_message1 = "O horário que você está tentando alterar está bloqueado."
notification_icon1 = "C:\\Bancamais\\icon.ico"
notification_title2 = "PROGRAMA FINALIZADO"
notification_message2 = f"O programa foi finalizado pelo usuário {pc_name}."

log_file = r'\\CC-CAIXA01\Pasta Teste\log.txt'

#Configuração do logger
logger = logging.getLogger('my_logger') #Cria o objeto de log
logger.setLevel(logging.INFO) #Configura o nível de log
handler = logging.FileHandler(log_file) #Cria arquivo handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S') #Define o formato do log
handler.setFormatter(formatter) #Define o formato do log para o handler
logger.addHandler(handler) #Adiciona o handler ao logger
logger.info(f"O programa foi iniciado pelo PC: {pc_name}")


while True:
    url = "https://www.timeapi.io/api/Time/current/zone?timeZone=America/Sao_Paulo"
    try:
        response = requests.get(url)
    except Exception as e:
        logger.error(f"Erro ao tentar acessar a API => {e} PC: {pc_name}")
        time.sleep(10)
        continue
    checkresponse = response.json()
    hora = checkresponse["hour"]
    minuto = checkresponse["minute"]
    segundos = checkresponse["seconds"]
    ano = checkresponse["year"]
    mes = checkresponse["month"]
    dia = checkresponse["day"]

    horario = f'{ano}-{mes}-{dia} {hora}:{minuto}:{segundos}'
    horario_dt = datetime.datetime.strptime(horario, '%Y-%m-%d %H:%M:%S')

    data = datetime.datetime.now()
    formatted_date = data.strftime('%Y-%#m-%#d %#H:%#M:%S')
    data_dt = datetime.datetime.strptime(formatted_date, '%Y-%m-%d %H:%M:%S')

    time_diff = abs((horario_dt - data_dt).total_seconds())

    if time_diff <= tolerance_seconds:
        pass
    else:
        hora = checkresponse["hour"] + 3
        milisegundo = checkresponse["milliSeconds"]

        try:
            win32api.SetSystemTime(
                ano,     
                mes,     
                0,       
                dia,     
                hora,    
                minuto,  
                segundos,
                milisegundo 
            )
            logger.info(f"Tentativa de alteração de horário detectada => ({data_dt}) mas o horário foi alterado para => ({horario_dt}). PC: {pc_name}")
            notification.notify(title=notification_title1, message=notification_message1, app_name="Time Blocker", app_icon=notification_icon1)
        except Exception as e:
            logger.info(f"Erro ao alterar o horário. {e} PC: {pc_name}")

    if os.path.exists('C:\\ever1401.txt'):
        logger.info(f'O programa foi finalizado pelo PC: {pc_name}')
        notification.notify(title=notification_title2, message=notification_message2, app_name="Time Blocker")
        try:
            os.remove('C:\\ever1401.txt')
        except:
            pass
        break

    main_script = 'BmaisTask.exe'  # Replace with your main executable filename
    main_script_path = 'C:\\Bancamais\\BmaisTask.exe'  # Replace with the actual path to your main executable

    antikill()

    antikill()

    antikill()
