---
title: Блоки — часть 2. Задачи 18–36 с подробными решениями
kind: solutions
units: [2043420]
tasks: []
order: 26
summary: Системы из 3–5 блоков и трёх грузов (задачи 4.1–6.7) и бруски на столе (5.2–5.4). Два приёма: исключение натяжений и «метод одного натяжения»; эквивалентная масса блока с двумя грузами.
---

Продолжение разборов листка **Pulleys**. Начало и метод — в конспектах «Блоки, нити, тележки и клинья — метод решения» и «Блоки — часть 1».

**Соглашения те же.** Оси $y$ вниз от потолка, $a > 0$ означает движение вниз. Буквы $A, B, C, D, E$ — блоки (синие на рисунках), $T_1, T_2, \dots$ — натяжения разных нитей (оранжевые). Рядом с рисунком подписано, какие куски принадлежат какой нити.

## Два приёма для больших систем

### Приём 1. Одна степень свободы: исключаем натяжения (задачи 18–24)

В задачах 18–24 три груза, но **движение одного определяет движение всех** (одна степень свободы). План:
1. По нитям выражаем ускорения всех тел через одно, $a = a_3$. Получаем $a_1 = k_1 a$, $a_2 = k_2 a$.
2. Из условий для невесомых блоков выражаем натяжения друг через друга.
3. Пишем второй закон для трёх грузов, складываем их с подходящими множителями так, чтобы лишние натяжения сократились, и находим $a$.
4. Проверка энергией: $a = g\dfrac{\sum m_i k_i}{\sum m_i k_i^2}$.

### Приём 2. Две степени свободы: «метод одного натяжения» (задачи 25, 29–36)

Когда грузы могут двигаться независимо (две степени свободы), удобнее так:
1. Из условий для невесомых блоков **все натяжения выражаем через одно**, например $\tau$. Это работает, потому что каждый невесомый блок связывает натяжения своих нитей числом: $T_1 = 2T_2$ и т.п.
2. Для каждого груза из второго закона: $a_i = g - \dfrac{(\text{итоговая сила нитей вверх})}{m_i}$. Например, $a_1 = g - \dfrac{\tau}{m_1}$.
3. Подставляем все $a_i$ в уравнение связи. Получается **одно уравнение с одним неизвестным $\tau$**.
4. Находим $\tau$, затем нужное ускорение.

:::def Эквивалентная масса блока с двумя грузами
Подвижный невесомый блок, через который перекинута нить с грузами $m_a$ и $m_b$, для нити, держащей его ось, ведёт себя как **один груз массой**
$$\mu = \frac{4m_a m_b}{m_a + m_b}.$$
**Вывод.** Пусть ось блока движется с ускорением $a_0$ вниз, натяжение нити через блок $T$. Тогда $a_a = g - T/m_a$, $a_b = g - T/m_b$, а связь даёт $a_a + a_b = 2a_0$. Отсюда $T = \dfrac{2m_a m_b}{m_a + m_b}(g - a_0)$, и ось держит силу $2T = \mu(g - a_0)$. Ровно так держала бы груз массой $\mu$, движущийся с ускорением $a_0$.

Заметим, что $\mu \le m_a + m_b$, равенство только при $m_a = m_b$. Пара неравных грузов «весит» для оси меньше суммы своих масс: они ускоряются, а не висят.
:::

---

## Задача 18 (4.1)

<svg class="fig scanfig" viewBox="0 0 222 598" style="width:278px" role="img" aria-label="Задача 18"><image class="scan" href="/fig/pul/18.png" width="222" height="598"/><text class="lb lt" x="33" y="200" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="124" y="150" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="100" y="300" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="207" y="200" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="33" y="410" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="166" y="420" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="140" y="515" text-anchor="middle">2T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="62" y="118" text-anchor="middle">A</text><text class="lb lp" x="140" y="342" text-anchor="middle">B</text><text class="lb lp" x="76" y="460" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_3 = \dfrac{4m_1 - 4m_2 + m_3}{16m_1 + 16m_2 + m_3}\,g$.

**Нити:** $T_1$ — от $m_1$ через $A$ к $m_2$; $T_2$ — от низа $m_1$ под $C$ к оси $B$; $T_3$ — от низа $m_2$ под $B$ к потолку. Груз $m_3$ висит на $C$.

:::hint Подсказка
Свяжите ускорения: $a_2 = -a_1$ (нить через $A$), $a_B = \tfrac12 a_2$ (нить $T_3$), $2a_3 = a_1 + a_B$ (нить $T_2$). Должно получиться $a_1 = 4a_3$, $a_2 = -4a_3$. Блок $B$ даёт $T_2 = 2T_3$.
:::

:::solution Решение
**1. Связи.**
- Нить $T_1$: $y_1 + y_2 = \text{const}$, поэтому $a_2 = -a_1$.
- Нить $T_3$: $(y_B - y_2) + y_B = \text{const}$, поэтому $a_B = \tfrac12 a_2 = -\tfrac12 a_1$.
- Нить $T_2$: $(y_C - y_1) + (y_C - y_B) = \text{const}$, поэтому $2a_C = a_1 + a_B = \tfrac12 a_1$.

Итак, $a_1 = 4a$, $a_2 = -4a$, $a_B = -2a$, где $a = a_C = a_3$.

**2. Невесомые блоки.** Блок $B$: вверх $2T_3$, вниз $T_2$, поэтому $T_2 = 2T_3$. Блок $C$ с грузом $m_3$ тянут вверх $2T_2 = 4T_3$.

**3. Второй закон.**
$$m_1(4a) = m_1 g - T_1 + T_2 = m_1 g - T_1 + 2T_3, \qquad (1)$$
$$m_2(-4a) = m_2 g - T_1 + T_3, \qquad (2)$$
$$m_3 a = m_3 g - 4T_3. \qquad (3)$$

**4. Решаем.** (1) − (2) убирает $T_1$:
$$4a(m_1 + m_2) = (m_1 - m_2)g + T_3 \;\Rightarrow\; T_3 = 4a(m_1 + m_2) - (m_1 - m_2)g.$$
Подставим в (3):
$$m_3 a = m_3 g - 16a(m_1 + m_2) + 4(m_1 - m_2)g \;\Rightarrow\; a = \frac{4m_1 - 4m_2 + m_3}{16m_1 + 16m_2 + m_3}\,g.$$
Натяжение $T_3 = \dfrac{m_3(3m_1 + 5m_2)}{16m_1 + 16m_2 + m_3}g > 0$. Нити натянуты при любых массах.

**Проверка энергией.** $k = (4, -4, 1)$: $a = g\dfrac{4m_1 - 4m_2 + m_3}{16m_1 + 16m_2 + m_3}$. Совпало.
:::

## Задача 19 (4.2)

<svg class="fig scanfig" viewBox="0 0 221 598" style="width:276px" role="img" aria-label="Задача 19"><image class="scan" href="/fig/pul/19.png" width="221" height="598"/><text class="lb lt" x="31" y="200" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="100" y="165" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="206" y="120" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="166" y="262" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="31" y="410" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="166" y="410" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="140" y="515" text-anchor="middle">2T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="62" y="118" text-anchor="middle">A</text><text class="lb lp" x="136" y="206" text-anchor="middle">B</text><text class="lb lp" x="74" y="460" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_3 = \dfrac{4m_1 - 2m_2 + m_3}{16m_1 + 4m_2 + m_3}\,g$.

**Нити:** $T_1$ — от $m_1$ через $A$, под $B$, к потолку; $T_2$ — от низа $m_1$ под $C$ к низу $m_2$; $T_3$ — от верха $m_2$ к оси $B$ (груз $m_2$ висит на блоке $B$).

:::hint Подсказка
$m_2$ и блок $B$ движутся вместе. Блок $B$: $T_3 = 2T_1$. Связи дают $a_1 = 4a_3$, $a_2 = -2a_3$.
:::

