---
title: "Логические функции (Boolean functions) — подробно, с задачами"
kind: notes
tasks: [49243189]
order: 10
summary: Операции и таблицы истинности, законы алгебры логики с доказательствами, упрощение формул, СДНФ/СКНФ, логические элементы и схемы, подсчёт решений логических уравнений, проверка на Python.
---

Часть темы *CS Assessment: Boolean functions, Numeral Systems, NumPy, Images*. Остальные части — в отдельных конспектах.

## 1. Высказывания и операции

**Логическая переменная** принимает два значения: 1 (истина, *true*) и 0 (ложь, *false*). **Логическая функция** от $n$ переменных — правило, которое каждому из $2^n$ наборов значений ставит в соответствие 0 или 1. Её полностью описывает **таблица истинности** (*truth table*) из $2^n$ строк.

| A | B | ¬A | A ∧ B | A ∨ B | A ⊕ B | A → B | A ≡ B |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 | **0** | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 |

:::def Что означает каждая операция
- **NOT** (¬A, $\overline A$, отрицание) — меняет значение.
- **AND** (A ∧ B, A·B, конъюнкция) — 1, только если **обе** 1. Как умножение 0/1.
- **OR** (A ∨ B, A + B, дизъюнкция) — 1, если **хотя бы одна** 1.
- **XOR** (A ⊕ B, «исключающее или») — 1, если значения **разные**. Это сложение по модулю 2.
- **Импликация** (A → B, «если A, то B») — ложна **только** при A = 1, B = 0. «Обещание нарушено, только если условие выполнено, а результата нет».
- **Эквивалентность** (A ≡ B, A ↔ B) — 1, если значения **одинаковые**. Это ¬(A ⊕ B).
:::

**Порядок действий:** ¬ → ∧ → ∨ и ⊕ → → → ≡. Скобки меняют порядок, как в арифметике.

<svg class="fig" viewBox="0 0 700 170" width="700">
  <path class="l f3" d="M60 40 L90.0 40 A25.0 25.0 0 0 1 90.0 90 L60 90 Z"/>
  <line class="l" x1="30.0" y1="55.0" x2="60.0" y2="55.0"/>
  <line class="l" x1="30.0" y1="75.0" x2="60.0" y2="75.0"/>
  <line class="l" x1="115.0" y1="65.0" x2="137.0" y2="65.0"/>
  <text class="i" x="26.0" y="51.0">A</text>
  <text class="i" x="26.0" y="91.0">B</text>
  <text class="i" x="139.0" y="70.0">A·B</text>
  <text class="s" x="90.0" y="140.0" text-anchor="middle">AND (И)</text>
  <path class="l f3" d="M232 40 Q265.0 40 292 65.0 Q265.0 90 232 90 Q247.0 65.0 232 40 Z"/>
  <line class="l" x1="202.0" y1="55.0" x2="238.0" y2="55.0"/>
  <line class="l" x1="202.0" y1="75.0" x2="238.0" y2="75.0"/>
  <line class="l" x1="292.0" y1="65.0" x2="314.0" y2="65.0"/>
  <text class="i" x="198.0" y="51.0">A</text>
  <text class="i" x="198.0" y="91.0">B</text>
  <text class="i" x="316.0" y="70.0">A+B</text>
  <text class="s" x="262.0" y="140.0" text-anchor="middle">OR (ИЛИ)</text>
  <path class="l f3" d="M404 40 Q437.0 40 464 65.0 Q437.0 90 404 90 Q419.0 65.0 404 40 Z"/>
  <path class="l" d="M396 40 Q411.0 65.0 396 90"/>
  <line class="l" x1="374.0" y1="55.0" x2="410.0" y2="55.0"/>
  <line class="l" x1="374.0" y1="75.0" x2="410.0" y2="75.0"/>
  <line class="l" x1="464.0" y1="65.0" x2="486.0" y2="65.0"/>
  <text class="i" x="370.0" y="51.0">A</text>
  <text class="i" x="370.0" y="91.0">B</text>
  <text class="i" x="488.0" y="70.0">A⊕B</text>
  <text class="s" x="434.0" y="140.0" text-anchor="middle">XOR</text>
  <polygon class="l f3" points="576.0,45.0 622.0,65.0 576.0,85.0"/>
  <circle class="l fb" cx="627.0" cy="65.0" r="5.0"/>
  <line class="l" x1="546.0" y1="65.0" x2="576.0" y2="65.0"/>
  <line class="l" x1="632.0" y1="65.0" x2="652.0" y2="65.0"/>
  <text class="i" x="542.0" y="59.0">A</text>
  <text class="i" x="654.0" y="70.0">¬A</text>
  <text class="s" x="606.0" y="140.0" text-anchor="middle">NOT (НЕ)</text>
</svg>

## 2. Законы алгебры логики

