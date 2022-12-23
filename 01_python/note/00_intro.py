print('hello')
# ctrl+Z 하고 enter 하면 다시 $로 빠져나올 수 있음.

# 샐행 시, "$ python 01_python/00_intro.py" 경로 반드시 확인!
# cd 01_python/

import webbrowser

# chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

webbrowser.open('google.com')

# ctrl + / 하면 모두 주석 처리
webbrowser.open('https://finance.naver.com/item/main.naver?code=006400')
webbrowser.open('https://finance.naver.com/item/main.naver?code=035900')
webbrowser.open('https://finance.naver.com/item/main.naver?code=035720')

for x in ['006400', '035900', '035720']:
    webbrowser.open_new_tab(f'https://finance.naver.com/item/main.naver?code={x}')
