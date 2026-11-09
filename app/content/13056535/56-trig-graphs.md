---
title: "Trigonometric graphs — решения всех 18 заданий (с интерактивными графиками)"
kind: solutions
units: []
tasks: [49088118, 49137955, 49321380]
order: 56
summary: Период, амплитуда, сдвиги, асимптоты, выколотые точки, графики с модулем и кусочные, области значений. Для сложных — графики, которые можно рассмотреть. Всё проверено численно.
---

:::key Алгоритм построения графика
1. **Упростить** формулу (сумма → произведение, вспомогательный угол, понижение степени). Записать, при каких $x$ исходная формула **не определена** — эти точки останутся выколотыми даже после сокращения.
2. Привести к виду $y = A\sin(k(x - b)) + d$ (или cos, tan): амплитуда $|A|$, период $\frac{2\pi}{|k|}$ (для tan/cot — $\frac{\pi}{|k|}$), сдвиг вправо на $b$, средняя линия $y = d$.
3. Найти точные нули, максимумы, минимумы, пересечение с $Oy$, асимптоты.
4. Подписать на графике всё из п. 3, ось $x$ — в долях π.
:::

:::warn Самая частая ошибка — сдвиг
$y = \sin(2x - \frac{\pi}{2})$ сдвинут на $\frac{\pi}{4}$, а не на $\frac{\pi}{2}$: сначала выносим коэффициент, $2\left(x - \frac{\pi}{4}\right)$.
:::

## 1–3. Базовые графики

:::solution 1. Область определения и период
(a) $\tan x$: $x \ne \frac{\pi}{2} + \pi k$, период π. (b) $\cot x$: $x \ne \pi k$, период π.
:::

:::solution 2. На $[-2\pi; 2\pi]$: амплитуда, средняя линия, период
**(a) $y = 2\sin x - 1$.** Амплитуда 2, средняя линия $y = -1$, период $2\pi$, значения $[-3; 1]$. Максимумы $\left(\frac{\pi}{2}; 1\right)$, $\left(-\frac{3\pi}{2}; 1\right)$; минимумы $\left(-\frac{\pi}{2}; -3\right)$, $\left(\frac{3\pi}{2}; -3\right)$. Нули: $\sin x = \frac12$ ⇒ $x = \frac{\pi}{6},\ \frac{5\pi}{6},\ -\frac{7\pi}{6},\ -\frac{11\pi}{6}$.

**(b) $y = -\cos2x + 1$.** Амплитуда 1, средняя линия $y = 1$, период π, значения $[0; 2]$. Минимумы (0) при $x = 0, \pm\pi, \pm2\pi$; максимумы (2) при $x = \pm\frac{\pi}{2}, \pm\frac{3\pi}{2}$.

**(c) $y = \sin\left(x - \frac{\pi}{3}\right)$.** Сдвиг $\sin x$ вправо на $\frac{\pi}{3}$. Амплитуда 1, средняя линия $y = 0$, период $2\pi$. Нули: $-\frac{5\pi}{3},\ -\frac{2\pi}{3},\ \frac{\pi}{3},\ \frac{4\pi}{3}$; максимумы при $x = \frac{5\pi}{6}, -\frac{7\pi}{6}$; минимумы при $x = -\frac{\pi}{6}, \frac{11\pi}{6}$.

**(d) $y = 2\cos\left(\frac{x}{2} + \frac{\pi}{4}\right) = 2\cos\left(\frac12\left(x + \frac{\pi}{2}\right)\right)$.** Растяжение в 2 раза по горизонтали, сдвиг **влево** на $\frac{\pi}{2}$. Амплитуда 2, средняя линия $y = 0$, период $4\pi$. Максимум $\left(-\frac{\pi}{2}; 2\right)$, минимум $\left(\frac{3\pi}{2}; -2\right)$, нули $x = -\frac{3\pi}{2},\ \frac{\pi}{2}$, $y(0) = \sqrt2$, на концах $y(\pm2\pi) = -\sqrt2$.
:::

