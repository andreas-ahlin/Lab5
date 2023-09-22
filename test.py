class Country:
    def __init__(self, name, area, pop):
        self.name = str(name)
        self.area = float(area)
        self.pop = int(pop)
        self.dens = self.calc_dens()

    def calc_dens(self):
        return round(float(self.pop/self.area), 1)


def read_file(file_name):
    with open(file_name, "r") as file:
        country_list = []
        for line in file.readlines():
            name, area, pop = line.split(",")[0:3]
            country = Country(name, area, pop)
# facts = line.split(",")
# country = Country(facts[0], facts[1], facts[2])
        country_list.append(country)
    return country_list


def __str__(self):
    return f"{self.name:<16} {self.area:<12} {self.pop:<11} {self.dens}"


def main():
    try:
        print(f"{'Country':<16} {'Area':<12} {'Population':<11} {'Density'}")
        countries = Country.read_file("europa.txt")
        for country in countries:
            print(country)
    except:
        print("File format incorrect!")
    # for i in range(len(countries)):
    # # print(countries[i].name)
    # # print(countries[i].area)
    # # print(countries[i].pop)
    # # print(countries[i].dens)
    # print(countries[i])


main()
