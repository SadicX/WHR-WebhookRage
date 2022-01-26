# Gay quien me robe el código xd
from colorama import Fore as fore
from colorama import init
import threading
import json
from colorama import Fore
import requests
import asyncio
import threading
init(autoreset=True)
sessions = requests.Session()
r = fore.LIGHTRED_EX
b = fore.LIGHTBLUE_EX
w = fore.WHITE
proxies = []
async def info( words):
  print(f"{r}[{Fore.WHITE}WBR S4K T34M{r}] {b}- {Fore.WHITE}{words}")
def check_hook(hook):
    info = requests.get(hook).text
    if "\"Mensaje\": \"Webhook desconocida\"" in info:
        return False
    return True
webhook = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Webhook: ")
if(check_hook(webhook) == False):
  print(f"{r}[{Fore.WHITE}ADVERTENCIA{r}] {b}- {Fore.WHITE}Webhook no válido")
advanced = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Modo avanzado? [Y\\N]: ")
if advanced == "y" or advanced == "Y":
    advanced = True
else:
    advanced = False
async def logo():
  print(f""" {Fore.BLACK}
                                                                                            
             `8.`888b                 ,8'           8 8888        8           8 888888888o.             
               `8.`888b               ,8'            8 8888        8           8 8888    `88.            
                `8.`888b             ,8'             8 8888        8           8 8888     `88            
                 `8.`888b     .b    ,8'              8 8888        8           8 8888     ,88            
                  `8.`888b    88b  ,8'               8 8888        8           8 8888.   ,88'    Made By SadicX        
                   `8.`888b .`888b,8'                8 8888        8           8 888888888P'     Version: 2.0      
                    `8.`888b8.`8888'                 8 8888888888888           8 8888`8b                 
                     `8.`888`8.`88'                  8 8888        8           8 8888 `8b.               
                      `8.`8' `8,`'                   8 8888        8           8 8888   `8b.             
                       `8.`   `8'                    8 8888        8           8 8888     `88. 

             {fore.BLACK}WebHook{fore.GREEN}Rage By S4K       {Fore.BLACK}""".replace(f"═",f"{Fore.WHITE}═{Fore.GREEN}"))
async def webhookspammer(webhookurl,amount,message,name = None):
    for i in range(int(amount)):
        data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://i.ibb.co/kXc84x5/static-1.png"})
        if(len(data.text) == 0):
            if(data.status_code == "204" or data.status_code == 204):
                await info("Enviados: " + str(message))
            pass
        else:
            result = json.loads(data.text)
            seconds = (float(int(result['retry_after']))/1000)%60
            await info("Durmiendo... " + str(float(int(seconds))) + " Segundos para evitar la prohibición del límite de velocidad")
            await asyncio.sleep(seconds)
    await info("Terminado!")
    await start()
async def webhooksender(webhookurl,message,name = None):
        data = requests.post(webhook, json={"Contenido": str(message), "Nombre": str(name), "avatar_url": "https://i.ibb.co/kXc84x5/static-1.png"})
        await info(data.status_code)
        if(data.status_code == 204):
            await info("Enviado: " + str(message))
        else:
            await info("Error!")
        await asyncio.sleep(2)
        await start()
async def sendbeforedeletion(webhookurl,message,name = None):
        data = requests.post(webhook, json={"Contenido": str(message), "Nombre": str(name), "avatar_url": "https://i.ibb.co/kXc84x5/static-1.png"})
        if(data.status_code == 204):
            await info("Sent: " + str(message))
        else:
            await info("Error!")
        lit = requests.delete(webhook)
        if(lit.status_code == 204):
            await info("Webhook eliminado!")
async def deletion(webhookurl, message):
    await sendbeforedeletion(webhookurl=webhook,message=message,name=None)
async def webhookcreator(token,isbotornot,name,channelid):
        requests.post(f"https://discord.com/api/v8/channels/{channelid}/webhooks", json={"Autorización": str(token), "Nombre": str(name), "avatar_url": "https://i.ibb.co/kXc84x5/static-1.png"})
async def start():
  await logo()
  print(f"                    {Fore.GREEN}┌─────────{Fore.GREEN}──────────────────────────────{Fore.GREEN}─────────────────────{Fore.GREEN}─────────┐")
  print(f"                    {Fore.GREEN}│[{Fore.WHITE}1{Fore.GREEN}]  {Fore.WHITE}Webhook Spammer                                       {fore.GREEN}          │")
  print(f"                    {Fore.GREEN}│[{Fore.WHITE}2{Fore.GREEN}]  {Fore.WHITE}Webhook Emisor                                       {fore.GREEN}           │")
  print(f"                    {Fore.GREEN}│[{Fore.WHITE}3{Fore.GREEN}]  {Fore.WHITE}Webhook Eliminador                                  {fore.GREEN}            │")
  print(f"                    {Fore.GREEN}│[{Fore.WHITE}4{Fore.GREEN}]  {Fore.WHITE}Webhook Creador                                    {fore.GREEN}             │")
  print(f"                    {Fore.GREEN}└─────────{Fore.GREEN}──────────────────────────────{Fore.GREEN}─────────────────────{Fore.GREEN}─────────┘")
  choice = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Elección: ")
  if(choice == "1"):
       if(advanced == False):
            message = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Mensage: ")
            amount = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Cantidad: ")
            threading.Thread(target=await webhookspammer(webhookurl=webhook,amount=amount,message=message,name=None)).start()
       else:
                message = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Mensage: ")
                amount = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Cantidad: ")
                name = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Nombre: ")
                threading.Thread(target=await webhookspammer(webhookurl=webhook,amount=amount,message=message,name=name)).start()
  elif(choice == "2"):
        if(advanced == False):
            message = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Mensage: ")
            threading.Thread(target=await webhooksender(webhookurl=webhook,message=message)).start()
        else:
                message = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Mensage: ")
                name = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Nombre: ")
                threading.Thread(target=await webhooksender(webhookurl=webhook,message=message,name=name)).start()
  elif(choice == "3"):
            message = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Mensaje para enviar antes de la eliminación: ")
            threading.Thread(target=await deletion(webhookurl=webhook,message=message)).start()
  elif(choice == "4"):
            tokeninput = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Usuario O Bot Token: ")
            isbotornot = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ ¿Es este token un bot?? [Y\\N]: ")
            name = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Nombre del webhook: ")
            chanid = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ ID del Canal: ")
            threading.Thread(target=await webhookcreator(token=tokeninput,isbotornot=isbotornot,name=name,channelid=chanid)).start()
loop = asyncio.get_event_loop()
loop.run_until_complete(start())
