# CloudeosApi

Cloudeos.com için python api kullanımı örnegidir, api dökümanlarından bakarak bu örneği genişletebilirsiniz.

### Mevcut istek örnekleri:
- Get Account Detail
- Get Current Balance
- Create Server
- Get Server Lists
- Destroy Server
- Create SSH Key
- Get SSH Keys



### Example

Çalıştırılacak örnek kodlarda cloudeos.py içe aktarmadan önce aynı dizinde olduğuna dikkat ediniz. Example klasöründeki kodları direkt olarak çalıştırmak isterseniz cloudeos.py dosyasını o dizine kopyalayabilir/taşıyabilirsiniz.

#### Get Account Detail:
```
from cloudeos import API


cloudeos = API("username", "password")

account_detail = cloudeos.get_accountDetail()

print(account_detail)
```


#### Create Server:
```
from cloudeos import API


cloudeos = API("username", "password")

name	 = "MyServer"
region	 = "ist2"
package  = "eos1"
image	 = "ubuntu-16-04-x64"
ssh_keys = "MySSHKey" #key olusturulmussa veya istege bagli

create   = cloudeos.create_server(name, region, package, image, ssh_keys=ssh_keys)

print(create)
```


Diğer örnekleri Examples klasöründe bulabilir ve genişletebilirsiniz.
