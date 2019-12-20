from cloudeos import API


cloudeos = API("username", "password")

account_detail = cloudeos.get_accountDetail()

print(account_detail)