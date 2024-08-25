import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from chat.routing import \
    websocket_urlpatterns  # Замените 'chat' на имя вашего приложения

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    }
)
