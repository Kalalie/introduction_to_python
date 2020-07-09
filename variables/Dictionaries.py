groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

print(groceries)

print(groceries["Baby Spinach"])
print(groceries["Crackers"])

groceries["Crackers"] = 2.50
print(groceries)

groceries["Avocado"] = 1.00
print(groceries)

for item in groceries:
    print(item)
    print(groceries[item])

print()

for item, price in groceries.items():
    print(item, price)

cohorts = {
    "perth" : ["Anna", "Fanny", "Felicity", "Viv"],
    "brisbane" : ["Teagan","Vivian","Nic","Joy"]
}
print(cohorts)

for cohort, peeps in cohorts.items():
    print(cohort)
    for peep in peeps:
        print(peep)
    print()

all_cohorts = {
    2019: {
        "perth": ["Anna", "Sarah", "Nina", "Ellie"]
    },
    2020: {
        "perth": ["Anna", "Viv", "Nic", "Teagen"],
        "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
    }
}

for year, cohorts in all_cohorts.items():
    print(year)
    for city, cohort in cohorts.items():
        print(city, cohort)
        for peep in cohort:
            print(peep)

print(all_cohorts[2020]["perth"][0])