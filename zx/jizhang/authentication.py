__author__ = 'zx'
# coding：utf-8

from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
import datetime

EXPIRED_TOKEN = 14


class ExpiredTokenAuthentication(TokenAuthentication):
	def authenticate_credentials(self, key):
		model = self.get_model()
		try:
			token = model.objects.select_related('user').get(key=key)
		except model.DoesNotExist:
			raise exceptions.AuthenticationFailed(_('Invalid token.'))

		if not token.user.is_active:
			raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

		now = datetime.datetime.now()
		interval = (now - token.created).days
		# interval = (now - token.created).seconds
		if interval > EXPIRED_TOKEN:
			raise exceptions.AuthenticationFailed('Token expired')
		return (token.user, token)