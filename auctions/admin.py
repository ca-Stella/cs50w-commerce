from django.contrib import admin

# Register your models here.
from .models import User, Auction, WatchList, Bids

# Register your models here.
admin.site.register(User)
admin.site.register(Auction)
admin.site.register(WatchList)
admin.site.register(Bids)