# LIMP Gateway for Unifonic
This repo is a [LIMP](https://github.com/masaar/limp) [Package](https://github.com/masaar/limp-docs/blob/APIv5.8/api/package.md) for the sole purpose of integrating [Unifonic SMS](https://www.unifonic.com/SMS) into LIMP apps using [LIMP Gateways](https://github.com/masaar/limp-docs/blob/APIv5.8/api/gateways.md).

## How-to
1. Clone this repo into your LIMP `modules` folder.
2. Add following to your app package config:
```python
'vars':{
	'unifonic':{'sid':'YOUR_UNIFONIC_SID_HERE'}
}
```
3. Unifonic gateway requires following args:
   1. `phone`: Target phone number using international format with prefixed `+`. Type `str`.
   2. `content`: Message body. Type `str`.
4. Use Unifonic gateway using LIMP Gateway Controller:
```python
from gateway import Gateway

Gateway.send('unifonic', phone=phone, content=content)
```