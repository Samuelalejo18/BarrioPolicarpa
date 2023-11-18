import networkx as nx
import matplotlib.pyplot as plt


def nodos_sin_camino_ida_vuelta(G):
    nodos_sin_camino = []
    for nodo in G.nodes:
        for otro_nodo in G.nodes:
            if nodo != otro_nodo:
                if not (nx.has_path(G, nodo, otro_nodo) and nx.has_path(G, otro_nodo, nodo)):

                    nodos_sin_camino.append((nodo, otro_nodo))

    return nodos_sin_camino

G = nx.DiGraph()
nodos_sin_camino = nodos_sin_camino_ida_vuelta(G)

if not nodos_sin_camino:
    print("El grafo es fuertemente conexo, tiene camino de ida y vuelta entre todos los nodos. Por lo tanto es posible viajar desde cualquier punto A a B")
else:
    print("El grafo no es fuertemente conexo, no tiene camino de ida y vuelta entre los siguientes nodos:")
    for par in nodos_sin_camino:
        print(par)
    print("Por lo tanto es posible viajar desde cualquier punto A a B")




G.add_node("1")
G.add_node("2")
G.add_node("3")
G.add_node("4")
G.add_node("5")
G.add_node("6")
G.add_node("7")
G.add_node("8")
G.add_node("9")
G.add_node("10")
G.add_node("11")
G.add_node("12")
G.add_node("13")
G.add_node("14")
G.add_node("15")
G.add_node("16")
G.add_node("17")
G.add_node("18")
G.add_node("19")
G.add_node("20")
G.add_node("21")
G.add_node("22")
G.add_node("23")
G.add_node("24")
G.add_node("25")
G.add_node("26")
G.add_node("27")
G.add_node("28")
G.add_node("29")
G.add_node("30")
G.add_node("31")
G.add_node("32")
G.add_node("33")
G.add_node("34")
G.add_node("35")
G.add_node("36")
G.add_node("37")
G.add_node("38")
G.add_node("39")
G.add_node("40")
G.add_node("41")
G.add_node("42")
G.add_node("43")
G.add_node("44")
G.add_node("45")
G.add_node("46")
G.add_node("47")
G.add_node("48")
G.add_node("49")
G.add_node("50")
G.add_node("51")
G.add_node("52")
G.add_node("53")
G.add_node("54")
G.add_node("55")
G.add_node("56")
G.add_node("57")
G.add_node("58")
G.add_node("59")
G.add_node("60")
G.add_node("61")
G.add_node("62")
G.add_node("63")

G.add_edge("1","2")
G.add_edge("2","3")
G.add_edge("3","4")
G.add_edge("1","5")
G.add_edge("5","1")
G.add_edge("5","6")
G.add_edge("6","5")
G.add_edge("2","6")
G.add_edge("6","2")
G.add_edge("6","7")
G.add_edge("7","6")
G.add_edge("7","8")
G.add_edge("8","7")
G.add_edge("3","7")
G.add_edge("7","3")
G.add_edge("4","8")
G.add_edge("8","4")
G.add_edge("5","9")
G.add_edge("9","5")
G.add_edge("9","10")
G.add_edge("10","9")
G.add_edge("6","10")
G.add_edge("10","6")
G.add_edge("10","11")
G.add_edge("11","10")
G.add_edge("7","11")
G.add_edge("11","7")
G.add_edge("11","12")
G.add_edge("12","11")
G.add_edge("8","12")
G.add_edge("12","8")
G.add_edge("9","13")
G.add_edge("13","9")
G.add_edge("13","14")
G.add_edge("14","13")
G.add_edge("10","14")
G.add_edge("14","10")
G.add_edge("14","15")
G.add_edge("15","14")
G.add_edge("8","12")
G.add_edge("11","15")
G.add_edge("15","11")
G.add_edge("15","16")
G.add_edge("16","15")
G.add_edge("12","16")
G.add_edge("16","12")
G.add_edge("13","17")
G.add_edge("17","13")
G.add_edge("17","18")
G.add_edge("18","17")
G.add_edge("18","14")
G.add_edge("14","18")
G.add_edge("18","19")
G.add_edge("19","18")
G.add_edge("15","19")
G.add_edge("19","15")
G.add_edge("19","20")
G.add_edge("20","19")
G.add_edge("20","16")
G.add_edge("16","20")

G.add_edge("17","21")
G.add_edge("21","17")

G.add_edge("22","23")
G.add_edge("23","22")
G.add_edge("23","18")
G.add_edge("18","23")
G.add_edge("23","24")
G.add_edge("24","23")
G.add_edge("19","24")
G.add_edge("24","19")
G.add_edge("24","25")
G.add_edge("25","24")
G.add_edge("20","29")
G.add_edge("29","20")

G.add_edge("26","27")
G.add_edge("27","26")
G.add_edge("23","27")
G.add_edge("27","23")
G.add_edge("24","28")
G.add_edge("28","24")

G.add_edge("28","29")
G.add_edge("29","28")
G.add_edge("21","30")
G.add_edge("30","21")

G.add_edge("30","31")
G.add_edge("31","30")

G.add_edge("27","31")
G.add_edge("31","27")

G.add_edge("31","32")
G.add_edge("32","31")

G.add_edge("32","28")
G.add_edge("28","32")

