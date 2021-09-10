import re
import Customer

black_list = []
other_list = []

with open('C:\\Users\\sanjum\\Desktop\\Devops\\venv\\unmv8h36uh\\777_m3_datasets_v1.0\\FairDealCustomerData.csv') as file:
    for row in file:
        spilt_names = re.split('[,.]',row)
        data = list(map(lambda z:z.strip(),spilt_names))
        prod_cust = Customer.Customer(title=data[1],first_name=data[2],last_name=data[0],Blacklisted=(data[3] == '1'))


        try:
            Customer.create_order(prod_cust)
            other_list.append(prod_cust)
        except Customer.CustomerNotAllowedException:
            black_list.append(prod_cust)

print('List of Customer in FairDeal have been BlackListed')
kite = '{} {} {}'
for g in black_list:
    print(kite.format(g.title,g.first_name,g.last_name))






