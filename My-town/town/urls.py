from .views import (NewsListView, NewsDetailView, feedback, contact_view, AnnouncementListView, AnnouncementDetailView,
                    OfficialDocumentsListView, OfficialDocumentsDetailView, HistoryPage, TownHallManagementListView,
                    search_view, index, passport_of_town, vacancy, MapView)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('feedback/', feedback, name='feedback'),
    path('contact/', contact_view, name='contact'),
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('documents/', OfficialDocumentsListView.as_view(), name='documents_list'),
    path('documents/<int:pk>/', OfficialDocumentsDetailView.as_view(), name='documents_detail'),
    path('history/', HistoryPage.as_view(), name='history'),
    path('town_hall_managements/', TownHallManagementListView.as_view(), name='town_hall_management_list'),
    path('passport/', passport_of_town, name='passport_of_town'),
    path('vacancy/', vacancy, name='vacancy'),
    path('search/', search_view, name='search_view'),
    path('map/', MapView.as_view(), name='map'),


]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
