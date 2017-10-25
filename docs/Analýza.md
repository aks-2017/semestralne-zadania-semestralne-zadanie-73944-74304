# RepFlow
## Analýza
V článku bolo implementované Repflow na skrátenie FCT(Flow Completion Time) v TCP(Transmission Control Protocol) sieťach, v ktorom sa pomocou nástrojov Mininet a NS-3 replikovali krátke TCP toky. Toto riešenie bolo navrhnuté pre dátové centrá, v ktorých sa ako jedným z hlavných protokolov používa protokol TCP a topológia Fat-tree. 

Hlavným problémom na ktorý sa RepFlow zameral bolo čakanie krátkych tokov vo fronte s dlhými. Vďaka tomu, že v sieti v dátových centrách je viac rovnako dobrých ciest, ktorými je možné tok vyslať, krátke toky môžme vyslať po inej ceste, kde nebudú čakať.

Cesty sa vyberajú pomocou ECMP(Equal-cost multi-path), ktorý zahashuje tok a pošle po jednej ceste. Na tejto ceste však môže nastať kolízia, ak sa na danej ceste už niečo posiela a krátky tok bude musieť čakať kým sa dokončí odosielanie paketov alebo dlhého toku. Tento jav sa nazýva head-of-line blocking. Tento problém je možné vyriešiť replikáciou toku, pretože je malá pravdepodobnosť, že oba toky budú odosielané po rovnakej ceste. Prvý doručený tok ukončí prenos.

### FCT (Flow Completion Time)[1]
Je čas dokončenia prenosu informácií poslaného zo zdrojového bodu do cieľového bodu.

### Head-of-line blocking[2]
Je to dej, ktorý sa deje v sieťach pri posielaní paketov. Keď sa v sieťach posielaju pakety na cieľového používateľa môžu blokovať ďalšie prichádzajúce pakety. Táto situácia sa volá Head-of-line blocking. 

### Mininet[3]
Mininet je nástroj, ktorý vytvára realistickú virtuálnu sieť. Na tejto sieti je možné zaviesť skutočný kernel, prepínač a aplikačný kód. Toto sa deje na jednom stroji napríklad na virtuálnom stroji. 
Na vytváranie sa využíva príkaz sudo mn, ktorý vie vytvoriť hostov, switche alebo controllery.
Tento systém je založený na BSD Open Source licencí a teda je stiahnuteľný zadarmo, preto sa často využíva na vzdelávanie a testovanie.

### RiplPOX[4]
RiplPOX je jednoduchý kontroler v dátových centrách postavený na Ripl. RiplPOX poskytuje príklad Openflow kontrolera, ktorý používa statický opis siete na vytvorenie cesty. Nutnosťou použitia RiplPOX-u je, že musí používať rovnakú topológiu ako Mininet.

## Návrh
Na overenie implementácie použijeme nástroj Mininet, do ktorého implementujeme replikovanie krátkych tokov a toto riešenie overíme na transportných štruktúrach Data mining a vyhľadávanie na webe.

Ako prvé vytvoríme topológiu, pre dané riešenie. Vytvorenie TCP spojenia v danej topológii. Po vytvorení TCP spojenia medzi jednotlivými komponentami, implementujeme replikácie krátkych tokov. Najprv vytvoríme funkciu, ktorá zhodnotí či daný tok je krátky tok, teda jeho veľkosť je do 100KB. Potom keď dorazí krátky tok, vytvoríme dva TCP sokety, cez ktoré pošleme identické pakety.

Využijeme štandrad TCP-New Reno, ktorý bol využitý v mnohých štúdiach. Inicializačné okno bude nastavené na 12KB a prepínače budú využívať DropTail queues s veľkosťou buffra 100 paketov.

Repflow využíva rovnaké parametre ako TCP, ale všetky toky menšie ako 100KB budú replikované.  
Obr.1 - 1 pod z topológie 4-pod Fat-tree [5]
Náš návrh budeme testovať na začiatku na jednom pode z topológie 4-pod Fat-tree.Obr. 1

Z ktorých zistíme správnosť riešenia. Ďalej budeme testovať na celej štruktúre 4-pod Fat-tree, ktorý bude vybalancovaný ECMP stratégiou. 
Obr. 2 - topológia 4-pod Fat-tree[5]
A budeme porovnávať, aké výsledky dostaneme s použitím TCP a aké s použitím Repflow. Následne naše výsledky porovnáme s výsledkami, ktoré namerali tvorcovia článku RepFlow: Minimizing Flow Completion Times with Replicated Flows in Data Centers.

### Nástroje:
V projekte budeme využívať python, kvôli kompatibilite s mininetom. 
RiplPOX je nainštalovaný ako controler na prepínačoch pre podporu ECMP.

### Topológia a nastavenia:
Budeme používať 4-pod Fat-tree so 16 hostami prepojené 20 prepínačmi (viď obrázok vyššie), každý so 4 portmi. Každý port má buffer s veľkosťou 50 paketov. Šírka pásma prenosu je nastavená na 20Mb a oneskorenie na 1ms, čo predstavuje minimálne oneskorenie, ktoré podporuje Mininet bez vysoko-presných časovačov.

### Obmedzenia:
Mininet sa stáva nestabilným, keď zaťaženie presahuje 0,5 , čo môže spôsobiť jeho obmedzenie v škálovateľnosti.

## Zdroje
[1] Nandita Dukkipati, Nick McKeown : Why Flow-Completion Time is the Right metric for
Congestion Control and why this means we need new algorithms: Computer Systems Laboratory, Stanford University, Stanford, CA 94305-9030, USA

[2] Valter Popeskic. HOL Head-of-line blocking.
https://howdoesinternetwork.com/2015/hol-head-of-line-blocking

[3] http://mininet.org/

[4] MurphyMc. 2013. RipL-POX (Ripcord-Lite for POX): A simple network controller for OpenFlow-based data centers 
https://github.com/MurphyMc/riplpox

[5]Karishma Sureka. 2014. Datacenters - Reduction of Broadcast traffic using SDN
http://sdn-in-datacenters.blogspot.sk/2014/04/literature-survey-portland-design.html


