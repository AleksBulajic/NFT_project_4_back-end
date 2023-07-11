from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

class InvalidTokenException(exceptions.AuthenticationFailed):
    default_detail = 'Invalid token.'
    default_code = 'invalid_token'


class InactiveUserException(exceptions.AuthenticationFailed):
    default_detail = 'User inactive or deleted.'
    default_code = 'inactive_user'

    
class CustomTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
        except self.model.DoesNotExist:
            raise InvalidTokenException()

        if not token.user.is_active:
            raise InactiveUserException()

        return (token.user, token)