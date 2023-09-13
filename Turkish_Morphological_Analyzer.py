from tkinter import *
import re
import hfst_dev
from hfst_dev import compile_lexc_file

analyzer1 = compile_lexc_file('good_hfst_for_button.lexc')

root = Tk()
root.title("Turkish Morphological Analyser")
root.geometry("750x340")

out = []
def on_change():
  out.clear()
  out.append(e.get())
  currentword_box.delete(1.0, "end-1c")
  currentword_box.insert("end-1c", str(out[0]))
  analyzed_box.delete(1.0, "end-1c")
  output_box.delete(1.0, "end-1c")
  b1["state"] = "normal"
  b2["state"] = "normal"
  b3["state"] = "normal"
  b4["state"] = "normal"
  b5["state"] = "normal"
  b6["state"] = "normal"
  b7["state"] = "normal"
  b8["state"] = "normal"
  b9["state"] = "normal"
  b10["state"] = "normal"
  b11["state"] = "normal"
  analyzeb["state"] = "normal"
  b0["state"] = "disabled"
  e.delete(0, "end")
e = Entry(root)
e.grid(column=0, row=0)
#e.bind("<Return>", on_change)
ebutton = Button(root, text="Enter", command=on_change)
ebutton.grid(column=1, row=0)

currentword_label = Label(root, text="Kelimeniz:")
currentword_label.grid(column=3, row=0)
currentword_box = Text(root, width=20, height=1)
currentword_box.grid(column=4, row=0)
currentword_box.insert("end-1c", "")

outputbox_label = Label(root, text="Kelimeniz:")
outputbox_label.grid(column=1, row=8)
output_box = Text(root, width=30, height=1)
output_box.grid(column=2, row=8)
output_box.insert("end-1c", "")

