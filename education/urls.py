from rest_framework.routers import DefaultRouter  # noqa: F401

from .resources import LessonViewSet, ModuleViewSet, TaskViewSet, LevelViewSet, TagViewSet  # noqa: F401

router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'modules', ModuleViewSet, basename='modules')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'levels', LevelViewSet, basename='levels')
router.register(r'tags', TagViewSet, basename='tags')
urlpatterns = router.urls
