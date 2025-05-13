#  Age in Seconds
# Ask the user for their age in years and calculate approximately how many seconds old they are.

users_age = int(input("How old are you? "))

age_in_seconds = users_age * 365 * 24 * 60 * 60

print("You are alive for", age_in_seconds, "seconds")