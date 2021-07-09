# **Flutter Developer Packages**
Flutter supports using shared packages contributed by other developers to the Flutter and Dart ecosystems. This allows quickly building an app without having to develop everything from scratch. They are open source libraries of code that other people have created, which you can incorporate into your project to make work easy and less time-consuming.
You can find many open source packages, their different versions, examples, usage instructions on [pub.dev](pub.dev "pub.dev").

## **Using External Packages**
In this step, we'll see how to use an external open-source package, *english_words* for this particular tutorial, which contains a few thousand of the most used English words with some utility functions.
Here is a good tutorial on how to add and use the *english_words* package - [Youtube](https://www.youtube.com/watch?v=OYCyUV5919o) (recommended) or the flutter documentation - [Using Packages (flutter.dev)](https://flutter.dev/docs/get-started/codelab#step-2-use-an-external-package).

### What is **pubspec.yaml**
The pubspec file specifies dependencies that the project requires, such as particular packages (and their versions), fonts, or image files. It also specifies other requirements, such as dependencies on developer packages (like testing or mocking packages), or particular constraints on the version of the Flutter SDK.

## **Using Package in an App**
In this mini-app, we will use the *english_words* package, to create listview.
A good tutorial to create a listview using the external package **[Building a ListView in Flutter](https://medium.com/flutter-community/flutter-building-a-listview-in-flutter-3ea0c56dd496)**(recommended). Try to understand the code and write it rather than copy/pasting it.
This as also a tutorial to use *english_words* to create an infinite list view - [ProgrammerSought](https://www.programmersought.com/article/2539538887/).
It is also available on the Get Started Section of Flutter Documentation - [Create an Infinite Scrolling ListView](https://flutter.dev/docs/get-started/codelab#step-4-create-an-infinite-scrolling-listview).

If you want to know more details about list views, [this](https://pusher.com/tutorials/flutter-listviews/) is a good place to visit.

If you are facing any issues, you can refer to the following GitHub repo which contains a working app.
```
git clone https://github.com/vedk/flutter_package_try.git
```
Open the cloned project in Android Studio.
*You will have to click "pub get" in the pop up which comes up on bottom right.*