:::solution Решение
**1. Связи.**
- $T_3$: $a_2 = a_B$.
- $T_1$: $y_1 + 2y_B = \text{const}$, поэтому $a_1 = -2a_B = -2a_2$.
- $T_2$: $2y_C - y_1 - y_2 = \text{const}$, поэтому $2a_3 = a_1 + a_2 = -a_2$.

Итого $a_2 = -2a$, $a_1 = 4a$, где $a = a_3$.

**2. Блок $B$:** вверх $2T_1$, вниз $T_3$, поэтому $T_3 = 2T_1$.

**3. Второй закон.**
$$m_1(4a) = m_1 g - T_1 + T_2, \qquad (1)$$
$$m_2(-2a) = m_2 g - T_3 + T_2 = m_2 g - 2T_1 + T_2, \qquad (2)$$
$$m_3 a = m_3 g - 2T_2. \qquad (3)$$

**4. Решаем.** 2·(1) − (2) убирает $T_1$:
$$8m_1 a + 2m_2 a = (2m_1 - m_2)g + T_2 \;\Rightarrow\; T_2 = (8m_1 + 2m_2)a - (2m_1 - m_2)g.$$
Подставим в (3):
$$m_3 a = m_3 g - (16m_1 + 4m_2)a + (4m_1 - 2m_2)g \;\Rightarrow\; a = \frac{4m_1 - 2m_2 + m_3}{16m_1 + 4m_2 + m_3}\,g.$$

**Проверка энергией.** $k = (4, -2, 1)$, знаменатель $16m_1 + 4m_2 + m_3$. Совпало.
:::

## Задача 20 (4.3)

<svg class="fig scanfig" viewBox="0 0 221 598" style="width:276px" role="img" aria-label="Задача 20"><image class="scan" href="/fig/pul/20.png" width="221" height="598"/><text class="lb lt" x="31" y="280" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="124" y="100" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="98" y="240" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="206" y="170" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="166" y="420" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="140" y="515" text-anchor="middle">2T<tspan class="sb" dy="4">1</tspan></text><text class="lb lp" x="62" y="68" text-anchor="middle">A</text><text class="lb lp" x="136" y="274" text-anchor="middle">B</text><text class="lb lp" x="76" y="460" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_3 = \dfrac{m_3 - 4m_1 - 2m_2}{16m_1 + 4m_2 + m_3}\,g$.

**Нити:** $T_1$ — от верха $m_1$ через $A$, под $C$, к низу $m_2$; $T_2$ — от низа $m_1$ под $B$ к потолку; $T_3$ — от верха $m_2$ к оси $B$ (на рисунке не подписана, это короткая связка $B$–$m_2$).

:::hint Подсказка
$m_2$ висит на оси $B$ и движется вместе с ним. Блок $B$ огибает нить $T_2$, поэтому $T_3 = 2T_2$. Связи: $a_1 = -4a_3$, $a_2 = -2a_3$.
:::

:::solution Решение
**1. Связи.**
- $T_3$: $a_2 = a_B$.
- $T_2$: $(y_B - y_1) + y_B = \text{const}$, поэтому $a_B = \tfrac12 a_1$, то есть $a_2 = \tfrac12 a_1$.
- $T_1$: $y_1 + y_C + (y_C - y_2) = \text{const}$, поэтому $a_1 + 2a_3 - a_2 = 0$, то есть $\tfrac12 a_1 + 2a_3 = 0$.

Итого $a_1 = -4a$, $a_2 = -2a$, где $a = a_3$.

**2. Блок $B$:** вверх $2T_2$, вниз $T_3$, поэтому $T_3 = 2T_2$.

**3. Второй закон.**
$$m_1(-4a) = m_1 g - T_1 + T_2, \qquad (1)$$
$$m_2(-2a) = m_2 g - T_3 + T_1 = m_2 g - 2T_2 + T_1, \qquad (2)$$
$$m_3 a = m_3 g - 2T_1. \qquad (3)$$

**4. Решаем.** 2·(1) + (2) убирает $T_2$:
$$-8m_1 a - 2m_2 a = (2m_1 + m_2)g - T_1 \;\Rightarrow\; T_1 = (2m_1 + m_2)g + (8m_1 + 2m_2)a.$$
Подставим в (3):
$$m_3 a = m_3 g - (4m_1 + 2m_2)g - (16m_1 + 4m_2)a \;\Rightarrow\; a = \frac{m_3 - 4m_1 - 2m_2}{16m_1 + 4m_2 + m_3}\,g.$$

**Проверка энергией.** $k = (-4, -2, 1)$: числитель $m_3 - 4m_1 - 2m_2$, знаменатель $16m_1 + 4m_2 + m_3$. Совпало. Здесь $m_1$ и $m_2$ оба поднимаются, когда $m_3$ опускается.
:::

## Задача 21 (4.4)

<svg class="fig scanfig" viewBox="0 0 222 599" style="width:278px" role="img" aria-label="Задача 21"><image class="scan" href="/fig/pul/21.png" width="222" height="599"/><text class="lb lt" x="44" y="152" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="110" y="168" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="206" y="100" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="70" y="292" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="12" y="460" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="79" y="392" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="171" y="392" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="171" y="235" text-anchor="middle">T<tspan class="sb" dy="4">4</tspan></text><text class="lb lt" x="150" y="475" text-anchor="middle">2T<tspan class="sb" dy="4">3</tspan></text><text class="lb lp" x="76" y="118" text-anchor="middle">A</text><text class="lb lp" x="144" y="190" text-anchor="middle">B</text><text class="lb lp" x="42" y="341" text-anchor="middle">D</text><text class="lb lp" x="110" y="426" text-anchor="middle">E</text></svg>

**Ответ учителя:** $a_3 = 3\,\dfrac{4m_1 - 2m_2 + 3m_3}{16m_1 + 4m_2 + 9m_3}\,g$.

**Нити:** $T_1$ — от $m_1$ через $A$, под $B$, к потолку; $T_2$ — связка «низ $m_1$ — ось $D$»; $T_3$ — от пола вверх через $D$, под $E$, к низу $m_2$; $T_4$ — связка «верх $m_2$ — ось $B$». Груз $m_3$ висит на $E$.

:::hint Подсказка
$m_1$ движется вместе с $D$, $m_2$ — вместе с $B$. Тогда $a_1 = -2a_2$ и $2a_3 = 2a_1 + a_2$. Должно получиться $a_1 = \tfrac43 a_3$, $a_2 = -\tfrac23 a_3$. Отсюда тройки и девятки в ответе.
:::

:::solution Решение
**1. Связи.**
- $T_2$, $T_4$ (жёсткие связки): $a_D = a_1$, $a_B = a_2$.
- $T_1$: $y_1 + 2y_B = \text{const}$, поэтому $a_1 = -2a_2$.
- $T_3$: $(y_{\text{пол}} - y_D) + (y_E - y_D) + (y_E - y_2) = \text{const}$, поэтому $2a_E = 2a_D + a_2 = 2a_1 - \tfrac12 a_1 = \tfrac32 a_1$.

Итого $a_1 = \tfrac43 a$, $a_2 = -\tfrac23 a$, где $a = a_E = a_3$.

**2. Невесомые блоки.**
- $D$: обе ветви нити $T_3$ уходят от него **вниз** (к полу и к $E$), значит тянут вниз с силой $2T_3$. Держит его связка $T_2$, поэтому $T_2 = 2T_3$.
- $B$: вверх $2T_1$, вниз $T_4$, поэтому $T_4 = 2T_1$.

**3. Второй закон.**
$$m_1 \cdot \tfrac43 a = m_1 g - T_1 + T_2 = m_1 g - T_1 + 2T_3, \qquad (1)$$
$$m_2 \cdot \left(-\tfrac23 a\right) = m_2 g - T_4 + T_3 = m_2 g - 2T_1 + T_3, \qquad (2)$$
$$m_3 a = m_3 g - 2T_3. \qquad (3)$$

