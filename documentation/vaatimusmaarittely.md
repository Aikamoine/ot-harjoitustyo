# Vaatimusmäärittely - Sudoku-harjoitustyö

## Sovelluksen toiminta
Sovelluksen avulla käyttäjä voi pelata Sudoku-pelejä itseään "vastaan". Sovellus toimii paikallisessa ympäristössä ja sillä on yksi käyttäjä kerrallaan. 

### [Sudokun säännöt](https://fi.wikipedia.org/wiki/Sudoku)
"Sudoku on logiikkapeli, jossa tehtävänä on täyttää neliönmuotoinen ruudukko merkeillä niin että jokaisella vaakarivillä ja pystyrivillä sekä jokaisessa osaneliössä käytetään samaa merkkiä tasan yhden kerran. Ruudukossa on aluksi valmiina jo muutama merkki. Yleisin sudoku on 9 × 9 -ruudukko, joka on jaettu yhdeksään 3 × 3 ruudun osaneliöön, ja merkkeinä käytetään numeroita 1–9."

## Käyttöliittymä
Sovelluksessa on kolme eri näkymää. Aloitusruudulta valitaan millaisen pelin haluaa aloittaa - itse syötetyn sudokun vai valmiiksi tallennetun. Valinnasta riippuen aukeaa joko peliruutu suoraan tai sitten aukeaa ruutu, jossa voi täyttää sudokupelin aloitusnumerot ja sen jälkeen aloittaa kyseisen pelin.

Päivitys 2.5.: Poistettu itse luodun sudokun lisääminen käyttöliittymän vaatimuksista - sen sijaan tehty mahdollisuus lisätä csv-muotoinen sudoku peliin.

## Perusversion vaatimusmäärittely
- Peli on tyypillinen 9 x 9 sudoku (tehty)
- Käyttäjä voi aloittaa pelin (tehty)
- Käyttäjä pystyy syöttämään pelin täyttämättömiin ruutuihin numeroita 1 - 9 (tehty)
- Käyttäjä ei voi syöttää mihinkään kohtaan sellaista numeroa, jonka syöttäminen rikkoisi sudokun sääntöjä (tehty)
- Ohjelma tunnistaa kun ruudukko on täytetty ja onnittelee käyttäjää sydämellisesti (tehty)
- Pelillä on graafinen käyttöliittymä (tehty)
- Pelaaja voi arpoa uuden pelin riittävän suuresta joukosta valmiita sudokuja (tehty)
- Pelin voi tallentaa ja palauttaa (tehty)
- Pelimenusta voi mennä päämenuun (tehty)
- Pelimenusta voi pyytää antamaan yhden oikean numeron (tehty)

## Jatkokehitysideoita
- Mahdollisuus tehdä eri kokoisia sudokuja
- Tyhjiin ruutuihin voi merkitä muistiinpanoksi/testiksi pieniä numeroita
- Sudokun rivi/sarake/ruudukko välähtää punaisena sen mukaan, mikä virhe estää arvon syöttämisen
- Mahdollisuus pitää tallennettuna ja ladattavissa useampi peli kerrallaan
- Virheviesti käyttäjälle, joka yrittää ladata tallennetun pelin kun sellaista ei ole
