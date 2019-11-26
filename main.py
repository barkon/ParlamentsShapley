from itertools import permutations

parlament = {
    "A": 15,
    "B": 35,
    "C": 25,
    "D": 25
}

sejms = {
    2011: {
        "PO": 207,
        "PIS": 157,
        "PALIKOT": 40,
        "PSL": 28,
        "SLD": 28,
    },
    2007: {
        "PO": 209,
        "PIS": 166,
        "LID": 53,
        "PSL": 31,
        "MN": 1,
    },
    2005: {
        "PIS": 165,
        "PO": 141,
        "SAMO": 60,
        "SLD": 58,
        "LPR": 36,
    },
    1997: {
        "AWS": 201,
        "SLD": 164,
        "UW": 60,
        "PSL": 27,
        "ROP": 8,
    },
    1993: {
        "SLD": 179,
        "PSL": 138,
        "UD": 77,
        "UP": 43,
        "KPN": 23,
    }
}

threshold = 230


def main():
    for year, sejm in sejms.items():
        perms = permutations(sejm.keys())
        party_contr = {party: 0 for party in sejm}
        number_of_perms = 0
        for perm in perms:
            total_power = 0
            found = False
            for party in perm:
                if not found:
                    total_power += sejm[party]
                    if total_power > threshold:
                        party_contr[party] += 1
                        found = True
            number_of_perms += 1
        shapley = {party: contr/number_of_perms for party, contr in party_contr.items()}
        print('shapley for year', year, sejm, 'is', shapley)


if __name__ == '__main__':
    main()
