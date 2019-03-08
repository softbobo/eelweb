# [softbobo/eelweb](https://github.com/softbobo/eelweb)

This is becoming a website for EEL throughout the next weeks.

This is being developed in Python 3.7.2, but should work from Python 3.3 on (no guarantee given). You can easily try this out on your own machine. 

## Installation

Clone the repo:

```bash
$ git clone git@github.com:softbobo/eelweb.git
$ cd eelweb
```

Create and activate your virtual environment:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install the dependencies:

```bash
$ pip install -r requirements.txt
```

## Usage

With your virtualenv activated, run: 

```bash
$ flask run
```
This sets up a very basic server, which allows you to access the app in your browser under `https://localhost:5000`.

## TODO

- add license 
- set up navigation between sub-urls
- set up logging

