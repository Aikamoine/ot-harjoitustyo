# OHJELMISTOTEKNIIKKA 2021

## Yleistä

### [Sudokun säännöt](https://fi.wikipedia.org/wiki/Sudoku)

"Sudoku on logiikkapeli, jossa tehtävänä on täyttää neliönmuotoinen ruudukko merkeillä niin että jokaisella vaakarivillä ja pystyrivillä sekä jokaisessa osaneliössä käytetään samaa merkkiä tasan yhden kerran. Ruudukossa on aluksi valmiina jo muutama merkki. Yleisin sudoku on 9 × 9 -ruudukko, joka on jaettu yhdeksään 3 × 3 ruudun osaneliöön, ja merkkeinä käytetään numeroita 1–9."

### Tämän hetkinen toiminta

Tällä hetkellä sovellus toimii komentorivillä. Se tulostaa yhden esimerkkisudokun ilman mitään muotoiluja ruutujen välillä. Tyhjään ruutuun voi syöttää numeron.

Kun ohjelma käynnistyy, komentoriville tulostuu sudoku-peli. Voit lisätä numeroita tyhjiin ruutuihin kirjoittamalla komentoriville koordinaatit ja arvon muodossa "x,y,arvo". Taulukon origo on vasemmassa yläkulmassa, eli vasemman yläkulman sijanti on 0,0. Vasempaan yläkulmaan voi siis sijoittaa arvon 6 kirjoittamalla "0,0,6".

Pelin suorittaminen loppuu, kun kirjoitat "end". Saat pelin automaattisesti ratkaistua, kun kirjoitat "solve". Yli viisi merkkiä pitkät syötteet jätetään huomioimatta. Komentorivikäyttöliittymästä ei ole tarkoituskaan tehdä lopullista versiota, joten tämän syötteen validointiin ei erityisesti tulla panostamaan.

## Dokumentaatio

- [Työaikakirjanpito](https://github.com/Aikamoine/ot-harjoitustyo/blob/master/documentation/tyoaikakirjanpito.md)
- [Vaatimusmäärittely](https://github.com/Aikamoine/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/Aikamoine/ot-harjoitustyo/blob/master/documentation/arkkitehtuuri.md)

## Komennot

### Asennus ja käynnistys

- Asenna Poetryn avulla riippuvuudet komentorivillä:
```bash
poetry install
```
- Käynnistä ohjelma komennolla:
```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testikattavuusraportin saat luotua komennolla:

```bash
poetry run invoke coverage-report
```

Tiedostossa .pylintrc määritetyt tarkastukset suoritetaan komennolla:

```bash
poetry run invoke style-check
```
