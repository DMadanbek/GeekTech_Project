from django.urls import path
from Favourite import views
from Project.views import LawListApiView

urlpatterns = [
    path("/lawfavorites/",views.lawfavourites),
    path("api/v1/lawwitsfavourite",views.law_wits_favourite)

]