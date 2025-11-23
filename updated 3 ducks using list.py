ducks = ["duck 1" "yellow duck", "duck 2" "red duck", "duck 3" "green duck"]
ducks.extend(["duck 4""purple duck", "duck 5" "mint duck"])

def main():
    for name in ducks:
        parts = name.split(" ", 2)
        color = parts[2]
        print(f"This is {name}, and his/her color is {color}.")
main()
