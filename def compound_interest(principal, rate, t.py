def compound_interest(principal, rate, time):
    return round(principal * (1 + rate) ** time, 2)

principal = float(input('input principal: '))
rate = float(input('input rate: '))
time = float(input('input time : '))
finalas = compound_interest(principal, rate, time)
print(f'bla bla bla {time}, bla bla bla {finalas}')

    