# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HSZ1Ic2I9UVXpr8TspgZePE5aN4uvgDL
"""

def kasallik_tashxisi(alomat):
  if alomat =="grip":
   return"sizga gripxod ichishni tavsiya qilaman "
  elif alomat=="qorin ogriq":
   return"sizga espemuzam ichishni tavsiya qilaman "
  elif alomat=="oyoq ogriq ":
   return"sizga bolnol surishni tavsiya qilaman "
  elif alomat=="koz ogriq ":
   return"sizga telefondan uzoqroq turishni tavsiya qilaman "
  elif alomat=="quloq ogriq ":
   return"sizga quloqchindan kamroq foydalanishni tavsiya qilaman "
  elif alomat=="kogil aynish":
   return"sizga toza havoga chiqishni tavsiya qilaman "
  elif alomat=="burun ogriq ":
   return"sizga boshqalarni ishiga burun suqmasligingizni tavsiya qilaman "
  elif alomat=="tish  ogriq ":
   return"sizga qupen ichishni  tavsiya qilaman "
  elif alomat=="tomoq ogriq ":
   return"sizga muzday narsalar yemaslikni va ichmaslikni  tavsiya qilaman "
  elif alomat=="kongil ogriq ":
   return"sizga sevishmaslikni tavsiya qilaman "
  else :
    return "noaniq kasallik ,shifoxonaga murojat qiling "
alomat =input ("alomatni kiriting")
natija= kasallik_tashxisi(alomat)
print(natija)

def telefon_narxlari(model):
 if modeli=="honor x6a":
   return"uzb:1200000,rus:1100000 "
 else :
    return "noaniq model adminga murojat qiling 93 272 01 09 "
model=input ("modelni kiriting")
natija=telefon_narxlari(model)
print(natija)