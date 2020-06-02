print("Hello World!")
print(type(3))
print(type("Kim"))
ballots =1,341
print(type(ballots))
print(type(73.81))
print(type(""))
isDog = True
print(type(isDog))
num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True
print(num_candidates)
print(won_election)
print(candidate)

print("-------")
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16- 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)

print("-------")
print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print( 5 + (9 * 3 / 2 - 4))
print(5 + (9 * 3 / (2 - 4)))


counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[0])
print(counties[1])
print(counties[2])
print(counties[-1])
print(counties[-2])

print("------")
print(len(counties))
print("--------")
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
print(counties[1:3])
print("--------*20")

counties.append("El Paso")
counties.insert(2,"El Paso")
print(len(counties))
print(counties)

counties.remove("El Paso")
print(counties)

counties.pop(3)
counties.pop(-1)
print(counties)
print("--------")

Counties = ["Arapahoe","Denver","Jefferson"]
counties.append("El Paso")
counties.remove("Arapahoe")
print(counties)
counties.append("Denver")
counties.append("Jefferson")
counties.pop(0)
counties.pop(0)
counties.append("Arapahoe")
print(counties)



print("------")
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict["Arapahoe"])
print(counties_dict["Denver"])
print(counties_dict["Jefferson"])
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys)
print(counties_dict.values())
print(counties_dict.get("Denver"))

print("-"*20)
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data.append({"county": "El Paso", "registered_voters": 461149})

voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.pop(0)
voting_data.pop(0) 
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
print(voting_data)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

print("---"*50)
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


print("---"*40)
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

print("Keys")
for county in counties_dict.keys():
    print(county)

print("Values")
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

print("Items")
county, voters in counties_dict.items()
print(county, " county has ", voters, "registered voters")   


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters' )

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]
for data in voting_data:
    print(f'{data["county"]} county has {data} registered voters') 






