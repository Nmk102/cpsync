---
title: "NumPy — массивы, индексация, маски, broadcasting, оси"
kind: notes
tasks: [49243189]
order: 30
summary: Как устроен ndarray (shape, dtype), создание массивов, срезы и «вид vs копия», булевы маски, векторные операции, broadcasting, агрегирование по осям, типичные ошибки. С задачами и проверенными ответами.
---

## 1. Зачем NumPy

Список Python хранит ссылки на объекты, и цикл по нему медленный. **NumPy-массив** (`ndarray`) хранит числа одного типа подряд в памяти, а операции над ним выполняются внутри на C — **в 10–100 раз быстрее** и без циклов в коде («векторизация»).

```python
import numpy as np
a = np.array([1, 2, 3, 4])
print(a * 2)          # [2 4 6 8]        — каждый элемент умножен на 2
print(a + a)          # [2 4 6 8]
print(a ** 2)         # [ 1  4  9 16]
print([1, 2] * 2)     # [1, 2, 1, 2]     — а со списком это повторение!
```

## 2. Форма и тип

:::def Главные атрибуты
- `a.shape` — размеры по осям, кортеж: `(4,)` — вектор, `(3, 4)` — матрица 3 строки × 4 столбца, `(h, w, 3)` — цветная картинка.
- `a.ndim` — число осей, `a.size` — число элементов.
- `a.dtype` — тип элементов: `int64`, `float64`, `uint8` (0…255 — пиксели), `bool`.
:::

```python
m = np.arange(12).reshape(3, 4)
print(m)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(m.shape, m.ndim, m.size, m.dtype)   # (3, 4) 2 12 int64
```

**Создание:** `np.zeros((3, 4))`, `np.ones(5)`, `np.full((2, 2), 7)`, `np.arange(0, 10, 2)` → `[0 2 4 6 8]`, `np.linspace(0, 1, 5)` → `[0. 0.25 0.5 0.75 1.]`, `np.random.randint(0, 10, size=(3, 3))`.

## 3. Индексация и срезы

```python
m[1, 2]       # 6          — строка 1, столбец 2
m[1]          # [4 5 6 7]  — вся строка 1
m[:, 2]       # [ 2  6 10] — весь столбец 2
m[0:2, 1:3]   # [[1 2] [5 6]] — подматрица
m[::-1]       # строки в обратном порядке
m[:, ::2]     # каждый второй столбец
m[[0, 2]]     # строки 0 и 2 («причудливая» индексация списком)
```

:::warn Срез — это «вид», а не копия
`b = m[0:2, 1:3]` не копирует данные: изменение `b` меняет `m`! Нужна копия — `b = m[0:2, 1:3].copy()`. Индексация списком или маской (`m[[0, 2]]`, `m[m > 5]`) всегда даёт **копию**.
:::

## 4. Булевы маски

Сравнение массива даёт массив из `True`/`False` той же формы. Им можно **выбирать** и **присваивать**:
```python
a = np.array([5, -2, 7, 0, -9, 3])
mask = a > 0              # [ True False  True False False  True]
print(a[mask])            # [5 7 3]
print(mask.sum())         # 3 — сколько положительных (True = 1)
a[a < 0] = 0              # обнулить отрицательные
print(a)                  # [5 0 7 0 0 3]
print(np.where(a > 4, 1, 0))   # [1 0 1 0 0 0] — «если, то, иначе» поэлементно
```
Условия соединяются `&` (и), `|` (или), `~` (не) — **со скобками**: `a[(a > 0) & (a < 6)]`. Слова `and`/`or` с массивами не работают.

## 5. Агрегирование и оси

`sum`, `mean`, `max`, `min`, `argmax`, `std` по всему массиву или вдоль оси:

```python
m = np.arange(12).reshape(3, 4)
print(m.sum())            # 66
print(m.sum(axis=0))      # [12 15 18 21] — суммы по столбцам (схлопнули ось 0 — строки)
print(m.sum(axis=1))      # [ 6 22 38]    — суммы по строкам
print(m.max(axis=1))      # [ 3  7 11]
print(m.argmax())         # 11 — индекс максимума в «развёрнутом» массиве
```

:::tip Как запомнить `axis`
`axis=k` — это ось, которая **исчезает**. У матрицы `(3, 4)` после `sum(axis=0)` форма `(4,)`, после `sum(axis=1)` — `(3,)`.
:::

## 6. Broadcasting

Операции над массивами **разной формы** работают, если формы «совместимы»: сравниваем размеры **с конца**, они должны быть равны или один из них равен 1. Недостающие оси считаются единичными.

