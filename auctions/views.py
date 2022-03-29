from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import Listing, User, WatchList, Bid

class NewBidForm(forms.Form):
    bid = forms.IntegerField(label="bid")

def index(request):
    activeListings = Listing.objects.filter(active=True)
    return render(request, "auctions/index.html",{
        "listings": activeListings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image = request.POST["image"]
        current_user = request.user
        newListing = Listing(title = title, description = description, price = price, image = image, active = True, user=current_user)
        newListing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html")

def listing(request, listing_id):
    if request.method == "POST":
        pass
    else:
        listing = Listing.objects.get(pk=listing_id)
        currentPrice = listing.price
        print (currentPrice)
        highestBid = Bid.objects.filter(price=currentPrice, currentListing = listing_id)
        print (highestBid.user)
        form = NewBidForm(initial={'bid': currentPrice})
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "form": form,
            "highestBid": highestBid
        })

def addWatchList(request, listing_id):
    watchlisting = Listing.objects.get(id=listing_id)
    user_id = request.user
    newWatchList = WatchList(user=user_id, currentListing=watchlisting)
    newWatchList.save()
    url = reverse('listing', kwargs={'listing_id': listing_id})
    return HttpResponseRedirect(url)

def watchList(request):
    user_id = request.user
    currentlyWatching = WatchList.objects.filter(user=user_id).values("currentListing")
    listings = Listing.objects.filter(id__in=currentlyWatching)
    return render (request, "auctions/watchlist.html", {
        "listings": listings
    })
def closelist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    listing.active = False
    listing.save()
    url = reverse('listing', kwargs={'listing_id': listing_id})
    return HttpResponseRedirect(url)

def bid(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk=listing_id)
        newBid = request.POST["bid"]
        if int(newBid) <= listing.price:
            pass
        else:
            listing.price = newBid
            listing.save()
            user_id = request.user
            newBidModel = Bid(user= user_id, price=newBid, currentListing = listing)
            newBidModel.save()
            url = reverse('listing', kwargs={'listing_id': listing_id})
            return HttpResponseRedirect(url)


