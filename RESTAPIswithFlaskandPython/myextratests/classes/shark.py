class Shark:
    #The constructor method:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Writing my methods
    def swim(self):
        #reference the name and age, look how concatenate string an integer at the same time
        print(self.name + " is swimming and She is " + str(self.age) + " years old")

    def be_awesome(self):
        #reference the name
        print(self.name + " is being awesome.")

def main():
    sammy = Shark("Sammy", 30)
    sammy.swim()
    sammy.be_awesome()


if __name__ == "__main__":
    main()

