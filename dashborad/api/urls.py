from dashborad.api.views import 
(
api_detail_health_view,
api_update_health_view,
api_delete_health_view,
api_post_health_view
)

from django.urls import path


urlpatterns=[
    path('<slug>/',api_detail_health_view,name='detail'),
    path('<slug>/update',api_update_health_view,name='update'),
    path('<slug>/delete',api_delete_health_view,name='delete'),
    path('create',api_post_health_view,name='create'),

]

