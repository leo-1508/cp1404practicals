def read_wimbledon_data(filename):

    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            if line.strip():
                parts = line.strip().split("\t")
                year = parts[0]
                winner_name = parts[2]
                winner_country = parts[1]
                data.append((year, winner_name, winner_country))
    return data


def count_wimbledon_champions(data):

    champion_counts = {}
    for item in data:
        winner_name = item[1]
        if winner_name in champion_counts:
            champion_counts[winner_name] += 1
        else:
            champion_counts[winner_name] = 1
    return champion_counts


def list_countries_of_champions(data):

    countries = set()
    for item in data:
        winner_country = item[2]
        countries.add(winner_country)
    sorted_countries = sorted(countries)
    return sorted_countries


def main():
    filename = "wimbledon_champions.txt"
    data = read_wimbledon_data(filename)


    champion_counts = count_wimbledon_champions(data)


    countries = list_countries_of_champions(data)


    print("Wimbledon Champions:")
    for player, wins in sorted(champion_counts.items()):
        print(f"{player} {wins}")


    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
