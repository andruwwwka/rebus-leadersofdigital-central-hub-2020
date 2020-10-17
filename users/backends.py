import jwt

from django.conf import settings

from rest_framework import authentication, exceptions

from .models import Profile


class JWTAuthentication(authentication.BaseAuthentication):
    """Логика аутентификации по JWT токену."""

    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        """Разбор авторизационного заголовка и аутентификация."""
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()
        if not auth_header:
            return None
        if len(auth_header) == 1:
            return None
        elif len(auth_header) > 2:
            return None
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
        if prefix.lower() != auth_header_prefix:
            return None
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """Аутентификация пользователя."""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            msg = 'Аутентификация невозможна. Токен невозможно декодировать'
            raise exceptions.AuthenticationFailed(msg)
        try:
            user = Profile.objects.get(pk=payload['id'])
        except Profile.DoesNotExist:
            msg = 'Пользователь не найден.'
            raise exceptions.AuthenticationFailed(msg)
        if not user.is_active:
            msg = 'Пользователь деактивирован.'
            raise exceptions.AuthenticationFailed(msg)
        return (user, token)