:::formula Основные законы
| Закон | Для ∧ | Для ∨ |
|---|---|---|
| переместительный | $A \land B = B \land A$ | $A \lor B = B \lor A$ |
| сочетательный | $(A \land B) \land C = A \land (B \land C)$ | то же для ∨ |
| распределительный | $A \land (B \lor C) = A \land B \lor A \land C$ | $A \lor B \land C = (A \lor B) \land (A \lor C)$ ⚠ |
| де Моргана | $\overline{A \land B} = \overline A \lor \overline B$ | $\overline{A \lor B} = \overline A \land \overline B$ |
| поглощения | $A \land (A \lor B) = A$ | $A \lor A \land B = A$ |
| склеивания | $A \land B \lor A \land \overline B = A$ | $(A \lor B) \land (A \lor \overline B) = A$ |
| с константами | $A \land 1 = A$, $A \land 0 = 0$ | $A \lor 0 = A$, $A \lor 1 = 1$ |
| дополнения | $A \land \overline A = 0$ | $A \lor \overline A = 1$ |
| идемпотентности | $A \land A = A$ | $A \lor A = A$ |

Ещё: $\overline{\overline A} = A$, $A \to B = \overline A \lor B$, $A \equiv B = A B \lor \overline A\,\overline B$, $A \oplus B = A\overline B \lor \overline A B$.
:::

⚠ Второй распределительный закон ($A \lor BC = (A \lor B)(A \lor C)$) непривычен — в обычной арифметике $a + bc \ne (a + b)(a + c)$. Здесь он верен, потому что $A \lor A = A$.

:::proof Как доказывать законы — таблицей истинности
Закон де Моргана $\overline{A \lor B} = \overline A \land \overline B$:

| A | B | A ∨ B | ¬(A ∨ B) | ¬A | ¬B | ¬A ∧ ¬B |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | **1** | 1 | 1 | **1** |
| 0 | 1 | 1 | **0** | 1 | 0 | **0** |
| 1 | 0 | 1 | **0** | 0 | 1 | **0** |
| 1 | 1 | 1 | **0** | 0 | 0 | **0** |

Столбцы совпадают на всех 4 наборах ⇒ функции равны ∎
:::

## 3. Упрощение формул

:::key Порядок действий при упрощении
1. Избавиться от → и ≡: $A \to B = \overline A \lor B$.
2. Опустить отрицания на переменные законами де Моргана.
3. Раскрыть скобки (распределительный закон) и применить поглощение, склеивание, $A\overline A = 0$, $A \lor \overline A = 1$.
:::

:::example Пример 1. $\overline{A \to B} \lor A$
$\overline{A \to B} = \overline{\overline A \lor B} = A \land \overline B$. Тогда $A\overline B \lor A = A$ (поглощение).
:::

:::example Пример 2. $(A \lor B)(\overline A \lor B)$
Раскрываем: $A\overline A \lor AB \lor B\overline A \lor BB = 0 \lor AB \lor \overline AB \lor B = B(A \lor \overline A \lor 1) = B$.
Быстрее склеиванием: $(B \lor A)(B \lor \overline A) = B$.
:::

:::example Пример 3. $\overline{\overline A \land B} \land (A \lor \overline B)$
$\overline{\overline A \land B} = A \lor \overline B$. Получаем $(A \lor \overline B)(A \lor \overline B) = A \lor \overline B$, то есть $B \to A$.
:::

## 4. Формула по таблице истинности (СДНФ и СКНФ)

:::def СДНФ (*sum of products*)
Берём строки, где $F = 1$. Для каждой — конъюнкция всех переменных: без черты, если переменная в этой строке 1, с чертой, если 0. Соединяем конъюнкции через ∨.
:::

:::def СКНФ (*product of sums*)
Берём строки, где $F = 0$. Для каждой — дизъюнкция: переменная **с чертой**, если в строке 1, без черты, если 0. Соединяем через ∧.
:::

:::example Пример. «Голосование трёх» (*majority*): $F = 1$, если хотя бы две переменные из $A$, $B$, $C$ равны 1
Единицы в строках 011, 101, 110, 111:
$$F = \overline ABC \lor A\overline BC \lor AB\overline C \lor ABC.$$
Упрощаем склеиванием (строку $ABC$ можно использовать несколько раз, так как $X \lor X = X$):
$ABC \lor \overline ABC = BC$, $ABC \lor A\overline BC = AC$, $ABC \lor AB\overline C = AB$ ⇒ $F = AB \lor BC \lor AC$.
:::

## 5. Логические схемы

Каждой операции соответствует **логический элемент** (*logic gate*), а формуле — схема. Входы слева, выход справа; формула читается от входов к выходу.

