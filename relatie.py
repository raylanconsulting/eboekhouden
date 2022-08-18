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
