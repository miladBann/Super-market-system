
items = {
    100: {
        'name': "tomato",
        "price/kg": 5.80,
        "code": 100,
        "sale": "none"
    },
    101: {
        "name": "qucamber",
        "price/kg": 2.60,
        "code": 101,
        "sale": "none"
    },
    102: {
        "name": "karrot",
        "price/kg": 0.80,
        "code": 102,
        "sale": "none"
    },
    103: {
        "name": "green pepper",
        "price/kg": 3.20,
        "code": 103,
        "sale": "none"
    },
    104: {
        "name": "red bell pepper",
        "price/kg": 3.50,
        "code": 104,
        "sale": "none"
    },
    106: {
        "name": "egg plant",
        "price/kg": 8.40,
        "code": 106,
        "sale": "none"
    },
    108: {
        "name": "onion",
        "price/kg": 5.50,
        "code": 108,
        "sale": "none"
    },
    109: {
        "name": "white kabbage",
        "price/kg": 2.20,
        "code": 109,
        "sale": "none"
    },
    110: {
        "name": "red kabbage",
        "price/kg": 3.10,
        "code": 110,
        "sale": "none"
    },
    113: {
        "name": "pear",
        "price/kg": 4.10,
        "code": 113,
        "sale": "none"
    },
    114: {
        "name": "red apple",
        "price/kg": 6.20,
        "code": 114,
        "sale": "none"
    },
    115: {
        "name": "yellow apple",
        "price/kg": 7.10,
        "code": 115,
        "sale": "none"
    },
    116: {
        "name": "green apple",
        "price/kg": 5.40,
        "code": 116,
        "sale": "none"
    },
    135: {
        "name": "avocado",
        "price/kg": 4.60,
        "code": 135,
        "sale": "none"
    },
    169: {
        "name": "water melon",
        "price/kg": 8,
        "code": 169,
        "sale": "none"
    },
    140: {
        "name": "melon",
        "price/kg": 7.40,
        "code": 140,
        "sale": "none"
    }
}


def find_stuff(stuff):
    for item in items:
        if items[item]["name"] == stuff:
            print(item)


find_stuff("melon")
