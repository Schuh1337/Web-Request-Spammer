import requests, time, ctypes

PURPLE = '\033[95m'
RED = '\033[91m'
ENDC = '\033[0m'

targeturl = "https://schuh.wtf"
nrequests = 100

def set_console_title(title, response_time):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{title}Response Time: {response_time:.2f} seconds")

def send_request(url, request_number, response_times):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_time = end_time - start_time
        set_console_title(f"URL: {url} - Requests: {request_number + 1} - ", response_time)
        response_times.append(response_time)
    except requests.exceptions.RequestException as e:
        print(RED + f"Request failed: {e}" + ENDC)
    except Exception as e:
        print(RED + f"{e}" + ENDC)

response_times = []

for i in range(nrequests):
    try:
        send_request(targeturl, i, response_times)
    except Exception as e:
        print(RED + f"{e}" + ENDC)
        time.sleep(15)

if response_times:
    avg_response_time = sum(response_times) / len(response_times)
    print(PURPLE + f"[#] Successful Requests:" + ENDC, len(response_times))
    print(PURPLE + f"[#] Average Response Time:" + ENDC, f"{avg_response_time:.2f} seconds")
input()
