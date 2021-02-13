# Instructions
This test will test your ability to understand a new code base and make a change.

## Goal
The goal of this test is to extend the functionality of the "whalesay" web app to include a new
message ***by only editing "extension.py"***.
Specifically, a GET on /whalesay/carta should print out the 🐳 saying "This test was easy! 🎉" E.g. 

```
$ curl http://localhost:5000/whalesay/test

          This test was easy! 🎉
                    ##         .
              ## ## ##        ==
           ## ## ## ## ##    ===
       /"""""""""""""""""\___/ ===
      {                       /  ===-
       \______ O           __/
         \    \         __/
          \____\_______/

```

## Running the application
Open up a terminal and run the following command to launch the server in debug mode (it will automatically
reload when you change the code):

```
FLASK_APP=test_01.whalesay.app flask run  --reload
```

In a different terminal, you can run this command to test your code:
```
curl http://localhost:5000/whalesay/test
```

