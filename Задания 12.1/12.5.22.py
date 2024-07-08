print("Игра Mab Libs")
print("---Все о птицах---")
print()
adjective_0 = input("прилагательное - ")
plural_noun_1 = input("существительное(мн.ч) - ")
adjective_color_2 = input("прилагательное_цвет - ")
adjective_color_3 = input("прилагательное_цвет - ")
adjective_color_4 = input("прилагательное_цвет - ")
adjective_5 = input("прилагательное - ")
noun_6 = input("существительное - ")
plural_noun_body_parts_7 = input("существительное(мн.ч), части тела - ")
verb_8 = input("глагол - ")
verb_9 = input("глагол - ")
adjective_10 = input("прилагательное - ")
plural_noun_animals_11 = input("существительное(мн.ч),животные - ")
verb_12 = input("глагол - ")
noun_13 = input("глагол - ")
verb_14 = input("глагол - ")
plural_noun_animals_15 = input("существительное(мн.ч),животные - ")
plural_noun_16 = input("существительное(мн.ч) - ")
verb_17 = input("глагол - ")
plural_noun_18 = input("существительное(мн.ч) - ")
plural_noun_19 = input("существительное(мн.ч) - ")

s = ""
lines = [line.strip() for line in open('mad_libs.txt')]
for line in lines:
	s += line
print()
print()
print(s.format(adjective_0,plural_noun_1,adjective_color_2,adjective_color_3,
	  adjective_color_4,adjective_5,noun_6,plural_noun_body_parts_7,verb_8,
	  verb_9,adjective_10,plural_noun_animals_11,verb_12,noun_13,verb_14,
	  plural_noun_animals_15,plural_noun_16,verb_17,plural_noun_18,plural_noun_19))  