**4. Решаем.** 2·(1) − (2) убирает $T_1$:
$$\tfrac83 m_1 a + \tfrac23 m_2 a = (2m_1 - m_2)g + 3T_3.$$
Из (3): $T_3 = \tfrac12 m_3(g - a)$. Подставим и умножим на 6:
$$(16m_1 + 4m_2)a = (12m_1 - 6m_2)g + 9m_3(g - a)$$
$$\Rightarrow\; a = \frac{3(4m_1 - 2m_2 + 3m_3)}{16m_1 + 4m_2 + 9m_3}\,g.$$

**Проверка энергией.** $k = \left(\tfrac43, -\tfrac23, 1\right)$: числитель $\tfrac43 m_1 - \tfrac23 m_2 + m_3$, знаменатель $\tfrac{16}{9}m_1 + \tfrac49 m_2 + m_3$. Умножим оба на 9 и получим ответ.
:::

## Задача 22 (4.5)

<svg class="fig scanfig" viewBox="0 0 222 599" style="width:278px" role="img" aria-label="Задача 22"><image class="scan" href="/fig/pul/22.png" width="222" height="599"/><text class="lb lt" x="44" y="152" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="142" y="160" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="71" y="292" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="12" y="460" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="79" y="392" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="173" y="382" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="112" y="292" text-anchor="middle">T<tspan class="sb" dy="4">4</tspan></text><text class="lb lt" x="207" y="200" text-anchor="middle">T<tspan class="sb" dy="4">4</tspan></text><text class="lb lt" x="151" y="475" text-anchor="middle">2T<tspan class="sb" dy="4">3</tspan></text><text class="lb lp" x="77" y="118" text-anchor="middle">A</text><text class="lb lp" x="145" y="323" text-anchor="middle">B</text><text class="lb lp" x="43" y="341" text-anchor="middle">D</text><text class="lb lp" x="111" y="426" text-anchor="middle">E</text></svg>

**Ответ учителя:** $a_3 = 3\,\dfrac{4m_1 - 4m_2 + 3m_3}{16m_1 + 16m_2 + 9m_3}\,g$.

**Нити:** $T_1$ — от $m_1$ через $A$ к $m_2$; $T_2$ — связка «низ $m_1$ — ось $D$»; $T_3$ — от пола через $D$, под $E$, к оси $B$; $T_4$ — от низа $m_2$ под $B$ к потолку.

:::hint Подсказка
$a_2 = -a_1$ (нить через $A$), $a_B = \tfrac12 a_2$, $2a_3 = 2a_1 + a_B$. Невесомые блоки: $T_2 = 2T_3$ (блок $D$), $T_3 = 2T_4$ (блок $B$).
:::

:::solution Решение
**1. Связи.**
- $T_1$: $a_2 = -a_1$.
- $T_2$: $a_D = a_1$.
- $T_4$: $(y_B - y_2) + y_B = \text{const}$, поэтому $a_B = \tfrac12 a_2 = -\tfrac12 a_1$.
- $T_3$: $-2y_D + 2y_E - y_B = \text{const}$, поэтому $2a_E = 2a_1 + a_B = \tfrac32 a_1$.

Итого $a_1 = \tfrac43 a$, $a_2 = -\tfrac43 a$, где $a = a_3$.

**2. Блоки.** $D$: $T_2 = 2T_3$. $B$: вверх $2T_4$, вниз $T_3$, поэтому $T_4 = \tfrac12 T_3$.

**3. Второй закон.**
$$m_1 \cdot \tfrac43 a = m_1 g - T_1 + 2T_3, \qquad (1)$$
$$m_2 \cdot \left(-\tfrac43 a\right) = m_2 g - T_1 + \tfrac12 T_3, \qquad (2)$$
$$m_3 a = m_3 g - 2T_3. \qquad (3)$$

**4. Решаем.** (1) − (2):
$$\tfrac43(m_1 + m_2)a = (m_1 - m_2)g + \tfrac32 T_3, \qquad T_3 = \tfrac12 m_3(g - a).$$
Умножим на 12: $16(m_1 + m_2)a = 12(m_1 - m_2)g + 9m_3(g - a)$, откуда
$$a = \frac{3(4m_1 - 4m_2 + 3m_3)}{16m_1 + 16m_2 + 9m_3}\,g.$$

**Проверка энергией.** $k = \left(\tfrac43, -\tfrac43, 1\right)$. Совпало.
:::

## Задача 23 (4.6)

<svg class="fig scanfig" viewBox="0 0 221 599" style="width:276px" role="img" aria-label="Задача 23"><image class="scan" href="/fig/pul/23.png" width="221" height="599"/><text class="lb lt" x="44" y="165" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="112" y="165" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="206" y="100" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="12" y="400" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="79" y="267" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="79" y="392" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="172" y="392" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="172" y="240" text-anchor="middle">T<tspan class="sb" dy="4">4</tspan></text><text class="lb lt" x="151" y="475" text-anchor="middle">2T<tspan class="sb" dy="4">3</tspan></text><text class="lb lp" x="77" y="118" text-anchor="middle">A</text><text class="lb lp" x="145" y="188" text-anchor="middle">B</text><text class="lb lp" x="43" y="223" text-anchor="middle">D</text><text class="lb lp" x="111" y="426" text-anchor="middle">E</text></svg>

**Ответ учителя:** $a_3 = 3\,\dfrac{8m_1 - 2m_2 + 3m_3}{64m_1 + 4m_2 + 9m_3}\,g$.

**Нити:** $T_1$ — от оси $D$ через $A$, под $B$, к потолку; $T_2$ — от пола вверх через $D$ к верху $m_1$; $T_3$ — от низа $m_1$ под $E$ к низу $m_2$; $T_4$ — связка «верх $m_2$ — ось $B$».

:::hint Подсказка
Блок $D$ «перевёрнутый», как в задаче 8: обе ветви $T_2$ идут от него вниз (к полу и к $m_1$), поэтому $T_1 = 2T_2$ и $a_1 = 2a_D$. А $a_D = -2a_B$. Значит, $m_1$ движется в 4 раза быстрее $B$.
:::

:::solution Решение
**1. Связи.**
- $T_1$: $y_D + 2y_B = \text{const}$, поэтому $a_D = -2a_B$.
- $T_2$: $(y_{\text{пол}} - y_D) + (y_1 - y_D) = \text{const}$, поэтому $a_1 = 2a_D = -4a_B$.
- $T_4$: $a_2 = a_B$, поэтому $a_2 = -\tfrac14 a_1$.
- $T_3$: $2a_E = a_1 + a_2 = \tfrac34 a_1$.

Итого $a_1 = \tfrac83 a$, $a_2 = -\tfrac23 a$, где $a = a_3$.

**2. Блоки.** $D$: вверх $T_1$, вниз $2T_2$, поэтому $T_1 = 2T_2$. $B$: вверх $2T_1$, вниз $T_4$, поэтому $T_4 = 2T_1 = 4T_2$.

**3. Второй закон.**
$$m_1 \cdot \tfrac83 a = m_1 g - T_2 + T_3, \qquad (1)$$
$$m_2 \cdot \left(-\tfrac23 a\right) = m_2 g - 4T_2 + T_3, \qquad (2)$$
$$m_3 a = m_3 g - 2T_3. \qquad (3)$$

**4. Решаем.** 4·(1) − (2) убирает $T_2$:
$$\tfrac{32}{3}m_1 a + \tfrac23 m_2 a = (4m_1 - m_2)g + 3T_3, \qquad T_3 = \tfrac12 m_3(g - a).$$
Умножим на 6: $(64m_1 + 4m_2)a = (24m_1 - 6m_2)g + 9m_3(g - a)$, откуда
$$a = \frac{3(8m_1 - 2m_2 + 3m_3)}{64m_1 + 4m_2 + 9m_3}\,g.$$

