# 12. Create a dictionary of cities and temperatures (float). Print cities where the temperature is greater than 40.

dict = {
    "kolkata":40.5,
    "delhi":35.8,
    "mumbai":32.4,
    "chennai":38.2,
    "hyderabad":36.7,
    "Ahmedabad":45.4
}

for i in dict:
    if dict[i] > 40:
        print("Cities with temperature greater than 40 :",i)