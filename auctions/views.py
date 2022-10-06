from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, AuctionForm, WatchList, Bid, BidForm, Comment, CommentForm


def index(request):
    auctions = Auction.objects.all()
    liveauctions = auctions.filter(closed=False)
    deadauctions = auctions.filter(closed=True)
    return render(request, "auctions/index.html", {
        "liveauctions": liveauctions,
        "deadauctions": deadauctions,
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


def create(request):
    if request.method == "POST":
        # Access username
        user = User.objects.get(username=request.user)

        # Take in data submitted and save as form
        form = AuctionForm(request.POST, request.FILES)

        # Check if form data is valid
        if form.is_valid(): 
            auction = form.save(commit=False)
            auction.user = user
            auction.winner = user
            auction.current_price = auction.starting_bid
            auction.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html", {
            "form": AuctionForm()
        })


def listing(request, listing_id):
    # Access username
    user = User.objects.get(username=request.user)
    # Access listing
    listing = Auction.objects.get(pk = listing_id)
    # Access comments
    try:
        comments = Comment.objects.filter(listing = listing_id).all().order_by('-datetime')
    except Comment.DoesNotExist:
        comments = None

    # Set wachlist text
    if user.watched.filter(listing=listing): 
        watchlist_text = "Stop Watching"
    else:
        watchlist_text = "Watchlist"

    if request.method == "POST":
        # If owner closes listing
        if 'close' in request.POST:
            listing.closed = True
            listing.save()

            return render(request, "auctions/listing.html", {
                "listing": listing,
                "comments": comments,
                "commentform": CommentForm()
            })

        # If comment is added
        if 'commentpost' in request.POST: 
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = user
                comment.listing = listing
                comment.save()

        # Else if watchlist button is clicked
        elif 'watchlist' in request.POST:
            if user.watched.filter(listing=listing):
                user.watched.filter(listing = listing).delete()
                watchlist_text = "Watchlist"
            else: 
                watch = WatchList()
                watch.user = user
                watch.listing = listing
                watch.save()
                watchlist_text = "Stop Watching"

        # Else if a bid is submitted
        elif 'bid' in request.POST:
            # Take in data submitted 
            form = BidForm(request.POST)

            # Check if form data is valid
            if form.is_valid(): 
                bid = form.save(commit=False)

                if bid.bid_price == None or bid.bid_price < listing.current_price:
                    return render(request, "auctions/listing.html", {
                        "listing": listing,
                        "watchlist_text": watchlist_text,
                        "bidform": BidForm(),
                        "message": "Error: Invalid bid price!",
                        "comments": comments,
                        "commentform": CommentForm()
                    })
                else:
                    bid.user = user
                    bid.save()
                    listing.current_price = bid.bid_price
                    listing.winner = user
                    listing.save()

        return render(request, "auctions/listing.html", {
            "listing": listing,
            "watchlist_text": watchlist_text,
            "bidform": BidForm(),
            "comments": comments, 
            "commentform": CommentForm()
        })

    # Else, if owner is checking in
    if user == listing.user and listing.closed == False:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "owner": True,
            "comments": comments,
            "commentform": CommentForm()
        })

    # Else, if winner is checking in on closed listing
    elif user == listing.winner and listing.closed:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "winner": True, 
            "comments": comments,
            "commentform": CommentForm()
        })


    # Otherwise, default load
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "watchlist_text":watchlist_text,
        "bidform": BidForm(),
        "comments": comments,
        "commentform": CommentForm()
    })

def watchlist(request):
    # Access username
    user = User.objects.get(username=request.user)
    watchauctions = user.watched.all()
    return render(request, "auctions/watchlist.html", {
        "watchauctions": watchauctions,
    })

def categories(request):
    pass