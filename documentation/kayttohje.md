# Sudoku-ohjelman käyttöohje

Ohjelman viimeisimmän julkaistun version löydät [täältä](https://github.com/Aikamoine/ot-harjoitustyo/releases).

## Asennus ja käynnistys

- Asenna Poetryn avulla riippuvuudet komentorivillä:
```bash
poetry install
```
- Käynnistä ohjelma komennolla:
```bash
poetry run invoke start
```

## [Sudokun säännöt](https://fi.wikipedia.org/wiki/Sudoku)

"Sudoku on logiikkapeli, jossa tehtävänä on täyttää neliönmuotoinen ruudukko merkeillä niin että jokaisella vaakarivillä ja pystyrivillä sekä jokaisessa osaneliössä käytetään samaa merkkiä tasan yhden kerran. Ruudukossa on aluksi valmiina jo muutama merkki. Yleisin sudoku on 9 × 9 -ruudukko, joka on jaettu yhdeksään 3 × 3 ruudun osaneliöön, ja merkkeinä käytetään numeroita 1–9."

## Pelaaminen

Pelin käynnistyessä aukeaa päävalikko:
![main_menu](./pictures/main_menu.png)

Täällä voit valita pelin vaikeusasteen, aloittaa valitun vaikeusasteen pelin, ladata aiemmin tallennetun pelin, tai sulkea ohjelman. Jos aikaisempaa peliä ei löydy tallennettuna, niin "Jatka edellistä" valinta alustaa uuden heleppo-tasoisen sudokun.

Kaikissa pelin valikoissa voit liikkua hiirellä tai nuolilla. Valitseminen onnistuu hiiren ykköspainikkeella tai enter-näppäimellä.

Pelin aloittaminen tai lataaminen johtaa peliruudukkoon:
![game_view](./pictures/game_view.png)

Näet korostettuna aina ruudun, johon arvoa ollaan syöttämässä. Voit valita toisen ruudun nuolinäppäimillä, tai hiiren ykköspainikkeella. Uuden arvon voi syöttää näppäimistön numeroriviltä, tai numpadista. Valitun arvon voi poistaa delete- tai backspace-painikkeella.

Numeron lisääminen onnistuu vain, jos lisäys on sudokun sääntöjen mukainen ja ruudussa ei ole alkuperäiseen asetelmaan kuuluva arvo. Poistaminen onnistuu, jos poistettava arvo ei kuulu sudokun alkuperäiseen asetelmaan.

Pelin aikana pääset menuun painamalla ESC-näppäintä tai hiiren kakkospainiketta:
![game_menu](./pictures/game_menu.png)

Jatka-valinnalla pääset takaisin käynnissä olevaan peliin. "Anna oikea numero" -valinta tuo oikeasta ratkaisusta numeron sudokussa valittuna olevaan ruutuun. "Tallenna ja palaa päävalikkoon" tekee juuri mitä sen voisi kuvitella tekevän - kuten tekee myös "Lopeta tallentamatta". Huomaa, että sovelluksessa voi olla tallennettuna kerrallaan vain yksi peli - edellisen yli kirjoitetaan armottomasti, jos tallennat sen päälle!

Kun saat ruudun täytettyä, aukeaa voittonäkymä, jossa sinua onnitellaan mahtavasta uroteostasi. Tästä näkymästä voit palata päävalikkoon aloittamaan uutta peliä, tai sulkea pelin.

Missä tahansa vaiheessa voit sammuttaa oikean yläreunan ruksista.
