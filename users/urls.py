from .views import SignUpView,ProfileView,UpdateProfileView,AddRemoveSaveView,SavedView,RecentlyViewedView
from django.urls import path

app_name='users'
urlpatterns = [
    path('signup',SignUpView.as_view(),name='signup'),
    path('profile/<str:username>',ProfileView.as_view(),name='profile'),
    path('update',UpdateProfileView.as_view(),name='update'),
    path('addremovesaved/<int:product_id>',AddRemoveSaveView.as_view(),name='addremovesaved'),
    path('saveds',SavedView.as_view(),name='saveds'),
    path('recently_viewed',RecentlyViewedView.as_view(),name='recently_viewed'),
]
