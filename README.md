#    | PASSWORD LOCKER |


## Description
This application is used to store users online account credentials like account user names, email and passwords. Be warned that each session is stored in the RAM. So as soon as the application is closed, all data stored is lost.

## Specs
1. Add users.
2. Login as a user.
3. Display stored credentials.
4. Add credentials.
5. Copy account Details to clipboard.

## Setup

First clone this repo:

```
https://github.com/HarryThuku/Password-Locker-IP.git
```

Navigate into the project folder:

```
$ cd Password-Locker-IP
```

Install the projects' dependencies from the requirements.txt file:

```
$ pip install -r requirements.txt
```

You can now run the program by typing the following code in your terminal:

```
$ python interface.py
```
If you run into an error, try running the code by specifying the python version, example:
```
$ python3 interface.py
```

## How it Works

This is a simple image describing how the application works.

![usecaseDiagram](https://user-images.githubusercontent.com/40566766/55885094-59ca8500-5bba-11e9-8ea0-54fdb22a74f4.jpg)

## Security
The user logs into the system using a password. The passwords are neither hashed nor salted, as I did not have enough time to implement these features.

#### NOTE: This is an academic project. It therefore is in its beta version, hence may have some bugs.
