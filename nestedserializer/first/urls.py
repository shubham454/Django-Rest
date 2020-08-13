from django.urls import path,include
from first import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router1 = DefaultRouter()
#
# router.register('', views.HospitalAPIView, basename='hospital')
# router1.register('', views.DoctorAPIView, basename='doctor')

urlpatterns = [
    # path('hospital/', views.HospitalAPIView),
    # path('hospital/', include(router.urls)),
    # path('hospital/<int:pk>', include(router.urls)),
    # path('doctor/', include(router1.urls)),
    # path('doctor/<int:pk>', include(router1.urls))
    path('hospital/', views.HospitalApiView.as_view()),
    path('hospital/<int:pk>/', views.HospitalApiView.as_view()),
    path('doctor/', views.DoctorApiView.as_view()),
    path('doctor/<int:pk>/', views.DoctorApiView.as_view())
]