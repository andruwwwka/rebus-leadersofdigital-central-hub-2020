from rest_framework.routers import DefaultRouter  # noqa: F401

from .resources import ObsceneWordViewSet  # noqa: F401


router = DefaultRouter()
router.register(r'obscene_words', ObsceneWordViewSet, basename='obscene_words')
urlpatterns = router.urls
