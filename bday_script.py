import schedule
import time
import webbrowser

def acecess_FB():
	print('Its working')
	url = 'https://www.facebook.com/'
	chrome = webbrowser.get('chrome')
	chrome.open_new('https://www.facebook.com/')
	return

acecess_FB()
# schedule.every(1).minutes.do(acecess_FB)
# schedule.every().day.at('20:00').do(acecess_FB)


# while True:
# 	schedule.run_pending()
# 	time.sleep(1)