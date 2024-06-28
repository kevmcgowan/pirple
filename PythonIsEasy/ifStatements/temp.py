# if condition:
#     Action

click = False

like = 0

click = True

if click == True:
    like = like + 1
    click = False

# print (like)

temperature = 20
thermo = 15
# print(thermo)

if temperature <= 15:
    thermo = thermo + 5

# print (thermo)

if temperature >= 20:
    thermo = thermo - 3

# print(thermo)

time = "Day"
sleepy = False
pyjamas = "Unknown"
InBed = True

print(pyjamas)

# if time == "Night" and sleepy == True:
if time == "Night" or sleepy == True:    
    pyjamas = "On"

elif time == "Morning":
    pyjamas = "On"

else:
    pyjamas = "Off"

print(pyjamas)

