## Highscore

Flask app for aggregating musial score from many sites!

To run first build docker image:

```
docker run -d -p 8050:8050 scrapinghub/splash
```

And then go to src directory:

```
cd src/scrappers/
```

from where you can run scrapy spider (scrapper script)

```
python run.py
```

by now it will scrap SONG value parameter and save it into result.json


IN PROGESS:

- Add basic frontend (gallery of score first pages)


TODO:

~~-  Wrap this script into some kind of app framework (flask, Django etc)~~

- Add cleaning of urls in musescore results (it is scaled down)
- Add possibility to visit site with visible score 
