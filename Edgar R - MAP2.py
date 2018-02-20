Normal_world = {
    'THE_ROOM': {
        'NAME': "The Room",
        'DESCRIPTION': "You enter the mysterious room called the room. You can't see a lot of things since the room \n"
                       "is dimly lit. All you can really see is that people have been here. It is all messy as if \n"
                       "they were looking for something. They probably found it or game up since they was a corner \n"
                       "of the room that was neat and clean. To the West is the Mirror room.",
        'PATHS': {
            'WEST': 'MIRROR_R'
        }
    },
    'BOOK_SECTION': {
        'NAME': "Book Section",
        'DESCRIPTION': "You reach the book section of the store. You see famous books in the 'Famous book section'. \n"
                       "Their were books from the 'Harry Potter' series and the books series of 'Percy Jackson and \n"
                       "the Olympians'. To the North is the Walkway, to the South is a door that is leading outside \n"
                       "and to the West is the clothing section.",
        'PATHS': {
            'NORTH': 'WALKWAY',
            'SOUTH': 'BACK_STORE',
            'WEST': 'CLOTHING_SECTION'
        }
    },
    'CLOTHING_SECTION': {
        'NAME': "Clothing Section",
        'DESCRIPTION': "You reach the clothing section. You see lines of clothes missing. The only thing you see \n"
                       "is armor that seems to fit you. It seems to be made out of chain mail armor. To the East \n"
                       "is the book section of the store.",
        'PATHS': {
            'EAST': 'BOOK_SECTION'
        }
    },
    'BACK_STORE': {
        'NAME': "Back of Store",
        'DESCRIPTION': "You reached the back of the store. You see a garbage can that is full of trash. You see a \n"
                       "graffiti that says 'He came'. What that meant was a mystery",
        'PATHS': {
            'NORTH': '',
            'EAST': '',
            'SOUTH': '',
            'WEST': ''
        }
    },
    'SCHOOL_HOUSE': {
        'NAME': "School House",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': '',
            'EAST': '',
            'SOUTH': '',
            'WEST': ''
        }
    },
    '': {
        'NAME': " ",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': '',
            'EAST': '',
            'SOUTH': '',
            'WEST': ''
        }
    },
}
