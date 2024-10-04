# Nederlands

# Lijst van mogelijke structuren

| Commando                 | Python-equivalent          | Voorbeeld              |
| ------------------------ | -------------------------- | ---------------------- |
| Neem een getal, \<int\>. | \<var\> = \<int\>          | Neem een getal, 5.     |
| Neem het vorige getal.   | \<var1\> = \<var2\>        | Neem het vorige getal. |
| Vraag een getal.         | \<var\> = int(input("> ")) | Vraag een getal.       |
| Tel er \<int\> bij op.   | \<var\> += \<int\>         | Tel er 3 bij op.       |
| Trek er \<int\> van af.  | \<var\> += \<int\>         | Trek er 6 van af.      |
| Zeg \<string\>.          | print(\<string\>)          | Zeg "Hallo, wereld.".  |
| Zeg het getal.           | print(\<var\>)             | Zeg het getal.         |
| Blijf dat herhalen.      | while True:                | Blijf dat herhalen.    |

# Voorbeeldprogramma's

Hello world:

```
Zeg "Hallo, wereld!".
```

Fibonacci:

```
Neem een getal, 1.
Neem een getal, 1.

Tel er het vorige getal bij op.
Zeg het getal.
Neem het vorige getal.
Blijf dat herhalen.
```

# Uitvoeren

Om een Nederlands programma uit te voeren zijn enkele mogelijkheden, waarvan de twee meestgebruikte hier vermeld staan.

## 1. Via de Python interpreter

Het is mogelijk een Nederlands programma te laten uitvoeren door Python. Om dit te doen, dient deze repository gekloond te worden. Vervolgens kan in een command line, die geopend is in de map van de repository, het volgende commando uitgevoerd worden:

```
python Nederlands.py <bestand> [output]
```

Waarbij `<bestand>` dient vervangen te worden door ofwel de naam van het bestand (indien het bestand zich in de huidige directory bevindt), ofwel het pad naar het bestand. `[output]`, indien gegeven, is een bestand waarnaar alle output die geprint wordt door het programma geschreven wordt. Indien dit bestand al bestaat, zal de output worden toegevoegd aan het einde van het bestand.

## 2. Via de mens

Om een programma in Nederlands uit te voeren kan ook de volgende methode gebruikt worden. Neem een screenshot (geen foto aub, de tekst moet leesbaar zijn) van een Nederlands programma, en stuur die door naar een mens naar keuze, met de opdracht om de instructies op de screenshot uit te voeren. Indien de code van het programma niet op een screenshot past, kan de code ook als tekst gekopieerd worden.

LET OP! Het uitvoeren van Nederlandse programma's via de mens is niet uitvoerig getest, en kan bijgevolg vreemde afwijkingen vertonen. Indien u zeker bent dat uw code geen fouten bevat, kan het wenselijk zijn uw code te [transpileren](https://translate.google.com) en het resultaat te gebruiken in plaats van de oorspronkelijke code.

# TODOS

Lijst van (gekende) onacceptabele bugs die momenteel geprocrastineerd worden:

- Aangezien het puntkarakter gebruikt wordt als seperator en hier geen extra check op zit, kan de punt niet in een string gebruikt worden.
- Er kunnen geen dubbele aanhalingstekens in strings gebruikt worden.
- De controle op een lege lijn trekt op geen kloten.
