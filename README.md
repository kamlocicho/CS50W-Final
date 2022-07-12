## Distinctiveness and Complexity
The project is an ordinary e-commerce store. Among other projects, it stands out with the implementation of the basket, and usage of the [ImageField](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ImageField) allowing you to transfer files from frontend to the backend layer, store them in a files directory and finally display on pages. Project is using bootstrap as a CSS framework. Moreover, I implemented authentication system and ability to add items to a watchlist. Whole project contains 4 models and 6 views (all described below).

## How to run application
`pip install -r requirements.txt`

`python3 manage.py runserver`

## All views
- **Index view** - lists out all the products available.
- **Auth views** - allow full authentication.
- **Product view** - displays description, price and image with two buttons that allows to add item with given quantity to cart and add item to watchlist.
- **Category view** - displays all products from given category.
- **Watchlist view** - displays all watched products only if you are authenticated.
- **Cart view** - displays items in your cart with their quantity and total price, also displays button allowing you to remove items from cart.

## Models
- **User**
    - watchlist(ManyToMany relation to Product)
    - cart(ForeignKey to CartItem)
- **Product**
    - title
    - description
    - price
    - image(configured ImageField)
    - category(ForeignKey to Category)
- **Category**
    - name
- **CartItem**
    - product(ForeignKey to Product)
    - quantity

## Additional information
All the images are being saved in directiory ./files/products.

Products can me created only from admin page so that only admins can do it.

### Admin credentials
`username: test123`

`password: 123`