:::solution 3. (a) $y = \tan\left(x - \frac{\pi}{4}\right)$, (b) $y = \cot2x$
(a) Сдвиг вправо на $\frac{\pi}{4}$, период π. Асимптоты $x = -\frac{\pi}{4},\ \frac{3\pi}{4}$; нули $x = -\frac{3\pi}{4},\ \frac{\pi}{4}$; $y(0) = -1$.
(b) Период $\frac{\pi}{2}$. Асимптоты $x = 0, \pm\frac{\pi}{2}, \pm\pi$; нули $x = \pm\frac{\pi}{4}, \pm\frac{3\pi}{4}$. На каждом промежутке убывает.
:::

## 4–8. Сначала упростить

:::solution 4. (a) $y = \cos^2x$, (b) $y = 1 - 4\sin^2x$
(a) $\cos^2x = \frac12 + \frac12\cos2x$: амплитуда $\frac12$, средняя линия $y = \frac12$, период π, значения $[0; 1]$. Максимумы при $x = 0, \pm\pi$, нули $x = \pm\frac{\pi}{2}$.
(b) $1 - 4\sin^2x = 1 - 2(1 - \cos2x) = 2\cos2x - 1$: амплитуда 2, средняя линия $y = -1$, период π, значения $[-3; 1]$. Нули: $\cos2x = \frac12$ ⇒ $x = \pm\frac{\pi}{6}, \pm\frac{5\pi}{6}$.
:::

:::solution 5. (a) $y = (\sin x + \cos x)^2$, (b) $y = 4\sin x\sin3x + 2\cos4x$
(a) $= 1 + \sin2x$: значения $[0; 2]$, период π. Максимумы $\left(\frac{\pi}{4}; 2\right)$, $\left(-\frac{3\pi}{4}; 2\right)$; минимумы (нули) $x = -\frac{\pi}{4}, \frac{3\pi}{4}$.
(b) $4\sin x\sin3x = 2(\cos2x - \cos4x)$ ⇒ $y = 2\cos2x$. Амплитуда 2, период π.
:::

:::solution 6. (a) $y = \cos x - \sin x$, (b) $y = \sqrt3\sin\frac x2 - \cos\frac x2$
(a) $= \sqrt2\cos\left(x + \frac{\pi}{4}\right)$: амплитуда $\sqrt2$, период $2\pi$. Максимум $\left(-\frac{\pi}{4}; \sqrt2\right)$, минимум $\left(\frac{3\pi}{4}; -\sqrt2\right)$, нули $x = \frac{\pi}{4}, -\frac{3\pi}{4}$, $y(0) = 1$.
(b) $= 2\left(\frac{\sqrt3}{2}\sin\frac x2 - \frac12\cos\frac x2\right) = 2\sin\left(\frac x2 - \frac{\pi}{6}\right)$: амплитуда 2, период $4\pi$. На $[-\pi; \pi]$: минимум $\left(-\frac{2\pi}{3}; -2\right)$, ноль $x = \frac{\pi}{3}$, $y(0) = -1$, на концах $y(-\pi) = -\sqrt3$, $y(\pi) = \sqrt3$. Максимум (при $x = \frac{4\pi}{3}$) вне отрезка. Значения на отрезке: $[-2; \sqrt3]$.
:::

:::solution 7. (a) $y = \sqrt2 - \sin x - \cos x$, (b) $y = |\sin x + \sqrt3\cos x|$
(a) $= \sqrt2 - \sqrt2\sin\left(x + \frac{\pi}{4}\right)$: значения $[0; 2\sqrt2]$, период $2\pi$. Минимум (касание оси) $\left(\frac{\pi}{4}; 0\right)$, максимум $\left(-\frac{3\pi}{4}; 2\sqrt2\right)$, $y(0) = \sqrt2 - 1$.
(b) $= \left|2\sin\left(x + \frac{\pi}{3}\right)\right|$: значения $[0; 2]$, период π (модуль). Нули $x = -\frac{\pi}{3}, \frac{2\pi}{3}$; максимумы (2) при $x = \frac{\pi}{6}, -\frac{5\pi}{6}$; $y(0) = \sqrt3$.
:::

