# APIs
## Introduction
In basic terms, APIs are a set of functions and procedures that allow for the creation of applications that access data and features of other applications, services, or operating systems.

The following video and article are good places to understand more about APIs:
* https://www.youtube.com/watch?v=XGa4onZP66Q
* https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/

## Example
Here we will have a look at a small and simple example of an API: https://thatcopy.pw/catapi/rest/

This API will give you a random URL which points to a picture of a cat!

To test this API, visit https://thatcopy.pw/catapi/rest/ in any web browser.
You will see a webpage with text similar to the following:
```json
{"id":19,"url":"https://i.thatcopy.pw/cat/LsSZNPk.jpg","webpurl":"https://i.thatcopy.pw/cat-webp/LsSZNPk.webp","x":43.4,"y":44.97}
```

This is a JSON response. Visit the URL given in the `url` field. You you be greeted by a random cat!

Many common APIs give a similar JSON response. Many programming languages have special packages to extract data from such a JSON response.