G.add_edge("32","33")
G.add_edge("33","32")

G.add_edge("33","29")
G.add_edge("29","33")


G.add_edge("34","33")

G.add_edge("30","35")
G.add_edge("35","30")

G.add_edge("35","36")
G.add_edge("36","35")

G.add_edge("31","36")
G.add_edge("36","31")

G.add_edge("36","37")
G.add_edge("37","36")

G.add_edge("37","32")
G.add_edge("32","37")

G.add_edge("37","38")
G.add_edge("38","37")

G.add_edge("33","38")

G.add_edge("38","39")
G.add_edge("39","38")


G.add_edge("39","34")

G.add_edge("35","40")
G.add_edge("40","35")

G.add_edge("40","41")
G.add_edge("41","40")

G.add_edge("42","41")
G.add_edge("41","42")

G.add_edge("42","36")
G.add_edge("36","42")

G.add_edge("42","43")
G.add_edge("43","42")

G.add_edge("37","43")
G.add_edge("43","37")

G.add_edge("43","44")
G.add_edge("44","43")

G.add_edge("38","44")

G.add_edge("44","45")
G.add_edge("45","44")

G.add_edge("45","39")


G.add_edge("40","47")
G.add_edge("47","40")

G.add_edge("47","40")
G.add_edge("40","47")

G.add_edge("47","48")
G.add_edge("48","47")

G.add_edge("48","41")
G.add_edge("41","48")

G.add_edge("43","50")
G.add_edge("50","43")

G.add_edge("50","51")
G.add_edge("51","50")

G.add_edge("44","51")

G.add_edge("51","52")
G.add_edge("52","51")

G.add_edge("52","45")


G.add_edge("47","53")
G.add_edge("53","47")

G.add_edge("53","54")
G.add_edge("54","53")

G.add_edge("54","48")
G.add_edge("48","54")

G.add_edge("54","55")
G.add_edge("55","54")

G.add_edge("55","50")
G.add_edge("50","55")

G.add_edge("55","56")
G.add_edge("56","55")

G.add_edge("56","57")
G.add_edge("57","56")

G.add_edge("51","57")

G.add_edge("57","58")
G.add_edge("58","57")


G.add_edge("58","52")


G.add_edge("63","58")

G.add_edge("57","62")

G.add_edge("63","62")

G.add_edge("62","61")

G.add_edge("56","61")
G.add_edge("61","56")

G.add_edge("61","60")

G.add_edge("54","60")
G.add_edge("60","54")

G.add_edge("60","59")

G.add_edge("59","53")
G.add_edge("53","59")
G.add_edge("43","46")
G.add_edge("46","43")
G.add_edge("46","50")
G.add_edge("50","46")

G.add_edge("49","46")
G.add_edge("46","49")


node_positions = {
    "1": (0, -2),
    "2": (2, -2),
    "3": (4, -2),
    "4": (6, -2),
    "5": (0, -4),
    "6": (2, -4),
    "7": (4, -4),
    "8": (6, -4),
    "9": (0, -6),
    "10": (2, -6),
    "11": (4, -6),
    "12": (6, -6),
    "13": (0, -8),
    "14": (2, -8),
    "15": (4, -8),
    "16": (6, -8),
    "17": (0, -10),
    "18": (2, -10),
    "19": (4, -10),
    "20": (6, -10),
    "21": (0, -13),
    "22": (1, -12),
    "23": (2, -12),
    "24": (4, -12),
    "25": (5.4, -12),
    "26": (1, -14),
    "27": (2, -14),
    "28": (4, -14),
    "29": (6, -14),
    "30": (0, -16),
    "31": (2, -16),
    "32": (4, -16),
    "33": (6, -16),
    "34": (7, -16),
    "35": (0, -18),
    "36": (2, -18),
    "37": (4, -18),
    "38": (6, -18),
    "39": (7, -18),
    "40": (0, -20),
    "41": (1.5, -20),
    "42": (2, -20),
    "43": (4, -20),
    "44": (6, -20),
    "45": (7, -20),
    "46": (4, -21),
    "47": (0, -22),
    "48": (1.5, -22),
    "49": (3.5, -21),
    "50": (4, -23),
    "51": (6, -23),
    "52": (7, -23),
    "53": (0, -25),
    "54": (1.5, -25),
    "55": (4, -25),
    "56": (4, -26),
    "57": (6, -26),
    "58": (7, -26),
    "59": (0, -28),
    "60": (1.5, -28),
    "61": (4, -28),
    "62": (6, -28),
    "63": (7, -28),
}

nodos_sin_camino = nodos_sin_camino_ida_vuelta(G)

if not nodos_sin_camino:
    print("El grafo es fuertemente conexo, tiene camino de ida y vuelta entre todos los nodos. Por lo tanto es posible viajar desde cualquier punto A a B")
else:
    print("El grafo no es fuertemente conexo, no tiene camino de ida y vuelta entre los siguientes nodos:")
    for par in nodos_sin_camino:
        print(par)
    print("Por lo tanto es posible viajar desde cualquier punto A a B")
plt.figure(figsize=(10, 10))
nx.draw(G, pos=node_positions, with_labels=True, node_size=300, node_color='red', font_size=12, font_color='white', font_weight='bold')


plt.title("Grafo Dirigido")
plt.show()
