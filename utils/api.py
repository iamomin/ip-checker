import requests
from utils.common import Logger

import constants as c


class _HTTP(object):
	"""Base HTTP Client"""

	def __init__(self):
		super(_HTTP, self).__init__()
		self.logger = Logger.get_logger()

	def _get(self, api_url):
		"""
		Get Request

		:param api_url: GET Request URL
		:return: JSON response as dictionary
		"""
		self.logger.debug(f'Api URL: {api_url}')
		return requests.get(api_url).json()


class IfConfig(_HTTP):
	"""
	IfConfig Class

	Communicate to ifconfig service to fetch requesting client information
	"""

	def __init__(self):
		super(IfConfig, self).__init__()

	def what_is_my_ip(self):
		"""
		What is my IP

		Fetch the GET end point JSON response

		:return: Response details as a dictionary
		"""
		d = self._get(c.API_URL)
		self.logger.debug(f'Raw response: {d}')

		m = f"Country: {d['country']}, Latitude: {d['latitude']}, Longitude: {d['longitude']}, IP: {d['ip']}"
		self.logger.info(m)

		return d