<svg class="fig" viewBox="0 0 640 200" width="640">
  <rect class="l f3" x="20.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="37.0" y="62.0" text-anchor="middle">1</text>
  <rect class="l f3" x="54.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="71.0" y="62.0" text-anchor="middle">2</text>
  <rect class="l f3" x="88.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="105.0" y="62.0" text-anchor="middle">3</text>
  <rect class="l f3" x="20.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text x="37.0" y="96.0" text-anchor="middle">4</text>
  <rect class="l f3" x="54.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text x="71.0" y="96.0" text-anchor="middle">5</text>
  <rect class="l f3" x="88.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text x="105.0" y="96.0" text-anchor="middle">6</text>
  <rect class="l f3" x="20.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text x="37.0" y="130.0" text-anchor="middle">7</text>
  <rect class="l f3" x="54.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text x="71.0" y="130.0" text-anchor="middle">8</text>
  <rect class="l f3" x="88.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text x="105.0" y="130.0" text-anchor="middle">9</text>
  <text x="140.0" y="95.0" text-anchor="middle">+</text>
  <rect class="l f2" x="160.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="177.0" y="62.0" text-anchor="middle">10</text>
  <rect class="l f2" x="194.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="211.0" y="62.0" text-anchor="middle">20</text>
  <rect class="l f2" x="228.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="245.0" y="62.0" text-anchor="middle">30</text>
  <rect class="l d" x="160.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text class="s" x="177.0" y="96.0" text-anchor="middle">10</text>
  <rect class="l d" x="194.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text class="s" x="211.0" y="96.0" text-anchor="middle">20</text>
  <rect class="l d" x="228.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text class="s" x="245.0" y="96.0" text-anchor="middle">30</text>
  <rect class="l d" x="160.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text class="s" x="177.0" y="130.0" text-anchor="middle">10</text>
  <rect class="l d" x="194.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text class="s" x="211.0" y="130.0" text-anchor="middle">20</text>
  <rect class="l d" x="228.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text class="s" x="245.0" y="130.0" text-anchor="middle">30</text>
  <text x="280.0" y="95.0" text-anchor="middle">=</text>
  <rect class="l f1" x="300.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="317.0" y="62.0" text-anchor="middle">11</text>
  <rect class="l f1" x="334.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="351.0" y="62.0" text-anchor="middle">22</text>
  <rect class="l f1" x="368.0" y="40.0" width="34.0" height="34.0" rx="0"/>
  <text x="385.0" y="62.0" text-anchor="middle">33</text>
  <rect class="l f1" x="300.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text x="317.0" y="96.0" text-anchor="middle">14</text>
  <rect class="l f1" x="334.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text x="351.0" y="96.0" text-anchor="middle">25</text>
  <rect class="l f1" x="368.0" y="74.0" width="34.0" height="34.0" rx="0"/>
  <text x="385.0" y="96.0" text-anchor="middle">36</text>
  <rect class="l f1" x="300.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text x="317.0" y="130.0" text-anchor="middle">17</text>
  <rect class="l f1" x="334.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text x="351.0" y="130.0" text-anchor="middle">28</text>
  <rect class="l f1" x="368.0" y="108.0" width="34.0" height="34.0" rx="0"/>
  <text x="385.0" y="130.0" text-anchor="middle">39</text>
  <text class="s" x="20.0" y="170.0">shape (3, 3) + shape (3,) → строка «копируется» вниз (пунктир) — без реального копирования</text>
  <text class="s" x="430.0" y="60.0">Правило: размеры сравниваются</text>
  <text class="s" x="430.0" y="78.0">с конца; они должны быть</text>
  <text class="s" x="430.0" y="96.0">равны или один из них = 1</text>
</svg>

```python
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m + np.array([10, 20, 30]))      # прибавили к каждой строке
print(m - m.mean(axis=0))              # вычесть среднее каждого столбца
col = np.array([[100], [200], [300]])  # форма (3, 1)
print(m + col)                         # прибавили к каждому столбцу
```
`(3, 3) + (3,)` ✓; `(3, 3) + (3, 1)` ✓; `(3, 3) + (2,)` ✗ — ошибка `operands could not be broadcast`.

## 7. Полезные функции

| Задача | Код |
|---|---|
| изменить форму | `a.reshape(2, -1)` (−1 — «посчитай сам») |
| транспонировать | `m.T` |
| склеить | `np.concatenate([a, b])`, `np.vstack`, `np.hstack` |
| отсортировать | `np.sort(a)`, индексы сортировки `np.argsort(a)` |
| уникальные | `np.unique(a, return_counts=True)` |
| накопленная сумма | `np.cumsum(a)` |
| ограничить диапазон | `np.clip(a, 0, 255)` |
| матричное умножение | `A @ B` (а `A * B` — поэлементное!) |

:::warn Переполнение в NumPy
В отличие от обычных чисел Python, элементы NumPy имеют фиксированный размер. `np.array([200], dtype=np.uint8) + 100` даёт `[44]` (300 − 256): переполнение «по кругу». С пикселями это частая ошибка — сначала переводите в `int` или `float`, считайте, потом `np.clip(…, 0, 255).astype(np.uint8)`.
:::

## 8. Проверь себя

:::task 1. `a = np.arange(1, 11)`. Получите: чётные элементы; сумму квадратов; массив, где числа больше 5 заменены на 5.
:::answer
`a[a % 2 == 0]` → `[ 2  4  6  8 10]`; `(a ** 2).sum()` → 385; `np.minimum(a, 5)` или `np.clip(a, None, 5)` → `[1 2 3 4 5 5 5 5 5 5]`.
:::
:::

:::task 2. Матрица `m` формы (4, 5). Найдите номер строки с наибольшей суммой.
:::answer
`m.sum(axis=1).argmax()` — `sum(axis=1)` даёт 4 суммы строк, `argmax` — номер наибольшей.
:::
:::

:::task 3. Нормируйте каждую строку матрицы `m` (float), чтобы сумма строки стала 1.
:::answer
`m / m.sum(axis=1, keepdims=True)` — `keepdims=True` оставляет форму `(n, 1)`, и broadcasting делит каждую строку на её сумму. Без `keepdims` форма `(n,)` поделила бы **столбцы** (или дала ошибку).
:::
:::

:::task 4. Что выведет код: `b = np.zeros(3); c = b; c[0] = 5; print(b)`?
:::answer
`[5. 0. 0.]` — `c = b` не копирует, это то же самое имя для того же массива. Копия: `c = b.copy()`.
:::
:::

:::task 5. Посчитайте, сколько раз встречается каждое число в `a = np.array([3, 1, 3, 2, 3, 1])`.
:::answer
`np.unique(a, return_counts=True)` → `(array([1, 2, 3]), array([2, 1, 3]))`. Для неотрицательных целых ещё быстрее `np.bincount(a)` → `[0 2 1 3]`.
:::
:::
