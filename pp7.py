# Practice problem 7-------------->>>>>> Search Engine
sentences = ["this is good", "Python is not python snake", "Python is cool", " Princy is a good girl",
             "Python is an interpreted, high-level, general-purpose programming language",
             "Pythons design philosophy emphasizes code readability with its notable use of significant whitespace.", ]

user_input = input("Please enter your query string: ")

results = list(filter(lambda y: user_input.lower() in y.lower(), sentences))
if len(results) > 0:
    print(f"{len(results)} results found :")
    # i = 0
    for index, item in enumerate(results):
        print(f"\t\t{index + 1}. {item}")
        # i += 1
else:
    print("No results found!!")
