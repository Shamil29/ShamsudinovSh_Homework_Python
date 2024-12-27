from address import Address
from mailing import Mailing

to_address = Address("108851", "Щербинка", "Театральная", "1", "23")
from_address = Address("117405", "Москва", "Варшавское шоссе", "152", "46")

mailing = Mailing(to_address, from_address, 256, 245631)

print(mailing)
