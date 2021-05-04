# OHJELMISTOTEKNIIKKA 2021

## Yleistä

### [Sudokun säännöt](https://fi.wikipedia.org/wiki/Sudoku)

"Sudoku on logiikkapeli, jossa tehtävänä on täyttää neliönmuotoinen ruudukko merkeillä niin että jokaisella vaakarivillä ja pystyrivillä sekä jokaisessa osaneliössä käytetään samaa merkkiä tasan yhden kerran. Ruudukossa on aluksi valmiina jo muutama merkki. Yleisin sudoku on 9 × 9 -ruudukko, joka on jaettu yhdeksään 3 × 3 ruudun osaneliöön, ja merkkeinä käytetään numeroita 1–9."

## Dokumentaatio

- [Työaikakirjanpito](https://github.com/Aikamoine/ot-harjoitustyo/blob/master/documentation/tyoaikakirjanpito.md)
- [Vaatimusmäärittely](https://github.com/Aikamoine/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/Aikamoine/ot-harjoitustyo/blob/master/documentation/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/Aikamoine/ot-harjoitustyo/blob/master/documentation/kayttohje.md)

## Komennot

### Asennus ja käynnistys

- Asenna Poetryn avulla riippuvuudet komentorivillä:
```bash
poetry install
```
- Ensimmäisellä kerralla suorita aloitusasetukset:
```bash
poetry run invoke initialize
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
