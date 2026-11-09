---
title: "Vectors: GCSE practice — решения всех 10 заданий"
kind: solutions
units: []
tasks: [49291935, 49321380]
order: 61
summary: Столбцы, параллельный перенос, параллелограмм, деление отрезка в отношении, параллельность и коллинеарность, пересечение медиан/чевиан, шестиугольник, теорема Вариньона. Проверено вычислениями.
---

:::key Три главных инструмента
1. **Деление отрезка.** Если $P$ на $AB$ и $AP : PB = m : n$, то $\vec{OP} = \vec{OA} + \frac{m}{m + n}\vec{AB} = \frac{n\,\vec{OA} + m\,\vec{OB}}{m + n}$.
2. **Параллельность.** $\vec u \parallel \vec v$ ⇔ $\vec u = k\vec v$. Если ещё и есть общая точка — точки лежат на одной прямой (коллинеарны).
3. **Пересечение двух прямых.** Запишите одну и ту же точку двумя путями с неизвестными $s$ и $t$, приравняйте коэффициенты при $\vec a$ и $\vec b$ (они не параллельны, поэтому разложение единственно).
:::

:::solution 1. $\vec a = \binom{3}{-7}$, $\vec b = \binom{4}{2}$. Найти $\vec b - 2\vec a$
$\vec b - 2\vec a = \binom{4 - 6}{2 + 14} = \binom{-2}{16}$.
:::

:::solution 2. Треугольник $A(-2; 1)$, $B(4; 1)$, $C(1; 5)$, перенос на $\vec t = \binom{3}{-2}$
**(a)** К каждой точке прибавляем $\vec t$: $A'(1; -1)$, $B'(7; -1)$, $C'(4; 3)$.
**(b)** $\vec{AC} = \binom{1 - (-2)}{5 - 1} = \binom{3}{4}$, длина $\sqrt{9 + 16} = 5$.
**(c)** $A' \to D(-1; 4)$: $\binom{-1 - 1}{4 - (-1)} = \binom{-2}{5}$. Один перенос $A \to D$: $\binom{3}{-2} + \binom{-2}{5} = \binom{1}{3}$ (проверка: $(-2 + 1; 1 + 3) = (-1; 4)$ ✓).
:::

:::solution 3. Параллелограмм $OACB$, $\vec{OA} = \vec a$, $\vec{OB} = \vec b$, диагонали пересекаются в $M$
(a) $\vec{AB} = \vec b - \vec a$. (b) $\vec{OC} = \vec a + \vec b$ (правило параллелограмма).
(c) Диагонали делятся пополам: $\vec{OM} = \frac12(\vec a + \vec b)$, $\vec{AM} = \vec{OM} - \vec a = \frac12(\vec b - \vec a)$.
(d) $\vec{MB} = \vec b - \frac12(\vec a + \vec b) = \frac12(\vec b - \vec a)$ — совпадает с $\vec{AM}$: $M$ — середина $AB$ ✓.
:::

:::solution 4. $AP : PB = 2 : 3$; $Q$ за точкой $B$, $BQ = \frac12 AB$
**(a)** $\vec{OP} = \vec a + \frac25(\vec b - \vec a) = \frac35\vec a + \frac25\vec b$. $\vec{OQ} = \vec b + \frac12(\vec b - \vec a) = \frac32\vec b - \frac12\vec a$.
**(b)** Вдоль прямой: $AP = \frac25 AB$, $AQ = AB + \frac12 AB = \frac32AB$, $PQ = \frac32AB - \frac25AB = \frac{11}{10}AB$.
$AP : PQ = \frac25 : \frac{11}{10} = 4 : 11$.
:::

:::solution 5. $OP : PA = OQ : QB = 2 : 1$
**(a)** $\vec{OP} = \frac23\vec a$, $\vec{OQ} = \frac23\vec b$ ⇒ $\vec{PQ} = \frac23(\vec b - \vec a)$.
**(b)** $\vec{AB} = \vec b - \vec a$, значит, $\vec{PQ} = \frac23\vec{AB}$ — векторы пропорциональны ⇒ $PQ \parallel AB$ ∎
**(c)** $PQ : AB = 2 : 3$.
:::

