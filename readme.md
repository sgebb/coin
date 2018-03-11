# coincoin

TODO:
- Integrasjonstester, tester av blockchain-logikken. Test av "valid transaction" osv
- Sørge for at trådene dør
- Støtte flere noder

- Validere transaksjoner (ikke bare true)
- Consensus-algorithm
- Når er en transaksjon OK
    - Må bevise at den som sender transaksjonen = Sender
    - Må sjekke at sender har penger på sin konto.
- Når forkaster man egen CHain
    - Noen poster en chain som er lenger enn sin egen
    - OG genesis blocken er den samme?
    - OG den nye chainen er gyldig.

Real usecase: Kan man gjøre finansieringsbevis/lån-godtatt på kjeden? Verifikasjon av en sum over X uten å avsløre hvor mye?
Engangspassord, sjekke om større, return true eller false, må ha nytt signert passord for hver sjekk. Banken legger inn hvor mye penger du har, du lager engangspassord for å sjekke likviditet. Varighet på finansieringsbevis fram til X dager?