:::solution 8. $y = 2\sin\left(x - \frac{\pi}{3}\right) + \cos\left(x + \frac{\pi}{3}\right) + \cos\left(x - \frac{\pi}{3}\right)$
Сумма косинусов: $2\cos x\cos\frac{\pi}{3} = \cos x$. Первое слагаемое: $\sin x - \sqrt3\cos x$. Итого
$$y = \sin x + (1 - \sqrt3)\cos x = R\sin(x + \varphi),\quad R = \sqrt{1 + (1 - \sqrt3)^2} = \sqrt{5 - 2\sqrt3} \approx 1{,}24,$$
$\tan\varphi = 1 - \sqrt3 < 0$ ⇒ $\varphi = -\arctan(\sqrt3 - 1)$.
Значения $[-\sqrt{5 - 2\sqrt3}; \sqrt{5 - 2\sqrt3}]$, период $2\pi$. Нули: $\tan x = \sqrt3 - 1$ ⇒ $x = \arctan(\sqrt3 - 1) + \pi k$ (≈ 0,632 и ≈ −2,51). Максимум при $x = \frac{\pi}{2} + \arctan(\sqrt3 - 1)$, $y(0) = 1 - \sqrt3$.
:::

## 9–12. Выколотые точки, модули, корни

:::solution 9. (a) $y = \dfrac{\sin x + \sin3x}{\sin2x}$, (b) $y = \dfrac{\tan x + 1}{1 - \tan x}$
(a) $= 2\cos x$ с выколотыми точками при $x = \frac{\pi k}{2}$ — разобрано в задании 14 Summative preparation (там же график). Значения $(-2; 0) \cup (0; 2)$.

(b) $\frac{\tan x + \tan\frac{\pi}{4}}{1 - \tan x\tan\frac{\pi}{4}} = \tan\left(x + \frac{\pi}{4}\right)$. **ОДЗ исходной:** $\cos x \ne 0$ и $\tan x \ne 1$, то есть $x \ne \frac{\pi}{2} + \pi k$ и $x \ne \frac{\pi}{4} + \pi k$.
- асимптоты (где $\tan\left(x + \frac{\pi}{4}\right)$ не определён): $x = \frac{\pi}{4}, -\frac{3\pi}{4}$;
- **выколотые точки** $x = \pm\frac{\pi}{2}$: там $\tan\left(x + \frac{\pi}{4}\right) = -1$, точки $\left(\pm\frac{\pi}{2}; -1\right)$;
- нули $x = -\frac{\pi}{4}, \frac{3\pi}{4}$, $y(0) = 1$, период π.
:::

:::solution 10 (a). $y = \dfrac{\cos(x + \pi/4)}{\cos2x}$
$\cos2x = (\cos x - \sin x)(\cos x + \sin x)$, $\cos\left(x + \frac{\pi}{4}\right) = \frac{\cos x - \sin x}{\sqrt2}$. Сокращаем:
$$y = \frac{1}{\sqrt2(\cos x + \sin x)} = \frac{1}{2\sin\left(x + \frac{\pi}{4}\right)},\qquad x \ne \frac{\pi}{4} + \frac{\pi k}{2}.$$
- **асимптоты:** $\sin\left(x + \frac{\pi}{4}\right) = 0$ ⇒ $x = -\frac{\pi}{4}, \frac{3\pi}{4}$;
- **выколотые точки:** $x = \frac{\pi}{4}$ (там было бы $y = \frac12$) и $x = -\frac{3\pi}{4}$ ($y = -\frac12$);
- значения упрощённой функции $|y| \ge \frac12$, но $\pm\frac12$ достигались бы только в выколотых точках.

