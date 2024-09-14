import os
import tkinter.font as tk_font

from function.ProjectFunctions import t_load

p_ = os.path.dirname(__file__)
PATH = os.path.abspath(os.path.join(p_, '..'))
DATA_FILE_PATH = os.path.join(PATH, "data")
ICON_FILE_PATH = os.path.join(PATH, "icon")
os.makedirs(DATA_FILE_PATH, exist_ok=True)
A_PATH = os.path.join(DATA_FILE_PATH, "a")
B_PATH = os.path.join(DATA_FILE_PATH, "b")
C_PATH = os.path.join(DATA_FILE_PATH, "c")
D_PATH = os.path.join(DATA_FILE_PATH, "d")
E_PATH = os.path.join(DATA_FILE_PATH, "e")
F_PATH = os.path.join(DATA_FILE_PATH, "f")
G_PATH = os.path.join(DATA_FILE_PATH, "g")
H_PATH = os.path.join(DATA_FILE_PATH, "h")
I_PATH = os.path.join(DATA_FILE_PATH, "i")
J_PATH = os.path.join(DATA_FILE_PATH, "j")
K_PATH = os.path.join(DATA_FILE_PATH, "k")
L_PATH = os.path.join(DATA_FILE_PATH, "l")
M_PATH = os.path.join(DATA_FILE_PATH, "m")
N_PATH = os.path.join(DATA_FILE_PATH, "n")
O_PATH = os.path.join(DATA_FILE_PATH, "o")
P_PATH = os.path.join(DATA_FILE_PATH, "p")
Q_PATH = os.path.join(DATA_FILE_PATH, "q")
R_PATH = os.path.join(DATA_FILE_PATH, "r")
S_PATH = os.path.join(DATA_FILE_PATH, "s")
T_PATH = os.path.join(DATA_FILE_PATH, "t")
U_PATH = os.path.join(DATA_FILE_PATH, "u")
V_PATH = os.path.join(DATA_FILE_PATH, "v")
W_PATH = os.path.join(DATA_FILE_PATH, "w")
X_PATH = os.path.join(DATA_FILE_PATH, "x")
Y_PATH = os.path.join(DATA_FILE_PATH, "y")
Z_PATH = os.path.join(DATA_FILE_PATH, "z")
AA_PATH = os.path.join(DATA_FILE_PATH, "aa")
AB_PATH = os.path.join(DATA_FILE_PATH, "ab")
W_ROOT2_C_VAR_2_PATH = os.path.join(DATA_FILE_PATH, "w_root2_c_var_2_path")
ICON_PATH = os.path.join(ICON_FILE_PATH, "main_icon.ico")

v2 = int(t_load(D_PATH) or 1)
v3 = int(t_load(E_PATH) or 0)
v4 = int(t_load(F_PATH) or 0)

font_style1 = tk_font.Font(family="宋体", size=12)
font_style2 = tk_font.Font(family="等线", size=12)
font_style3 = tk_font.Font(family="黑体", size=12)

if v2 % 2 == 1:
    FONT_STYLE = font_style1
elif v3 % 2 == 1:
    FONT_STYLE = font_style2
elif v4 % 2 == 1:
    FONT_STYLE = font_style3

UTC_TIME = [
                "UTC-12:00", "UTC-11:00", "UTC-10:00", "UTC-09:00", "UTC-09:30", "UTC-08:00", "UTC-07:00",
                "UTC-06:00", "UTC-05:00", "UTC-04:00", "UTC-03:00", "UTC-02:00", "UTC-01:00", "UTC+00:00",
                "UTC-00:00", "UTC+01:00", "UTC+02:00", "UTC+03:00", "UTC+03:30", "UTC+04:00", "UTC+04:30",
                "UTC+05:00", "UTC+05:30", "UTC+05:45", "UTC+06:00", "UTC+06:30", "UTC+07:00", "UTC+08:00",
                "UTC+08:45", "UTC+09:00", "UTC+09:30", "UTC+10:00", "UTC+10:30", "UTC+11:00", "UTC+12:00",
                "UTC+12:45", "UTC+13:00", "UTC+14:00"
]

