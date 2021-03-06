# Calculate timing of Output Qn for fixed capacitor & variable resistor.

resistor = [1000000,2.2*1000000,4.7*1000000,10*1000000]
#            1Mohm   2.2Mohm     4.7Mohm     10Mohm


fosc = []
for r in resistor:
    R = 910000      #470K=24hr / 910K=1hr
    C = 0.22 / 1000000 # C=0.22uF
    f = 1 / (2.2 * (r+R) * C )
    fosc.append(f)
print ("Fosc = " + str(fosc))

# fosc = [1.81, 0.826, 0.386, 0.181]

for freq in fosc:
    print("\nFrequency = " + str(freq) + str("Hz") )
    for n in range(4,15,1):
        t = (2**n)/freq
        if t > 59 :
            if t>3599:
                print("Q" + str(n) + " = " + str(t/3600) + " hour")
            else:
                print("Q" + str(n) + " = " + str(t/60) + " min")
        else:
            print("Q" + str(n) + " = " + str(t) + " sec")
