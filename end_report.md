Vertaispalautteen lisäksi ryhmä laatii projektin kulusta pienen raportin (noin 2 sivua)

    Kerrataan jokaisen sprintin aikana kohdatut ongelmat (prosessiin-, projektityöskentelyyn- ja teknisiin asioihin liittyvät)
    Mikä sujui projektissa hyvin, mitä pitäisi parantaa seuraavaa kertaa varten
    Mitä asioita opitte, mitä asioita olisitte halunneet oppia, mikä tuntui turhalta
    Jos raportti puuttuu, vähennetään ryhmältä 2 pistettä
    Raportti palautetaan lisäämällä raporttiin linkki projektin GitHubin README:hen
    Raportista tulee ilmetä jokaisen projektiin osallistuneen nimi
    Raportin deadline perjantaina 22.12. klo 23:59

# Loppuraportti
Ryhmän Citeninja loppuraportti ohjelmistotuotannon miniprojektista.

Ryhmässä jäseninä olivat Santeri Tolonen, Jerry Lehtinen, Roni Bärman, Pauli Karels ja Niko Keurulainen.

## Sprinttien aikana kohdatut ongelmat
### Sprint 1 @ 16. - 23.11.2023
Tehtävien jakamisen käytänteet eivät olleet vielä täysin selkeät ensimmäisen sprintin aikana. Työ sujui kuitenkin tehokkaasti ja ohjelman runko saatiin rakenettua mallikkaasti. Iso määrä arkkitehtuuriin vaikuttavia päätöksiä tuli tehtyä lennosta, mutta myös refraktorointiin saatiin heti kiinnitettyä huomiota ja ohjelman runko pysyi pääasiallisesti hyvin selkeänä.

Testaaminen haki projektin alussa muotoaan ja githubiin tuli pushattua koodia, joka ei läpäissyt testiä.

Myös parikoodausta kokeiltiin heti alussa ja se koettiin mielekkääksi etenkin suunnitteluun ja pohdintaan liittyvissä töissä.

### Sprint 2 @ 23. - 30.11.2023
Toisen sprintin sprint backlog saatiin pilkottua pieniin ja hyvin hallittaviin työtehtäviin. Vastuut jaettiin selkeästi ja työaikaa arvioitiin ja seurattiin onnistuneesti.

Branchejä päästiin hieman kokeilemaan ja mergeäminen tuli tarpeeseen. 

Teknisesti ja ulkonäöllisesti sovellus kehittyi valtavasti, kun Flask otettiin käyttöö ja sovellus sai webbikäyttöliittymän.

Sprintin 2 jälkeen tehty retroperspektiivi oli todella onnistunut ja antoi tiimille hyvää dataa ja näkemystä työskentelyynsä. Fyysinen piirtotaulu auttoi hahmottamaan sprintin onnistumisia ja haasteita ja opit saatiin selkeästi ylös.

### Sprint 3 @ 30.11 - 7.12.2023
Edellisestä sprintistä oppineena, sprint 3 saatiin suunniteltua ja pilkottua sopivan kokoisiksi työtehtäviksi ja työskentely käytänteen hioituivat. 

Sprintin aikana sovellus kehittyi teknisesti suuria harppauksia, kun ohjelmisto siirtyi käyttämään tietokantaa sekä sovellukseen lisättiin käyttäjätunnusten rekisteröinti ja kirjautumistoiminnot.

Haasteena sprintissä 3 oli konfikuroinnin haasteet ja hitaus sekä pylint ignoren käyttäminen työn eteenpäin saattamiseksi.

### Sprint 4 @ 7.- 14.12.2023
Sprint 4 otti oppia aiemman sprintin retroperspektiivistä. Tähän liittyi konfiguroinnin vähentäminen ja työn tehostaminen yleisesti. 

Websovellus sai loistavan kasvojen kohotuksen, kun sivuston ulkonäkö päivitettiin nykyaikaiseen muotoon. 

Haasteena kuitenkin ilmeni tietokannan laajentaminen, jossa estimoidut lisäykset eivät täsmänneet tarvittavaa aikaa. 


## Projektin sujuvuus ja opit
Projektissa opittiin työskentelyä pienessä ketteränohjelmistokehityksen tiimissä. Projektin aikana opeteltiin uusia työskentelytapoja, kommunikaatiota, kokouskäytäntöjä ja dokumentaatiota. Kokouskäytännöt sujuivat hyvin koko projektin aikana ja niiden arvo huomattiin retroperspektiiveissä, joka vahvisti käytäntöjen toteuttamista. Asiakastapaamisia edeltävät pre meet-up kokoukset koettiin todella hyväksi käytännöksi ja asiakastapaamisen jälkeen suoritettava retroperspektiivi ja uuden sprintin suunnittelu kriittisiksi.

Parikoodaamista kokeiltiin ja se tuntui mielekkäältä. Parityöskentelyä olisi voinut soveltaa myös enemmän. Kommunikaation tärkeys yleisesti koettiin tärkeäksi osaksi ohjelmistokehitystä ja asia varmasti korostuisi isommissa ja pidemmissä hankkeissa. Kommunikaatioon liipaten myös dokumentaation tärkeys nousi esille. Scrumin suosittelema samassa tilassa työskentely ja daily scrum palaverit olisivat kiinnostava lisä ja kokeiltava asia seuraavissa hankkeissa.

Jatkuvan julkaisun tekniikka oli mielenkiintoista ja sujui mallikkaasti. Joitain testejä rikkovia committeja tehtiin, mutta koodi saatiin korjattua ripeästi. Pienillä työtapojen hiomisilla ja käytännöillä asiakkaalla olisi ollut käytännössä täysin toimiva tuote kokoajan käytössää.

Projektissa ei menty kovin syvälle teknisiin asioihin ja näiden soveltaminen periytyi pitkälti jäsenien aiemmista projekteista ja kokemuksesta. Joitain teknisiähaasteita ilmeni joissa scrum tyyppinen samassa tilassa työskentely auttaisi haasteiden nopeaan reagointiin.

Haastavalta projektissa tuntui mahdollinen ylitestaaminen, etenkin isompien refraktorointien yhteydessä. Työelämässä liiallinen testaaminen osoittautuisi myös ajallisesti ja kustannuksiltaan turhan raskaaksi. Joitain refraktorointeja jätettiinkin tekemättä, koska ne vaikuttaisivat suureen määrään testejä.
