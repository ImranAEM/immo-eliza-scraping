class Property():
    """
    Class to store data describing a property to buy
    """

    def __init__(self, id, locality: str = None, postcode: int = None, price: int = None, type: int = 0, subtype: str = None, sale_type: int = 0, nb_rooms: int = None, area: int = None, equipped_kitchen: int = None, furnished: int = None, open_fire: int = None, terrace: int = None, garden: int = None, facades: int = None, pool: int= None, state: int = 0,url: str = None):
        self.id = id
        self.locality = locality
        self.postcode = postcode
        self.price = price
        self.type = type # (house - 0/ appartment - 2)
        self.subtype = subtype # property subtype
        self.sale_type = sale_type # type of sale (1 - to rent / 2 - for sale / 3 - public sale / 4 - shared accomodation) (no life sales)
        self.rooms = nb_rooms #number of rooms
        self.area = area #living area in m2
        self.kitchen = equipped_kitchen # (No - 0/ Yes - 1)
        self.furnished = furnished # (No - 0/ Yes - 1)
        self.open_fire = open_fire # (No - 0/ Yes - 1), open fire presence
        self.terrace = terrace # area in m2 or None if no terrace
        self.garden = garden # area in m2 or None if no garden
        self.facades = facades # number of facades
        self.pool = pool # (No - 0/ Yes - 1) presence or swimming pool
        self.state = state # state of the house (1 - new / 2 - excellent / 3 - fully renovated / 4 - normal / 5 - to renovate)
       # self.energy_class = energy_class # state of the house (1 - new / 2 - excellent / 3 - fully renovated / 4 - normal / 5 - to renovate)
        self.url = url