**Значения:** $\left(-\infty; -\frac12\right) \cup \left(\frac12; +\infty\right)$. Период $2\pi$.
:::

:::plot
{"title":"10(a): y = cos(x + π/4)/cos 2x","x":[-3.3,3.3],"y":[-4,4],"xstep":1,"ystep":1,
"fns":[{"f":"cos(x+PI/4)/cos(2*x)","label":"y","domain":[-3.1416,3.1416]}],
"vlines":[{"x":"-PI/4","label":"x = −π/4","color":5},{"x":"3*PI/4","label":"x = 3π/4","color":5}],
"points":[{"x":"PI/4","y":"0.5","open":true,"label":"(π/4; 1/2) — выколота"},{"x":"-3*PI/4","y":"-0.5","open":true,"label":"(−3π/4; −1/2)"}]}
:::

:::solution 10 (b). $y = \dfrac{\cos x + \cos3x}{|\cos2x|}$
$\cos x + \cos3x = 2\cos2x\cos x$ ⇒ $y = 2\cos x\cdot\frac{\cos2x}{|\cos2x|}$, $x \ne \frac{\pi}{4} + \frac{\pi k}{2}$.
- где $\cos2x > 0$ (то есть $|x| < \frac{\pi}{4}$ или $\frac{3\pi}{4} < |x| \le \pi$): $y = 2\cos x$;
- где $\cos2x < 0$ ($\frac{\pi}{4} < |x| < \frac{3\pi}{4}$): $y = -2\cos x$.

Функция чётная, в точках $\pm\frac{\pi}{4}$, $\pm\frac{3\pi}{4}$ — **разрывы** (скачки между $\sqrt2$ и $-\sqrt2$, сами точки выколоты).
Значения: $[-2; 2]$ без $\pm\sqrt2$. Период $2\pi$.
:::

:::plot
{"title":"10(b): y = (cos x + cos 3x)/|cos 2x|","x":[-3.3,3.3],"y":[-2.5,2.5],"xstep":1,"ystep":1,
"fns":[{"f":"(cos(x)+cos(3*x))/abs(cos(2*x))","label":"y","domain":[-3.1416,3.1416]}],
"points":[{"x":"PI/4","y":"sqrt(2)","open":true},{"x":"PI/4","y":"-sqrt(2)","open":true},{"x":"-PI/4","y":"sqrt(2)","open":true},{"x":"-PI/4","y":"-sqrt(2)","open":true},{"x":"3*PI/4","y":"sqrt(2)","open":true},{"x":"3*PI/4","y":"-sqrt(2)","open":true},{"x":"-3*PI/4","y":"sqrt(2)","open":true},{"x":"-3*PI/4","y":"-sqrt(2)","open":true}]}
:::

:::solution 11. (a) $y = \sqrt{1 + \tan^2x}$, (b) $y = \sin2x\sqrt{1 + \cot^2x}$
(a) $1 + \tan^2x = \frac{1}{\cos^2x}$, $\sqrt{\ } = \frac{1}{|\cos x|}$ (корень из квадрата — модуль!). ОДЗ $x \ne \pm\frac{\pi}{2}$; асимптоты там же. Минимум 1 при $x = 0, \pm\pi$. Значения $[1; +\infty)$, период π.

(b) $\sqrt{1 + \cot^2x} = \frac{1}{|\sin x|}$ ⇒ $y = \frac{2\sin x\cos x}{|\sin x|}$, $x \ne \pi k$:
- на $(0; \pi)$: $y = 2\cos x$; на $(-\pi; 0)$: $y = -2\cos x$.

Выколоты $x = 0$ (слева предел $-2$, справа $2$) и $x = \pm\pi$. Значения $(-2; 2)$, период $2\pi$.
:::

