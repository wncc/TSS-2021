# Week 3

We hope that you are clear with your Week-2 concepts.
You should now be familiar with the basics of Flutter.
This week we will cover those topics which will enable you to make reak world apps.

In general, any useful app will get some data from the internet.
This week, you will learn how this is done.

You will also learn about Firebase, a service provided by Google.
Firebase enables you to add features like database, login, storage etc. to your app.

We shall cover the following topics in Week 3.
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

# Demonstration App
Since now you all know what an API is and what is it used for, you can finally make an App using flutter which fetches data from an API.
Fetching data from the internet is necessary for most apps. Luckily, Dart and Flutter provide tools, such as the http package, for this type of work.

This recipe uses the following steps:

1. Add the http package.
2. Make a network request using the http package.
3. Convert the response into a custom Dart object.
4. Fetch and display the data with Flutter.

Some common apps which require the fetching of data are Weather Report app, News App and World Clock App etc.

For the demonstration purpose we'll be making a World Clock App using the [Net Ninja](https://www.youtube.com/watch?v=WghpP9W2vXo&list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ&index=22&ab_channel=TheNetNinja) playlist.
For this week you'll have to watch videos from 22 to 35. Watch these videos very carefully as they are very important for learning how to fetch the data from an API!

## Note
It's very much possible that the package that you use might be deprecated, in that case look for other similar packages on flutter's website. You may DM the course moderators if you face any such issue.
In case you have any doubts in API or the implementation of the packages used, feel free to discuss in the telegram group. 

# **Introduction to Firebase**
Firebase is a Backend-as-a-Service (Baas). It provides developers with a variety of tools and services to help them develop quality apps, grow their user base, and earn profit. It is built on Google’s infrastructure.
It is categorized as a NoSQL database program, which stores data in JSON-like documents.
Developers relying on this platform get access to services that they would have to develop themselves, and it enables them to lay focus on delivering robust application experiences.

### What type of apps can be developed?
* Android
* iOS
* Web

Here is a good article on Firebase - [Medium](https://medium.com/firebase-developers/what-is-firebase-the-complete-story-abridged-bcc730c5f2c0)

## **Key Features**

#### 1. Authentication
Authentication is basically the registration, sign in and user verification part of the app.
Firebase Authentication provides backend services to authenticate users to your app. It supports authentication using passwords, phone numbers, popular federated identity providers like Google, Facebook and Twitter, and more.

Video about Firebase Authentication - [YouTube](https://www.youtube.com/watch?time_continue=1&v=8sGY55yxicA&feature=emb_logo)

#### 2. Realtime Database
The Firebase Realtime Database is a cloud-hosted database. Data is stored as JSON and synchronized in realtime to every connected user. When you build cross-platform apps with our iOS, Android, and JavaScript SDKs, all the users share one Realtime Database instance and automatically receive updates with the newest data.

Video about Realtime Database - [YouTube](https://www.youtube.com/watch?v=U5aeM5dvUpA)

#### 3. Hosting
Firebase Hosting allows fast and secure hosting for our web application, static and dynamic content, and microservices. It is production-grade web content hosting for the developers. We can easily and quickly deploy web apps and serve both static and dynamic content.

#### 4. Storage
Cloud Storage for Firebase lets you upload and share user generated content, such as images and video, which allows you to build rich media content into your apps. Your data is stored in a Google Cloud Storage bucket. Cloud Storage for Firebase lets you securely upload these files directly from mobile devices and web browsers.

Video about Firebase Storage - [YouTube](https://www.youtube.com/watch?v=_tyjqozrEPY)

Here you can find everything about Firebase and its services - [Documentation](https://firebase.flutter.dev/)

##### More Optional Content
Will be covered in week 4

* [Connect Flutter App with Firebase](https://firebase.google.com/docs/flutter/setup?platform=ios)
* [Getting Started with Firebase](https://www.raywenderlich.com/7426050-firebase-tutorial-for-flutter-getting-started)
* [Getting Started with Firebase Realtime Database](https://medium.com/firebase-tips-tricks/how-to-use-firebase-realtime-database-with-flutter-ebd98aba2c91)


# Assignment for Week-3

So for this week we learn about APIs so now we will be creating a ***Weather App*** using the Api offered by https://openweathermap.org/current (You will need to create an account for the api key) . Feel free to Explore the Api doc
and get to know more. You will be getting a json file as a product from the api and you will need a jsondecoder. You can read more about them from the flutter documentation. 

For location you will need to include a relevant flutter package:
- https://pub.dev/packages/location
- https://pub.dev/packages/flutter_spinkit (for the loading screen)
- import 'package:http/http.dart' as http; (for using the url from the api to get the data)

For the App it should have 2 features and 3 screens. 
- Feature 1 : Gets the location as soon as the app loads and displays the Weather.
- Feature 2 : The user can search for the location and get the weather.
- Screen 1 : Loading screen - Gets the loaction and weather from that and then sends it to the Weather Screen
- Screen 2: Weather screen - Has two buttons on the top One for detecting the location again and the other for city search (from the searching screen)
- Screen 3: Searching Screen - Takes the input as the name of a city 
- The required permissions will need to be given too:
- ![image](https://user-images.githubusercontent.com/73156496/125968988-a2704f1c-6691-4b8d-ad3b-419a3549d446.png)


The snapshots of the structure and the given screens is given below-
 - ![image](https://user-images.githubusercontent.com/73156496/125969241-0f3ad8c9-00a8-4353-8f0b-2f1a38bde7ce.png)
 - ![image](https://user-images.githubusercontent.com/73156496/125969288-904c0e95-fbff-48db-a075-94f3afa36c2e.png)
 - ![image](https://user-images.githubusercontent.com/73156496/125969340-96002be9-7bc8-4300-9142-578c60863ba2.png)

These set of permissions need to be set in the AndroidManifest.xml file (android/app/src/main/AndroidManifest.xml)
![image](https://user-images.githubusercontent.com/73156496/125969659-b4702f8e-9ed0-47c6-ab38-06630c02bd02.png)


<p align="center">Created with :heart: by <a href="https://www.wncc-iitb.org/">WnCC</a></p>
