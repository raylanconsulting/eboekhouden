from zeep import Client as ZeepClient
from factuur import Factuur
from mutatie import Mutatie
from relatie import Relatie
from grootboekrekening import Grootboekrekening

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
    