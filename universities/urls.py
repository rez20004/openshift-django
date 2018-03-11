# from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UniversitiesViewSet

router = DefaultRouter()
router.register(r'universities', UniversitiesViewSet)

# Adding routing to the urlpatterns
urlpatterns = router.urls