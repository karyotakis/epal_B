# -*- coding: utf-8 -*-
# Άσκηση if
# Χωρίς έλεγχο ορθότητας εισαγωγής

bathmos = input("Δώσε βαθμό του μαθητή: ")

if 17.5 <= bathmos <= 20:
    print "Άριστα"
elif 15.5 <= bathmos <= 17.4:
    print "Πολύ καλά"
elif 13.5 <= bathmos <= 15.4:
    print "Καλά"
elif 9.5 <= bathmos <= 13.4:
    print "Μέτρια"
elif 0 <= bathmos <= 9.4:
    print "Άπορρίπτεται"
