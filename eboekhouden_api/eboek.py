from zeep import Client as ZeepClient

# the add classes

# former relatie.py

class Relatie:
    def __init__(
        self,
        id: int,
        adddatum: str, 
        code: str,  
        bedrijf: str,
        contactpersoon: str,
        geslacht: str,
        adres: str,
        postcode: str,
        plaats: str,
        land: str,
        adres2: str,
        postcode2: str,
        plaats2: str,
        land2: str,
        telefoon: str,
        gsm: str,
        fax: str,
        email: str,
        site: str,
        notitie: str,
        btwnummer: str,
        kvknummer: str,
        aanhef: str,
        iban: str,
        bic: str,
        bp: str,
        la: str,
        gbid: int,
        geenemail: int,
        niewsbrief: int,
        
    ):
        self.id = id
        self.adddatum = adddatum
        self.code = code
        self.bedrijf = bedrijf
        self.contactpersoon = contactpersoon
        self.geslacht = geslacht
        self.adres = adres
        self.postcode = postcode
        self.plaats = plaats
        self.land = land
        self.adres2 = adres2
        self.postcode2 = postcode2
        self.plaats2 = plaats2
        self.land2 = land2
        self.telefoon = telefoon
        self.gsm = gsm
        self.fax = fax
        self.email = email
        self.site = site
        self.notitie = notitie
        self.btwnummer = btwnummer
        self.kvknummer = kvknummer
        self.aanhef = aanhef
        self.iban = iban
        self.bic = bic
        self.bp = bp
        self.la = la
        self.gbid = gbid
        self.geenemail = geenemail
        self.nieuwsbrief = niewsbrief

    def export(self):
        return dict(
            ID=self.id,
            AddDatum=self.adddatum,
            Code=self.code,
            Bedrijf=self.bedrijf,
            Contactpersoon=self.contactpersoon,
            Geslacht=self.geslacht,
            Adres=self.adres,
            Postcode=self.postcode,
            Plaats=self.plaats,
            Land=self.land,
            Adres2=self.adres2,
            Postcode2=self.postcode2,
            Plaats2=self.plaats2,
            Land2=self.land2,
            Telefoon=self.telefoon,
            GSM=self.gsm,
            FAX=self.fax,
            Email=self.email,
            Site=self.site,
            Notitie=self.notitie,
            Bankrekening = "",
            Girorekening = "",
            BTWNummer=self.btwnummer,
            KvkNummer=self.kvknummer,
            Aanhef=self.aanhef,
            IBAN=self.iban,
            BIC=self.bic,
            BP=self.bp,
            Def1 = "",
            Def2 = "",
            Def3 = "",
            Def4 = "",
            Def5 = "",
            Def6 = "",
            Def7 = "",
            Def8 = "",
            Def9 = "",
            Def10 = "",
            LA=self.la,
            Gb_ID=self.gbid,
            GeenEmail=self.geenemail,
            NieuwsbriefgroepenCount=self.nieuwsbrief,
        )

# end former relatie.py

# former mutatie_regel.py

class MutatieRegel:
    def __init__(
        self,
        bedrag_invoer: str,
        bedrag_excl_btw: str,
        bedrag_btw: str,
        bedrag_incl_btw: str,
        btw_code: str,
        btw_percentage: str,
        tegenrekening_code: str,
        kostenplaats_id: str,
    ):
        self.bedrag_invoer = bedrag_invoer
        self.bedrag_excl_btw = bedrag_excl_btw
        self.bedrag_btw = bedrag_btw
        self.bedrag_incl_btw = bedrag_incl_btw
        self.btw_code = btw_code
        self.btw_percentage = btw_percentage
        self.tegenrekening_code = tegenrekening_code
        self.kostenplaats_id = kostenplaats_id

    def export(self):
        return dict(
            BedragInvoer=self.bedrag_invoer,
            BedragExclBTW=self.bedrag_excl_btw,
            BedragBTW=self.bedrag_btw,
            BedragInclBTW=self.bedrag_incl_btw,
            BTWCode=self.btw_code,
            BTWPercentage=self.btw_percentage,
            TegenrekeningCode=self.tegenrekening_code,
            KostenplaatsID=self.kostenplaats_id,
        )

# end former mutatie_regel.py

# form mutatie.py


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


# end former mutatie.py

# former grootboekrekening.py

