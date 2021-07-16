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






