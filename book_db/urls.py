from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book_db.views import BookListViewSet

router = DefaultRouter()
router.register('image', BookListViewSet, basename='image')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<str:id>/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)