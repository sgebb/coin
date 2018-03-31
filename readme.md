# coincoin

TODO:
- Integrasjonstester, tester av blockchain-logikken. Test av "valid transaction" osv
- Sørge for at trådene dør
- Støtte flere noder
- Ha en nodeaddresse hardkodet inn (eller param).
- Spre nodeliste til nettverket gradvis, og fjern de som er døde

- Validere transaksjoner (ikke bare true)
- Consensus-algorithm
- Når er en transaksjon OK
    - Må bevise at den som sender transaksjonen = Sender
    - Må sjekke at sender har penger på sin konto.
    - Unngår doublespend ved å sjekke hver transaksjon
- Når forkaster man egen CHain
    - Noen poster en chain som er lenger enn sin egen
    - OG genesis blocken er den samme?
    - OG den nye chainen er gyldig.

Real usecase: Kan man gjøre finansieringsbevis/lån-godtatt på kjeden? Verifikasjon av en sum over X uten å avsløre hvor mye?
Engangspassord, sjekke om større, return true eller false, må ha nytt signert passord for hver sjekk. Banken legger inn hvor mye penger du har, du lager engangspassord for å sjekke likviditet. Varighet på finansieringsbevis fram til X dager?
Evt:
Computas-BONG-chain
Adresser fra computasappen? 
Putt bongene i genesis
Verifiser bong-transaksjoner, ingen rewards

# Presentere:

## Hva er blockchain
	-Kjede med blocks, lever i minnet til alle noder.
	-Mye til felles med git
	-Block: {transaksjoner[], index, timestamp, proof, previous_hash}
	-Transaksjon: {avsender, mottaker, mengde, timestamp}


## Hva får man med blockchain
	-Immutabilitet - umulig å endre historikk
	-Distribuert - ingen server
    -Trustless

## Hva trenger man for å lage en minimal blockchain
	-En definisjon av en block
	-En genesis-block
    -En oppgave å løse (POW) og en belønning
	-En consensus-algoritme
    -En måte å være klient og server på samtidig

## Valg
    -Den som forger må si ifra til alle andre
    -Den som lager en transaksjon må si ifra til alle andre
    -Vinnerens transaksjoner blir tatt med, alt annet går ut.


# Flyt for å dele noder
Ny node, kjenner til en som er connected
Send en post med tom liste til den ene
Den svarer med alle sine noder og lengden på chainen - så kan man spørre om hele om den er lenger?
Du legger til halvparten av nodene

Hvert minutt:
Post dine noder til fem av nodene
Hvis noen ikke svarer - dropp dem
