import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = "+441234567890"

ch_number = phonenumbers.parse(number, "GB")
print(geocoder.description_for_number(ch_number, "en"))

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