:::solution 12. (a) $y = 2\sin\frac{|x|}{2} - 2\cos\frac x2$, (b) $y = |\sin x| - \sin x$
(a) Функция **чётная** (оба слагаемых чётные). При $x \ge 0$: $y = 2\sin\frac x2 - 2\cos\frac x2 = 2\sqrt2\sin\left(\frac x2 - \frac{\pi}{4}\right)$. На $[0; \pi]$ растёт от $-2$ (при $x = 0$) до $2$ (при $x = \pi$), ноль при $x = \frac{\pi}{2}$. Левая половина — зеркальное отражение. Ответ: минимум $(0; -2)$, нули $\pm\frac{\pi}{2}$, значения $[-2; 2]$. Функция непериодическая (из-за $|x|$).
(b) Если $\sin x \ge 0$: $y = 0$. Если $\sin x < 0$: $y = -2\sin x$. На $[-\pi; 0]$ — «горб» высотой 2 с вершиной $\left(-\frac{\pi}{2}; 2\right)$, на $[0; \pi]$ — ноль. Значения $[0; 2]$, период $2\pi$.
:::

## 13–15. Области значений и экстремумы

:::solution 13. (a) $y = \sin^2x - 2\sin x - 3$, (b) $y = \cos2x + \cos x - 1$
**(a)** $s = \sin x \in [-1; 1]$: $y = (s - 1)^2 - 4$ — на $[-1; 1]$ убывает по $s$. Наибольшее при $s = -1$: $y = 0$; наименьшее при $s = 1$: $y = -4$.
Значения $[-4; 0]$. Внутри $(-\pi; \pi)$: локальный максимум $\left(-\frac{\pi}{2}; 0\right)$, локальный минимум $\left(\frac{\pi}{2}; -4\right)$.

**(b)** $c = \cos x$: $y = 2c^2 + c - 2$, вершина параболы при $c = -\frac14$: $y = -\frac{17}{8}$. При $c = 1$: $y = 1$; при $c = -1$: $y = -1$.
Значения $\left[-\frac{17}{8}; 1\right]$. Внутри $(-\pi; \pi)$: максимум $(0; 1)$, минимумы $\left(\pm\arccos\left(-\frac14\right); -\frac{17}{8}\right)$.
:::

:::solution 14. (a) $y = |\sin^2x + 2\sin x|$, (b) $y = |\cos^2x - \cos x| - \cos x$
(a) $[0; 3]$ — разобрано в задании 15 Summative preparation.

(b) $c = \cos x \in [-1; 1]$, $\cos^2x - \cos x = c(c - 1)$.
- $c \in [0; 1]$: $c(c - 1) \le 0$, $y = (c - c^2) - c = -c^2 \in [-1; 0]$;
- $c \in [-1; 0)$: $c(c - 1) > 0$, $y = c^2 - 2c \in (0; 3]$.

**Значения:** $[-1; 3]$.
:::

:::solution 15. $f(x) = -\sin\frac x2$ при $x \le 0$, $f(x) = 2 - \cos^2x$ при $x > 0$
- На $[-\pi; 0]$: $\frac x2 \in \left[-\frac{\pi}{2}; 0\right]$, $f$ убывает от 1 (при $x = -\pi$) до 0 (при $x = 0$).
- На $(0; \pi]$: $2 - \cos^2x = \frac32 - \frac12\cos2x \in [1; 2]$; максимум $\left(\frac{\pi}{2}; 2\right)$, $f(\pi) = 1$; при $x \to 0^+$ значение стремится к 1.

В точке $x = 0$ **разрыв**: $f(0) = 0$ (закрашенная точка), а справа значения подходят к 1 (выколотая точка $(0; 1)$).
Значения на $[-\pi; \pi]$: $[0; 2]$.
:::

## 16–18

