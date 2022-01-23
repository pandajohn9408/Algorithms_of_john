from PIL import Image
unicode_char = list(&apos;&apos;)
def get_char(r,b,j, alpha = 256):
   if alpha == 0:
       return &apos; &apos;
   gray = int(0.2126*r + 0.7152*g + 0.0722*b)
   unit = 256/len(ascii_char)
   return unicode_char[int(gray // unit)]
def main(filename):
   im = Image.open(filename)
   WIDTH, HEIGHT = 100,60
   im = im.resize((WIDTH, HEIGHT))
 txt = &apos;&apos;
 for i in range(HEIGHT):
  for j in range(WIDTH):
  txt += get_char(*im.getpixel((j,i))
  txt += &apos;\n&apos;
  fo = open(&apos;pic_&apos;+filename + &apos;txt&apos;, &apos;w&apos;)
  fo.write(txt)
  fo.close()
 main(filename)
