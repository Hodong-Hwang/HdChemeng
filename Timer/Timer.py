import requests
import webbrowser
from datetime import datetime, timedelta

# 서버 URL 및 대상 URL 설정
target_url = "https://sports.cfmc.or.kr/rent/reservation/index/2024/08/13/1/CHEONAN01/19/6"

    
# 특정 시간에 맞춰 URL 열기
def open_url_at_target_time(target_hour, target_minute, target_second, target_millisecond):
    while True:
        server_time = datetime.strptime(requests.head(target_url).headers.get('Date'), '%a, %d %b %Y %H:%M:%S %Z')

        # 초, 밀리초까지 맞추기 위해 조건을 미세 조정
        if (server_time.hour == target_hour and
            server_time.minute == target_minute and
            server_time.second == target_second):                
            # Chrome 경로 지정
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                
            # 지정된 URL을 Chrome에서 열기
            webbrowser.get(chrome_path).open(target_url)
            print(f"Opened {target_url} at {server_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
            break
        print(f"Server time (UST): {server_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")


# 21시 00분 00초 000밀리초(한국 표준시)에 URL 열기 시작
open_url_at_target_time(15-9, 56, 0, 0)