The API for url validation can be accessed at https://wikimedia-url-validation.herokuapp.com/ (since it's hosted on heroku, it might take a few seconds to wake up. So the first request might be slow to respond.)

Usage: Send a POST request to `/` with a `url` field in the request body containing the url to be validated. You will recieve a response detailing if the url is allowed, or not, with an appropriate status code.

# Example Usage

**Request**
```
{
    "url":"https://en.wikipedia.org/wiki/CODA_(2021_film)"
}
```
**Response**
```
Status: 400 Bad Request
{
    "detail": "Wikipedia articles not allowed!"
}
```
---
**Request**
```
{
    "url":"https://summerofcode.withgoogle.com/about"
}
```
**Response**
```
Status: 200 OK
{
    "url": "https://summerofcode.withgoogle.com/about"
}
```
---
**Request**
```
{
    "url":"https://www.google.com/search?q=gsoc"
}
```
**Response**
```
Status: 400 Bad Request
{
    "detail": "Search engine results not allowed!"
}
```