# Widgets in Flutter
## Introduction
What is a widget?
You might have seen and used the widgets on Android and iOS.
They are tiles which hold content and can update themselves.
Flutter expands on the concept of widgets.

In Flutter, *everything is a widget.*
The buttons, checkboxes, sliders, textboxes etc. are all are widgets.
Moreover, even layout is a widget.
You can also group two or more widgets together to create another widget.

## Installing Android Studio and Flutter
Follow the instructions below to install and test your setup.
If you have already installed Flutter, jump directly to step 3.
1. Install Flutter: see https://flutter.dev/docs/get-started/install.
2. Setup Android Studio: read https://flutter.dev/docs/get-started/editor?tab=androidstudio.
3. Test that everything works by following the instructions on https://flutter.dev/docs/get-started/test-drive?tab=androidstudio.

>**NOTE:**
>1. You might also require JDK 8, which can be obtained from [here](https://adoptopenjdk.net/?variant=openjdk8&>jvmVariant=hotspot).
>2. It is also recommend to set the `JAVA_HOME` and `JDK_HOME` environment variables.
>3. A physical device can be very helpful for testing your apps if you have less than 16 GB of RAM.
>4. Alternatively, you can also test your apps in the web browser.

## A Simple App
Now it is time to create a simple app.
Let's make an app which displays "Hello World."
Follow the steps in [this tutorial](https://flutter.dev/docs/get-started/codelab#step-1-create-the-starter-flutter-app).
**Only follow Step 1 in the previous link. We will cover Step 2 later in the course.**

We reiterate the important observations from the tutorial:
1. The `main()` method uses arrow (`=>`) notation. Use arrow notation for one-line functions or methods.
2. The app extends `StatelessWidget`, which makes the app itself a widget. *In Flutter, almost everything is a widget, including alignment, padding, and layout.*
3. The `Scaffold` widget, from the Material library, provides a default app bar, and a body property that holds the widget tree for the home screen. The widget subtree can be quite complex.
4. A widget's main job is to provide a `build()` method that describes how to display the widget in terms of other, lower level widgets.
5. The body for this example consists of a `Center` widget containing a `Text` child widget. The `Center` widget aligns its widget subtree to the center of the screen.


## More Widgets
In this section, we will explore more widgets.
You can find all the UI widgets provided by Flutter in the [widget catalog](https://flutter.dev/docs/development/ui/widgets/material).

### <b>[Button](https://api.flutter.dev/flutter/material/ElevatedButton-class.html)</b>
Flutter has two types of buttons: `ElevatedButton` and `TextButton`.
Both have a similar functionality and only differ in the visual style.
Follow the short tutorial on creating an `ElevatedButton` [here](https://api.flutter.dev/flutter/material/ElevatedButton-class.html). Don't forget to press the "Run" button.

You can set the `onPressed` property to any function you wish.

Here are some important observations:
1. If the `onPressed` property is set to `null`, the button is disabled.
2. If the `onPressed` property is set to `() {}`, the button is enabled. Here `() {}` represents an empty function, which does nothing.

### <b>[Container](https://api.flutter.dev/flutter/widgets/Container-class.html)</b>
Container is a convenience widget that combines common painting, positioning and sizing of widgets.
It is often useful while building complex UI.

Run the command below on the command prompt (for Windows) or Terminal (on GNU/Linux and macOS):
```
git clone https://github.com/vedk/flutter_container_example.git
```
This repo contains the complete code for making a container and even rotating it.
You can read more about it from [here](https://api.flutter.dev/flutter/widgets/Container-class.html).

**Get a feel for how things work in Flutter. You keep composing functions, i.e. f(g(x)), to build the UI.
The functions which you compose are constructors of the class with the same name.**

### <b>[Row](https://api.flutter.dev/flutter/widgets/Row-class.html) and [Column](https://api.flutter.dev/flutter/widgets/Column-class.html)</b>
`Row` is a widget that displays its children in a horizontal array.
`Column` is a widget that displays its children in a vertical array.
These widgets are often used for layout.
Note that these widgets do not have scrolling capabilities if the contents overflow.

Clone the following project and to get an understanding of how to use `Row` or `Column`.
```
git clone https://github.com/vedk/flutter_column_example
```

Often, the contents will require the use of an `Expanded` widget for proper spacing.
Read [this](https://api.flutter.dev/flutter/widgets/Row-class.html) entry on `Row` to understand the use of `Expanded`.

### <b>Checkbox</b>
You are probably familiar with a checkbox.
But in Flutter the checkbox along with many other widgets is *special.*
**In Flutter the checkbox does not update its UI state (i.e. checked/unchecked) by itself when it is tapped.**
This brings us to one of the most important principles in Flutter:
> **In Flutter the UI is a function of state, i.e. UI = f(state)**.
> Thus when the state changes, ***you must*** call the `setState()` function.

Once this is understood, clone the following repo to see the above principle in action.
```
git clone https://github.com/vedk/flutter_checkbox_example.git
```
Focus on the lines 41-46 in lib/main.dart
```dart
onChanged: (bool? value) {
            setState(() {
              // if you comment out the statement below, the checkbox will not
              // change state
              isChecked = value!;
            });
```
See how when the state changes on tapping the checkbox, the `setState()` function is called which changes the UI state of the checkbox.
Flutter maintains a distinction between the UI state and internal state of the widgets.
`setState()` is responsible for redrawing the widgets to match the afore mentioned two states by calling the `build()` function. You have to make sure that you call `setState()` whenever the UI must be updated.

### <b>A slight detour...</b>
You might have observed that in many of our programs, the classes extends (i.e. inherit) `StatelessWidget`, `StatefulWidget` and `State<T>`.

A stateless widget never changes. It is never redrawn due to any user interaction. `Icon`, `IconButton` and `Text` are examples of stateless widgets. Stateless widgets subclass `StatelessWidget`.

A stateful widget is dynamic: for example, it can change its appearance in response to events triggered by user interactions or when it receives data. `Checkbox`, `Radio`, `Slider`, `InkWell`, `Form`, and `TextField` are examples of stateful widgets. Stateful widgets subclass `StatefulWidget`.

A widget's state is stored in a subclass of `State<T>` object, separating the widget's state from its appearance. The state consists of values that can change, like a slider's current value or whether a checkbox is checked. When the widget's state changes, the state object calls setState(), telling the framework to redraw the widget.

### <b>[BottomNavigationBar](https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html)</b>
A widget that's displayed at the bottom of an app for selecting among a small number of views, typically between three and five.
Instagram has one.

See [this link](https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html) and follow the given code.
You should be able to follow along.
Notice how the `setState()` function is used.

### <b>[TextField](https://api.flutter.dev/flutter/material/TextField-class.html)</b>
A text field lets the user enter text, either with hardware keyboard or with an onscreen keyboard.
Read the description and the code from [here](https://api.flutter.dev/flutter/material/TextField-class.html).

Some important points:
1. The [`TextEditingController`](https://api.flutter.dev/flutter/widgets/TextEditingController-class.html) will take care to change the UI state of the `TextField` as you type text.
2. The `dispose()` method is similar to what is called destructor in C++.

## Where next?
The widgets covered here are just a fraction of what are available.
Checkout the [widget catalog](https://flutter.dev/docs/development/ui/widgets/material) for more widgets.