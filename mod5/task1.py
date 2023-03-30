import subprocess
import os

def start_server_on_port():
    rc = subprocess.call(['lsof', '-i',  ':5000'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    if rc == 0:
        output = subprocess.check_output(['lsof', '-i', ':5000'])
        pid = int((output.decode('utf-8').split()[10]))
        os.kill(pid, 9)
        print(f'Process with PID {pid} terminated')
        subprocess.Popen(['python', 'task_1main.py'])
        print('server run!!')
    if rc == 1:
        print('server run')
        subprocess.Popen(['python', 'task1_main.py'])


if __name__ == '__main__':
    start_server_on_port()