**Проверка энергией.** $k = \left(\tfrac83, -\tfrac23, 1\right)$: в знаменателе $\tfrac{64}{9}m_1$. Груз $m_1$ движется быстрее всех, поэтому его инертность умножена на $(8/3)^2$.
:::

## Задача 24 (4.7)

<svg class="fig scanfig" viewBox="0 0 255 599" style="width:319px" role="img" aria-label="Задача 24"><image class="scan" href="/fig/pul/24.png" width="255" height="599"/><text class="lb lt" x="44" y="170" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="166" y="150" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="12" y="400" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="79" y="267" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="79" y="397" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="199" y="392" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="140" y="287" text-anchor="middle">T<tspan class="sb" dy="4">4</tspan></text><text class="lb lt" x="233" y="200" text-anchor="middle">T<tspan class="sb" dy="4">4</tspan></text><text class="lb lt" x="165" y="482" text-anchor="middle">2T<tspan class="sb" dy="4">3</tspan></text><text class="lb lp" x="86" y="118" text-anchor="middle">A</text><text class="lb lp" x="172" y="323" text-anchor="middle">B</text><text class="lb lp" x="43" y="223" text-anchor="middle">D</text><text class="lb lp" x="120" y="426" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_3 = 3\,\dfrac{8m_1 - 4m_2 + 3m_3}{64m_1 + 16m_2 + 9m_3}\,g$.

**Нити:** $T_1$ — от оси $D$ через $A$ к верху $m_2$; $T_2$ — от пола через $D$ к верху $m_1$; $T_3$ — от низа $m_1$ под $C$ к оси $B$; $T_4$ — от низа $m_2$ под $B$ к потолку.

:::hint Подсказка
$a_D = -a_2$, $a_1 = 2a_D$, $a_B = \tfrac12 a_2$, $2a_3 = a_1 + a_B$. Блоки: $T_1 = 2T_2$, $T_3 = 2T_4$.
:::

:::solution Решение
**1. Связи.**
- $T_1$: $y_D + y_2 = \text{const}$, поэтому $a_D = -a_2$.
- $T_2$: $a_1 = 2a_D = -2a_2$.
- $T_4$: $a_B = \tfrac12 a_2$.
- $T_3$: $2a_C = a_1 + a_B = -2a_2 + \tfrac12 a_2 = -\tfrac32 a_2$.

Итого $a_2 = -\tfrac43 a$, $a_1 = \tfrac83 a$, где $a = a_3$.

**2. Блоки.** $D$: $T_1 = 2T_2$. $B$: вверх $2T_4$, вниз $T_3$, поэтому $T_4 = \tfrac12 T_3$.

**3. Второй закон.**
$$m_1 \cdot \tfrac83 a = m_1 g - T_2 + T_3, \qquad (1)$$
$$m_2 \cdot \left(-\tfrac43 a\right) = m_2 g - T_1 + T_4 = m_2 g - 2T_2 + \tfrac12 T_3, \qquad (2)$$
$$m_3 a = m_3 g - 2T_3. \qquad (3)$$

**4. Решаем.** 2·(1) − (2):
$$\tfrac{16}{3}m_1 a + \tfrac43 m_2 a = (2m_1 - m_2)g + \tfrac32 T_3, \qquad T_3 = \tfrac12 m_3(g - a).$$
Умножим на 12: $(64m_1 + 16m_2)a = (24m_1 - 12m_2)g + 9m_3(g - a)$, откуда
$$a = \frac{3(8m_1 - 4m_2 + 3m_3)}{64m_1 + 16m_2 + 9m_3}\,g.$$

**Проверка энергией.** $k = \left(\tfrac83, -\tfrac43, 1\right)$. Совпало.
:::

---

## Задача 25 (5.1). Блок на блоке — две степени свободы

<svg class="fig scanfig" viewBox="0 0 257 394" style="width:321px" role="img" aria-label="Задача 25"><image class="scan" href="/fig/pul/25.png" width="257" height="394"/><text class="lb lt" x="28" y="230" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="192" y="170" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="124" y="300" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="232" y="300" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="88" y="120" text-anchor="middle">A</text><text class="lb lp" x="160" y="240" text-anchor="middle">B</text></svg>

**Ответ учителя:** $a_1 = \dfrac{m_1(m_2 + m_3) - 4m_2 m_3}{m_1(m_2 + m_3) + 4m_2 m_3}\,g$.

:::hint Подсказка
Здесь грузы $m_2$ и $m_3$ могут двигаться независимо от $m_1$. Это две степени свободы, энергетическая проверка «в одну строку» не работает. Используйте эквивалентную массу: блок $B$ с грузами $m_2, m_3$ ведёт себя как один груз $\mu = \dfrac{4m_2 m_3}{m_2 + m_3}$. Получится машина Атвуда $m_1$ против $\mu$.
:::

:::solution Решение (метод одного натяжения)
**Нити:** $T_1$ — от $m_1$ через $A$ к оси $B$; $T_2$ — через $B$ от $m_2$ к $m_3$.

**1. Связи.** $T_1$: $a_B = -a_1$. $T_2$: $a_2 + a_3 = 2a_B = -2a_1$.

**2. Блок $B$:** $T_1 = 2T_2$. Обозначим $\tau = T_2$.

**3. Ускорения через $\tau$:**
$$a_1 = g - \frac{2\tau}{m_1}, \qquad a_2 = g - \frac{\tau}{m_2}, \qquad a_3 = g - \frac{\tau}{m_3}.$$

**4. Подставим в связь** $a_2 + a_3 = -2a_1$:
$$2g - \tau\left(\frac1{m_2} + \frac1{m_3}\right) = -2g + \frac{4\tau}{m_1} \;\Rightarrow\; \tau\left(\frac4{m_1} + \frac1{m_2} + \frac1{m_3}\right) = 4g,$$
$$\tau = \frac{4m_1 m_2 m_3}{m_1 m_2 + m_1 m_3 + 4m_2 m_3}\,g.$$

**5. Ответ.**
$$a_1 = g - \frac{2\tau}{m_1} = \frac{m_1(m_2 + m_3) - 4m_2 m_3}{m_1(m_2 + m_3) + 4m_2 m_3}\,g.$$
Заодно: $a_2 = g - \dfrac{\tau}{m_2} = \dfrac{m_1 m_2 - 3m_1 m_3 + 4m_2 m_3}{m_1(m_2 + m_3) + 4m_2 m_3}\,g$, а $a_3$ получается из $a_2$ заменой $m_2 \leftrightarrow m_3$.
:::

:::tip Проверка через эквивалентную массу
$\mu = \dfrac{4m_2 m_3}{m_2 + m_3}$, и по формуле машины Атвуда $a_1 = \dfrac{m_1 - \mu}{m_1 + \mu}g$. Умножим числитель и знаменатель на $(m_2 + m_3)$ и получим ответ учителя. Частный случай $m_2 = m_3 = m$ даёт $\mu = 2m$, то есть блок с двумя одинаковыми грузами — это просто груз $2m$.
:::

## Задача 26 (5.2). Брусок и блок с двумя грузами

<svg class="fig scanfig" viewBox="0 0 291 325" style="width:364px" role="img" aria-label="Задача 26"><image class="scan" href="/fig/pul/26.png" width="291" height="325"/><text class="lb lt" x="146" y="31" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="225" y="110" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="158" y="225" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="266" y="225" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="196" y="172" text-anchor="middle">B</text></svg>

**Ответ учителя:** $a_M = \dfrac{4m_1 m_2}{M(m_1 + m_2) + 4m_1 m_2}\,g$.

:::hint Подсказка
Замените блок $B$ с грузами на эквивалентный груз $\mu = \dfrac{4m_1 m_2}{m_1 + m_2}$. Получится задача 2: брусок на столе и висящий груз.
:::

:::solution Решение
**Нити:** $T_1$ — от бруска через угловой блок к оси $B$; $T_2$ — через $B$ от $m_1$ к $m_2$.