:::solution 6. $\vec{OA} = 3\vec a$, $\vec{OB} = 6\vec b$, $AP : PB = 2 : 1$, $\vec{OQ} = 2\vec a + 8\vec b$
**(a)** $\vec{OP} = 3\vec a + \frac23(6\vec b - 3\vec a) = \vec a + 4\vec b$.
**(b)** $\vec{OQ} = 2(\vec a + 4\vec b) = 2\vec{OP}$. Векторы $\vec{OP}$ и $\vec{OQ}$ параллельны и имеют общую точку $O$ ⇒ $O$, $P$, $Q$ на одной прямой ∎
**(c)** Порядок $O$, $P$, $Q$ ($\vec{OQ}$ того же направления и вдвое длиннее); $OP : PQ = 1 : 1$ — $P$ середина $OQ$.
:::

:::solution 7. Найти $k$ ($M$ — середина $OA$, $B$ — середина $AC$, $\vec{ON} = k\vec b$, $M$, $N$, $C$ на одной прямой)
$\vec{OM} = 3\vec a$. $B$ — середина $AC$ ⇒ $\vec{OC} = 2\vec{OB} - \vec{OA} = 12\vec b - 6\vec a$.
$\vec{MN} = k\vec b - 3\vec a$, $\vec{MC} = 12\vec b - 9\vec a$. Коллинеарность: $\vec{MN} = \lambda\vec{MC}$.
Сравниваем коэффициенты при $\vec a$: $-3 = -9\lambda$ ⇒ $\lambda = \frac13$; при $\vec b$: $k = 12\lambda = 4$.

**Ответ:** $k = 4$.
:::

:::solution 8. $M$ — середина $OA$, $ON : NB = 2 : 1$, $AN \cap BM = X$
**(a)** Два пути к $X$:
- по $AN$: $\vec{OX} = \vec a + s\left(\frac23\vec b - \vec a\right) = (1 - s)\vec a + \frac{2s}{3}\vec b$;
- по $BM$: $\vec{OX} = \vec b + t\left(\frac12\vec a - \vec b\right) = \frac t2\vec a + (1 - t)\vec b$.

Приравниваем: $1 - s = \frac t2$, $\frac{2s}{3} = 1 - t$. Из первого $t = 2 - 2s$, подставляем: $\frac{2s}{3} = 2s - 1$ ⇒ $s = \frac34$, $t = \frac12$.
$$\vec{OX} = \frac14\vec a + \frac12\vec b.$$
**(b)** $\vec{AX} = s\,\vec{AN}$ с $s = \frac34$ ⇒ $AX : XN = 3 : 1$. $\vec{BX} = t\,\vec{BM}$ с $t = \frac12$ ⇒ $BX : XM = 1 : 1$.
:::

:::solution 9. Правильный шестиугольник $ABCDEF$, $\vec{AB} = \vec a$, $\vec{AF} = \vec b$, $M$ — середина $CD$
Пусть $O$ — центр. Правильный шестиугольник состоит из 6 равносторонних треугольников, поэтому $ABOF$ — ромб и $\vec{AO} = \vec a + \vec b$. Кроме того, $BC \parallel AO$ и $BC = AO$ ($ABCO$ — тоже ромб).

(a) $\vec{BC} = \vec{AO} = \vec a + \vec b$.
(b) $\vec{AC} = \vec{AB} + \vec{BC} = 2\vec a + \vec b$.
(c) $\vec{AD} = 2\vec{AO} = 2\vec a + 2\vec b$ (большая диагональ проходит через центр и вдвое длиннее стороны).
(d) $\vec{AM} = \frac12(\vec{AC} + \vec{AD}) = 2\vec a + \frac32\vec b$.
:::

:::solution 10. Середины сторон четырёхугольника (теорема Вариньона)
$A$ — начало координат, $\vec{AB} = \vec b$, $\vec{AC} = \vec c$, $\vec{AD} = \vec d$. Середины: $P = \frac{\vec b}{2}$, $Q = \frac{\vec b + \vec c}{2}$, $R = \frac{\vec c + \vec d}{2}$, $S = \frac{\vec d}{2}$.

**(a)** $\vec{PQ} = \frac{\vec c}{2}$, $\vec{SR} = \frac{\vec c}{2}$. Векторы равны ⇒ $PQ \parallel SR$ и $PQ = SR$ ⇒ $PQRS$ — параллелограмм ∎ (Обе стороны — половина диагонали $AC$.)

**(b)** $\vec{PS} = \frac{\vec d - \vec b}{2} = \frac12\vec{BD}$, $\vec{PQ} = \frac12\vec{AC}$. Ромб ⇔ соседние стороны равны ⇔ $|\vec{AC}| = |\vec{BD}|$.

**Ответ:** диагонали $AC$ и $BD$ равны по длине.
:::