analyzedbox_label = Label(root, text="Sonuç:")
analyzedbox_label.grid(column=1, row=10)
analyzed_box = Text(root, width=30, height=1)
analyzed_box.grid(column=2, row=10)
analyzed_box.insert("end-1c", "")
person_morphemes = ["+1sg", "+1pl", "+2sg", "+2pl", "+3pl"]
def button0():
  if out[-1] in person_morphemes:
    b7["state"] = "normal"
    b8["state"] = "normal"
    b9["state"] = "normal"
    b10["state"] = "normal"
    b11["state"] = "normal"
  if out[-1] == "+Prog":
    b1["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b5["state"] = "normal"
    b6["state"] = "normal"
  if out[-1] == "+Neg":
    b2["state"] = "normal"
  if out[-1] == "+Aorist":
    b1["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
  if out[-1] == "+Future":
    b1["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b5["state"] = "normal"
    b6["state"] = "normal"
  if out[-1] == "+Past_Ev":
    b1["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b5["state"] = "normal"
    b6["state"] = "normal"
  if out[-1] == "+Past":
    b1["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b6["state"] = "normal"
    b5["state"] = "normal"
  out.remove(out[-1])
  if "+Aorist" in out:
    b1["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
  if "+Prog" in out:
    b1["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
  if "+Future" in out:
    b1["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
  if "+Past_Ev" in out:
    b5["state"] = "disabled"
  if "+Past" in out:
    b6["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b0 = Button(root, text="Backspace", command=button0)
b0.grid(column=2, row=1)

def BSswitch():
  if len(out) == 1:
    b0["state"] = "disabled"
  else:
    b0["state"] = "normal"
BSswitch()

def button1():
  out.append("+Prog")
  b1["state"] = "disabled"
  b3["state"] = "disabled"
  b4["state"] = "disabled"
  if "+Past_Ev" in out:
    b6["state"] = "disabled"
  if "+Past_Ev" in out:
    b6["state"] = "disabled"
  if "+Past" in out:
    b5["state"] = "disabled"
  if "+Past" in out:
    b5["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b1 = Button(root, text="Progressive", command=button1)
b1.grid(column=0, row=2)

def button2():
  out.append("+Neg")
  b2["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b2 = Button(root, text="Negative", command=button2)
b2.grid(column=0, row=3)

def button3():
  out.append("+Aorist")
  if "+Past" in out:
    b5["state"] = "disabled"
  if "+Past_Ev" in out:
    b6["state"] = "disabled"
  b1["state"] = "disabled"
  b3["state"] = "disabled"
  b4["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b3 = Button(root, text="Aorist", command=button3)
b3.grid(column=0, row=4)

def button4():
  out.append("+Future")
  b1["state"] = "disabled"
  b3["state"] = "disabled"
  b4["state"] = "disabled"
  if "+Past_Ev" in out:
    b6["state"] = "disabled"
  if "+Past_Ev" in out:
    b6["state"] = "disabled"
  if "+Past" in out:
    b5["state"] = "disabled"
  if "+Past" in out:
    b5["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b4 = Button(root, text="Future", command=button4)
b4.grid(column=0, row=5)

def button5():
  out.append("+Past_Ev")
  b5["state"] = "disabled"
  if "+Past" in out:
    b1["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
  if "+Aorist" in out:
    b6["state"] = "disabled"
  if "+Prog" in out:
    b6["state"] = "disabled"
  if "+Future" in out:
    b6["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b5 = Button(root, text="Past Evidential", command=button5)
b5.grid(column=0, row=6)

def button6():
  out.append("+Past")
  b6["state"] = "disabled"
  if "+Past_Ev" in out:
    b1["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
  if "+Aorist" in out:
    b5["state"] = "disabled"
  if "+Prog" in out:
    b5["state"] = "disabled"
  if "+Future" in out:
    b5["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b6 = Button(root, text="Past", command=button6)
b6.grid(column=0, row=7)

def button7():
  out.append("+1sg")
  b7["state"] = "disabled"
  b8["state"] = "disabled"
  b9["state"] = "disabled"
  b10["state"] = "disabled"
  b11["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b7 = Button(root, text="1st Person Singular", command=button7)
b7.grid(column=4, row=2)

def button8():
  out.append("+1pl")
  b7["state"] = "disabled"
  b8["state"] = "disabled"
  b9["state"] = "disabled"
  b10["state"] = "disabled"
  b11["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b8 = Button(root, text="1st Person Plural", command=button8)
b8.grid(column=4, row=3)

def button9():
  out.append("+2sg")
  b7["state"] = "disabled"
  b8["state"] = "disabled"
  b9["state"] = "disabled"
  b10["state"] = "disabled"
  b11["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b9 = Button(root, text="2nd Person Singular", command=button9)
b9.grid(column=4, row=4)

def button10():
  out.append("+2pl")
  b7["state"] = "disabled"
  b8["state"] = "disabled"
  b9["state"] = "disabled"
  b10["state"] = "disabled"
  b11["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b10 = Button(root, text="2nd Person Plural", command=button10)
b10.grid(column=4, row=5)

def button11():
  out.append("+3pl")
  b7["state"] = "disabled"
  b8["state"] = "disabled"
  b9["state"] = "disabled"
  b10["state"] = "disabled"
  b11["state"] = "disabled"
  out_str = "".join(out)
  output_box.delete(1.0, "end-1c")
  output_box.insert("end-1c", out_str)
  BSswitch()
b11 = Button(root, text="3rd Person Plural", command=button11)
b11.grid(column=4, row=6)

def analyze():
  morpheme_list = "".join(out)
  morpheme_list = "".join(morpheme_list)

  monosyl_sonorant = ["al","bil","bul","dur","gel","gör",
                      "kal","ol","öl","san","var","ver","vur"]
  voiceless = ["f","s","t","k","ç","ş","h","p"]
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
      elif ek_list[0][-1] not in vowels :
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

  order_list = {"Neg": 1, "Neg1": 1, "Aorist_c": 2, "Aorist_v": 2, "Aorist_3":2,
                "Aorist_neg": 2, "Aorist_Neg1sg": 2, "Aorist_Neg1pl": 2,
                "Prog": 2, "Prog1": 2,
                "Future_c": 3, "Future_v": 3,
                "Future_c_y": 3, "Future_v_y":3,
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
  analyzed_box.delete(1.0, "end-1c")
  analyzed_box.insert("end-1c", out_analyzed)

analyzeb = Button(root, text="analyze", command=analyze)
analyzeb.grid(column=2, row=9)
b1["state"] = "disabled"
b2["state"] = "disabled"
b3["state"] = "disabled"
b4["state"] = "disabled"
b5["state"] = "disabled"
b6["state"] = "disabled"
b7["state"] = "disabled"
b8["state"] = "disabled"
b9["state"] = "disabled"
b10["state"] = "disabled"
b11["state"] = "disabled"
b0["state"] = "disabled"
analyzeb["state"] = "disabled"


root.mainloop()

