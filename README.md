## Highscore

Flask app for aggregating musial score from many sites!

To run first build docker image:

```
docker run -d -p 8050:8050 scrapinghub/splash
```

And run flask app by using command:

```
python run.py
```

IN PROGESS:

Frontend features:
- ~~ Add basic data bout scrapped score (number of overall score) ~~
- ~~ prettify search bar ~~
- ~~ prettify result page ~~
- ~~ add progress bar (scrapy usage is taking long) ~~

TODO:

- ~~ Wrap this script into some kind of app framework (flask, Django etc)~~
- ~~ Add cleaning of urls in musescore results (it is scaled down) ~~
- Add possibility to visit site with visible score 
- Add possibility to download scores (with convertion to default image extension)
- Add some validation
- Create docker-compose file for running app with one command
- publish app on heroku (choose free options XD)
- add keyboard control over searched results (arrow keys to move to next/previous)
