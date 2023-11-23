# Definition of Done (DoD)

## Koodin laatu:

- Noudattaa kerrosarkkitehtuurin mallia
    - Luokat on järjestetty toimintansa mukaan omiin kerroksiin, jotka muodostavat loogisen kokonaisuuden abstraktiotasonsa toiminnallisuuden suhteen 

- Koodi on hyvin muotoiltu, luettava ja noudattaa tiimin tyyliohjeita (pylint)

- Funktiot, metodit ja muuttujat ovat järkevästi nimettyjä

- Vertaisarvioitu ja hyväksytty

## Testaus:

- Yksikkötestit kirjoitettu ja läpäisty
- Integraatiotestit kirjoitettu ja läpäisty
    - Sprintistä 2 lähtien kirjoitettu Robot-Frameworkillä, kuvaten user storyn hyväksymiskriteereitä
- Toteutetaan jatkuvan integraation (CI) mallin mukaisesti, missä toimitetaan jatkuvasti toimiva versio sovelluksesta asiakkaalle
    - Testit eivät saa mennä rikki uuden toiminnallisuuden myötä
