class Customer:
    def __init__(self,title,first_name,last_name,Blacklisted):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.Blacklisted = Blacklisted

    def is_blacklisted(self):
        return self.Blacklisted

    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.last_name

    def get_title(self):
        return self.title


class CustomerNotAllowedException(Exception):
    def __init__(self,Customer):
        pass

def create_order(Customer):
    if Customer.is_blacklisted():
        raise CustomerNotAllowedException(Customer)

