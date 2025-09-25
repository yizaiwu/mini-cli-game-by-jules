# This file will contain the game map and location data.

WORLD_MAP = {
    (0, 0): {
        "name": "寧靜的森林",
        "description": "你身處一片寧靜的森林中，四周綠樹環繞。",
        "monster": None,
    },
    (1, 0): {
        "name": "森林小徑",
        "description": "一條蜿蜒的小徑穿過森林，通往未知的地方。",
        "monster": "slime", # A slime is here!
    },
    (2, 0): {
        "name": "古老的廢墟",
        "description": "你來到一處古老的廢墟，斷垣殘壁訴說著逝去的時光。",
        "monster": None,
    },
    (0, 1): {
        "name": "潺潺的小溪",
        "description": "一條清澈的小溪從你腳邊流過，水聲潺潺。",
        "monster": None,
    },
    (1, 1): {
        "name": "村莊廣場",
        "description": "這裡是村莊的中心，一個小廣場。你從這裡開始你的冒險。",
        "monster": None,
    },
    (2, 1): {
        "name": "鐵匠鋪",
        "description": "一間鐵匠鋪，傳來叮叮噹噹的打鐵聲。",
        "monster": None,
    },
    (0, 2): {
        "name": "廣闊的平原",
        "description": "你來到一片廣闊的平原，視野遼闊。",
        "monster": None,
    },
    (1, 2): {
        "name": "平原上的巨石",
        "description": "平原上矗立著一塊巨大的石頭，不知從何而來。",
        "monster": None,
    },
    (2, 2): {
        "name": "陡峭的山壁",
        "description": "你走到平原的盡頭，前方是無法攀爬的陡峭山壁。",
        "monster": None,
    },
}

MAP_WIDTH = 3
MAP_HEIGHT = 3

def get_location(x, y):
    """Gets the location object at the given coordinates."""
    return WORLD_MAP.get((x, y))