from mutatie_regel import MutatieRegel

class Mutatie:
    def __init__(
        self,
        soort: str,
        datum: str,
        rekening: str,
        relatie_code: str,
        factuurnummer: str,
        omschrijving: str,
        betalingstermijn: str,
        inexbtw: str,
        mutatie_regels: MutatieRegel
    ):
        self.soort = soort
        self.datum = datum
        self.rekening = rekening
        self.relatie_code = relatie_code
        self.factuurnummer = factuurnummer
        self.omschrijving = omschrijving
        self.betalingstermijn = betalingstermijn
        self.inexbtw = inexbtw
        self.mutatie_regels = mutatie_regels

    def export(self):
        exported_mutatie_regels = []

        for index, mutatie_regel in enumerate(self.mutatie_regels):
            exported_mutatie_regels.append({**mutatie_regel.export()})

        return dict(
            MutatieNr="99999",
            Soort=self.soort,
            Datum=self.datum,
            Rekening=self.rekening,
            RelatieCode=self.relatie_code,
            Factuurnummer=self.factuurnummer,
            Omschrijving=self.omschrijving,
            Betalingstermijn=self.betalingstermijn,
            InExBTW=self.inexbtw,
            MutatieRegels=dict(cMutatieRegel=exported_mutatie_regels),
        )