ZHI_DICT_NUM = {
            "子":1,
            "丑":2,
            "寅":3,
            "卯":4,
            "辰":5,
            "巳":6,
            "午":7,
            "未":8,
            "申":9,
            "酉":10,
            "戌":11,
            "亥":12
}

TIAN_GAN_DICT = {
            0:("甲","木","阳"),
            1:("甲","木","阳"),
            2:("乙","木","阴"),
            3:("丙","火","阳"),
            4:("丁","火","阴"),
            5:("戊","土","阳"),
            6:("己","土","阴"),
            7:("庚","金","阳"),
            8:("辛","金","阴"),
            9:("壬","水","阳"),
            10:("癸","水","阴")
}

DI_ZHI_DICT = {
            1: ("子", "阳", "水", "鼠"),
            2: ("丑", "阴", "土", "牛"),
            3: ("寅", "阳", "木", "虎"),
            4: ("卯", "阴", "木", "兔"),
            5: ("辰", "阳", "土", "龙"),
            6: ("巳", "阴", "火", "蛇"),
            7: ("午", "阳", "火", "马"),
            8: ("未", "阴", "土", "羊"),
            9: ("申", "阳", "金", "猴"),
            10: ("酉", "阴", "金", "鸡"),
            11: ("戌", "阳", "土", "狗"),
            12: ("亥", "阴", "水", "猪")
}

YUE_GAN_DICT = {
            "甲":("甲","木","阳"),
            "乙":("乙","木","阴"),
            "丙":("丙","火","阳"),
            "丁":("丁","火","阴"),
            "戊":("戊","土","阳"),
            "己":("己","土","阴"),
            "庚":("庚","金","阳"),
            "辛":("辛","金","阴"),
            "壬":("壬","水","阳"),
            "癸":("癸","水","阴")

}

YUE_ZHI_DICT = {
            1:("寅", "阳", "木", "虎"),
            2:("卯", "阴", "木", "兔"),
            3:("辰", "阳", "土", "龙"),
            4:("巳", "阴", "火", "蛇"),
            5:("午", "阳", "火", "马"),
            6:("未", "阴", "土", "羊"),
            7:("申", "阳", "金", "猴"),
            8:("酉", "阴", "金", "鸡"),
            9:("戌", "阳", "土", "狗"),
            10:("亥", "阴", "水", "猪"),
            11:("子", "阳", "水", "鼠"),
            12:("丑", "阴", "土", "牛")
}

SHI_CHEN_DICT = {
            1: ("丑", "阴", "土", "牛"),
            2: ("丑", "阴", "土", "牛"),
            3: ("寅", "阳", "木", "虎"),
            4: ("寅", "阳", "木", "虎"),
            5: ("卯", "阴", "木", "兔"),
            6: ("卯", "阴", "木", "兔"),
            7: ("辰", "阳", "土", "龙"),
            8: ("辰", "阳", "土", "龙"),
            9: ("巳", "阴", "火", "蛇"),
            10: ("巳", "阴", "火", "蛇"),
            11: ("午", "阳", "火", "马"),
            12: ("午", "阳", "火", "马"),
            13: ("未", "阴", "土", "羊"),
            14: ("未", "阴", "土", "羊"),
            15: ("申", "阳", "金", "猴"),
            16: ("申", "阳", "金", "猴"),
            17: ("酉", "阴", "金", "鸡"),
            18: ("酉", "阴", "金", "鸡"),
            19: ("戌", "阳", "土", "狗"),
            20: ("戌", "阳", "土", "狗"),
            21: ("亥", "阴", "水", "猪"),
            22: ("亥", "阴", "水", "猪"),
            23: ("子", "阳", "水", "鼠"),
            24: ("子", "阳", "水", "鼠"),
}