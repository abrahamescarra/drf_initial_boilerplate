from content.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('model1', Model1ViewSet, 'model1')
router.register('model2', Model2ViewSet, 'model2')

urlpatterns = [
    #  path('mark_all_read',MarkAllReaded.as_view(),name='mark_all_read'),
    #  path('mark_read',MarkReaded.as_view(),name='mark_read'),
]+router.urls