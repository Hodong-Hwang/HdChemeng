import ntplib
from datetime import datetime, timedelta
import time
import webbrowser
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

# NTP 서버 목록
#ntp_servers = ['pool.ntp.org', 'time.google.com', 'time.windows.com','time.cloudflare.com']
ntp_servers = ['time.google.com', 'time.windows.com','time.cloudflare.com']

target_url = "https://sports.cfmc.or.kr/rent/reservation/index/2024/08/13/1/CHEONAN01/19/6"
client = ntplib.NTPClient()

# NTP를 통해 현재 시간 가져오기 (멀티스레딩과 타임아웃 적용)
def fetch_ntp_time(server):
    try:
        response = client.request(server, version=3, timeout=0.02)  # 타임아웃을 1초로 설정
        ntp_time = datetime.utcfromtimestamp(response.tx_time)
        return ntp_time + timedelta(hours=9)  # KST로 변환
    except (ntplib.NTPException, OSError):
        return None

# NTP를 통해 현재 시간 가져오기
def get_ntp_time():
    with ThreadPoolExecutor(max_workers=len(ntp_servers)) as executor:
        future_to_server = {executor.submit(fetch_ntp_time, server): server for server in ntp_servers}
        done, _ = wait(future_to_server.keys(), return_when=FIRST_COMPLETED)  # 가장 먼저 완료된 작업을 기다림
        for future in done:
            result = future.result()
            if result:
                return result     
    raise Exception("Failed to connect to any NTP servers.")      

# 특정 시간에 맞춰 URL 열기
def open_url_at_target_time(target_hour, target_minute, target_second, target_millisecond):
    while True:
        ntp_time = get_ntp_time()
        current_time = ntp_time.time()

        # ms까지 정밀한 비교를 위해 부동소수점 사용
        target_time = target_hour * 3600 + target_minute * 60 + target_second + target_millisecond / 1000
        current_time_in_seconds = (current_time.hour * 3600 +
                                       current_time.minute * 60 +
                                       current_time.second +
                                       current_time.microsecond / 1000000)

        print(f"Current NTP time (KST): {ntp_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
            
        if current_time_in_seconds >= target_time:
            # Chrome 경로 지정          
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'            
            # 지정된 URL을 Chrome에서 열기
            webbrowser.get(chrome_path).open(target_url)
            print(f"Opened {target_url} at {ntp_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
            break
        # 10밀리초마다 시간 확인
# 21시 00분 00초 000밀리초(한국 표준시)에 URL 열기 시작
open_url_at_target_time(20, 59, 59, 750)