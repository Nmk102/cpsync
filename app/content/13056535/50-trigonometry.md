---
title: Тригонометрия — всё в одном месте
kind: notes
units: [2103923]
tasks: [48785897, 48832703, 48915257, 48936939, 49034991, 49088118, 49137955, 49160495, 49170921, 49224265, 49227638, 49321380]
order: 50
summary: Единичная окружность, точные значения, формулы, уравнения (общие решения), графики, обратные функции, теоремы синусов и косинусов, пеленги.
---

Тригонометрия — самый большой блок первого триместра и значительная часть экзамена 27 ноября. Здесь собрано всё по порядку, а решения листков — в отдельных материалах.

## 1. Радианы и единичная окружность

$$180^\circ = \pi\ \text{рад}, \qquad 1\ \text{рад} \approx 57{,}3^\circ, \qquad x^\circ = x\cdot\frac{\pi}{180}.$$

На единичной окружности точка, повернутая на угол $t$, имеет координаты $(\cos t;\,\sin t)$, а $\tan t = \dfrac{\sin t}{\cos t}$.

:::plot
{"title":"Единичная окружность","x":[-1.6,1.6],"y":[-1.25,1.25],"aspect":0.78,
 "params":{"t":{"min":0,"max":6.2832,"step":0.0262,"value":0.5236,"label":"угол t (рад)"}},
 "fns":[{"f":"sqrt(1-x^2)","color":4,"domain":[-1,1]},{"f":"-sqrt(1-x^2)","color":4,"domain":[-1,1]},{"f":"tan(t)*x","color":3,"dash":true,"label":"прямая через начало и точку"}],
 "vlines":[{"x":"cos(t)","color":1,"label":"cos t"}],
 "hlines":[{"y":"sin(t)","color":2,"label":"sin t"}],
 "points":[{"x":"cos(t)","y":"sin(t)","label":"(cos t; sin t)","color":5}],
 "out":[{"label":"t в градусах","expr":"t*180/PI"},{"label":"sin t","expr":"sin(t)"},{"label":"cos t","expr":"cos(t)"},{"label":"tan t","expr":"abs(cos(t))<1e-6 ? 'не определён' : tan(t)"}]}
:::

**Знаки по четвертям** — правило *All Students Take Calculus*: в I четверти положительны **все**, во II — **sin**, в III — **tan**, в IV — **cos**.

## 2. Точные значения

| $t$ | $0$ | $\frac\pi6$ | $\frac\pi4$ | $\frac\pi3$ | $\frac\pi2$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\sin t$ | $0$ | $\frac12$ | $\frac{\sqrt2}2$ | $\frac{\sqrt3}2$ | $1$ | $0$ |
| $\cos t$ | $1$ | $\frac{\sqrt3}2$ | $\frac{\sqrt2}2$ | $\frac12$ | $0$ | $-1$ |
| $\tan t$ | $0$ | $\frac{\sqrt3}3$ | $1$ | $\sqrt3$ | — | $0$ |

Приведение: $\sin(\pi - t) = \sin t$, $\cos(\pi - t) = -\cos t$, $\sin(\pi + t) = -\sin t$, $\sin\left(\frac\pi2 - t\right) = \cos t$, $\sin(-t) = -\sin t$, $\cos(-t) = \cos t$.

## 3. Формулы

:::formula Основные тождества
$$\sin^2 t + \cos^2 t = 1, \qquad 1 + \tan^2 t = \frac1{\cos^2 t}, \qquad \tan t\cdot\cot t = 1$$
:::

:::formula Сложение
$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta,\qquad \cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$$
$$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$$
:::

:::formula Двойной угол и понижение степени
$$\sin2t = 2\sin t\cos t, \qquad \cos2t = \cos^2t - \sin^2t = 2\cos^2t - 1 = 1 - 2\sin^2t, \qquad \tan 2t = \frac{2\tan t}{1 - \tan^2t}$$
$$\cos^2t = \frac{1 + \cos2t}2, \qquad \sin^2t = \frac{1 - \cos2t}2$$
:::

:::formula Сумма в произведение и вспомогательный угол
$$\sin\alpha + \sin\beta = 2\sin\frac{\alpha + \beta}2\cos\frac{\alpha - \beta}2, \qquad \cos\alpha + \cos\beta = 2\cos\frac{\alpha + \beta}2\cos\frac{\alpha - \beta}2$$
$$a\sin t + b\cos t = \sqrt{a^2 + b^2}\,\sin(t + \varphi), \quad \text{где } \cos\varphi = \frac{a}{\sqrt{a^2+b^2}},\ \sin\varphi = \frac{b}{\sqrt{a^2+b^2}}$$
Пример: $\sin t + \cos t = \sqrt2\sin\left(t + \frac\pi4\right)$, поэтому значения от $-\sqrt2$ до $\sqrt2$.
:::

## 4. Уравнения: общие решения

| Уравнение | Общее решение ($n \in \mathbb Z$) | Частные случаи |
|---|---|---|
| $\sin x = a$, $\lvert a\rvert \le 1$ | $x = \arcsin a + 2\pi n$ или $x = \pi - \arcsin a + 2\pi n$ | $\sin x = 0$: $x = \pi n$; $\sin x = 1$: $x = \frac\pi2 + 2\pi n$ |
| $\cos x = a$, $\lvert a\rvert \le 1$ | $x = \pm\arccos a + 2\pi n$ | $\cos x = 0$: $x = \frac\pi2 + \pi n$; $\cos x = 1$: $x = 2\pi n$ |
| $\tan x = a$ | $x = \arctan a + \pi n$ | — |