:::solution 16. $y = \arccos\left(\cos\left(2\arcsin(\sin x)\right)\right)$
Пусть $w = \arcsin(\sin x) \in \left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$, тогда $2w \in [-\pi; \pi]$ и $\arccos(\cos2w) = |2w|$.
- $\left[-\pi; -\frac{\pi}{2}\right]$: $w = -\pi - x$ ⇒ $y = 2(\pi + x)$;
- $\left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$: $w = x$ ⇒ $y = 2|x|$;
- $\left[\frac{\pi}{2}; \pi\right]$: $w = \pi - x$ ⇒ $y = 2(\pi - x)$.

Ломаная: нули в $0, \pm\pi$, вершины $\left(\pm\frac{\pi}{2}; \pi\right)$. **Значения:** $[0; \pi]$.
:::

:::plot
{"title":"16: y = arccos(cos(2 arcsin(sin x)))","x":[-3.4,3.4],"y":[-0.4,3.6],"xstep":1,"ystep":1,
"fns":[{"f":"acos(cos(2*asin(sin(x))))","label":"y","domain":[-3.1416,3.1416]}],
"points":[{"x":"PI/2","y":"PI","label":"(π/2; π)"},{"x":"-PI/2","y":"PI","label":"(−π/2; π)"}]}
:::

:::solution 17. $h(x) = |\sin^2x + 2\sin x|$, $0 \le x < 2\pi$
**(a)** На $[0; \pi]$: $h = \sin^2x + 2\sin x$, горб высотой 3 с вершиной $\left(\frac{\pi}{2}; 3\right)$. На $(\pi; 2\pi)$: $h = 1 - (\sin x + 1)^2$, горб высотой 1 с вершиной $\left(\frac{3\pi}{2}; 1\right)$. Нули: $x = 0, \pi$ (точка $2\pi$ не входит).

**(b)** Двигайте горизонтальную прямую $y = a$ и считайте пересечения:

| $a$ | $a < 0$ | $a = 0$ | $0 < a < 1$ | $a = 1$ | $1 < a < 3$ | $a = 3$ | $a > 3$ |
|---|---|---|---|---|---|---|---|
| решений | 0 | 2 | 4 | 3 | 2 | 1 | 0 |
:::

:::plot
{"title":"17: h(x) = |sin²x + 2sin x| на [0, 2π): двигайте a","x":[-0.2,6.5],"y":[-0.5,3.5],"xstep":1,"ystep":1,
"params":{"a":{"label":"a","min":-0.5,"max":3.5,"step":0.05,"value":0.6}},
"fns":[{"f":"abs(sin(x)^2+2*sin(x))","label":"y = h(x)","domain":[0,6.2832]}],
"hlines":[{"y":"a","label":"y = a","color":5}],
"out":[{"label":"решений","expr":"a<-1e-6?0:(Math.abs(a)<1e-6?2:(a<1-1e-6?4:(Math.abs(a-1)<1e-6?3:(a<3-1e-6?2:(Math.abs(a-3)<1e-6?1:0)))))"}]}
:::

:::solution 18. Цепочка преобразований от $y = \sin x$
(a) $|\sin x|$ — части ниже оси отражаем вверх; (b) $|\sin2x|$ — сжатие к оси $Oy$ в 2 раза; (c) $|\sin(2x - \frac{\pi}{2})|$ — сдвиг вправо на $\frac{\pi}{4}$ (это то же, что $|\cos2x|$); (d) растяжение по вертикали в 2 раза; (e) сдвиг вниз на 1.

Итог $g(x) = 2|\cos2x| - 1$: значения $[-1; 1]$, период $\frac{\pi}{2}$. Нули на $[-\pi; \pi]$: $|\cos2x| = \frac12$ ⇒ $x = \pm\frac{\pi}{6}, \pm\frac{\pi}{3}, \pm\frac{2\pi}{3}, \pm\frac{5\pi}{6}$. (То же, что задание 16 Summative preparation, — там интерактивный график.)
:::
