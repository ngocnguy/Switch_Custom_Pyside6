def alpha(hex_color, opacity):
   if hex_color.startswith('#'):
      hex_color = hex_color[1:]
   # Chuyển đổi từ chuỗi HEX thành dạng số nguyên 16 phân số ở cơ số 16
   r = int(hex_color[0:2], 16)
   g = int(hex_color[2:4], 16)
   b = int(hex_color[4:6], 16)

   # Trả về giá trị RGBA
   rgba = (r, g, b, opacity)
   return "rgba"+str(rgba)


def alpha_hex_to_rgb(hex_color):
   if hex_color.startswith('#'): 
      hex_color = hex_color[1:]
   # Chuyển đổi từ chuỗi HEX thành dạng số nguyên 16 phân số ở cơ số 16
   r = int(hex_color[0:2], 16)
   g = int(hex_color[2:4], 16)
   b = int(hex_color[4:6], 16)


   # Trả về giá trị RGBA
   rgb = (r, g, b)
   return "rgb"+str(rgb)


def strshadow_to_element_color(strshadow :str):
   elements = strshadow.split()
   opacity = elements[3].split(",")
   color_enter = alpha(opacity[0],float(opacity[1]))
   q_color=list(map(float,color_enter[5:-1].split(',')))

   opacity_qcolor=q_color[3]*255
   color_result=f"QColor({int(q_color[0])},{int(q_color[1])},{int(q_color[2])},{round(opacity_qcolor)})"
   return color_result
  

# color=strshadow_to_element_color("0 1 2 #625151,0.24")

# print(color)

# def tong()
