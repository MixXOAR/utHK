import os
from threading import Thread
import keyboard, pyautogui
import configparser
import pymem, time
import eel

path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\UNDERTALE\\undertale.ini"
path_file0 = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\UNDERTALE\\file0"
path_file9 = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\UNDERTALE\\file9"
stop_anim = False


config = configparser.ConfigParser()

eel.init('web')

@eel.expose
def set_nickname(nickname):
	config.read(path)
	config["General"]["Name"] = f'"{nickname}"'
	with open(path, 'w') as configfile:config.write(configfile); configfile.close()
	with open(path) as f: lines = f.readlines(); f.close()
	for i in range(0, len(lines)):lines[i] = f'{lines[i][0].upper()}{lines[i][1:]}'
	with open(path, "w") as f: f.writelines(lines); f.close()
	with open(path_file0) as f: lines = f.readlines(); lines[0] = f'{nickname}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[0] = f'{nickname}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
@eel.expose
def set_level(level):
	with open(path_file0) as f: lines = f.readlines(); lines[1] = f'{level}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[1] = f'{level}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
@eel.expose
def set_money(gold):
	with open(path_file0) as f: lines = f.readlines(); lines[10] = f'{gold}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[10] = f'{gold}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
def set_health(heal):
	with open(path_file0) as f: lines = f.readlines(); lines[2] = f'{heal}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[2] = f'{heal}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
@eel.expose
def set_maxhealth(heal):
	with open(path_file0) as f: lines = f.readlines(); lines[3] = f'{heal}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[3] = f'{heal}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
@eel.expose
def set_attack(attack):
	with open(path_file0) as f: lines = f.readlines(); lines[4] = f'{attack}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[4] = f'{attack}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
	with open(path_file0) as f: lines = f.readlines(); lines[5] = f'{attack}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[5] = f'{attack}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
@eel.expose
def set_armor(armor):
	with open(path_file0) as f: lines = f.readlines(); lines[6] = f'{armor}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[6] = f'{armor}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
	with open(path_file0) as f: lines = f.readlines(); lines[7] = f'{armor}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[7] = f'{armor}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()
@eel.expose
def set_kills(dies):
	with open(path_file0) as f: lines = f.readlines(); lines[9] = f'{dies}\n'; f.close()
	with open(path_file0, "w") as f: f.writelines(lines); f.close()
	with open(path_file9) as f: lines = f.readlines(); lines[9] = f'{dies}\n'; f.close()
	with open(path_file9, "w") as f: f.writelines(lines); f.close()

@eel.expose
def set_fight_health(health):
	set_health(health)
	pm = pymem.Pymem("UNDERTALE.exe")
	client0 = pymem.process.module_from_name(pm.process_handle, "UNDERTALE.exe").lpBaseOfDll
	client = pm.read_uint(client0 + 0x0039A14C)
	num1 = pm.read_int(client + 0x18)
	#num3 = pm.read_double(num2 + 0x60) ### HEALTH NOW
	pm.write_double(num1 + 0x2F8, float(health))
	pm.close_process()

# TODO: finish this
def fight_nickname_animation():
	pm2 = pymem.Pymem("UNDERTALE.exe")
	client0 = pymem.process.module_from_name(pm2.process_handle, "UNDERTALE.exe").lpBaseOfDll
	client = pm2.read_uint(client0 + 0x005B3094)
	num1 = pm2.read_int(client + 0x618)
	nickname_off = nickname_anim
	while True:
		try:
			for letter in range(0, len(nickname_anim)):
				if stop_anim: pm2.close_process(); break
				nickname_off = nickname_off.replace(nickname_anim[letter], '|"')
				pm2.write_string(num1 + 0x3A0, nickname_off)
				nickname_off = nickname_anim
				time.sleep(0.2)
			if stop_anim: pm2.close_process(); break
		except:break

# TODO: finish this
@eel.expose
def fight_nickname(nickname):
	global stop_anim
	stop_anim = False
	pm = pymem.Pymem("UNDERTALE.exe")
	client0 = pymem.process.module_from_name(pm.process_handle, "UNDERTALE.exe").lpBaseOfDll
	client = pm.read_uint(client0 + 0x005B3094)
	num1 = pm.read_int(client + 0x618)
	pm.write_string(num1 + 0x3A0, nickname)
	pm.close_process()

@eel.expose
def set_real_gold(gold):
	try:
		pm = pymem.Pymem("UNDERTALE.exe")
		client0 = pymem.process.module_from_name(pm.process_handle, "UNDERTALE.exe").lpBaseOfDll
		client = pm.read_uint(client0 + 0x0039A148)
		num1 = pm.read_int(client + 0x4)
		pm.write_double(num1 + 0xE0, float(gold))
		pm.close_process()
	except Exception as e: print(e)

@eel.expose
def start_an(nickname):
	global nickname_anim, stop_anim
	nickname_anim = nickname
	stop_anim = False
	Thread(target=fight_nickname_animation).start()
@eel.expose
def stom_animation():
	global stop_anim
	stop_anim = True

eel.start('main.html', size=(500, 300))