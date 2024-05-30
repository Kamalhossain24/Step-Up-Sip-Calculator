amount = 5000
yearly_return = 25
year_for = 20

returns = yearly_return / 12 / 100

total_value = 0

for year in range(1, year_for + 1):
    annual_principal = amount * (1.1 ** (year - 1))
    for month in range(12):
        total_value = (total_value + annual_principal) * (1 + returns)

total_value = round(total_value)
print("The expected amount :", total_value)
