from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm

class User(AbstractUser):
    pass

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")
    bid_price=models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.user} bidding ${self.bid_price}"

class Auction(models.Model):
    CATEGORIES = [
        ('CLOTH', 'Clothes'),
        ('ELECT', 'Electronics'),
        ('HEALTH', 'Health'),
        ('HOBBY', 'Hobbies'),
        ('KIDTO', 'Toys'),
        ('SPORT', 'Sports'),
        ('TOOLS', 'Tools'),
        ('OTHER', 'None'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    starting_bid = models.DecimalField(max_digits=8, decimal_places=2)
    bids = models.ManyToManyField(Bid, blank=True, related_name="listing", null=True)
    current_price = models.DecimalField(max_digits=8, decimal_places=2)
    winner = models.ForeignKey(User, related_name="wins", on_delete=models.CASCADE, blank=True, null=True)
    url = models.ImageField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, default=CATEGORIES[7][0], blank=True)
    closed = models.BooleanField(default=False)

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
        super(BidForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    listing = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments", null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} commented {self.text}"

class CommentForm(ModelForm):
    class Meta: 
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'