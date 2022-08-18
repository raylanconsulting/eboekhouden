from factuur_regel import FactuurRegel

class Factuur:
    def __init__(
        self,
        factuurnummer: str,
        relatie_code: str,
        datum: str,
        betalingstermijn: int,
        factuur_sjabloon: str,
        per_email_verzenden: str,
        email_onderwerp: str,
        email_bericht: str,
        email_van_adres: str,
        email_van_naam: str,
        automatische_incasso: str,
        incasso_iban: str,
        incasso_machtiging_soort: str,
        incasso_machtiging_id: str,
        incasso_machtiging_datum_ondertekening: str,
        incasso_machtiging_first: str,
        incasso_rekeningnummer: str,
        incasso_tnv: str,
        incasso_plaats: str,
        incasso_omschrijving_regel1: str,
        incasso_omschrijving_regel2: str,
        incasso_omschrijving_regel3: str,
        in_boekhouding_plaatsen: str,
        boekhoudmutatie_omschrijving: str,
        factuur_regels: FactuurRegel,
    ):
        self.factuurnummer = factuurnummer
        self.relatie_code = relatie_code
        self.datum = datum
        self.betalingstermijn = betalingstermijn
        self.factuur_sjabloon = factuur_sjabloon
        self.per_email_verzenden = per_email_verzenden
        self.email_onderwerp = email_onderwerp
        self.email_bericht = email_bericht
        self.email_van_adres = email_van_adres
        self.email_van_naam = email_van_naam
        self.automatische_incasso = automatische_incasso
        self.incasso_iban = incasso_iban
        self.incasso_machtiging_soort = incasso_machtiging_soort
        self.incasso_machtiging_id = incasso_machtiging_id
        self.incasso_machtiging_datum_ondertekening = incasso_machtiging_datum_ondertekening
        self.incasso_machtiging_first = incasso_machtiging_first
        self.incasso_rekeningnummer = incasso_rekeningnummer
        self.incasso_tnv = incasso_tnv
        self.incasso_plaats = incasso_plaats
        self.incasso_omschrijving_regel1 = incasso_omschrijving_regel1
        self.incasso_omschrijving_regel2 = incasso_omschrijving_regel2
        self.incasso_omschrijving_regel3 = incasso_omschrijving_regel3
        self.in_boekhouding_plaatsen = in_boekhouding_plaatsen
        self.boekhoudmutatie_omschrijving = boekhoudmutatie_omschrijving
        self.factuur_regels = factuur_regels
        

    def export(self):
        exported_factuur_regels = []

        for index, factuur_regal in enumerate(self.factuur_regels):
            exported_factuur_regels.append({**factuur_regal.export()})
    
        return dict(
            Factuurnummer=self.factuurnummer,
            Relatiecode=self.relatie_code,
            Datum=self.datum,
            Betalingstermijn=self.betalingstermijn,
            Factuursjabloon=self.factuur_sjabloon,
            PerEmailVerzenden=self.per_email_verzenden,
            EmailOnderwerp=self.email_onderwerp,
            EmailBericht=self.email_bericht,
            EmailVanAdres=self.email_van_adres,
            EmailVanNaam=self.email_van_naam,
            AutomatischeIncasso=self.automatische_incasso,
            IncassoIBAN=self.incasso_iban,
            IncassoMachtigingSoort=self.incasso_machtiging_soort,
            IncassoMachtigingID=self.incasso_machtiging_id,
            IncassoMachtigingDatumOndertekening=self.incasso_machtiging_datum_ondertekening,
            IncassoMachtigingFirst=self.incasso_machtiging_first,
            IncassoRekeningNummer=self.incasso_rekeningnummer,
            IncassoTnv=self.incasso_tnv,
            IncassoPlaats=self.incasso_plaats,
            IncassoOmschrijvingRegel1=self.incasso_omschrijving_regel1,
            IncassoOmschrijvingRegel2=self.incasso_omschrijving_regel2,
            IncassoOmschrijvingRegel3=self.incasso_omschrijving_regel3,
            InBoekhoudingPlaatsen=self.in_boekhouding_plaatsen,
            BoekhoudmutatieOmschrijving=self.boekhoudmutatie_omschrijving,
            Regels=dict(cFactuurRegel=exported_factuur_regels),
        )
