class Shark:
    #The constructor method:
    def __init__(self, name):
        self.name = name

    # Writing my methods
    def swim(self):
        #reference the name
        print(self.name + " is swimming.")

    def be_awesome(self):
        #reference the name
        print(self.name + " is being awesome.")

def main():
    sammy = Shark("Sammy")
    sammy.be_awesome()

    stevie = Shark("Stevie")
    stevie.swim()

if __name__ == "__main__":
    main()

