# Widgets in Flutter
## Introduction
What is a widget?
You might have seen and used the widgets on Android and iOS.
They are tiles which hold content and can update themselves.
Flutter takes the concept of widgets to the next level.

In Flutter, *everything is a widget.*
The buttons, checkboxes, sliders, textboxes etc. are all are widgets.
Moveover, even layout is a widget.
You can also group two or more widgets together to create another widget.

## Installing Android Studio and Flutter
Follow the instructions below to install and test your setup.
If you have already installed Flutter, jump directly to step 3.
1. Install Flutter: see https://flutter.dev/docs/get-started/install.
2. Setup Android Studio: read https://flutter.dev/docs/get-started/editor?tab=androidstudio.
3. Test that everything works by following the instructions on https://flutter.dev/docs/get-started/test-drive?tab=androidstudio.

>**NOTE:**
>1. You might also require JDK 8, which can be obtained from [here](https://adoptopenjdk.net/?variant=openjdk8&>jvmVariant=hotspot).
>2. It is also recommened to set the `JAVA_HOME` and `JDK_HOME` environment variables.
>3. A physical device can be very helpful for testing your apps if you have less than 16 GB of RAM.

## A Simple App
Now it is time to create a simple app.
Let's make an app which displays "Hello World."
Follow the steps in [this tutorial](https://flutter.dev/docs/get-started/codelab#step-1-create-the-starter-flutter-app).
**Only follow Step 1 in the previous link. We will cover Step 2 later in the course.**

We reiterate the important observations from the tutorial:
1. The `main()` method uses arrow (`=>`) notation. Use arrow notation for one-line functions or methods.
2. The app extends `StatelessWidget`, which makes the app itself a widget. *In Flutter, almost everything is a widget, including alignment, padding, and layout.*
3. The `Scaffold` widget, from the Material library, provides a default app bar, and a body property that holds the widget tree for the home screen. The widget subtree can be quite complex.
4. A widget’s main job is to provide a `build()` method that describes how to display the widget in terms of other, lower level widgets.
5. The body for this example consists of a `Center` widget containing a `Text` child widget. The `Center` widget aligns its widget subtree to the center of the screen.


## More Widgets
In this section, we will explore more widgets.
You can find all the UI widgets provided by Flutter in the [widget catalog](https://flutter.dev/docs/development/ui/widgets/material).

### <b>Buttons</b>
Flutter has two types of buttons: `ElevatedButton` and `TextButton`.
Both have a similar functionality and only differ in the visual style.
Follow the short tutorial on creating an `ElevatedButton` [here](https://api.flutter.dev/flutter/material/ElevatedButton-class.html).

Here are some important observations:
1. If the `onPressed` property is set to `null`, the button is disabled.
2. If the `onPressed` property is set to `() {}`, the button is enabled. Here `() {}` represents an empty function, which does nothing.

### <b>Container</b>
Container is a convenience widget that combines common painting, positioning and sizing of widgets.
It is often useful while building complex UI.

Run the command on the command prompt (for Windows) or Terminal (on GNU/Linux and macOS):
```
git clone https://github.com/vedk/flutter_container_example.git
```
This repo contains the complete code for making a container and even rotating it.
You can read more about it from [here](https://api.flutter.dev/flutter/widgets/Container-class.html).

**Get a feel for how things work in Flutter. You keep composing functions, i.e. f(g(x)), to build the UI.
The functions which you compose are construtors of the class with the same name.**

### <b>Checkbox</b>