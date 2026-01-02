import platform
import subprocess

"""
Написать скрипт, который принимает на вход список ІР-адресов 
и проверяет их доступность с помощью ping-запросов. 
Результаты проверки сохраняются в отдельный файл.
"""

ip_addr_list_file = "ip_address_list.txt"
result_file = "results.txt"

def read_input_file():
    input = []

    with open(ip_addr_list_file, "r") as file:
        for line in file:
            input.append(line.strip())

    return input

def check_ping(ip_addr):
    result = ""
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', param, '1', ip_addr]

    ping_result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if ping_result.returncode == 0:
        result = f"{ip_addr}\t is available\n"
    else: 
        result = f"{ip_addr}\t is not available\n"

    return result

def write_output_file(results):
    with open(result_file, "w") as file:
        for result in results:
            file.write(result)

def main():
    results = []
    input = read_input_file()

    for ip_addr in input:
        results.append(check_ping(ip_addr))

    write_output_file(results)
            
if __name__ == "__main__":
    main()
    
    



