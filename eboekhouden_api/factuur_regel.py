class FactuurRegel:
    def __init__(
        self,
        aantal: int,
        eenheid: str,
        code: str,
        omschrijving: str,
        prijs_per_eenheid: str,
        btw_code: str,
        tegenrekening_code: str,
        kostenplaats_id: int,
    ):
        self.aantal = aantal
        self.eenheid = eenheid
        self.code = code
        self.omschrijving = omschrijving
        self.prijs_per_eenheid = prijs_per_eenheid
        self.btw_code = btw_code
        self.tegenrekening_code = tegenrekening_code
        self.kostenplaats_id = kostenplaats_id

    def export(self):
        return dict(
            Aantal=self.aantal,
            Eenheid=self.eenheid,
            Code=self.code,
            Omschrijving=self.omschrijving,
            PrijsPerEenheid=self.prijs_per_eenheid,
            BTWCode=self.btw_code,
            TegenrekeningCode=self.tegenrekening_code,
            KostenplaatsID=self.kostenplaats_id,
        )
        
    def __str__(self):
        return 'Factuurregels: aantal %s, Eenheid %s, Code %s' % (self.aantal, self.eenheid, self.code)


class Regels:
    def __init__(
        self,
        factuur_regels: FactuurRegel,
    ):
        self.factuur_regels = factuur_regels

    def export(self):
        exported_factuur_regels = []

        for index, factuur_regel in enumerate(self.factuur_regels):
            exported_factuur_regels.append({**factuur_regel.export()})
    
        return dict(
            Regels=dict(cFactuurRegel=exported_factuur_regels),
        )
    
    def __str__(self):
        return str(self.factuur_regels)