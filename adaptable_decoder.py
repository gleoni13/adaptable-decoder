from ast import match_case


string_name = "EXAMPLE."
string_trad = ""

string_name = string_name.lower()

def decode_character(char):
   match char:
      case "a":
         return "c"
      case "b":
         return "d"
      case "c":
         return "e"
      case "," | "." | "!":
         return "|"
     case " ":
         return " "
     case _:
         return char

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
