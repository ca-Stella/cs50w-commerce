# CS50's Web Programming - Commerce Assignment

This is an e-commerce auction page created as part of The CS50's Web Programming with Python and JavaScript course.  


## Outcomes
- Used SQL and migrations to create, modify, and build multiple databases
- Utilized forein keys and many-to-many relationships in SQL databases
- Learned more about Django's Models and ModelForms, including the use of choices
- Used the Django's admin interface to moderate the page
- Gained a better understanding of HTML and CSS
- Played around with CSS to style the webpages
- Used Git and GitHub for overall project management

### Technologies & Resources Used
- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="html" width="30" height="30"/> &emsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt = "python" width="30" height="30"/> &emsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="css" width="30" height="30"/> &emsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="django" width="30" height="30"/> &emsp; &emsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" alt="vscode" width="30" height="30"/> 
- Harry Potter images from <a href="https://harrypotter.fandom.com/wiki">Harry Potter Wiki</a>.

## Specifications 
- [x] Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings.
- [x] Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
- [x] The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).
- [x] Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.
	- [x] If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.
	- [x] If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.
	- [x] If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
	- [x] If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
	- [x] Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.
- [x] Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
- [x] Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.
- [x] Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.