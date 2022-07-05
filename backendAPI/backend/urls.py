from posixpath import basename
from django.urls import path, include
from .views import GoalsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('goals', GoalsViewSet, basename='goals')

urlpatterns = [
    path('', include(router.urls)),
    # path('goals/', GoalsList.as_view()),
    # path('goals/<int:id>/', GoalDetail.as_view())
]
