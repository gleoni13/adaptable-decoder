from ast import match_case


string_name = "ASQRMBC, GJ LMORPM RCKNM NMRP..A.. COQCPC GLDGLGRM, KY LML JY LMQRPY NYXGCLXY. GJ RSM JYQQGOKM QRYLLM APCYLBM SL ZPSQGM DYQRGBGMQM NCP RSRRM GJ BPYEMKYPC. AG YONCRRGYKM BCG PGOSJRYRG YJ NG..U.. NPCORM, M AMKC RG YZZGYKM DYRRM YOACLBCPC RG DYPCKM AYBCPC. LML BCJSBCPAG YLAMPY. G KYCORPG BCJJY LMRRC."
string_trad = ""

string_name = string_name.lower()

def trad(lettera):
    match lettera:
        case "a":
            return "c"
        case "b":
            return "d"
        case "c":
            return "e"
        case "d":
            return "f"
        case "e":
            return "g"
        case "f":
            return "h"
        case "g":
            return "i"
        case "h":
            return "j"
        case "i":
            return "k"
        case "j":
            return "l"
        case "k":
            return "m"
        case "l":
            return "n"
        case "m":
            return "o"
        case "n":
            return "p"
        case "o":
            return "q"
        case "p":
            return "r"
        case "q":
            return "s"
        case "r":
            return "t"
        case "s":
            return "u"
        case "t":
            return "v"
        case "u":
            return "w"
        case "v":
            return "x"
        case "w":
            return "y"
        case "x":
            return "z"
        case "y":
            return "a"
        case "z":
            return "b"
        case "," | "." | "!":
            return "|"
        case " ":
            return " "

# Iterate over the string
a = ""
for element in string_name:
    a = element
    a = trad(a)
    print(a)
    string_trad += a
print(string_trad)

with open('ris.txt', 'w', encoding='utf-8') as f:
    f.write(string_trad)