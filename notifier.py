import requests
import json
from time import sleep

slack_token = open("slackToken.txt", "r").read()
slack_user_name = open("slackUserName.txt", "r").read()


def send_slack_message(text, channel, blocks= None):
	return requests.post('https://slack.com/api/chat.postMessage', {
		'token': slack_token,
		'channel': channel,
		'text': text,
		'username': slack_user_name,
		'blocks': json.dumps(blocks) if blocks else None
		}).json()

counter = 1798
while True:
	try:
		resp1 = requests.get("https://teslatequila.tesla.com/")
		resp2 = requests.get("https://shop.tesla.com/product/tesla-tequila?sku=1617866-00-A")
	except requests.exceptions.RequestException as e:
		print("Error occured, trying again")
		sleep(3)
	if "out of stock" not in resp2.text.lower() or "out of stock" not in resp1.text.lower():
		print("IN STOCK")
		for i in range(1, 20):
			send_slack_message("IN STOCK! ! ! BUY BUY BUY!!! \n https://shop.tesla.com/product/tesla-tequila?sku=1617866-00-A", "#alert")
			sleep(1)
	if counter >= 1800:
		send_slack_message("(somewhat) Hourly Service Check: working", "#hourlyupdates")
		counter = 0
	sleep(2)
	counter+=1
