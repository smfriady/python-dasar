# Casting type data
# Merubah dari satu tipe data
# ke tipe data lain

# tipe data = int, float, str, bool
## INT
data_int = 1
print("data :", data_int, "bertipe : ",  type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # Akan false jika nilai int = 0
print("data :", data_float, "bertipe : ",  type(data_float))
print("data :", data_str, "bertipe : ",  type(data_str))
print("data :", data_bool, "bertipe : ",  type(data_bool))

print("-"*50)
## FLOAT
dt_2_float = 9.5
print("data :", dt_2_float, "bertipe : ",  type(dt_2_float))

data_2_int = int(dt_2_float)  # akan dibulatkan ke bawah
data_2_str = str(dt_2_float)
data_2_bool = bool(dt_2_float)  # Akan false jika nilai float = 0
print("data :", data_2_int, "bertipe : ",  type(data_2_int))
print("data :", data_2_str, "bertipe : ",  type(data_2_str))
print("data :", data_2_bool, "bertipe : ",  type(data_2_bool))

print("-"*50)
## BOOL
dt_3_bool = False
print("data :", dt_3_bool, "bertipe : ",  type(dt_3_bool))

data_3_int = int(dt_3_bool)  # True = 1, False = 0
data_3_str = str(dt_3_bool)
data_3_float = float(dt_3_bool)  # True = 1.0, False = 0.0
print("data :", data_3_int, "bertipe : ",  type(data_3_int))
print("data :", data_3_str, "bertipe : ",  type(data_3_str))
print("data :", data_3_float, "bertipe : ",  type(data_3_float))

print("-"*50)
## STR
dt_4_str = "Ucup"
print("data :", dt_4_str, "bertipe : ",  type(dt_4_str))

data_4_int = int(dt_4_str)  # string harus angka
data_4_float = float(dt_4_str) # string harus angka
data_4_bool = bool(dt_4_str)  #  False jika string kosong
print("data :", data_4_int, "bertipe : ",  type(data_4_int))
print("data :", data_4_float, "bertipe : ",  type(data_4_float))
print("data :", data_4_bool, "bertipe : ",  type(data_4_bool))
