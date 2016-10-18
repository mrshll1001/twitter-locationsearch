# twitter-locationsearch
Personal script for a friend.


## Prerequisites
The script requires you set up an app with apps.twitter.com, and retrieve your api token and secret. It also required that you generate your user's api token and secret. These should be pasted into the string variables in ```main.py```

It also requires that your system has tweepy installed:

### Installing tweepy on a mac

First we install easy_install. Open Terminal and type:
```
curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python
```
Next we use easy_install to install pip, the Python package manager

```
sudo easy_install pip
```
Now, we use pip to install tweepy
```
sudo pip install tweepy
```

Tweepy should be set up for you to use

## Usage
Run from the terminal with
```
python main.py
```

Follow the prompts on-screen. When the script finishes it will have written the results to a csv file in the same folder. Be aware that Twitter limites api usage in 15 min blocks. Once you hit that limit, you'll need to wait 15 mins before running the script again.
