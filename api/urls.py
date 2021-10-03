from django.conf.urls import include, url

from api.views import ManufacturerViewSet, ShoeTypeViewSet, ShoeColorViewSet, ShoeViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register('Maufacturer', ManufacturerViewSet)
router.register('ShoeType', ShoeTypeViewSet)
router.register('ShoeColor', ShoeColorViewSet)
router.register('Shoe', ShoeViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls))
]
