"""
A simple program adapted from pp153.

Demonstrates arbitrary keyword arguments
"""

def build_profile(first, last, **user_info):
    """Builds a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

albert = build_profile("albert", "einstein",
                       location="princeton", field="physics")

harry = build_profile("Harry", "Potter", school="Hogwarts", hair="Black",
                      patronus="Stag")

print(albert)
print("")
print(harry)
