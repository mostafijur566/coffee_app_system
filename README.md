# Instruction
> "Coffee Store Management"

## All endpoints
```bash
'register/' - To register a new user

'login/' - User login

'get-user/token/' - (e.g: get-user/234sdflasdg/) Pass the token and get the user name and the user role

'add-coffee/' - Add a coffee items to the database

'get-coffee/' - Get all existing coffee items from database 

'get-single-item/coffee_id' - (e.g: get-single-item/3/) Use coffee item id instead of coffee_id to get data of single item of coffee

'update-coffee/coffee_id/' - (e.g: update-coffee/3/) Use coffee item id instead of coffee_id to update a existing coffee item

'add-recommended-coffee/' - Add a recommend coffee items to the database

'get-recommended-coffee/' -  Get all existing recommend coffee items from database 

'get-single-recommended-item/coffee_id' - (e.g: get-single-recommended-item/3/) Use coffee item id instead of coffee_id to get data of single item of coffee

'update-recommended-coffee/coffee_id/' - (e.g: update-coffee/3/) Use coffee item id instead of coffee_id to update a existing coffee item

'is-favourite/coffee_id/' - (e.g: is-favourite/3/) Use coffee item id instead of coffee_id to add the item as favourite

'get-favourite/' - Get all favourite coffee items that user marked as favourite

'get-order/' - Get all order

'make-order/' - User can make a order

'delete-order/order_id/' - (e.g: delete-order/3/) User the order ID to delete an order from database
```

## Register - POST Request
```bash
How to pass json data using 'register/' endpoint-
{
   "email": "test@gmail.com",
   "username": "test",
   "password": "test123"
   "role": "buyer"
}

And server will return a token save the token for future use.
```

## Login - POST Request
```bash
How to pass json data using 'login/' endpoint-
{
   "username": "test@gmail.com",
   "password": "test123"
}

And server will return a token save the token for future use.
```

## Get username and role - GET Request
```bash
Use 'get-user/token/' to get user info. You need to pass the token in the endpoint to get that user info.

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Add a coffee item - POST Request
```bash
How to pass json data using 'add-coffee/' endpoint-
{
   "name": "Espresso",
    "ratings": "5",
    "taste": "excellent",
    "coffeeType": "cappuccino",
    "price": "250",
    "img": "test.jpg",
    "shopName": "test",
    "coffeeShopID": "1235",
    "location": "Dhaka, Bangladesh",
    "user": "test"
}
and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Get all coffee - GET Request
```bash
Use 'get-coffee/' to get all coffee items from server
and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Get single item of coffee - GET Request
```bash
Use 'get-single-item/coffee_id/' to get single coffee item from server
and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Update a coffee item - PUT Request
```bash
How to pass json data using 'update-coffee/coffee_id/' endpoint-
{
   "name": "Espresso",
    "ratings": "5",
    "taste": "excellent",
    "coffeeType": "cappuccino",
    "price": "250",
    "img": "test.jpg",
    "shopName": "test",
    "coffeeShopID": "1235",
    "location": "Dhaka, Bangladesh",
    "user": "test"
}

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Add a Recommended coffee item - POST Request
```bash
How to pass json data using 'add-recommended-coffee/' endpoint-
{
   "name": "Espresso",
    "ratings": "5",
    "taste": "excellent",
    "coffeeType": "cappuccino",
    "price": "250",
    "img": "test.jpg",
    "shopName": "test",
    "coffeeShopID": "1235",
    "location": "Dhaka, Bangladesh",
    "user": "test"
}
and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Get all Recommended coffee - GET Request
```bash
Use 'get-recommended-coffee/' to get all coffee items from server
and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Get single recommended item of coffee - GET Request
```bash
Use 'get-single-recommended-item/coffee_id/' to get single coffee item from server
and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Update a coffee item - PUT Request
```bash
How to pass json data using 'update-recommended-coffee/coffee_id/' endpoint-
{
   "name": "Espresso",
    "ratings": "5",
    "taste": "excellent",
    "coffeeType": "cappuccino",
    "price": "250",
    "img": "test.jpg",
    "shopName": "test",
    "coffeeShopID": "1235",
    "location": "Dhaka, Bangladesh",
    "user": "test"
}

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Add a coffee item as favourite - PATCH Request
```bash
Use 'is-favourite/coffee_id' to add an item as favourite.
How to pass json data using the endpoint-
{
    "isFavourite": true
}

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Get favourite coffee items - GET Request
```bash
Use 'get-favourite/' to get all favourite items that user marked as favourite

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Get all order - GET Request
```bash
Use 'get-order/' to get all order.

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Make an order - POST Request
```bash
How to pass json data using 'make-order/' endpoint-
{
    "user": "test",
    "coffee_id": 1,
    "name": "test",
    "size": "M",
    "quantity": 1,
    "address": "Chittagong",
    "contact": "017****"   
}

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Delete an order - DELETE Request
```bash
Use 'delete-order/order_id/' to delete an order from server. You need to pass the order id to delete an order.

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```