**Связи.** $T_1$: брусок сдвигается к краю на столько же, на сколько опускается $B$: $a_M = a_B$. $T_2$: $a_1 + a_2 = 2a_B$.

**Силы.** Блок $B$: $T_1 = 2T_2 = 2\tau$. Брусок: $M a_M = 2\tau$. Грузы: $a_1 = g - \tau/m_1$, $a_2 = g - \tau/m_2$.

**Решаем.** Связь: $2g - \tau\left(\dfrac1{m_1} + \dfrac1{m_2}\right) = 2a_M = \dfrac{4\tau}{M}$, откуда
$$\tau = \frac{2g}{\dfrac4M + \dfrac1{m_1} + \dfrac1{m_2}} = \frac{2Mm_1 m_2\,g}{M(m_1 + m_2) + 4m_1 m_2},$$
$$a_M = \frac{2\tau}{M} = \frac{4m_1 m_2}{M(m_1 + m_2) + 4m_1 m_2}\,g.$$

**Проверка.** Эквивалентная масса $\mu = \dfrac{4m_1 m_2}{m_1 + m_2}$ и задача 2 дают $a_M = \dfrac{\mu}{M + \mu}g$. Это тот же ответ.
:::

## Задача 27 (5.3). Два бруска, обнятых одной нитью

<svg class="fig scanfig" viewBox="0 0 283 263" style="width:354px" role="img" aria-label="Задача 27"><image class="scan" href="/fig/pul/27.png" width="283" height="263"/><text class="lb lt" x="138" y="31" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="150" y="110" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="205" y="50" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="262" y="150" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="150" y="72" text-anchor="middle">P</text></svg>

**Ответ учителя:** $a_m = \dfrac{m(M_1 + M_2)}{m(M_1 + M_2) + 4M_1 M_2}\,g$.

:::hint Подсказка
$M_2$ лежит на $M_1$ **без трения**, поэтому бруски скользят независимо. Нить $T_1$ идёт от $M_2$ вокруг подвижного блока $P$ к $M_1$. Значит, каждый брусок тянет сила $T_1$, а блок $P$ — сила $2T_1$. Связь: $2a_P = a_1 + a_2$.
:::

:::solution Решение
**Обозначения.** $a_1, a_2$ — ускорения брусков вправо, $a_P$ — ускорение блока $P$ вправо, $a$ — ускорение груза $m$ вниз.

**Связи.**
- $T_1$: $(x_P - x_2) + (x_P - x_1) = \text{const}$, поэтому $2a_P = a_1 + a_2$.
- $T_2$: $(x_{\text{угл}} - x_P) + y = \text{const}$, поэтому $a = a_P$.

**Силы.**
- Бруски по горизонтали: $M_1 a_1 = T_1$, $M_2 a_2 = T_1$. Трения нет, сила между брусками вертикальна.
- Блок $P$: $T_2 = 2T_1$.
- Груз: $ma = mg - 2T_1$.

**Решаем.** $2a = a_1 + a_2 = T_1\left(\dfrac1{M_1} + \dfrac1{M_2}\right)$, откуда $T_1 = \dfrac{2M_1 M_2}{M_1 + M_2}a$. Тогда
$$ma = mg - \frac{4M_1 M_2}{M_1 + M_2}a \;\Rightarrow\; a = \frac{m(M_1 + M_2)}{m(M_1 + M_2) + 4M_1 M_2}\,g.$$
Ускорения брусков: $a_1 = \dfrac{2M_2 m}{m(M_1 + M_2) + 4M_1 M_2}g$, $a_2 = \dfrac{2M_1 m}{\dots}g$. Лёгкий брусок едет быстрее.

**Смысл.** Два бруска на подвижном блоке ведут себя как один брусок с массой $\mu = \dfrac{4M_1 M_2}{M_1 + M_2}$. Это та же эквивалентная масса, что и для грузов, только без силы тяжести.
:::

## Задача 28 (5.4). То же плюс подвижный блок у груза

<svg class="fig scanfig" viewBox="0 0 316 393" style="width:395px" role="img" aria-label="Задача 28"><image class="scan" href="/fig/pul/28.png" width="316" height="393"/><text class="lb lt" x="132" y="161" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="142" y="238" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="195" y="188" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="226" y="262" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="292" y="150" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="236" y="297" text-anchor="middle">2T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="148" y="203" text-anchor="middle">P</text><text class="lb lp" x="300" y="290" text-anchor="middle">Q</text></svg>

**Ответ учителя:** $a_m = \dfrac{m(M_1 + M_2)}{m(M_1 + M_2) + 16M_1 M_2}\,g$.

:::hint Подсказка
Всё как в задаче 27, но нить $T_2$ теперь огибает подвижный блок $Q$, на котором висит груз. Значит, груз держат силой $2T_2 = 4T_1$, и он движется вдвое медленнее блока $P$.
:::

:::solution Решение
**Связи.** $2a_P = a_1 + a_2$. Нить $T_2$: $(x_{\text{угл}} - x_P) + 2y_Q = \text{const}$, поэтому $a_P = 2a$, где $a = a_Q$ — ускорение груза.

**Силы.** $M_1 a_1 = M_2 a_2 = T_1$; блок $P$: $T_2 = 2T_1$; груз с блоком $Q$: $ma = mg - 2T_2 = mg - 4T_1$.

**Решаем.** $a_1 + a_2 = 2a_P = 4a$, откуда $T_1 = \dfrac{4M_1 M_2}{M_1 + M_2}a$. Тогда
$$ma = mg - \frac{16M_1 M_2}{M_1 + M_2}a \;\Rightarrow\; a = \frac{m(M_1 + M_2)}{m(M_1 + M_2) + 16M_1 M_2}\,g.$$

**Проверка.** По сравнению с задачей 27 груз движется вдвое медленнее блока $P$. «Инертность» брусков для него выросла в $2^2 = 4$ раза: было $4M_1M_2$, стало $16M_1M_2$.
:::

## Задача 29 (5.5)

<svg class="fig scanfig" viewBox="0 0 290 394" style="width:362px" role="img" aria-label="Задача 29"><image class="scan" href="/fig/pul/29.png" width="290" height="394"/><text class="lb lt" x="28" y="190" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="163" y="152" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="102" y="262" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="263" y="180" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="242" y="305" text-anchor="middle">2T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="78" y="120" text-anchor="middle">A</text><text class="lb lp" x="134" y="206" text-anchor="middle">B</text><text class="lb lp" x="202" y="256" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_2 = 4\,\dfrac{m_2(m_1 + m_3) - m_1 m_3}{4m_2(m_1 + m_3) + m_1 m_3}\,g$.

**Нити:** $T_1$ — от $m_1$ через $A$ к оси $B$; $T_2$ — от $m_2$ через $B$, под $C$, к потолку. Груз $m_3$ висит на $C$.

:::hint Подсказка
Метод одного натяжения: $\tau = T_2$, тогда $T_1 = 2\tau$ (блок $B$), а $C$ держит $2\tau$. Связь для нити $T_2$: $a_2 + 2a_3 = 2a_B$, где $a_B = -a_1$.
:::

:::solution Решение
**Связи.** $T_1$: $a_B = -a_1$. $T_2$: $(y_2 - y_B) + (y_C - y_B) + y_C = \text{const}$, поэтому $a_2 + 2a_3 = 2a_B = -2a_1$.

**Ускорения через $\tau$:**
$$a_1 = g - \frac{2\tau}{m_1}, \qquad a_2 = g - \frac{\tau}{m_2}, \qquad a_3 = g - \frac{2\tau}{m_3}.$$

**Подставим в связь** $a_2 + 2a_3 + 2a_1 = 0$:
$$5g = \tau\left(\frac1{m_2} + \frac4{m_3} + \frac4{m_1}\right) \;\Rightarrow\; \tau = \frac{5m_1 m_2 m_3}{4m_1 m_2 + m_1 m_3 + 4m_2 m_3}\,g.$$

