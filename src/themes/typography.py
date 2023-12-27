from  ..entities import TypographyEntity


def rem_to_px(value):
  return round(float(value) * 16)

def px_to_rem(value):
  return f"{value / 16}rem"


def responsive_font_sizes(sm, md, lg):
    result = {
        "@media (min-width:600px)": {
            "font_size": px_to_rem(sm)
        },
        "@media (min-width:900px)": {
            "font_size": px_to_rem(md)
        },
        "@media (min-width:1200px)": {
            "font_size": px_to_rem(lg)
        }
    }
    
    return result

# # Gọi hàm calculate_font_sizes với các giá trị tùy ý
# font_sizes = calculate_font_sizes(14, 18, 24)

FONT_PRIMARY = 'Public Sans, sans-serif'; # Google Font
#FONT_SECONDARY = 'CircularStd, sans-serif'; # Local Font

TYPOGRAPHY = {
  "font_family": FONT_PRIMARY,
  "font_weight_regular": 400,
  "font_weight_medium": 600,
  "font_weight_bold": 700,
  "h1": {
    "font_weight": 800,
    "line_height": 80 / 64,
    "font_size": px_to_rem(40),
    **responsive_font_sizes(sm= 52, md= 58, lg= 64),
  },
  "h2": {
    "font_weight": 800,
    "line_height": 64 / 48,
    "font_size": px_to_rem(32),
    **responsive_font_sizes(sm = 40, md = 44, lg = 48 ),
  },
  "h3": {
    "font_weight": 700,
    "line_height": 1.5,
    "font_size": px_to_rem(24),
    **responsive_font_sizes(sm = 26, md = 30, lg = 32 ),
  },
  "h4": {
    "font_weight": 700,
    "line_height": 1.5,
    "font_size": px_to_rem(20),
    **responsive_font_sizes(sm = 20, md = 24, lg = 24 ),
  },
  "h5": {
    "font_weight": 700,
    "line_height": 1.5,
    "font_size": px_to_rem(18),
    **responsive_font_sizes(sm = 19, md = 20, lg = 20 ),
  },
  "h6": {
    "font_weight": 700,
    "line_height": 28 / 18,
    "font_size": px_to_rem(17),
    **responsive_font_sizes(sm = 18, md = 18, lg = 18 ),
  },
  "subtitle1": {
    "font_weight": 600,
    "line_height": 1.5,
    "font_size": px_to_rem(16),
  },
  "subtitle2": {
    "font_weight": 600,
    "line_height": 22 / 14,
    "font_size": px_to_rem(14),
  },
  "body1": {
    "line_height": 1.5,
    "font_size": px_to_rem(16),
  },
  "body2": {
    "line_height": 22 / 14,
    "font_size": px_to_rem(14),
  },
  "caption": {
    "line_height": 1.5,
    "font_size": px_to_rem(12),
  },
  "overline": {
    "font_weight": 700,
    "line_height": 1.5,
    "font_size": px_to_rem(12),
    "text_transform": 'uppercase',
  },
  "button": {
    "font_weight": 700,
    "line_height": 24 / 14,
    "font_size": px_to_rem(14),
    "text_transform": 'capitalize',
  },
    }


TYPOGRAPHY_OBJ = TypographyEntity(TYPOGRAPHY)

def func_typography():
   return TYPOGRAPHY_OBJ
   