class Grootboekrekening:
    def __init__(
        self,
        id: int,
        code: str,
        omschrijving: str,
        categorie: str,
        groep: str,
    ):
        self.id = id
        self.code = code
        self.omschrijving = omschrijving
        self.categorie = categorie
        self.groep = groep

    def export(self):

        return dict(
            ID=self.id,
            Code=self.code,
            Omschrijving=self.omschrijving,
            Categorie=self.categorie,
            Groep=self.groep,
        )
    

# end former grootboekrekening.py

# former factuur_regel
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

# end former factuur_regel.py

# former factuur.py

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

# end former factuur.py

# the get classes
class Facturen:
    def __init__(
        self,
        factuurnummer: str,
        relatiecode: str,
        datumvan: str,
        datumtm: str,
    ):
        self.factuurnummer = factuurnummer
        self.relatiecode = relatiecode
        self.datumvan = datumvan
        self.datumtm = datumtm

    def export(self):

        return dict(
            Factuurnummer=self.factuurnummer,
            Relatiecode=self.relatiecode,
            DatumVan=self.datumvan,
            DatumTm=self.datumtm,
        )


class Grootboekrekeningen:
    def __init__(
        self,
        id: int,
        code: str,
        categorie: str,
    ):
        self.id = id
        self.code = code
        self.categorie = categorie

    def export(self):

        return dict(
            ID=self.id,
            Code=self.code,
            Categorie=self.categorie,
        )


class Kostenplaatsen:
    def __init__(
        self,
        kostenplaatsid: int,
        kostenplaatsparentid: int,
        omschrijving: str,
    ):
        self.kostenplaatsid = kostenplaatsparentid
        self.kostenplaatsparentid = kostenplaatsparentid
        self.omschrijving = omschrijving

    def export(self):

        return dict(
            KostenplaatsID=self.kostenplaatsid,
            KostenplaatsParentID=self.kostenplaatsparentid,
            Omschrijving=self.omschrijving,
        )


class Mutaties:
    def __init__(
        self,
        mutatienr: int,
        mutatienrvan: int,
        mutatienrtm: int,
        factuurnummer: str,
        datumvan: str,
        datumtm: str,
        
    ):
        self.mutatienr = mutatienr
        self.mutatienrvan = mutatienrvan
        self.mutatienrtm = mutatienrtm
        self.factuurnummer = factuurnummer
        self.datumvan = datumvan
        self.datumtm = datumtm

    def export(self):

        return dict(
            MutatieNr=self.mutatienr,
            MutatieNrVan=self.mutatienrvan,
            MutatieNrTm=self.mutatienrtm,
            Factuurnummer=self.factuurnummer,
            DatumVan=self.datumvan,
            DatumTm = self.datumtm,

        )

class Relaties:
    def __init__(
        self,
        trefwoord: str,
        code: str,
        id: int,
    ):
        self.trefwoord = trefwoord
        self.code = code
        self.id = id

    def export(self):

        return dict(
            Trefwoord=self.trefwoord,
            Code=self.code,
            ID=self.id,
        )

class Saldi:
    def __init__(
        self,
        kostenplaatsid: int,
        datumvan: str,
        datumtot: str,
        categorie: str,
    ):
        self.kostenplaatsid = kostenplaatsid
        self.datumvan = datumvan
        self.datumtot = datumtot
        self.categorie = categorie

    def export(self):

        return dict(
            KostenPlaatsId=self.kostenplaatsid,
            DatumVan=self.datumvan,
            DatumTot=self.datumtot,
            Categorie=self.categorie,
        )


class Saldo:
    def __init__(
        self,
        gbcode: str,
        kostenplaatsid : int,
        datumvan: str,
        datumtot: str,
    ):
        self.gbcode = gbcode
        self.kostenplaatsid = kostenplaatsid
        self.datumvan = datumvan
        self.datumtot = datumtot

    def export(self):

        return dict(
            GbCode=self.gbcode,
            KostenPlaatsId=self.kostenplaatsid,
            DatumVan=self.datumvan,
            DatumTot=self.datumtot,
        )


