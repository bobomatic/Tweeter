# Tweeter
Twitter bot using Tweepy API

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Examples of Use](#examples-of-use)
* [Status](#status)
* [Sources](#sources)

## General Info
This project demonstrates some capabilities of the Tweepy Twitter API in Python.

## Technologies
This project is created with

Tweepy 3.10.0

## Setup
To run this project install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```
You will need a Twitter account and a Twitter API account.
Open keys.txt and paste in your twitter API keys and tokens, Save keys.txt

## Features
* displays user information (reads your twitter API auth codes from text file on local machine)
* displays recent tweets in your twitter feed
* displays the 5 most popular tweets based on the search_string you provide in the command line
* optional: retweets the most most popular tweet using your user account

### To do:
Further development will be required to:
- put authorisation info in a separate text file
- tidy up code (function/OO)

## Examples of Use

Usage: tweeter.py [none] search_string: [str] = ...

Output is displayed in the command line.

The following options are available:
* no options available

Code example:

`python3 tweeter.py olympics`
`python3 tweeter.py "Machine Learning"`

A search string is compulsory.

## Status
Basic demo functionality is complete.

## Sources
This project is inspired by Andrei Neagoie Python Zero to Mastery course:

https://www.udemy.com/course/complete-python-developer-zero-to-mastery
