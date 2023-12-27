from ..entities import ThemeEntity,ActionEntity,CommonEntity,LightEntity,PrimaryEntity,SecondaryEntity,InfoEntity,SuccessEntity,WarningEntity,ErrorEntity,CommonSmallEntity

from ..utils import alpha
GREY={
"0":"#FFFFFF",
"100":"#F9FAFB",
"200":"#F4F6F8",
"300":"#DFE3E8",
"400":"#C4CDD5",
"500":"#919EAB",
"600":"#637381",
"700":"#454F5B",
"800":"#212B36",
"900":"#161C24",
}

PRIMARY={
"lighter":"#C8FACD",
"light":"#5BE584",
"main":"#00AB55",
"dark":"#007B55",
"darker":"#005249",
"contrast_text":"#FFFFFF",    
}


SECONDARY={
"lighter":"#D6E4FF",
"light":"#84A9FF",
"main":"#3366FF",
"dark":"#1939B7",
"darker":"#091A7A",
"contrast_text":"#FFFFFF",    
}
INFO={
"lighter":"#CAFDF5",
"light":"#61F3F3",
"main":"#00B8D9",
"dark":"#006C9C",
"darker":"#003768",
"contrast_text":"#FFFFFF",    
}
SUCCESS={
"lighter":"#D8FBDE",
"light":"#86E8AB",
"main":"#36B37E",
"dark":"#1B806A",
"darker":"#0A5554",
"contrast_text":"#FFFFFF",    
}
WARNING={
"lighter":"#FFF5CC",
"light":"#FFD666",
"main":"#FFAB00",
"dark":"#B76E00",
"darker":"#7A4100",
"contrast_text":GREY['800'],    
}
ERROR={
"lighter":"#FFE9D5",
"light":"#FFAC82",
"main":"#FF5630",
"dark":"#B71D18",
"darker":"#7A0916",
"contrast_text":"#FFFFFF",    
}


class Struct:
      def __init__(self, **entries):
         self.__dict__.update(entries)
ACTION={
            'hover': alpha(GREY['500'],0.08),
            'selected':alpha(GREY['500'],0.16),
            'disabled': alpha(GREY['500'],0.8),
            'disabled_background': alpha(GREY['500'],0.24),
            'focus': alpha(GREY['500'],0.24),
            'hover_opacity': 0.08,
            'disabled_opacity': 0.48,
         }
PRIMARY_OBJ = PrimaryEntity(PRIMARY)
SECONDARY_OBJ = SecondaryEntity(SECONDARY)
INFO_OBJ = InfoEntity(INFO)
SUCCESS_OBJ = SuccessEntity(SUCCESS)
WARNING_OBJ = WarningEntity(WARNING)
ERROR_OBJ = ErrorEntity(ERROR)
ACTION_OBJ = ActionEntity({
            'hover': alpha(GREY['500'],0.08),
            'selected':alpha(GREY['500'],0.16),
            'disabled': alpha(GREY['500'],0.8),
            'disabled_background': alpha(GREY['500'],0.24),
            'focus': alpha(GREY['500'],0.24),
            'hover_opacity': 0.08,
            'disabled_opacity': 0.48,
         })
COMMON_SMALL={'black':'#000000','white':'#FFFFFF'}
COMMON_OBJ_SMALL=CommonSmallEntity(COMMON_SMALL)
COMMON={
         'common': COMMON_OBJ_SMALL,
         'primary':PRIMARY_OBJ ,
         'secondary':SECONDARY_OBJ ,
         'info':INFO_OBJ ,
         'success': SUCCESS_OBJ ,
         'warning':WARNING_OBJ ,
         'error':ERROR_OBJ ,
         'grey': GREY,
         'divider': alpha(GREY['500'],0.24),
         'action':ACTION_OBJ,
         #    'action':ActionEntity({
         #    'hover': alpha(GREY['500'],0.08),
         #    'selected':alpha(GREY['500'],0.16),
         #    'disabled': alpha(GREY['500'],0.8),
         #    'disabled_background': alpha(GREY['500'],0.24),
         #    'focus': alpha(GREY['500'],0.24),
         #    'hover_opacity': 0.08,
         #    'disabled_opacity': 0.48,})
      }
      