**Ответ.**
$$a_2 = g - \frac{\tau}{m_2} = \frac{4m_1 m_2 + m_1 m_3 + 4m_2 m_3 - 5m_1 m_3}{4m_1 m_2 + m_1 m_3 + 4m_2 m_3}\,g = 4\,\frac{m_2(m_1 + m_3) - m_1 m_3}{4m_2(m_1 + m_3) + m_1 m_3}\,g.$$

**Проверка.** При $m_2 \to 0$ получаем $a_2 \to -4g$: невесомый «груз» $m_2$ резко выдёргивается вверх. Это нормально, нить может тянуть его с любым ускорением. Если $m_1$ и $m_3$ очень лёгкие по сравнению с $m_2$, то $a_2 \to g$: удерживать $m_2$ почти нечему.
:::

---

## Задачи 30–36: общий план

Во всех семи задачах на подвижном блоке $C$ (или $D$) висит груз, а два других груза связаны с ним цепочкой блоков. Две степени свободы, поэтому решаем **методом одного натяжения**:
1. по условиям невесомых блоков выражаем все натяжения через одно $\tau$;
2. пишем $a_i = g - (\text{итоговая сила нитей вверх})/m_i$;
3. подставляем в связи и находим $\tau$.

Главное — правильно посчитать, **сколько раз и в какую сторону** каждая нить действует на каждый груз. Для этого на рисунках подписаны все натяжения.

## Задача 30 (6.1)

<svg class="fig scanfig" viewBox="0 0 273 708" style="width:341px" role="img" aria-label="Задача 30"><image class="scan" href="/fig/pul/30.png" width="273" height="708"/><text class="lb lt" x="39" y="240" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="195" y="250" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="39" y="450" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="146" y="440" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="243" y="480" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="113" y="597" text-anchor="middle">2T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="98" y="160" text-anchor="middle">A</text><text class="lb lp" x="164" y="342" text-anchor="middle">B</text><text class="lb lp" x="76" y="524" text-anchor="middle">D</text></svg>

**Ответ учителя:** $a_2 = \dfrac{m_2(m_1 + m_3) - 4m_1 m_3}{m_2(m_1 + m_3) + 4m_1 m_3}\,g$.

**Нити:** $T_1$ — от верха $m_1$ через $A$ к оси $B$; $T_2$ — от низа $m_1$ под $D$, через $B$, к $m_3$. Груз $m_2$ висит на $D$.

:::solution Решение
**Связи.** $T_1$: $a_B = -a_1$. $T_2$: $(y_D - y_1) + (y_D - y_B) + (y_3 - y_B) = \text{const}$, поэтому $2a_D - a_1 - 2a_B + a_3 = 0$, то есть $2a_D + a_1 + a_3 = 0$.

**Натяжения.** Блок $B$: вверх $T_1$, вниз две ветви $T_2$ (к $D$ и к $m_3$). Поэтому $T_1 = 2\tau$, где $\tau = T_2$.

**Силы на грузы.**
- $m_1$: вверх $T_1 = 2\tau$, вниз $\tau$ (нить снизу). Итого вверх $\tau$: $a_1 = g - \tau/m_1$.
- $m_3$: вверх $\tau$: $a_3 = g - \tau/m_3$.
- $m_2$ (блок $D$): вверх $2\tau$: $a_2 = g - 2\tau/m_2$.

**Связь:** $2\left(g - \dfrac{2\tau}{m_2}\right) + g - \dfrac{\tau}{m_1} + g - \dfrac{\tau}{m_3} = 0$, откуда
$$\tau = \frac{4g}{\dfrac4{m_2} + \dfrac1{m_1} + \dfrac1{m_3}} = \frac{4m_1 m_2 m_3}{m_2(m_1 + m_3) + 4m_1 m_3}\,g.$$
$$a_2 = g - \frac{2\tau}{m_2} = \frac{m_2(m_1 + m_3) - 4m_1 m_3}{m_2(m_1 + m_3) + 4m_1 m_3}\,g.$$
:::

:::tip Наблюдение
Ответ совпадает с задачей 25, если поменять роли: здесь $m_2$ «против» эквивалентной массы $\dfrac{4m_1 m_3}{m_1 + m_3}$. Грузы $m_1$ и $m_3$ оба тянут нить $T_2$ с одной стороны, и каждый с итоговой силой $\tau$.
:::

## Задача 31 (6.2)

<svg class="fig scanfig" viewBox="0 0 272 708" style="width:340px" role="img" aria-label="Задача 31"><image class="scan" href="/fig/pul/31.png" width="272" height="708"/><text class="lb lt" x="40" y="350" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="195" y="220" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="146" y="497" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="120" y="340" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="243" y="450" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="113" y="597" text-anchor="middle">2T<tspan class="sb" dy="4">1</tspan></text><text class="lb lp" x="98" y="160" text-anchor="middle">A</text><text class="lb lp" x="164" y="301" text-anchor="middle">B</text><text class="lb lp" x="76" y="524" text-anchor="middle">D</text></svg>

**Ответ учителя:** $a_2 = \dfrac{m_2(m_1 + m_3)}{m_2(m_1 + m_3) + 16m_1 m_3}\,g$.

**Нити:** $T_1$ — от оси $B$ через $A$, под $D$, к низу $m_1$; $T_2$ — от верха $m_1$ через $B$ к $m_3$.

:::solution Решение
**Связи.** $T_1$: $y_B + y_D + (y_D - y_1) = \text{const}$, поэтому $a_B + 2a_D - a_1 = 0$. $T_2$: $(y_1 - y_B) + (y_3 - y_B) = \text{const}$, поэтому $a_1 + a_3 = 2a_B$.

**Натяжения.** Блок $B$: вверх $T_1$, вниз $2T_2$. Поэтому $T_1 = 2\tau$, где $\tau = T_2$.

**Силы на грузы.**
- $m_1$: вверх $\tau$ (нить $T_2$ сверху), **вниз** $T_1 = 2\tau$ (нить $T_1$ уходит от него вниз к блоку $D$). Итого вниз $\tau$: $a_1 = g + \tau/m_1$.
- $m_3$: $a_3 = g - \tau/m_3$.
- $m_2$ на блоке $D$: вверх $2T_1 = 4\tau$: $a_2 = g - 4\tau/m_2$.

**Связь.** $a_B = \tfrac12(a_1 + a_3) = g + \dfrac{\tau}{2}\left(\dfrac1{m_1} - \dfrac1{m_3}\right)$. Подставим в $a_B + 2a_2 = a_1$:
$$g + \frac{\tau}{2m_1} - \frac{\tau}{2m_3} + 2g - \frac{8\tau}{m_2} = g + \frac{\tau}{m_1}$$
$$\Rightarrow\; 2g = \tau\left(\frac1{2m_1} + \frac1{2m_3} + \frac8{m_2}\right) \;\Rightarrow\; \tau = \frac{4m_1 m_2 m_3}{m_2(m_1 + m_3) + 16m_1 m_3}\,g.$$
$$a_2 = g - \frac{4\tau}{m_2} = \frac{m_2(m_1 + m_3)}{m_2(m_1 + m_3) + 16m_1 m_3}\,g.$$

**Наблюдение.** $a_2 > 0$ при любых массах: груз $m_2$ всегда опускается. А $a_1 = g + \tau/m_1 > g$: груз $m_1$ нить тянет вниз, и он падает быстрее свободного падения.
:::

## Задача 32 (6.3)

<svg class="fig scanfig" viewBox="0 0 274 708" style="width:342px" role="img" aria-label="Задача 32"><image class="scan" href="/fig/pul/32.png" width="274" height="708"/><text class="lb lt" x="195" y="195" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="195" y="365" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="39" y="350" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="119" y="478" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="243" y="520" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="113" y="597" text-anchor="middle">2T<tspan class="sb" dy="4">1</tspan></text><text class="lb lp" x="98" y="160" text-anchor="middle">A</text><text class="lb lp" x="164" y="424" text-anchor="middle">B</text><text class="lb lp" x="76" y="524" text-anchor="middle">D</text></svg>

