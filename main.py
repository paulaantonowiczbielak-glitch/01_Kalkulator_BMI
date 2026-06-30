wzrost = float(input("Podaj wzrost w metrach: "))
waga = float(input("Podaj wagę w kilogramach: "))
bmi = round(waga / (wzrost*wzrost),2 )
print("Twoje BMI wynosi:", bmi)
if bmi<18.5:
    print("Masz niedowagę")
elif bmi<25:
    print("Masz prawdiłową wagę")
elif bmi<30:
    print("Masz nadwagę")
else:
    print("Masz otyłość")
print("Dziękuję za skorzystanie z kalkulatora BMI")