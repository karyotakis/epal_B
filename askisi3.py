# -*- coding: utf-8 -*-
# Άσκηση 3
# έλεγχος διψήφιου δοθέντος αριθμού

X = input("Δώσε ένα αριθμό: ")
X = abs(X)  # για εντοπισμό αρνητικών αριθμών

if X < 10 or X >= 100:
    print "Ο αριθμός δεν είναι διψήφιος."
else:
    print "Ο αριθμός είναι διψήφιος."
