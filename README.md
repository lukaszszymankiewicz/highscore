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
- [x] Add basic data bout scrapped score (number of overall score),
- [x] prettify search bar,
- [x] prettify result page,
- [x] add progress bar (scrapy usage is taking long).

Backend features:
- [x] Wrap this script into some kind of app framework (flask, Django etc),
- [x] Add cleaning of urls in musescore results (it is scaled down),
- [x] Add possibility to visit site with visible score,
- [ ] Add possibility to download scores (with convertion to default image extension),
- [x] Show some indication if there is none results found (another endpoint?),
- [ ] Add some validation for url (Item Pipelines and DropItem),
- [ ] Create docker-compose file for running app with one command,
- [ ] publish app on heroku (choose free options XD).

Nice to have features:
- [ ] Add keyboard control over searched results (arrow keys to move to next/previous),
- [ ] Sort scores by its "rating".