**Ответ учителя:** $a_2 = \dfrac{m_2(m_1 + m_3)}{m_2(m_1 + m_3) + 4m_1 m_3}\,g$.

**Нити:** $T_1$ — от верха $m_1$ через $A$, под $D$, через $B$, к $m_3$; $T_2$ — связка «низ $m_1$ — ось $B$».

:::solution Решение
**Связи.** $T_2$: $a_B = a_1$. $T_1$: $y_1 + y_D + (y_D - y_B) + (y_3 - y_B) = \text{const}$, поэтому $a_1 + 2a_D - 2a_B + a_3 = 0$, то есть $2a_D - a_1 + a_3 = 0$.

**Натяжения.** Блок $B$ висит под грузом $m_1$. Связка $T_2$ тянет его вверх, а две ветви нити $T_1$ (к $D$ и к $m_3$) тянут вниз. Поэтому $T_2 = 2\tau$, где $\tau = T_1$.

**Силы на грузы.**
- $m_1$: вверх $\tau$, вниз связка $T_2 = 2\tau$. Итого вниз $\tau$: $a_1 = g + \tau/m_1$.
- $m_3$: $a_3 = g - \tau/m_3$.
- $m_2$ (блок $D$): $a_2 = g - 2\tau/m_2$.

**Связь** $2a_2 - a_1 + a_3 = 0$:
$$2g - \frac{4\tau}{m_2} - g - \frac{\tau}{m_1} + g - \frac{\tau}{m_3} = 0 \;\Rightarrow\; \tau = \frac{2m_1 m_2 m_3}{m_2(m_1 + m_3) + 4m_1 m_3}\,g.$$
$$a_2 = g - \frac{2\tau}{m_2} = \frac{m_2(m_1 + m_3)}{m_2(m_1 + m_3) + 4m_1 m_3}\,g.$$
:::

## Задача 33 (6.4)

<svg class="fig scanfig" viewBox="0 0 239 708" style="width:299px" role="img" aria-label="Задача 33"><image class="scan" href="/fig/pul/33.png" width="239" height="708"/><text class="lb lt" x="35" y="180" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="157" y="175" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="35" y="370" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="99" y="330" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="190" y="300" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="190" y="480" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="65" y="490" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="150" y="600" text-anchor="middle">2T<tspan class="sb" dy="4">3</tspan></text><text class="lb lp" x="80" y="120" text-anchor="middle">A</text><text class="lb lp" x="130" y="260" text-anchor="middle">E</text><text class="lb lp" x="66" y="422" text-anchor="middle">D</text><text class="lb lp" x="110" y="544" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_3 = \dfrac{m_3(m_1 + m_2)}{m_3(m_1 + m_2) + 16m_1 m_2}\,g$.

**Нити:** $T_1$ — от $m_1$ через $A$ к оси $E$; $T_2$ — от низа $m_1$ под $D$, через $E$, к верху $m_2$; $T_3$ — от низа $m_2$ под $C$ к оси $D$. Груз $m_3$ на $C$.

:::solution Решение
**Связи.**
- $T_1$: $a_E = -a_1$.
- $T_2$: $(y_D - y_1) + (y_D - y_E) + (y_2 - y_E) = \text{const}$, поэтому $2a_D - a_1 - 2a_E + a_2 = 0$, то есть $2a_D + a_1 + a_2 = 0$.
- $T_3$: $(y_C - y_2) + (y_C - y_D) = \text{const}$, поэтому $2a_C = a_2 + a_D$.

**Натяжения через $\tau = T_2$.**
- Блок $E$: вверх $T_1$, вниз $2\tau$, поэтому $T_1 = 2\tau$.
- Блок $D$: вверх $2\tau$ (обе ветви $T_2$ идут от него вверх), вниз $T_3$, поэтому $T_3 = 2\tau$.

**Силы на грузы.**
- $m_1$: вверх $2\tau$, вниз $\tau$: $a_1 = g - \tau/m_1$.
- $m_2$: вверх $\tau$, вниз $T_3 = 2\tau$: $a_2 = g + \tau/m_2$.
- $m_3$ (блок $C$): вверх $2T_3 = 4\tau$: $a_3 = g - 4\tau/m_3$.

**Связи.** $a_D = -\tfrac12(a_1 + a_2) = -g + \dfrac{\tau}{2}\left(\dfrac1{m_1} - \dfrac1{m_2}\right)$. Тогда
$$a_3 = \tfrac12(a_2 + a_D) = \frac{\tau}{4}\left(\frac1{m_1} + \frac1{m_2}\right).$$
Приравняем к $g - 4\tau/m_3$:
$$\tau\left(\frac1{4m_1} + \frac1{4m_2} + \frac4{m_3}\right) = g \;\Rightarrow\; \tau = \frac{4m_1 m_2 m_3}{m_3(m_1 + m_2) + 16m_1 m_2}\,g,$$
$$a_3 = g - \frac{4\tau}{m_3} = \frac{m_3(m_1 + m_2)}{m_3(m_1 + m_2) + 16m_1 m_2}\,g.$$
:::

## Задача 34 (6.5)

<svg class="fig scanfig" viewBox="0 0 240 708" style="width:300px" role="img" aria-label="Задача 34"><image class="scan" href="/fig/pul/34.png" width="240" height="708"/><text class="lb lt" x="36" y="152" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="158" y="165" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="36" y="290" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="97" y="265" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="190" y="400" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="66" y="500" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="95" y="364" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="150" y="600" text-anchor="middle">2T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="80" y="120" text-anchor="middle">A</text><text class="lb lp" x="130" y="240" text-anchor="middle">E</text><text class="lb lp" x="66" y="322" text-anchor="middle">D</text><text class="lb lp" x="110" y="544" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_3 = \dfrac{m_3(m_1 + m_2) - 4m_1 m_2}{m_3(m_1 + m_2) + 4m_1 m_2}\,g$.

**Нити:** $T_1$ — от $m_1$ через $A$ к оси $E$; $T_2$ — от низа $m_1$ под $D$, через $E$, под $C$, к низу $m_2$; $T_3$ — связка «верх $m_2$ — ось $D$».

:::solution Решение
**Связи.**
- $T_1$: $a_E = -a_1$.
- $T_3$: $a_2 = a_D$.
- $T_2$: $(y_D - y_1) + (y_D - y_E) + (y_C - y_E) + (y_C - y_2) = \text{const}$, поэтому $2a_D - a_1 - 2a_E + 2a_C - a_2 = 0$. С учётом $a_E = -a_1$ и $a_D = a_2$: $a_2 + a_1 + 2a_C = 0$.

**Натяжения через $\tau = T_2$.** Блок $E$: $T_1 = 2\tau$. Блок $D$: обе ветви $T_2$ уходят вверх, значит вверх $2\tau$, а вниз его держит связка $T_3$. Поэтому $T_3 = 2\tau$.

**Силы на грузы.**
- $m_1$: вверх $2\tau$, вниз $\tau$: $a_1 = g - \tau/m_1$.
- $m_2$: вверх $T_3 = 2\tau$, вниз $\tau$ (нить $T_2$ снизу): $a_2 = g - \tau/m_2$.
- $m_3$: вверх $2\tau$: $a_3 = g - 2\tau/m_3$.

**Связь** $a_1 + a_2 + 2a_3 = 0$:
$$4g = \tau\left(\frac1{m_1} + \frac1{m_2} + \frac4{m_3}\right) \;\Rightarrow\; \tau = \frac{4m_1 m_2 m_3}{m_3(m_1 + m_2) + 4m_1 m_2}\,g,$$
$$a_3 = g - \frac{2\tau}{m_3} = \frac{m_3(m_1 + m_2) - 4m_1 m_2}{m_3(m_1 + m_2) + 4m_1 m_2}\,g.$$

