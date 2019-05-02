from exchange_oop_json import Rates_Parser

rates_objt = Rates_Parser("json_2.json")

print(rates_objt)

print(rates_objt.aud)
print(rates_objt.gbp)

print(rates_objt.rates)

for key in rates_objt.rates:
    print(key+ rates_objt.rates[key])