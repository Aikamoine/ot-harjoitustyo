# Vaatimusmäärittely - Sudoku-harjoitustyö

## Sovelluksen toiminta
Sovelluksen avulla käyttäjä voi pelata Sudoku-pelejä itseään vastaan. Sovellus toimii paikallisessa ympäristössä ja sillä on yksi käyttäjä kerrallaan. 

### [Sudokun säännöt](https://fi.wikipedia.org/wiki/Sudoku)
"Sudoku on logiikkapeli, jossa tehtävänä on täyttää neliönmuotoinen ruudukko merkeillä niin että jokaisella vaakarivillä ja pystyrivillä sekä jokaisessa osaneliössä käytetään samaa merkkiä tasan yhden kerran. Ruudukossa on aluksi valmiina jo muutama merkki. Yleisin sudoku on 9 × 9 -ruudukko, joka on jaettu yhdeksään 3 × 3 ruudun osaneliöön, ja merkkeinä käytetään numeroita 1–9."

## Käyttöliittymä
Sovelluksessa on kolme eri näkymää. Aloitusruudulta valitaan millaisen pelin haluaa aloittaa - itse syötetyn sudokun vai valmiiksi tallennetun. Valinnasta riippuen aukeaa joko peliruutu suoraan tai sitten aukeaa ruutu, jossa voi täyttää sudokupelin aloitusnumerot ja sen jälkeen aloittaa kyseisen pelin.

## Perusversion vaatimusmäärittely
- Peli on tyypillinen 9 x 9 sudoku (tehty)
- Käyttäjä voi aloittaa pelin (tehty)
- Käyttäjä pystyy syöttämään pelin täyttämättömiin ruutuihin numeroita 1 - 9 (tehty)
- Käyttäjä ei voi syöttää mihinkään kohtaan sellaista numeroa, jonka syöttäminen rikkoisi sudokun sääntöjä (tehty)
- Ohjelma tunnistaa kun ruudukko on täytetty ja onnittelee käyttäjää sydämellisesti (tehty)
- Pelillä on graafinen käyttöliittymä
- Pelaaja voi arpoa uuden pelin riittävän suuresta joukosta valmiita sudokuja

## Jatkokehitysideoita
- Pelitilan voi tallentaa ja palauttaa sessioiden välillä
- Ohjelma osaa ehdottaa yhtä seuraavaa oikeaa numeroa
  - myös automaattitoiminto pelin ratkaisemiseen
- Mahdollisuus tehdä eri kokoisia sudokuja
- Valmiit sudokut on ryhmitelty vaikeustason mukaan, käyttäjä voi aloittaessa valita minkätasoisen pelin haluaa
- Tyhjiin ruutuihin voi merkitä muistiinpanoksi/testiksi pieniä numeroita
