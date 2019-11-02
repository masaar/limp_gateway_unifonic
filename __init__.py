# Ancora Imparo.

from config import Config

from otsdc.rest.client import OTSRestClient
from otsdc.url.http_url import HttpOTSUrl

def send_unifonic(phone, content):
	client = OTSRestClient(appSid=Config.vars['unifonic']['sid'])
	msg = client.messageResource
	msg.send(phone, content)

def config():
	return {
		'version':5.8,

		'gateways':{
			'unifonic':send_unifonic
		}
	}