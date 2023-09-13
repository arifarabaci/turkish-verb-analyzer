from tkinter import *
import re
import hfst_dev
from hfst_dev import compile_lexc_file
from hfst_dev import HfstTransducer

root = Tk()
root.title("Turkish Word Analyzer")
root.geometry("400x200")

analyzer = compile_lexc_file('bad_hfst.lexc')
analyzer = HfstTransducer(analyzer)
analyzer.invert()
analyzer1 = compile_lexc_file('good_hfst.lexc')

e = Entry(root)
e.grid(column=0, row=0)
output_morpheme = Text(root, width=25, height=1)
output_morpheme.grid(column=1, row=2)
output_morpheme.insert('end-1c', '')
outlabel = Label(root, text="Morphemes:")
outlabel.grid(column=0, row=2)
output_wordlabel = Label(root, text="Corrected Word:")
output_wordlabel.grid(column=0, row=3)
output_word = Text(root, width=25, height=1)
output_word.grid(column=1, row=3)
output_word.insert('end-1c', '')

def on_change(e):
    badout = analyzer.lookup(e.widget.get())

    morpheme_list = badout[0][0]

    monosyl_sonorant = ["al", "bil", "bul", "dur", "gel", "gör",
                        "kal", "ol", "öl", "san", "var", "ver", "vur"]
    voiceless = ["f", "s", "t", "k", "ç", "ş", "h", "p"]
    vowels = ["ö", "ü", "a", "ı", "e", "u", "o", "i"]
    ek_list = morpheme_list.split('+')[0:]  # list for vowel detection
    ilk_fiil = re.search("[+]", morpheme_list)
    if "+Prog" in morpheme_list:  # Ünlü daralması
        if "+Neg" not in morpheme_list:
            if ek_list[0][-1] in vowels:
                ek_list[0] = ek_list[0][:-1]

    if "+Prog" in morpheme_list:  # Prog ve negative için -meyor -meeyor şeklinde hataların giderilmesi
        if "+Neg" in morpheme_list:
            morpheme_list = morpheme_list.replace("+Neg", "+Neg1")
            morpheme_list = morpheme_list.replace("+Prog", "+Prog1")

    if "+Aorist" in morpheme_list:  # Aoriste consonan vowel atama, ve negative atama
        if "+Neg" not in morpheme_list:
            if ek_list[0][-1] in vowels:
                morpheme_list = morpheme_list.replace("+Aorist", "+Aorist_v")
            elif len(ek_list[0]) < 4:
                if ek_list[0] not in monosyl_sonorant:
                    morpheme_list = morpheme_list.replace("+Aorist", "+Aorist_3")
                else:
                    morpheme_list = morpheme_list.replace("+Aorist", "+Aorist_c")
            else:
                morpheme_list = morpheme_list.replace("+Aorist", "+Aorist_c")
        if "+Neg" in morpheme_list:
            if "+Past" not in morpheme_list:
                if "+1sg" in morpheme_list:
                    morpheme_list = morpheme_list.replace("+Aorist", "+Aorist_Neg1sg")
                    morpheme_list = morpheme_list.replace("+1sg", "")
                    morpheme_list = morpheme_list.replace("+Neg", "")
                if "+1pl" in morpheme_list:
                    morpheme_list = morpheme_list.replace("+Aorist", "+Aorist_Neg1pl")
                    morpheme_list = morpheme_list.replace("+1pl", "")
                    morpheme_list = morpheme_list.replace("+Neg", "")
                else:
                    morpheme_list = morpheme_list.replace("+Aorist", "+Aorist_neg")
            else:
                morpheme_list = morpheme_list.replace("+Aorist", "+Aorist_neg")

    if "+Caus" in morpheme_list:
        if ek_list[0][-1] in voiceless:
            morpheme_list = morpheme_list.replace("+Caus", "+Caus1")


    if "+Future" in morpheme_list:  # Future için consonant vowel atama
        if "+Neg" in morpheme_list:
            morpheme_list = morpheme_list.replace("+Future", "+Future_v")
            if "+Past" not in morpheme_list:
                if "+1sg" in morpheme_list:
                    morpheme_list = morpheme_list.replace("+Future_v", "+Future_v_y")
                if "+1pl" in morpheme_list:
                    morpheme_list = morpheme_list.replace("+Future_v", "+Future_v_y")
        if "+Neg" not in morpheme_list:
            if ek_list[0][-1] in vowels:
                morpheme_list = morpheme_list.replace("+Future", "+Future_v")
                if "+Past" not in morpheme_list:
                    if "+1sg" in morpheme_list:
                        morpheme_list = morpheme_list.replace("+Future_v", "+Future_v_y")
                    if "+1pl" in morpheme_list:
                        morpheme_list = morpheme_list.replace("+Future_v", "+Future_v_y")
            elif ek_list[0][-1] not in vowels:
                morpheme_list = morpheme_list.replace("+Future", "+Future_c")
                if "+Past" not in morpheme_list:
                    if "+1sg" in morpheme_list:
                        morpheme_list = morpheme_list.replace("+Future_c", "+Future_c_y")
                    if "+1pl" in morpheme_list:
                        morpheme_list = morpheme_list.replace("+Future_c", "+Future_c_y")

    if "+Past" in morpheme_list:
        if "+Past_Ev" in morpheme_list:
            morpheme_list = morpheme_list.replace("+Past", "+Past1")
            morpheme_list = morpheme_list.replace("+Past1_Ev", "+Past_Ev")
        if "+Future" in morpheme_list:
            morpheme_list = morpheme_list.replace("+Past", "+Past1")
            if "+Past1_Ev" in morpheme_list:
                morpheme_list = morpheme_list.replace("+Past1_Ev", "+Past_Ev")

    order_list = {"Caus":0, "Caus1":0, "Neg": 1, "Neg1": 1, "Aorist_c": 2, "Aorist_v": 2, "Aorist_3": 2,
                  "Aorist_neg": 2, "Aorist_Neg1sg": 2, "Aorist_Neg1pl": 2,
                  "Prog": 2, "Prog1": 2,
                  "Future_c": 3, "Future_v": 3,
                  "Future_c_y": 3, "Future_v_y": 3,
                  "Past_Ev": 4, "Past": 5, "Past1": 5,
                  "1sg": 6, "2sg": 6, "1pl": 6, "2pl": 6, "3pl": 6
                  }
    if "Past" in morpheme_list:
        listorder_for_past1 = morpheme_list.split('+')[:]
        order_for_past1 = []
        for elt in listorder_for_past1[1:]:
            order_for_past1.append((order_list[elt], elt))
        order_for_past1.sort()
        order_min = []
        for x in order_for_past1:
            order_min.append(x[0])
        if ek_list[0][-1] in voiceless:
            if min(order_min) == 5:
                morpheme_list = morpheme_list.replace("+Past", "+Past1")

    zaman = ["Aorist_c", "Aorist_v", "Aorist_3",
             "Aorist_neg", "Aorist_Neg1sg", "Aorist_Neg1pl",
             "Prog", "Prog1",
             "Future_c", "Future_v",
             "Future_c_y", "Future_v_y",
             "Past_Ev", "Past", "Past1"]
    if "Past" in morpheme_list:
        if "+3pl" in morpheme_list:
            listorder_for3pl = morpheme_list.split('+')[:]
            order_for3pl = []
            checkforzaman = []
            for item in listorder_for3pl:
                if item in zaman:
                    checkforzaman.append("True")
            if len(checkforzaman) > 1:
                order_list = {"Neg": 1, "Neg1": 1, "Aorist_c": 2, "Aorist_v": 2, "Aorist_3": 2,
                              "Aorist_neg": 2, "Aorist_Neg1sg": 2, "Aorist_Neg1pl": 2,
                              "Prog": 2, "Prog1": 2,
                              "Future_c": 3, "Future_v": 3,
                              "Future_c_y": 3, "Future_v_y": 3,
                              "Past_Ev": 5, "Past": 6, "Past1": 6,
                              "1sg": 7, "2sg": 7, "1pl": 7, "2pl": 7, "3pl": 4
                              }

    ek_list_for_order = morpheme_list.split('+')[:]
    new_order = []
    for elt in ek_list_for_order[1:]:
        new_order.append((order_list[elt], elt))
    new_order.sort()

    corrected_string = ek_list[0]
    for morpheme in new_order:
        corrected_string = corrected_string + "+" + morpheme[1]

    out_analyzed = analyzer1.lookup(corrected_string)
    out_analyzed = out_analyzed[0][0]
    output_morpheme.delete(1.0, 'end-1c')
    output_morpheme.insert('end-1c', badout[0][0])
    output_word.delete(1.0, 'end-1c')
    output_word.insert('end-1c', out_analyzed)
    print(badout[0][0])
    print(out_analyzed)

e.bind('<Return>', on_change)

root.mainloop()