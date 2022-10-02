from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm

class User(AbstractUser):
    pass

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")
    bid_price=models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.user} bidding {self.bid_price}"

class Auction(models.Model):
    CATEGORIES = [
        ('BOOKS', 'Books'),
        ('CLOTH', 'Clothes'),
        ('ELECT', 'Electronics'),
        ('HEALTH', 'Health'),
        ('HOBBY', 'Hobbies'),
        ('KIDTO', 'Toys'),
        ('SPORT', 'Sports'),
        ('OTHER', 'None'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    starting_bid = models.DecimalField(max_digits=8, decimal_places=2)
    bids = models.ManyToManyField(Bid, blank=True, related_name="listing", null=True)
    current_price = models.DecimalField(max_digits=8, decimal_places=2)
    url = models.ImageField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, default=CATEGORIES[7][0], blank=True)

    def __str__(self):
        return f"{self.title} from {self.user}"

class AuctionForm(ModelForm):
    class Meta: 
        model = Auction
        fields = ['title', 'description', 'starting_bid', 'url', 'category']

    def __init__(self, *args, **kwargs):
        super(AuctionForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watched")
    listing = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="watcher")

    def __str__(self):
        return f"{self.user} watching {self.listing}"



class BidForm(ModelForm):
    class Meta: 
        model = Bid
        fields = ['bid_price']

    def __init__(self, *args, **kwargs):
        super(AuctionForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'

class Comments(models.Model):
    pass