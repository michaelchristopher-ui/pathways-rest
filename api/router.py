from rest_framework import routers
from .views import student_viewset

router = routers.DefaultRouter()
router.register('student', student_viewset)
