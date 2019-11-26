# Ancora Imparo.

from config import Config

from typing import TypedDict
from otsdc.rest.client import OTSRestClient
from otsdc.url.http_url import HttpOTSUrl

def unifonic_gateway(phone: str, content: str, unifonic_auth: TypedDict('GATEWAY_UNIFONIC_AUTH', sid=str)=None):
	if not unifonic_auth:
		unifonic_auth = Config.vars['unifonic']
	client = OTSRestClient(appSid=unifonic_auth['sid'])
	msg = client.messageResource
	msg.send(phone, content)

def config():
	return {
		'version':5.8,

		'gateways':{
			'unifonic':unifonic_gateway
		}
	}