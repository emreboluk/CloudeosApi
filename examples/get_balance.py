from cloudeos import API


cloudeos = API("username", "password")

balance = cloudeos.get_balance()

print(balance)