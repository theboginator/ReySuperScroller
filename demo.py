collection = ["Mario", "Pikachu", "Bowser", "Link", "Marco Rubio", "Sonic", "Peach"]

upper = lambda x: x.upper()

def is_early_alpha(char_name :str):
    if char_name[0] < "P":
        return True
    return False

loud_names = list(map(upper, collection))
early_names = list(filter(is_early_alpha, loud_names))

for name in loud_names:
    print(name)

for name in early_names:
    print(name)