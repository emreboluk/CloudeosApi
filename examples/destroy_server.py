from cloudeos import API


cloudeos = API("username", "password")

id = "12231" # ornek

destroy = cloudeos.destroy_server(id)

print(destroy)