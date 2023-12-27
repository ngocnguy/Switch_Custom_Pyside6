class CreateShadowEntity:
    z1 : str = ""
    z4 : str = ""
    z8 : str = ""
    z12 : str = ""
    z16 : str = ""
    z20 : str = ""
    z24 : str = ""
    primary : str = ""
    info : str = ""
    secondary : str = ""
    success : str = ""
    warning : str = ""
    error : str = ""
    card : str = ""
    dialog : str = ""
    dropdown : str = ""
    

    def __init__(self,options):
        self.z1 = options['z1']
        self.z4 = options['z4']
        self.z8 = options['z8']
        self.z12 = options['z12']
        self.z16 = options['z16']
        self.z20 = options['z20']
        self.z24 = options['z24']
        self.primary = options['primary']
        self.info = options['info']
        self.secondary = options['secondary']
        self.success = options['success']
        self.warning = options['warning']
        self.error = options['error']
        self.card = options['card']
        self.dialog = options['dialog']
        self.dropdown = options['dropdown']