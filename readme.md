Work in progress

To run first build docker image:

docker run -d -p 8050:8050 scrapinghub/splash


And then go to src directory:

cd src/scrappers/

Then you can run first (by now) spider

python run.py

by now it will scrap SONG value parameter and save it into result.json


TODO:
a) Wrap this script into some kind of app framework (flask, Django etc)
b) Add cleaning of urls
c) Add basic frontend (gallery of score first pages)
