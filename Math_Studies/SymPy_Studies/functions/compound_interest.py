from math import exp
#So, let's try to calculate a simple continious interest:
starting_amount = 5000
interest_per_year = .20
time = 5
total = starting_amount * exp(interest_per_year * time) # We can use this formula to calculate: A = P x e^(rt)
# When A means total after interest, P means starting amount, r means interest rate and t represents time
print(f'{total:.4f}')
