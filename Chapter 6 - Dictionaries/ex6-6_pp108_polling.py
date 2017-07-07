"""

"""

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python'
       }


people_I_should_poll = ["matt", "jen", "sarah", "john", "samantha", "tina"]

for person in people_I_should_poll:
    if person in favorite_languages.keys():
        print(person.title() + ", thank you for responding to the poll!")
    else:
        print(person.title() + ", please respond to my poll :)")
