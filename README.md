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
- number of overall score indicator,
- prettify search bar.

TODO:

- ~~ Wrap this script into some kind of app framework (flask, Django etc)~~
- ~~ Add cleaning of urls in musescore results (it is scaled down) ~~

- Add possibility to visit site with visible score 
- Add basic data bout scrapped score (number of overall score, author, number of pages and so on)
