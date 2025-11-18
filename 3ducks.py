ducks = {"duck 1": "yellow duck", "duck 2": "red duck", "duck 3": "green duck"}
ducks.update({"duck 4": "purple duck", "duck 5": "mint duck"})

def main():
    for name in ducks.keys():
        print(f"This is {name}, and his/her color is {ducks[name]}.")
main()
