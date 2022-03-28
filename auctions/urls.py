from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watchList", views.watchList, name="watchList"),
    path("addWatchList/<int:listing_id>", views.addWatchList, name="addWatchList"),
    path("closelist", views.closelist, name="closelist"),
    path("bid", views.bid, name="bid"),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("<int:listing_id>", views.listing, name="listing")
]
