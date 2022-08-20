# eboekhouden
e-boekhouden.nl API
---

### A way to use these files could be by entering the next code:

---

`from eboekhouden_api import eboek`

`import logging`

`# to swith of Soap logging messages: "Forcing soap:address location to HTTPS"`

`logging.getLogger('zeep.wsdl.bindings.soap').setLevel(logging.ERROR)`

#### (where username is your "Gebruikersnaam" with e-boekhouden.nl. SecurityCode1 and SecurityCode2 are the Beveiligingscode 1 and -2 you can enter here as a string)
---

`Username = "myusername"`

`SecurityCode1 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"`

`SecurityCode2 = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX"`

---

### generate the session code
`sessie1 = eboek.Eboek(Username, SecurityCode1, SecurityCode2)`

`print(sessie1.session_id)`

---

#### use this session code to fetch data
---
### get saldi
---

`saldi_fin = eboek.Saldi(0,"2022-01-01","2022-03-31","VW")`

`saldi = sessie1.get_saldi(saldi_fin)`

`print(saldi)`

---

### get saldo
`saldo_fin = eboek.Saldo("1020",0,"2001-01-01", "2022-08-19")`

`saldo = sessie1.get_saldo(saldo_fin)`

`print(saldo)`

---
### get grootboekrekeningen
---
`lijst_grootboekrekeningen = eboek.Grootboekrekeningen(0,"","VW")`

`grootboekrekeningen = sessie1.get_grootboekrekeningen(lijst_grootboekrekeningen)`

`print(grootboekrekeningen)`

---
### get relaties
---

`lijst_relaties = eboek.Relaties("","",0)`

`relaties = sessie1.get_relaties(lijst_relaties)`

`print(relaties)`

---

### get open posten

---

`lijst_openposten = sessie1.get_openposten("Crediteuren")`

`print(lijst_openposten)`

---

### get mutaties
---
`lijst_mutaties = eboek.Mutaties(0,0,99999,"", "2022-01-01","2022-03-31")`

`mutaties = sessie1.get_mutaties(lijst_mutaties)`

`print(mutaties)`

---
### get kostenplaatsen
---
`lijst_kostenplaatsen = eboek.Kostenplaatsen(0,0,"")`

`kostenpl = sessie1.get_kostenplaatsen(lijst_kostenplaatsen)`

`print(kostenpl)`

---

### get facturen
---

`lijst_facturen = eboek.Facturen("","","2022-01-01", "2022-03-31")`

`fact = sessie1.get_facturen(lijst_facturen)`

`print(fact)`

---
### get administraties
---
`administratie = sessie1.get_administraties()`

`print(administratie)`

---

## adding transactions and master data
### Master data
---

### add relatie
---

`rel = eboek.Relatie(0,"2022-03-30","Test","Testbedrijf","","","Straat","Postcode","Plaats","Land","Straat2","Postcode2","Plaats2","Land2", "Tel", "Gsm","","info@raylan.nl","","", "", "", "Dhr", "", "", "B","0", 0, 0, 0)`

`nieuwerelatie = sessie1.add_relatie(rel)`

`print(nieuwerelatie)`

---
### add grootboekrekening
---

`grb = eboek.Grootboekrekening(0,"100T","Test rekening","BAL","")`

`nieuwerekening = sessie1.add_grootboekrekening(grb)`

`print(nieuwerekening)`

---
### Transactions
---
### add mutatie
---

`mut_nummer = sessie1.add_mutatie(eboek.Mutatie("Memoriaal","2021-03-24","1000","","","Test","","IN", [eboek.MutatieRegel("1000", "1000", "0", "1000", "0", "0", "0140", 0 )]))`
