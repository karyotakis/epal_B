# -*- coding: utf-8 -*-
# Άσκηση 6
# Απουσίες μαθητή
# Χωρίς έλεγχο ορθότητας εισαγωγής αριθμών

apoysies = input("Δώσε αριθμό συνολικών απουσιών μαθητή: ")
dikaiologhmenes = input("Δώσε αριθμό δικαιολογημένων απουσιών από γιατρό: ")

if dikaiologhmenes > 50:
    dikaiologhmenes = 50

if apoysies - dikaiologhmenes > 130:
    print "Ο μαθητής απορρίπτεται λόγω απουσιών."
else:
    print "Ο μαθητής μπορεί να δώσει εξετάσεις."
