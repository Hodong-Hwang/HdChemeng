import ntplib
from datetime import datetime, timedelta
import time
import webbrowser
import os

# NTP 서버 목록
ntp_servers = ['pool.ntp.org', 'time.google.com', 'time.windows.com']
target_url = "https://sports.cfmc.or.kr/rent/application/index/2024/08/06/1/CHEONAN01/19"

# NTP를 통해 현재 시간 가져오기
def get_ntp_time():
    client = ntplib.NTPClient()
    for server in ntp_servers:
        try:
            response = client.request(server, version=3)
            ntp_time = datetime.utcfromtimestamp(response.tx_time)
            return ntp_time + timedelta(hours=9)  # KST로 변환
        except ntplib.NTPException as e:
            print(f"NTPException: Failed to connect to {server}. Trying next server...")
    raise Exception("Failed to connect to any NTP servers.")

# 특정 시간에 맞춰 URL 열기
def open_url_at_target_time(target_hour, target_minute, target_second, target_millisecond):
    while True:
        try:
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
                if os.name == 'nt':  # Windows
                    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                elif os.name == 'posix':  # macOS 및 Linux
                    # macOS의 경우
                    chrome_path = 'open -a /Applications/Google\\ Chrome.app %s'
                    # 또는 Linux의 경우
                    # chrome_path = '/usr/bin/google-chrome %s'
                else:
                    raise EnvironmentError("Unsupported OS")
                
                # 지정된 URL을 Chrome에서 열기
                webbrowser.get(chrome_path).open(target_url)
                print(f"Opened {target_url} at {ntp_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
                break

        except Exception as e:
            print(f"Error retrieving NTP time: {e}")

        # 10밀리초마다 시간 확인
        time.sleep(0.01)

# 21시 00분 00초 000밀리초(한국 표준시)에 URL 열기 시작
open_url_at_target_time(16, 00, 59, 750)