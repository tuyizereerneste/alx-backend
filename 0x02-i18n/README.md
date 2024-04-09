0x02. i18n

"i18n" is a common abbreviation for "internationalization." The term is derived from the fact that there are 18 letters between the first "i" and the last "n" in the word "internationalization." Internationalization is the process of designing and developing software applications or products in a way that they can easily be adapted to different languages, regions without engineering changes.

TASKS:

1. First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title and “Hello world” as header h1.

2. In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

3. Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.

4. Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.

5. In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.

In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.
6. Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.

7. Change your get_locale function to use a user’s preferred local if it is supported.

The order of priority should be

Locale from URL parameters
Locale from user settings
Locale from request header
Default locale

8. Define a get_timezone function and use the babel.timezoneselector decorator.

The logic should be the same as get_locale:

Find timezone parameter in URL parameters
Find time zone from user settings
Default to UTC
