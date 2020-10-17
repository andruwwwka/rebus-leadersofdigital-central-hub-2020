from rest_framework.routers import DefaultRouter

from .resources import ObsceneWordViewSet, BanContentViewSet

router = DefaultRouter()
router.register(r'obscene_words', ObsceneWordViewSet, basename='obscene_words')
router.register(r'ban_contents', BanContentViewSet, basename='ban_contents')
urlpatterns = router.urls
