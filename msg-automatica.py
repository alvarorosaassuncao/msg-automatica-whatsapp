# Bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime

# Definir os contatos
contatos = ['+5522981127107']

# Definir intervalo de envio
while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'Oi princesa! não vejo a hora de ver você', datetime.now(
    ).hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctr + w')