<svg class="fig" viewBox="0 0 560 210" width="560">
  <path class="l f3" d="M120 30 L150.0 30 A25.0 25.0 0 0 1 150.0 80 L120 80 Z"/>
  <polygon class="l f3" points="140.0,130.0 186.0,150.0 140.0,170.0"/>
  <circle class="l fb" cx="191.0" cy="150.0" r="5.0"/>
  <path class="l f3" d="M330 75 Q363.0 75 390 100.0 Q363.0 125 330 125 Q345.0 100.0 330 75 Z"/>
  <line class="l" x1="40.0" y1="45.0" x2="120.0" y2="45.0"/>
  <line class="l" x1="40.0" y1="65.0" x2="120.0" y2="65.0"/>
  <line class="l" x1="40.0" y1="150.0" x2="140.0" y2="150.0"/>
  <text class="i" x="20.0" y="50.0">A</text>
  <text class="i" x="20.0" y="70.0">B</text>
  <text class="i" x="20.0" y="155.0">C</text>
  <path class="l" d="M175.0 55.0 L290 55.0 L290 90.0 L336 90.0"/>
  <path class="l" d="M196 150.0 L290 150.0 L290 110.0 L336 110.0"/>
  <line class="l" x1="390.0" y1="100.0" x2="420.0" y2="100.0"/>
  <text class="i" x="424.0" y="105.0">F</text>
  <text class="s tc3" x="200.0" y="22.0">A·B</text>
  <text class="s tc3" x="212.0" y="128.0">¬C</text>
  <text class="s" x="280.0" y="196.0" text-anchor="middle">F = (A AND B) OR (NOT C) = A·B + ¬C</text>
</svg>

**Полные наборы.** Любую функцию можно записать через {¬, ∧, ∨} (СДНФ это доказывает). Более того, достаточно **одного** элемента NAND ($\overline{A \land B}$): $\overline A = \text{NAND}(A, A)$, $A \land B = \overline{\text{NAND}(A, B)}$, $A \lor B = \text{NAND}(\overline A, \overline B)$. Поэтому процессоры собирают из одинаковых NAND-элементов.

:::example Полусумматор (*half adder*) — как компьютер складывает биты
Сложение двух битов: сумма $S = A \oplus B$, перенос $C = A \land B$. Проверка: $1 + 1 = 10_2$ — $S = 0$, $C = 1$ ✓. Из двух полусумматоров и OR собирается полный сумматор, а из цепочки полных — сложение чисел любой длины.
:::

## 6. Сколько решений у логического уравнения

:::key Метод
1. Если формула простая — посчитать, сколько наборов дают **0** (часто их меньше), и вычесть из $2^n$.
2. Если переменных много — перебрать на компьютере (см. код ниже).
:::

:::example Пример. Сколько наборов $(A, B, C, D)$ дают $(A \to B) \land (C \lor D) = 1$?
$A \to B$ истинна в 3 наборах из 4 (кроме $A = 1, B = 0$). $C \lor D$ — тоже в 3 из 4. Переменные независимы ⇒ $3 \cdot 3 = 9$.
:::

```python
from itertools import product

def F(a, b, c, d):
    return (not a or b) and (c or d)

print(sum(F(*v) for v in product([0, 1], repeat=4)))   # 9

# таблица истинности любой функции
for a, b, c in product([0, 1], repeat=3):
    maj = (a and b) or (b and c) or (a and c)
    print(a, b, c, int(maj))
```

:::tip Логика в Python и C++
В Python `and`, `or`, `not` работают с любыми значениями (0 — ложь). Для битов удобнее операции `&`, `|`, `^`, `~`: `a & b`, `a | b`, `a ^ b`. **Осторожно:** `~1 == -2` в Python (инвертируются все биты), для одного бита пишите `1 - a` или `a ^ 1`. В C++ то же: `&&`, `||`, `!` и побитовые `&`, `|`, `^`, `~`.
:::

## 7. Проверь себя

:::task 1. Упростите $\overline{A \lor \overline B} \lor \overline A$.
:::answer
$\overline{A \lor \overline B} = \overline A B$. Тогда $\overline AB \lor \overline A = \overline A$ (поглощение).
:::
:::

:::task 2. Докажите, что $A \to B$ и $\overline B \to \overline A$ равносильны.
:::answer
$\overline B \to \overline A = \overline{\overline B} \lor \overline A = B \lor \overline A = \overline A \lor B = A \to B$ ∎ (это **контрапозиция** — на ней основано доказательство «от противного»).
:::
:::

:::task 3. Сколько наборов $(x_1, \ldots, x_5)$ удовлетворяют $x_1 \land x_2 \to x_3 \lor x_4 \lor x_5$?
:::answer
Импликация ложна только при $x_1 = x_2 = 1$ и $x_3 = x_4 = x_5 = 0$ — это **один** набор. Ответ: $2^5 - 1 = 31$.
:::
:::

:::task 4. Постройте СДНФ функции, которая равна 1 ровно тогда, когда $A = B$, и упростите.
:::answer
Единицы в строках 00 и 11: $F = \overline A\,\overline B \lor AB$ — это $A \equiv B$.
:::
:::

:::task 5. Выразите $A \oplus B$ только через NAND.
:::answer
Пусть $N = \text{NAND}(A, B)$. Тогда $A \oplus B = \text{NAND}(\text{NAND}(A, N),\ \text{NAND}(B, N))$ — 4 элемента. Проверка таблицей: при $A = B = 1$: $N = 0$, оба внутренних NAND дают 1, итог 0 ✓; при $A = 1, B = 0$: $N = 1$, $\text{NAND}(1, 1) = 0$, $\text{NAND}(0, 1) = 1$, итог $\text{NAND}(0, 1) = 1$ ✓.
:::
:::
