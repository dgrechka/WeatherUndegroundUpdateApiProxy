# Weatherundeground weather station data send fix

[![Build Status](https://drone.k8s.grechka.family/api/badges/dgrechka/WeatherUndegroundUpdateApiProxy/status.svg)](https://drone.k8s.grechka.family/dgrechka/WeatherUndegroundUpdateApiProxy)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/dgrechka/WeatherUndegroundUpdateApiProxy?sort=semver)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/dgrechka/weather-underground-update-proxy?label=docker%20image&sort=semver)
![Docker Pulls](https://img.shields.io/docker/pulls/dgrechka/weather-underground-update-proxy)


## The issue
Some wheather stations (e.g. [wh2600](https://www.foshk.com/cables/wh2600.html)) while following [the wunderground protocol](https://support.weather.com/s/article/PWS-Upload-Protocol?language=en_US![image](https://user-images.githubusercontent.com/5637547/203302566-91ff80d3-f555-421f-a218-5bf30786b061.png)
) in sending live measured data erroneously set `host:` HTTP header to IP address instead of using domain name.

```
GET /weatherstation/updateweatherstation.php?ID=IVOLKOVS4&PASSWORD=XXXXXXXXX&tempf=26.4&humidity=88&dewptf=23.4&windchillf=22.5&winddir=17&windspeedmph=3.36&windgustmph=4.92&rainin=0.00&dailyrainin=0.00&weeklyrainin=0.00&monthlyrainin=0.28&yearlyrainin=16.82&solarradiation=0.00&UV=0&indoortempf=56.5&indoorhumidity=25&baromin=29.86&lowbatt=2&dateutc=2022-11-21%2013:29:52&softwaretype=WH2600GEN_V2.2.5&action=updateraw&realtime=1&rtfreq=5 HTTP/1.0
Accept: */*
Host: 52.22.134.222
Connection: Close
```

Which results in getting 404 reply.

To fix the issue the `host` must be set to domain name.

## Workaround solution (what this repo does)

Proxy the request through the web service which properly set the `host` header.

## How to use

1. Deploy the [built docker image (published on docker hub)](https://hub.docker.com/r/dgrechka/weather-underground-update-proxy).

e.g. with docker compose (replace IP address with proper value)
```
version: '2'

services:
  ui:
    image: dgrechka/weather-underground-update-proxy:latest
    restart: always
    ports:
      - 10.0.12.1:5000:5000
```

2. Point the whether station to send the data to the deployed service
3. The live data now should be successfully submitted to weather underground
