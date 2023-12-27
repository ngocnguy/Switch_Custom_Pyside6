from .palette import palette
from ..utils import alpha
from ..entities import CreateShadowEntity

THEMECOLOR = palette('light')

LIGHT_MODE = THEMECOLOR.grey["500"]

DARK_MODE = THEMECOLOR.common.black

def create_shadow(color):
  TRANSPARENT = alpha(color, 0.16)
  
  shadow = {
    "z1" : f"0 1 2 {TRANSPARENT}",
    "z4" : f"0 4 8 {TRANSPARENT}",
    "z8" : f"0 8 16 {TRANSPARENT}",
    "z12" : f"0 12 24 {TRANSPARENT}",
    "z16" : f"0 16 32 {TRANSPARENT}",
    "z20" : f"0 20 40 {TRANSPARENT}",
    "z24" : f"0 24 48 {TRANSPARENT}",
    
    "primary":f"0 8 16 {alpha(THEMECOLOR.primary.main, 0.24)}",
    "info": f"0 8 16 {alpha(THEMECOLOR.info.main, 0.24)}",
    "secondary":f"0 8 16 {alpha(THEMECOLOR.secondary.main, 0.24)}",
    "success": f"0 8 16 {alpha(THEMECOLOR.success.main, 0.24)}",
    "warning":f"0 8 16 {alpha(THEMECOLOR.warning.main, 0.24)}",
    "error":f"0 8 16 {alpha(THEMECOLOR.error.main, 0.24)}",
    
    "card": f"0 0 2 {alpha(color, 0.2)}, 0 12 24 {alpha(color, 0.12)}",
    "dialog": f"-40 40 80 {alpha(color, 0.24)}",
    "dropdown": f"0 0 2 {alpha(color, 0.24)}, -20 20 40 {alpha(color, 0.24)}",
  }

  SHADOW_OBJ = CreateShadowEntity(shadow)
  return SHADOW_OBJ


def func_custom_shadows(theme_mode):#neu chay vao ham nay thi dau tien se truyen gia tri cua LIGHT_MODE hoac DARK_MODE vao ham create_shadow
  #va nhung gia tri do deu la gia tri mau hex sau do truyen vao create_shadow(tu z1 den z24 ) va chay thay doi mau va kich thuoc tat ca cac component trong app
  return create_shadow(LIGHT_MODE) if theme_mode == 'light' else create_shadow(DARK_MODE)

