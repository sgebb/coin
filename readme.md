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


#Presentere:

Hva er blockchain
	Kjede med blocks
	Block: {transaksjoner[], index, timestamp, proof, previous_hash}
	Transaksjon: {avsender, mottaker, mengde, timestamp}


Hva får man med blockchain
	-Immutabilitet - umulig å endre historikk
	-Distribuert - ingen server
    -Trustless

Hva trenger man for å lage en minimal blockchain
	-En definisjon av en block
	-En genesis-block
    -En oppgave å løse (POW) og en belønning
	-En consensus-algoritme

Valg
    Den som forger må si ifra til alle andre
