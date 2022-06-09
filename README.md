# Instruction
> "Coffee Store Management"

## All endpoints
```bash
'register/' - To register a new user

'login/' - User login

'get-user/token/' - (e.g: get-user/234sdflasdg/) Pass the token and get the user name and the user role

'profile-info/' - Add profile info to the database

'add-coffee/' - Add a coffee items to the database

'get-coffee/' - Get all existing coffee items from database 

'get-single-item/coffee_id' - (e.g: get-single-item/3/) Use coffee item id instead of coffee_id to get data of single item of coffee

'update-coffee/coffee_id/' - (e.g: update-coffee/3/) Use coffee item id instead of coffee_id to update a existing coffee item

'add-recommended-coffee/' - Add a recommend coffee items to the database

'get-recommended-coffee/' -  Get all existing recommend coffee items from database 

'delete-recommended-coffee/recommend_coffee_id/' - (e.g: ddelete-recommended-coffee/3/) Pass the recommend_coffee_id to delete

'add-is-favourite/' - Add a coffee item to favourite list

'get-is-favourite/' - Get all favourite coffee items that user marked as favourite

'is-favourite/is_favourite_id/' - (e.g: is-favourite/3/) pass the is_favourite_id to make it true to false.

'get-order/' - Get all order

'make-order/' - User can make a order

'delete-order/order_id/' - (e.g: delete-order/3/) Use the order ID to delete an order from database
```

## Register - POST Request
```bash
How to pass json data using 'register/' endpoint-
{
   "name": "test",
   "email": "test@gmail.com",
   "username": "test",
   "password": "test123",
   "role": "buyer",
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

## Add profile info - POST Request
```bash
How to pass json data using 'profile-info/' endpoint-
Pass image file into "profile"

{
    "id": 1,
    "profile": "image file",
    "contact": 17,
    "address": "chittagong",
    "user": "mosta",
    "shopName": 1
}

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Add a coffee item - POST Request
```bash
How to pass json data using 'add-coffee/' endpoint-
In image field pass the image file and in shopName you need to use register shop name from server, Otherwise it will throw an error
{
   "name": "Espresso",
   "image": "test.jpg"
   "ratings": "5",
   "taste": "excellent",
   "coffeeType": "cappuccino",
   "description": "desc......"
   "price": "250",
   "shopName": "test",
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

## Update a coffee item - PATCH Request
```bash
How to pass json data using 'update-coffee/coffee_id/' endpoint-
Remember it is not necessary to use all fields. Use those fields you want to update.
If you want to update coffee name then just use name field-
{
  "name": "test"
}

All fields-
{
   "name": "Espresso",
   "image": "test.jpg"
   "ratings": "5",
   "taste": "excellent",
   "coffeeType": "cappuccino",
   "description": "desc......"
   "price": "250",
   "shopName": "test",
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
You need to pass the coffee_name
{
   "recommend": coffee_name,
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

## Delete a recommended coffee - DELETE Request
```bash
Use 'delete-recommended-coffee/recommended_coffee_id/' to delete a coffee item from recommended coffee table
and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Add a coffee item as favourite - POST Request
```bash
Use 'add-is-favourite/' to add an item as favourite.
How to pass json data using the endpoint-
{
    "user": "test",
    "favourite": true,
    "coffee": "test"
}

Remember you need to pass a register coffee name to add the item as favourite. you will get the item from 'get-coffee'

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Get favourite coffee items - GET Request
```bash
Use 'get-is-favourite/' to get all favourite items that user marked as favourite

and pass headers{
"Authorization": "Token ad6a56f22bba5043a1df2bc44655f205be7057a3"
}
Read flutter documentation for more info.
```

## Remove favourite coffee items from favourite list - PATCH Request
```bash
Use 'is-favourite/favourite_id/' to remove an item from favourite list
How to pass json data using the endpoint-
{
  "favourite": false
}

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