**Типы уравнений и методы:**
1. **Сводящиеся к квадратному**: $2\cos^2x - 3\cos x + 1 = 0$ → $t = \cos x$, не забыть $|t| \le 1$.
2. **Через формулы** — привести к одной функции одного аргумента: $\cos2x = \sin x \Rightarrow 1 - 2\sin^2x = \sin x$.
3. **Однородные** $a\sin x + b\cos x = 0$ → разделить на $\cos x$ (проверив, что $\cos x = 0$ не корень) → $\tan x = -\frac ba$.
4. **Разложение на множители**: $\sin2x = \sin x \Rightarrow \sin x(2\cos x - 1) = 0$. **Не делите** на $\sin x$ — потеряете корни!
5. **Вспомогательный угол**: $\sin x + \sqrt3\cos x = 1 \Rightarrow 2\sin\left(x + \frac\pi3\right) = 1$.

:::warn Отбор корней на промежутке
Если нужен промежуток (например, $[0;\,2\pi)$), выпишите корни для $n = -1, 0, 1, 2$ и оставьте попавшие. Проверьте **концы** промежутка — строгий или нестрогий. И **ОДЗ**: у $\tan x$ — $\cos x \ne 0$, у дробей — знаменатель.
:::

:::example $2\sin^2x + \sin x - 1 = 0$ на $[0;\,2\pi)$
$t = \sin x$: $2t^2 + t - 1 = 0 \Rightarrow t = \frac12$ или $t = -1$.
$\sin x = \frac12$: $x = \frac\pi6,\ \frac{5\pi}6$; $\ \sin x = -1$: $x = \frac{3\pi}2$. **Ответ:** $\frac\pi6;\ \frac{5\pi}6;\ \frac{3\pi}2$.
:::

## 5. Графики

| Функция | Период | Область значений | Нули |
|---|---|---|---|
| $\sin x$ | $2\pi$ | $[-1;\,1]$ | $\pi n$ |
| $\cos x$ | $2\pi$ | $[-1;\,1]$ | $\frac\pi2 + \pi n$ |
| $\tan x$ | $\pi$ | $\mathbb R$ | $\pi n$; асимптоты $x = \frac\pi2 + \pi n$ |

Для $y = a\sin(bx + c) + d$: амплитуда $|a|$, период $\frac{2\pi}{|b|}$, сдвиг $-\frac cb$, среднее значение $d$, наибольшее $d + |a|$, наименьшее $d - |a|$. Интерактивный график — в материале «Преобразования графиков функций».

## 6. Обратные тригонометрические функции

| Функция | Область определения | Область значений |
|---|---|---|
| $\arcsin x$ | $[-1;\,1]$ | $\left[-\frac\pi2;\,\frac\pi2\right]$ |
| $\arccos x$ | $[-1;\,1]$ | $[0;\,\pi]$ |
| $\arctan x$ | $\mathbb R$ | $\left(-\frac\pi2;\,\frac\pi2\right)$ |

- $\arcsin(-x) = -\arcsin x$, $\arctan(-x) = -\arctan x$, но $\arccos(-x) = \pi - \arccos x$.
- $\arcsin x + \arccos x = \frac\pi2$.
- $\sin(\arcsin x) = x$ при $x \in [-1;\,1]$, но $\arcsin(\sin x) = x$ **только** при $x \in \left[-\frac\pi2;\,\frac\pi2\right]$! Например, $\arcsin\left(\sin\frac{5\pi}6\right) = \frac\pi6$.
- $\cos(\arcsin x) = \sqrt{1 - x^2}$ (корень неотрицателен, так как $\arcsin x \in \left[-\frac\pi2;\,\frac\pi2\right]$).

## 7. Треугольники

:::formula Теоремы синусов и косинусов, площадь
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R, \qquad c^2 = a^2 + b^2 - 2ab\cos C, \qquad S = \frac12 ab\sin C$$
:::

- **Теорема синусов** — если известны сторона и противолежащий угол (+ ещё сторона или угол). Осторожно: при нахождении угла по синусу может быть **два ответа** (острый и тупой) — «неоднозначный случай».
- **Теорема косинусов** — две стороны и угол между ними (найти третью сторону) или три стороны (найти угол).

## 8. Пеленги (*bearings*)

Пеленг — угол **от направления на север по часовой стрелке**, записывается **тремя цифрами**: восток $090^\circ$, юг $180^\circ$, запад $270^\circ$.
- Обратный пеленг (из $B$ на $A$) = пеленг из $A$ на $B$ $\pm 180^\circ$.
- Решение: рисуем «северные стрелки» в каждой точке (они параллельны!), используем накрест лежащие углы, затем теоремы синусов и косинусов.

## 9. Чева и Менелай (из листка TLF)

Для треугольника $ABC$ с точками $A_1 \in BC$, $B_1 \in CA$, $C_1 \in AB$:

:::formula Теорема Чевы
Прямые $AA_1$, $BB_1$, $CC_1$ пересекаются в одной точке $\iff$
$$\frac{AC_1}{C_1B}\cdot\frac{BA_1}{A_1C}\cdot\frac{CB_1}{B_1A} = 1.$$
:::

:::formula Теорема Менелая
Точки $A_1$, $B_1$, $C_1$ (на сторонах или их продолжениях) лежат на одной прямой $\iff$
$$\frac{AC_1}{C_1B}\cdot\frac{BA_1}{A_1C}\cdot\frac{CB_1}{B_1A} = 1\quad\text{(в длинах отрезков; в направленных отрезках } = -1).$$
:::

Мнемоника: «обходим треугольник» $A \to C_1 \to B \to A_1 \to C \to B_1 \to A$ — вершина, точка, вершина, точка…

**Применение:** найти отношение, в котором точка делит отрезок (медианы — $2:1$, биссектрисы, отрезки к точкам касания вписанной окружности — все они пересекаются в одной точке по теореме Чевы).
