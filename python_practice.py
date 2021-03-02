# print("Hello World")
# print("Hello world")

# counties = ["A","B","C"]
# # print(counties[1])
# print(len(counties))

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson","regisgtered_voters":432438})

#for county_dict in voting_data:
#    print(county_dict)
# for i in range(len(voting_data)):
#     print(voting_data[i])

#??
# for county_dict in voting_data:
#    print(county_dict["registered-voters"])
#??
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")
# #print using an F-string
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])

# temp = int(input("What is the temperature outside?"))

# if temp > 80:
#     print("Turn on the AC.")

# else:
#     print("Open the window.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)