**Смысл.** Это снова «машина Атвуда с эквивалентной массой»: $m_3$ против $\mu = \dfrac{4m_1 m_2}{m_1 + m_2}$.
:::

## Задача 35 (6.6)

<svg class="fig scanfig" viewBox="0 0 240 708" style="width:300px" role="img" aria-label="Задача 35"><image class="scan" href="/fig/pul/35.png" width="240" height="708"/><text class="lb lt" x="35" y="160" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="158" y="160" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="35" y="370" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="124" y="410" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="100" y="250" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="190" y="380" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="66" y="510" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="150" y="600" text-anchor="middle">2T<tspan class="sb" dy="4">3</tspan></text><text class="lb lp" x="80" y="120" text-anchor="middle">A</text><text class="lb lp" x="130" y="220" text-anchor="middle">E</text><text class="lb lp" x="66" y="444" text-anchor="middle">D</text><text class="lb lp" x="110" y="544" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_3 = \dfrac{m_3(m_1 + 9m_2) - 16m_1 m_2}{m_3(m_1 + 9m_2) + 16m_1 m_2}\,g$.

**Нити:** $T_1$ — от $m_1$ через $A$ к оси $E$; $T_2$ — от низа $m_1$ под $D$ к низу $m_2$; $T_3$ — от верха $m_2$ через $E$, под $C$, к оси $D$.

:::hint Подсказка
Здесь натяжения различаются сильнее: $T_3 = 2T_2$ (блок $D$), $T_1 = 2T_3 = 4T_2$ (блок $E$). На груз $m_1$ вверх действует $4\tau$, а вниз $\tau$. Отсюда девятка в ответе: итоговая сила $3\tau$ и квадрат $3^2$.
:::

:::solution Решение
**Связи.**
- $T_1$: $a_E = -a_1$.
- $T_2$: $2a_D = a_1 + a_2$.
- $T_3$: $(y_2 - y_E) + (y_C - y_E) + (y_C - y_D) = \text{const}$, поэтому $a_2 - 2a_E + 2a_C - a_D = 0$, то есть $a_2 + 2a_1 + 2a_C - a_D = 0$.

Подставим $a_D = \tfrac12(a_1 + a_2)$: $\tfrac12 a_2 + \tfrac32 a_1 + 2a_C = 0$, то есть
$$a_2 + 3a_1 + 4a_3 = 0.$$

**Натяжения через $\tau = T_2$.**
- Блок $D$: вверх $2\tau$ (две ветви $T_2$ к $m_1$ и $m_2$), вниз $T_3$, поэтому $T_3 = 2\tau$.
- Блок $E$: вверх $T_1$, вниз $2T_3 = 4\tau$, поэтому $T_1 = 4\tau$.

**Силы на грузы.**
- $m_1$: вверх $4\tau$, вниз $\tau$: $a_1 = g - 3\tau/m_1$.
- $m_2$: вверх $T_3 = 2\tau$, вниз $\tau$: $a_2 = g - \tau/m_2$.
- $m_3$: вверх $2T_3 = 4\tau$: $a_3 = g - 4\tau/m_3$.

**Связь** $a_2 + 3a_1 + 4a_3 = 0$:
$$8g = \tau\left(\frac1{m_2} + \frac9{m_1} + \frac{16}{m_3}\right) \;\Rightarrow\; \tau = \frac{8m_1 m_2 m_3}{m_3(m_1 + 9m_2) + 16m_1 m_2}\,g,$$
$$a_3 = g - \frac{4\tau}{m_3} = \frac{m_3(m_1 + 9m_2) - 16m_1 m_2}{m_3(m_1 + 9m_2) + 16m_1 m_2}\,g.$$
:::

## Задача 36 (6.7)

<svg class="fig scanfig" viewBox="0 0 239 708" style="width:299px" role="img" aria-label="Задача 36"><image class="scan" href="/fig/pul/36.png" width="239" height="708"/><text class="lb lt" x="35" y="300" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="157" y="160" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="126" y="400" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="99" y="250" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="190" y="300" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="190" y="500" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="66" y="510" text-anchor="middle">T<tspan class="sb" dy="4">3</tspan></text><text class="lb lt" x="150" y="600" text-anchor="middle">2T<tspan class="sb" dy="4">3</tspan></text><text class="lb lp" x="80" y="120" text-anchor="middle">A</text><text class="lb lp" x="130" y="220" text-anchor="middle">E</text><text class="lb lp" x="66" y="444" text-anchor="middle">D</text><text class="lb lp" x="110" y="544" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_3 = \dfrac{m_3(9m_1 + m_2) + 32m_1 m_2}{m_3(9m_1 + m_2) + 64m_1 m_2}\,g$.

**Нити:** $T_1$ — от оси $E$ через $A$, под $D$, к низу $m_1$; $T_2$ — от верха $m_1$ через $E$ к верху $m_2$; $T_3$ — от низа $m_2$ под $C$ к оси $D$.

:::solution Решение
**Связи.**
- $T_1$: $y_E + y_D + (y_D - y_1) = \text{const}$, поэтому $a_E + 2a_D - a_1 = 0$.
- $T_2$: $a_1 + a_2 = 2a_E$.
- $T_3$: $2a_C = a_2 + a_D$.

**Натяжения через $\tau = T_2$.**
- Блок $E$: вверх $T_1$, вниз $2\tau$, поэтому $T_1 = 2\tau$.
- Блок $D$: вверх две ветви $T_1$ (к $A$ и к $m_1$), то есть $4\tau$; вниз $T_3$. Поэтому $T_3 = 4\tau$.

**Силы на грузы.**
- $m_1$: вверх $\tau$, вниз $T_1 = 2\tau$: $a_1 = g + \tau/m_1$.
- $m_2$: вверх $\tau$, вниз $T_3 = 4\tau$: $a_2 = g + 3\tau/m_2$.
- $m_3$: вверх $2T_3 = 8\tau$: $a_3 = g - 8\tau/m_3$.

**Связи по шагам.**
$a_E = \tfrac12(a_1 + a_2) = g + \dfrac{\tau}{2}\left(\dfrac1{m_1} + \dfrac3{m_2}\right)$.
$a_D = \tfrac12(a_1 - a_E) = \dfrac{\tau}{4}\left(\dfrac1{m_1} - \dfrac3{m_2}\right)$.
$a_3 = \tfrac12(a_2 + a_D) = \tfrac12\left[g + \dfrac{\tau}{4}\left(\dfrac1{m_1} + \dfrac9{m_2}\right)\right]$.

Приравняем к $g - 8\tau/m_3$:
$$\frac{\tau}{4}\left(\frac1{m_1} + \frac9{m_2}\right) + \frac{16\tau}{m_3} = g \;\Rightarrow\; \tau = \frac{4m_1 m_2 m_3}{m_3(9m_1 + m_2) + 64m_1 m_2}\,g,$$
$$a_3 = g - \frac{8\tau}{m_3} = \frac{m_3(9m_1 + m_2) + 32m_1 m_2}{m_3(9m_1 + m_2) + 64m_1 m_2}\,g.$$

**Наблюдение.** Здесь $0 < a_3 < g$ при любых массах, а $m_1$ и $m_2$ падают **быстрее $g$**: нити тянут их вниз.
:::

---

:::key Что вынести из части 2
1. При одной степени свободы выражаем все ускорения через одно и исключаем натяжения. Энергетическая проверка $a = g\sum m_i k_i/\sum m_i k_i^2$ сразу даёт ответ.
2. При двух степенях свободы применяем **метод одного натяжения**: все $T$ выражаем через $\tau$, все $a_i$ — через $\tau$, подставляем в связи.
3. **Эквивалентная масса** $\mu = 4m_a m_b/(m_a + m_b)$ для блока с двумя грузами (и для двух брусков на блоке, задачи 27–28) сводит многие задачи к машине Атвуда.
4. Груз может падать быстрее $g$, если нить тянет его вниз (задачи 12, 31, 36). Это не ошибка.
:::
