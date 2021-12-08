# Tviter

Aplikacija Tviter je pojednostavljena verzija web aplikacije Twitter. Tviter omogućava registraciju novog korisnika i stvaranje njegovog Tviter profila. Nakon stvaranja profila korisniku se omogućuje objavljivanje novih tvitova te interakcija sa postojećim Tvitovima u obliku lajkova i komentara. Tviterasi se mogu posjećivati profile drugih tviteraša te ih pratiti.

Modeli se sastoje od 4 klase:
- Tvit
- Tviteras
- Lajk
- Komentar

Klasa tvit:
- objavljivanje tekstualne poruke
- poruka je vremenski označena

Klasa Tviteras:
- osnovne informacija o tviterasu (ime, hendl, opis...)
- tviteras moze pratiti druge tviterase, ali oni njega automatski ne prate
- profil je vezan za određenog korisnika

Klasa Lajk:
- vezan je za određeni tvit

Klasa Komentar:
- dio za upis teksta
- vezan je za određeni tvit
