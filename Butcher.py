import numpy as np
from enum import Enum

# --- 1. Сущность "Таблица Бутчера" ---
class ButcherTableau:
    def __init__(self, a, b, c, name=""):
        self.matrix_A = np.array(a)
        self.weights_b = np.array(b)
        self.time_steps_c = np.array(c)
        self.num_stages_l = len(b)
        self.name = name

    def length(self):
        return self.num_stages_l

    def coeffsA(self):
        return self.matrix_A

    def coeffsB(self):
        return self.weights_b

    def coeffsC(self):
        return self.time_steps_c

# --- 2. Перечисление (Enum) вариантов ---
class ButcherID(Enum):
    TABLE_2_1 = "2.1"
    TABLE_2_2 = "2.2"
    TABLE_3_1 = "3.1"
    TABLE_3_2 = "3.2"
    TABLE_3_3 = "3.3"
    TABLE_4_1 = "4.1"

# --- 3. База данных таблиц ---
_TABLES = {
    ButcherID.TABLE_2_1: ButcherTableau(
        a=[[0, 0], [0.5, 0]],
        b=[0, 1],
        c=[0, 0.5],
        name="RK2 (Метод средней точки)"
    ),
    ButcherID.TABLE_2_2: ButcherTableau(
        a=[[0, 0], [1, 0]],
        b=[0.5, 0.5],
        c=[0, 1],
        name="RK2 (Метод Эйлера-Коши)"
    ),
    ButcherID.TABLE_3_1: ButcherTableau(
        a=[[0, 0, 0], [1/3, 0, 0], [0, 2/3, 0]],
        b=[1/4, 0, 3/4],
        c=[0, 1/3, 2/3],
        name="RK3 (Вариант 3.1)"
    ),
    ButcherID.TABLE_3_2: ButcherTableau(
        a=[[0, 0, 0], [2/3, 0, 0], [-1/3, 1, 0]],
        b=[1/4, 2/4, 1/4],
        c=[0, 2/3, 2/3],
        name="RK3 (Вариант 3.2)"
    ),
    ButcherID.TABLE_3_3: ButcherTableau(
        a=[[0, 0, 0], [0.5, 0, 0], [-1, 2, 0]],
        b=[1/6, 4/6, 1/6],
        c=[0, 0.5, 1],
        name="RK3 (Классический)"
    ),
    ButcherID.TABLE_4_1: ButcherTableau(
        a=[[0, 0, 0, 0], [0.5, 0, 0, 0], [0, 0.5, 0, 0], [0, 0, 1, 0]],
        b=[1/6, 2/6, 2/6, 1/6],
        c=[0, 0.5, 0.5, 1],
        name="RK4 (Классический)"
    )
}

# --- 4. Логика получения таблицы ---
def get_butcher_tableau(table_id: ButcherID):
    return _TABLES[table_id]

def get_num_butcher(n):
    Vector_myasnika = [
        ButcherID.TABLE_2_1,
        ButcherID.TABLE_2_2,
        ButcherID.TABLE_3_1,
        ButcherID.TABLE_3_2,
        ButcherID.TABLE_3_3,
        ButcherID.TABLE_4_1]
    return Vector_myasnika[n]



# ==========================================
#      КОНФИГУРАЦИЯ (ВЫБОР ВНУТРИ КОДА)
# ==========================================

# Чтобы сменить метод, просто измените значение переменной ниже.
# Доступные варианты:
# ButcherID.TABLE_2_1
# ButcherID.TABLE_2_2
# ButcherID.TABLE_3_1
# ButcherID.TABLE_3_2
# ButcherID.TABLE_3_3
# ButcherID.TABLE_4_1

SELECTED_METHOD = ButcherID.TABLE_4_1  # <--- МЕНЯТЬ ЗДЕСЬ
current_tableau = get_butcher_tableau(SELECTED_METHOD)
# --- Запуск ---
if __name__ == "__main__":
    # 1. Получаем таблицу напрямую, без вопросов в терминале
    current_tableau = get_butcher_tableau(SELECTED_METHOD)

