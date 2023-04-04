---
title: HSL
---
classDiagram
    
    HKLLaitehallinto <|-- Main  
    Kioski <|-- HKLLaitehallinto :luo kioski jarjestelmaan
    Matkakortti <|-- HKLLaitehallinto :luo matkakortti jarjestelmaan
    Matkakortti <|-- Kioski : osta_matkakortti()
    Lataajalaite <|-- HKLLaitehallinto :lisaa_lataaja()
    Lukijalaite <|-- HKLLaitehallinto :lisaa_lukija()
    Matkakortti <|-- Lataajalaite :arvo tai aika (lataus)
    Matkakortti <|-- Lukijalaite :vahenna(arvoa)
    Lukijalaite <|-- Matkakortti :osta_lippu()
    class Main{
        toiminnot
    
    }
    class Kioski{
        osta_matkakortti()
    }
    class Matkakortti{
        omistaja
        kasvata_arvoa()
        vahenna_arvoa()
        uusi_aika()
    }
    class Lataajalaite{
        lataa_arvoa()
        lataa_aikaa()

    }
    class Lukijalaite{
        osta_lippu()

    }
    class HKLLaitehallinto{
        lisaa_lataaja()
        lisaa_lukija()
        korttien ja laitteiden määrittely ja hallinnointi

    }

