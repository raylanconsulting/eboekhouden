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
    
