# Motorcycle-checker
Playing around with checking motorcycle plates

Note: edge cases where motorcycles that have a "wheelplan" designation of: "NOT STANDARD" will not be recorded as motorbikes.
A solution to this issue would require further analysis of the JSON package received from the DVLA VES API response.
Theoretically possible to confirm whether it is a motorbike or not through fields like: make, bodyType, vehicleClass and taxClass