COMMON_OBJ=CommonEntity(COMMON)
def palette(theme_mode):
   light={
    "mode": 'light',            
    "text": 
        {
        "primary":GREY["800"],
        "secondary":GREY["600"],
        "disabled":GREY["500"],
        },
    "background": 
        {
        "paper":"#FFFFFF",
        "default":"#FFFFFF",
        "neutral":GREY["200"],    
        },
    "action": COMMON_OBJ.action.update({"active":GREY["600"]}),

            }
   # light.update(COMMON)
   light_obj=LightEntity(light,COMMON)

   dark={
        "mode": 'dark',            
        "text": 
            {
            "primary":"#FFFFFF",
            "secondary":GREY["500"],
            "disabled":GREY["600"],
            },
        "background": 
            {
            "paper":GREY["800"],
            "default":GREY["900"],
            "neutral":alpha(GREY["500"],0.16),    
            },
        "action": COMMON_OBJ.action.update({"active":GREY["500"]}),

            }
   
   # dark.update(COMMON)

   # dark_theme_obj=ThemeEntity(dark)
   # # light_theme_obj=ThemeEntity(light)

   return light_obj if theme_mode=='light' else light_obj

'''
{
   "mode":"dark",
   "text":{
      "primary":"#FFFFFF",
      "secondary":"#919EAB",
      "disabled":"#637381"
   },
   "background":{
      "paper":"#212B36",
      "default":"#161C24",
      "neutral":"rgba(145, 158, 171, 0.16)"
   },
   "action":{
      "hover":"rgba(145, 158, 171, 0.08)",
      "selected":"rgba(145, 158, 171, 0.16)",
      "disabled":"rgba(145, 158, 171, 0.8)",
      "disabledBackground":"rgba(145, 158, 171, 0.24)",
      "focus":"rgba(145, 158, 171, 0.24)",
      "hoverOpacity":0.08,
      "disabledOpacity":0.48,
      "active":"#919EAB"
   },
   "common":{
      "black":"000000",
      "white":"#FFFFFF"
   },
   "primary":{
      "lighter":"#C8FACD",
      "light":"#5BE584",
      "main":"#00AB55",
      "dark":"#007B55",
      "darker":"#005249",
      "contrastText":"#FFFFFF"
   },
   "secondary":{
      "lighter":"#D6E4FF",
      "light":"#84A9FF",
      "main":"#3366FF",
      "dark":"#1939B7",
      "darker":"#091A7A",
      "contrastText":"#FFFFFF"
   },
   "info":{
      "lighter":"#CAFDF5",
      "light":"#61F3F3",
      "main":"#00B8D9",
      "dark":"#006C9C",
      "darker":"#003768",
      "contrastText":"#FFFFFF"
   },
   "success":{
      "lighter":"#D8FBDE",
      "light":"#86E8AB",
      "main":"#36B37E",
      "dark":"#1B806A",
      "darker":"#0A5554",
      "contrastText":"#FFFFFF"
   },
   "warning":{
      "lighter":"#FFF5CC",
      "light":"#FFD666",
      "main":"#FFAB00",
      "dark":"#B76E00",
      "darker":"#7A4100",
      "contrastText":"#212B36"
   },
   "error":{
      "lighter":"#FFE9D5",
      "light":"#FFAC82",
      "main":"#FF5630",
      "dark":"#B71D18",
      "darker":"#7A0916",
      "contrastText":"#FFFFFF"
   },
   "grey":{
      "0":"#FFFFFF",
      "100":"#F9FAFB",
      "200":"#F4F6F8",
      "300":"#DFE3E8",
      "400":"#C4CDD5",
      "500":"#919EAB",
      "600":"#637381",
      "700":"#454F5B",
      "800":"#212B36",
      "900":"#161C24"
   },
   "divider":"rgba(145, 158, 171, 0.24)"
}
'''