class Eboek:
    # initialisation methods
    client = None
    session_id: str = None

    username: str = None
    security_code_1: str = None
    security_code_2: str = None

    def __init__(self, username: str, security_code_1: str, security_code_2: str):
        self.username = username
        self.security_code_1 = security_code_1
        self.security_code_2 = security_code_2
        self.client = ZeepClient("https://soap.e-boekhouden.nl/soap.asmx?wsdl")
        self.connect()

    def connect(self):
        session = self.client.service.OpenSession(
            Username=self.username, SecurityCode1=self.security_code_1, SecurityCode2=self.security_code_2
        )
        self.session_id = session["SessionID"]

    # add methods
    def add_factuur(self, factuur: Factuur):
        exported_factuur = factuur.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, oFact=exported_factuur)
        response = self.client.service.AddFactuur(**params)
        return response
    
    def add_grootboekrekening(self, grootboekrekening: Grootboekrekening):
        exported_grootboekrekening = grootboekrekening.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, oGb=exported_grootboekrekening)
        response = self.client.service.AddGrootboekrekening(**params)
        return response
    
    
    def add_mutatie(self, mutatie: Mutatie):
        exported_mutatie = mutatie.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, oMut=exported_mutatie)
        response = self.client.service.AddMutatie(**params)
        return response
    
    
    def add_relatie(self, relatie: Relatie):
        exported_relatie = relatie.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, oRel=exported_relatie)
        response = self.client.service.AddRelatie(**params)
        return response
    
    
    # get methods
    def get_administraties(self):
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2)
        response = self.client.service.GetAdministraties(**params)
        return response
    
    
    # def get_artikelen(self, artikelen: Artikelen):
    #     """
    #     Filter on: (ArtikelID, ArtikelOmschrijving, ArtikelCode, GroepOmschrijving, GroepCode)
    #     """
    #     exported_artikelen = artikelen.export()
    #     params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, cFilter=exported_artikelen)
    #     response = self.client.service.GetArtikelen(**params)
    #     return response


    def get_facturen(self, facturen: Facturen):
        """
        Filter on: (Id, Code, Categorie)
        """
        exported_facturen = facturen.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, cFilter=exported_facturen)
        response = self.client.service.GetFacturen(**params)
        return response 


    def get_grootboekrekeningen(self, grootboekrekeningen: Grootboekrekeningen):
        """
        Filter on: (Id, Code, Categorie)
        """
        exported_grootboekrekeningen = grootboekrekeningen.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, cFilter=exported_grootboekrekeningen)
        response = self.client.service.GetGrootboekrekeningen(**params)
        return response 


    def get_kostenplaatsen(self, kostenplaatsen: Kostenplaatsen):
        """
        Filter on: (KostenplaatsID, KostenplaatsParentID, Omschrijving)
        """
        exported_kostenplaatsen = kostenplaatsen.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, cFilter=exported_kostenplaatsen)
        response = self.client.service.GetKostenplaatsen(**params)
        return response


    def get_mutaties(self, mutaties: Mutaties):
        """
        Filter on: (Id, Code, Categorie)
        """
        exported_mutaties = mutaties.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, cFilter=exported_mutaties)
        response = self.client.service.GetMutaties(**params)
        return response 


    def get_openposten(self, opsoort):
        """returns the open items. As well debtors and creditors.
        
        Args:
            opsoort (_type_): Enter "Crediteuren" for creditor open items
            "Debiteuren" for debtor open items

        Returns:
            _type_: details of the open items will be returned
        """
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, OpSoort=opsoort)
        response = self.client.service.GetOpenPosten(**params)
        return response


    def get_relaties(self, relaties: Relaties):
        """
        Filter on: (KostenPlaatsId, DatumVan, DatumTot, Categorie)
        """
        exported_relaties = relaties.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, cFilter=exported_relaties)
        response = self.client.service.GetRelaties(**params)
        return response   


    def get_saldi(self, saldi: Saldi):
        """
        Filter on: (KostenPlaatsId, DatumVan, DatumTot, Categorie)
        """
        exported_saldi = saldi.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, cFilter=exported_saldi)
        response = self.client.service.GetSaldi(**params)
        return response    

    def get_saldo(self, saldo: Saldo):
        """
        Filter on: (GbCode, KostenPlaatsId, DatumVan, DatumTot)
        """
        exported_saldo = saldo.export()
        params = dict(SessionID=self.session_id, SecurityCode2=self.security_code_2, cFilter=exported_saldo)
        response = self.client.service.GetSaldo(**params)
        return response
    