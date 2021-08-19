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

## Features
* displays user information (hard coded
* places them in a destination folder

### To do:
* image processing options e.g. grayscale, resize, thumbnail

## Examples of Use

Usage: jpg2png [none] source_directory: [str] = ... target_directory: Optional[str] = ...

Converted files are placed in the target folder.

The following options are available:
* no options available

Code example:

`python3 jpg2png Pokedex/ my_pngs/`

If the target folder is omitted, a folder named 'converted' will be created in the current directory

## Status
Basic jpg to png functionality is complete.
Further development will be required to introduce image processing options

## Sources
This project is inspired by Andrei Neagoie Python Zero to Mastery course:

https://www.udemy.com/course/complete-python-developer-zero-to-mastery
