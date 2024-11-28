# main routing for the whole app
from django.urls import path, include
from . import views

# list of urls the app will recognize

urlpatterns = [
    path('', views.place_list, name='place_list'),
# request to the empty string path(homepage) that says any requests
    # made to it should be handled by place_list function in views.py
    # path('admin/', admin.site.urls),
    path('visited', views.places_visited, name = 'places_visited'),
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited'),
    path('place/<int:place_pk>', views.place_details, name='place_details'),
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place'),
    # url for delete place feature
    path('about', views.about, name ='about')
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    # is it running locally using the dev server
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # if it is running locally, then add these routes to the static files