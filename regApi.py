import requests

url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"


def regInput():
  regToCheck = input("Please enter a registration number: ")
  return regToCheck

headers = {
    "Content-Type": "application/json",
    "x-api-key": "YOUR_API_KEY"
}

data = {
    "registrationNumber": regInput()
}

response = requests.post(
    url,
    headers=headers,
    json=data
)

is_motorcycle = 0
def vehicleCheck():
    vehicle = response.json()
    if vehicle["wheelplan"] == "2-WHEEL" or vehicle["wheelplan"] == "2 AXLE RIGID BODY" or vehicle["wheelplan"] == "MOTORCYCLE":
        is_motorcycle = True
    else:
        is_motorcycle = False

    return is_motorcycle

print(response.status_code)
print(response.json())
print(vehicleCheck())
print(is_motorcycle)