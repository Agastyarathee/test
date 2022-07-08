import time
import webbrowser

breaks = 3

for i in range(breaks):
  time.sleep(2*60*60)
  webbrowser.open('http://google.co.kr', new=2)