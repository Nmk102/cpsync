---
title: "Inverse trigonometric functions — решения всех 17 заданий"
kind: solutions
units: []
tasks: [49034991, 49160495, 49321380]
order: 55
summary: Сравнение, вычисление, доказательства равенств и тождеств, графики arcsin(sin x) и др. (интерактивно), области значений, уравнения и неравенства. Ответы проверены численно.
---

:::key Главное про обратные функции
| Функция | Область определения | Значения (главный диапазон) | Монотонность |
|---|---|---|---|
| $\arcsin x$ | $[-1; 1]$ | $\left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$ | возрастает |
| $\arccos x$ | $[-1; 1]$ | $[0; \pi]$ | убывает |
| $\arctan x$ | $\mathbb R$ | $\left(-\frac{\pi}{2}; \frac{\pi}{2}\right)$ | возрастает |
| $\text{arccot}\,x$ | $\mathbb R$ | $(0; \pi)$ | убывает |

**Смысл:** $\arcsin a$ — это **угол из главного диапазона**, синус которого равен $a$. Поэтому $\arcsin(\sin x) = x$ только когда $x$ сам лежит в $\left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$.

**Тождества:** $\arcsin x + \arccos x = \frac{\pi}{2}$, $\arctan x + \text{arccot}\,x = \frac{\pi}{2}$, $\arcsin(-x) = -\arcsin x$, $\arccos(-x) = \pi - \arccos x$.
:::

:::tip Приём «треугольник»
Чтобы найти, например, $\cos(\arctan\frac34)$, нарисуйте прямоугольный треугольник с катетами 3 и 4 (гипотенуза 5): $\cos = \frac45$. Знак определяйте по главному диапазону: для отрицательного аргумента $\arcsin$ и $\arctan$ угол лежит в IV четверти, $\arccos$ — во II.
:::

## 1. Сравнение чисел

:::solution 1)–5)
1) $\arccos$ убывает, $-0{,}3 < -0{,}2$ ⇒ $\arccos(-0{,}3) > \arccos(-0{,}2)$.
2) $\arcsin$ возрастает ⇒ $\arcsin\frac15 > \arcsin\frac16$.
3) $\arccos\frac23 = \arcsin\frac{\sqrt5}{3}$ (острый угол с косинусом $\frac23$ имеет синус $\sqrt{1 - \frac49}$). $\frac{\sqrt5}{3} \approx 0{,}75 > \frac13$ ⇒ $\arccos\frac23 > \arcsin\frac13$.
4) $\arccos\left(-\frac45\right) \in \left(\frac{\pi}{2}; \pi\right)$ — положительное, $\arcsin\left(-\frac56\right) < 0$ ⇒ первое больше.
5) Без калькулятора: $\cos^240^\circ = \frac{1 + \cos80^\circ}{2}$, а $\cos80^\circ = \sin10^\circ < \frac{\pi}{18} < 0{,}18$ (так как $\sin t < t$). Значит, $\cos^240^\circ < 0{,}59 < 0{,}64 = \left(\frac45\right)^2$ ⇒ $\cos40^\circ < \frac45$.
:::

## 2. Вычислить

:::solution 1)–4)
1) $\sin\left(\frac{\pi}{2} - \arccos0{,}6\right) = \cos(\arccos0{,}6) = 0{,}6$.
2) $\tan\left(\frac{3\pi}{2} - \alpha\right) = \cot\alpha$. При $\alpha = \arcsin\left(-\frac{5}{13}\right)$: $\sin\alpha = -\frac{5}{13}$, $\cos\alpha = \frac{12}{13}$ (IV четверть) ⇒ **$-\frac{12}{5}$**.
3) $\sin\left(\beta - \frac{3\pi}{2}\right) = \sin\left(\beta + \frac{\pi}{2}\right) = \cos\beta$. При $\beta = \arctan\frac34$ ⇒ **$\frac45$**.
4) $\cos(\arcsin a) = \sqrt{1 - a^2}$ (косинус в главном диапазоне арксинуса $\ge 0$). $(\sqrt3 - \sqrt2)^2 = 5 - 2\sqrt6$ ⇒ **$\sqrt{2\sqrt6 - 4}$**.
:::

## 3. Вычислить

:::solution 1) $\sin\left(\frac12\arcsin\left(-\frac{2\sqrt2}{3}\right)\right)$
$\theta = \arcsin\left(-\frac{2\sqrt2}{3}\right) \in \left(-\frac{\pi}{2}; 0\right)$, $\cos\theta = \sqrt{1 - \frac89} = \frac13$.
$\frac{\theta}{2} \in \left(-\frac{\pi}{4}; 0\right)$ — синус отрицательный:
$$\sin\frac{\theta}{2} = -\sqrt{\frac{1 - \cos\theta}{2}} = -\sqrt{\frac13} = -\frac{\sqrt3}{3}.$$
:::

:::solution 2) $\tan\left(5\arctan\frac{\sqrt3}{3} - \frac14\arcsin\frac{\sqrt3}{2}\right)$
$\arctan\frac{\sqrt3}{3} = \frac{\pi}{6}$, $\arcsin\frac{\sqrt3}{2} = \frac{\pi}{3}$. Аргумент: $\frac{5\pi}{6} - \frac{\pi}{12} = \frac{3\pi}{4}$. **Ответ:** $\tan\frac{3\pi}{4} = -1$.
:::

## 4. Доказать равенства

:::solution 1) $\arcsin\frac45 + \arcsin\frac{5}{13} + \arcsin\frac{16}{65} = \frac{\pi}{2}$
$\alpha = \arcsin\frac45$ ($\cos\alpha = \frac35$), $\beta = \arcsin\frac{5}{13}$ ($\cos\beta = \frac{12}{13}$).
$$\cos(\alpha + \beta) = \frac35\cdot\frac{12}{13} - \frac45\cdot\frac{5}{13} = \frac{16}{65} > 0.$$
α и β острые, их сумма $\in (0; \pi)$, а косинус положительный ⇒ $\alpha + \beta = \arccos\frac{16}{65} = \frac{\pi}{2} - \arcsin\frac{16}{65}$ ∎
:::

:::solution 2) $2\arctan\frac15 + \arctan\frac14 = \arctan\frac{32}{43}$
$\tan\left(2\arctan\frac15\right) = \frac{2/5}{1 - 1/25} = \frac{5}{12}$. Тогда
$$\tan(\text{левая часть}) = \frac{\frac{5}{12} + \frac14}{1 - \frac{5}{12}\cdot\frac14} = \frac{\frac23}{\frac{43}{48}} = \frac{32}{43}.$$
**Диапазон:** $\frac15, \frac14 < \frac{1}{\sqrt3}$ ⇒ каждый арктангенс $< \frac{\pi}{6}$, сумма $\in \left(0; \frac{\pi}{2}\right)$ — там тангенс определяет угол однозначно ∎
:::

:::warn Почему проверка диапазона обязательна
Из $\tan A = \tan B$ следует только $A = B + \pi k$. Например, $\tan(\arctan2 + \arctan3) = -1$, но сумма равна $\frac{3\pi}{4}$, а не $-\frac{\pi}{4}$ (задача 7).
:::

## 5. Найти

:::solution 1) $\arcsin\left(\sin\frac32\right)$; 2) $\arccos(\cos3)$
1) $\frac32 < \frac{\pi}{2} \approx 1{,}571$ — лежит в главном диапазоне ⇒ **$\frac32$**.
2) $3 < \pi$ — лежит в $[0; \pi]$ ⇒ **3**.
:::

## 6. Доказать тождества

:::solution 1)–3)
**Схема:** чтобы доказать $\text{arcf}(a) = \varphi$, достаточно проверить, что φ лежит в главном диапазоне и $f(\varphi) = a$.

1) $\alpha = \arctan x \in \left(-\frac{\pi}{2}; \frac{\pi}{2}\right)$. Тогда $\frac{\pi}{2} - \alpha \in (0; \pi)$ и $\cot\left(\frac{\pi}{2} - \alpha\right) = \tan\alpha = x$ ⇒ $\text{arccot}\,x = \frac{\pi}{2} - \alpha$ ∎
2) $\alpha = \arccos x \in [0; \pi]$ ⇒ $\pi - \alpha \in [0; \pi]$, $\cos(\pi - \alpha) = -x$ ⇒ $\arccos(-x) = \pi - \alpha$ ∎
3) $\alpha = \text{arccot}\,x \in (0; \pi)$ ⇒ $\pi - \alpha \in (0; \pi)$, $\cot(\pi - \alpha) = -x$ ⇒ $\text{arccot}(-x) = \pi - \alpha$ ∎
:::

## 7. Доказать равенства

:::solution 1) $\arctan2 + \arctan3 = \frac{3\pi}{4}$; 2) $\arcsin0{,}6 + \arcsin0{,}8 = \frac{\pi}{2}$
1) $\tan(\text{сумма}) = \frac{2 + 3}{1 - 6} = -1$. Каждый арктангенс больше $\frac{\pi}{4}$ (аргументы > 1) и меньше $\frac{\pi}{2}$, сумма $\in \left(\frac{\pi}{2}; \pi\right)$. Там тангенс равен −1 только в $\frac{3\pi}{4}$ ∎
2) Острый угол с синусом 0,8 имеет косинус 0,6 ⇒ $\arcsin0{,}8 = \arccos0{,}6$. Сумма $= \arcsin0{,}6 + \arccos0{,}6 = \frac{\pi}{2}$ ∎
:::

## 8. Графики

:::solution 1) $y = \arcsin(\sin x)$, 2) $y = \arccos(\cos x)$, 3) $y = \arctan(\tan x)$
1) На $\left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$: $y = x$. На $\left[\frac{\pi}{2}; \frac{3\pi}{2}\right]$: $y = \pi - x$ (потому что $\sin x = \sin(\pi - x)$, и $\pi - x$ в главном диапазоне). Дальше период $2\pi$. **«Пила-треугольник»** от $-\frac{\pi}{2}$ до $\frac{\pi}{2}$.
2) На $[0; \pi]$: $y = x$; на $[-\pi; 0]$: $y = -x$. То есть $y = |x|$ на $[-\pi; \pi]$, дальше период $2\pi$. Треугольники от 0 до π.
3) На $\left(-\frac{\pi}{2}; \frac{\pi}{2}\right)$: $y = x$, дальше период π: $y = x - \pi k$. В точках $\frac{\pi}{2} + \pi k$ функция **не определена** (выколотые точки на концах отрезков).
:::

:::plot
{"title":"Графики «функция от функции»: переключайте k","x":[-7,7],"y":[-2,3.5],"xstep":1,"ystep":1,
"params":{"k":{"label":"какой график: 1 — arcsin(sin x), 2 — arccos(cos x), 3 — arctan(tan x)","min":1,"max":3,"step":1,"value":1}},
"fns":[{"f":"k==1?asin(sin(x)):(k==2?acos(cos(x)):atan(tan(x)))","label":"выбранная функция"},{"f":"x","label":"y = x","color":4,"dash":true}],
"note":"Заметьте: совпадает с y = x только на главном диапазоне."}
:::

## 9. Области значений

:::solution 1)–4)
1) $2\arcsin x + 3$: $\arcsin x \in \left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$ ⇒ **$[3 - \pi; 3 + \pi]$**.
2) $t = \arccos x \in [0; \pi]$, $\frac{t}{t + 4} = 1 - \frac{4}{t + 4}$ — возрастает по $t$ ⇒ **$\left[0; \frac{\pi}{\pi + 4}\right]$**.
3) $t = \text{arccot}\,x \in (0; \pi)$ (концы **не** достигаются). $t^2 - \pi t = \left(t - \frac{\pi}{2}\right)^2 - \frac{\pi^2}{4}$: минимум $-\frac{\pi^2}{4}$ при $t = \frac{\pi}{2}$, к концам стремится к 0 ⇒ **$\left[-\frac{\pi^2}{4}; 0\right)$**.
4) $2\arcsin x + 3\arccos x = \frac{3\pi}{2} - \arcsin x$ ⇒ **$[\pi; 2\pi]$**.
:::

## 10 (= 13). Уравнения

:::solution 1) $\arcsin(x^2 - 5x + 1) = \frac{\pi}{6}$
⇔ $x^2 - 5x + 1 = \frac12$ (аргумент автоматически в $[-1; 1]$) ⇔ $2x^2 - 10x + 1 = 0$ ⇒ $x = \frac{5 \pm \sqrt{23}}{2}$.
:::

:::solution 2) $\arcsin(4x^3 - 3x^2 - 1) = \arcsin(x - 1)$
arcsin — взаимно однозначная, поэтому ⇔ аргументы равны **и** лежат в $[-1; 1]$: $x - 1 \in [-1; 1]$ ⇔ $x \in [0; 2]$.
$4x^3 - 3x^2 - 1 = x - 1$ ⇔ $x(4x^2 - 3x - 1) = 0$ ⇔ $x(x - 1)(4x + 1) = 0$.
$x = -\frac14 \notin [0; 2]$. **Ответ:** $x = 0$, $x = 1$.
:::

:::solution 3) $4\arcsin(x^2 - 4x + 4) = \pi$
$\arcsin((x - 2)^2) = \frac{\pi}{4}$ ⇔ $(x - 2)^2 = \frac{\sqrt2}{2}$ ⇒ $x = 2 \pm \sqrt{\frac{\sqrt2}{2}} = 2 \pm \frac{1}{\sqrt[4]{2}}$.
:::

## 11. Решить

:::solution 1)–4)
1) $\arcsin(\sin x) = x$ ⇔ $x \in \left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$.
2) $\sin(\arcsin x) = x$ при $x \in [-1; 1]$. Неравенство $x > 0$ ⇒ **$x \in (0; 1]$**.
3) $\arccos$ убывает: $\arccos x > \frac{\pi}{3} = \arccos\frac12$ ⇔ $x < \frac12$. С учётом области определения: **$x \in \left[-1; \frac12\right)$**.
4) $t = \arcsin x$: $t^2 - 5t + 4 \le 0$ ⇔ $1 \le t \le 4$. Но $t \le \frac{\pi}{2} < 4$, значит, $1 \le \arcsin x \le \frac{\pi}{2}$ ⇔ **$x \in [\sin1; 1]$**.
:::

## 12. $2\arcsin x = -\pi - (x + 1)^2$

:::solution Решение — оценкой
Левая часть $\ge 2\cdot\left(-\frac{\pi}{2}\right) = -\pi$. Правая $\le -\pi$. Равенство ⇔ обе равны $-\pi$: $\arcsin x = -\frac{\pi}{2}$ и $(x + 1)^2 = 0$. Оба дают $x = -1$.

**Ответ:** $x = -1$.
:::

## 14. Уравнения

:::solution 1) $\arctan(3x) = \arccos(8x)$
Обе части равны некоторому θ. $\arctan \in \left(-\frac{\pi}{2}; \frac{\pi}{2}\right)$, $\arccos \in [0; \pi]$ ⇒ $\theta \in \left[0; \frac{\pi}{2}\right)$, $x \ge 0$.
$\tan\theta = 3x$, $\cos\theta = 8x$, и для угла из I четверти $\cos\theta = \frac{1}{\sqrt{1 + \tan^2\theta}}$:
$$8x = \frac{1}{\sqrt{1 + 9x^2}} \iff 64x^2(1 + 9x^2) = 1 \iff 576x^4 + 64x^2 - 1 = 0 \iff x^2 = \frac{-64 + 80}{1152} = \frac{1}{72}.$$
**Ответ:** $x = \frac{1}{6\sqrt2} = \frac{\sqrt2}{12}$.
:::

:::solution 2) $\arcsin(3x) = \arccos(4x)$
Как задача 9(b) в Summative preparation: **$x = \frac15$**.
:::

:::solution 3) $\arctan(x + 2) - \arctan(x + 1) = \frac{\pi}{4}$
Тангенс разности: $\frac{(x + 2) - (x + 1)}{1 + (x + 2)(x + 1)} = 1$ ⇔ $(x + 1)(x + 2) = 0$ ⇒ $x = -1$ или $x = -2$.
Разность арктангенсов лежит в $(0; \pi)$ (arctan возрастает), там $\tan = 1$ только при $\frac{\pi}{4}$ — оба корня подходят. Проверка: $\arctan1 - \arctan0 = \frac{\pi}{4}$; $\arctan0 - \arctan(-1) = \frac{\pi}{4}$ ✓.
:::

:::solution 4) $\arcsin\left(\cos\left(3x - \frac{\pi}{4}\right)\right) = 2x$
**Условие на правую часть:** $2x \in \left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$ ⇔ $|x| \le \frac{\pi}{4}$. При нём уравнение ⇔ $\sin2x = \cos\left(3x - \frac{\pi}{4}\right)$, то есть $\cos\left(\frac{\pi}{2} - 2x\right) = \cos\left(3x - \frac{\pi}{4}\right)$:
- $3x - \frac{\pi}{4} = \frac{\pi}{2} - 2x + 2\pi k$ ⇒ $x = \frac{3\pi}{20} + \frac{2\pi k}{5}$: подходят $\frac{3\pi}{20}$ и $-\frac{\pi}{4}$ ($k = -1$);
- $3x - \frac{\pi}{4} = -\frac{\pi}{2} + 2x + 2\pi k$ ⇒ $x = -\frac{\pi}{4} + 2\pi k$: подходит $-\frac{\pi}{4}$.

**Ответ:** $x = -\frac{\pi}{4}$, $x = \frac{3\pi}{20}$.
:::

:::solution 5) $\arccos\left(\cos\left(\frac{\pi}{4} - 4\pi x\right)\right) = \pi - \arcsin\left(\sin\left(2\pi x + \frac{\pi}{4}\right)\right)$
**Шаг 1. Диапазоны.** Слева $[0; \pi]$, справа $\left[\frac{\pi}{2}; \frac{3\pi}{2}\right]$. Пусть $v = 2\pi x + \frac{\pi}{4}$, $w = \arcsin(\sin v)$. Правая часть $\pi - w$ должна быть $\le \pi$ ⇒ $w \in \left[0; \frac{\pi}{2}\right]$.

**Шаг 2.** Левый аргумент: $\frac{\pi}{4} - 4\pi x = \frac{3\pi}{4} - 2v$. Так как $\pi - w \in [0; \pi]$, равенство ⇔ $\cos\left(2v - \frac{3\pi}{4}\right) = \cos(\pi - w)$.

**Шаг 3.** $\sin v = \sin w$ ⇒ $v = w + 2\pi k$ или $v = \pi - w + 2\pi k$. Подставляем и решаем относительно $w \in \left[0; \frac{\pi}{2}\right]$:
- $v = w + 2\pi k$: $\cos\left(2w - \frac{3\pi}{4}\right) = \cos(\pi - w)$ даёт $w = \frac{7\pi}{12} + \frac{2\pi m}{3}$ или $w = -\frac{\pi}{4} + 2\pi m$ — ни одно не попадает в $\left[0; \frac{\pi}{2}\right]$.
- $v = \pi - w + 2\pi k$: $\cos\left(\frac{5\pi}{4} - 2w\right) = \cos(\pi - w)$ даёт $w = \frac{\pi}{4}$ или $w = \frac{\pi}{12}$.

**Шаг 4. Назад к $x$:**
- $w = \frac{\pi}{4}$: $v = \frac{3\pi}{4} + 2\pi k$ ⇒ $2\pi x = \frac{\pi}{2} + 2\pi k$ ⇒ $x = \frac14 + k$;
- $w = \frac{\pi}{12}$: $v = \frac{11\pi}{12} + 2\pi k$ ⇒ $2\pi x = \frac{2\pi}{3} + 2\pi k$ ⇒ $x = \frac13 + k$.

**Ответ:** $x = \frac14 + k$, $x = \frac13 + k$, $k \in \mathbb Z$. (Проверено численно: других корней нет.)
:::

## 15. Упростить $\arcsin x + \arcsin y - \arcsin\left(xy - \sqrt{1 - x^2}\sqrt{1 - y^2}\right)$, $x, y \in [0; 1]$

:::solution Решение
$\alpha = \arcsin x$, $\beta = \arcsin y \in \left[0; \frac{\pi}{2}\right]$, $\cos\alpha = \sqrt{1 - x^2}$, $\cos\beta = \sqrt{1 - y^2}$.
$xy - \sqrt{1 - x^2}\sqrt{1 - y^2} = \sin\alpha\sin\beta - \cos\alpha\cos\beta = -\cos(\alpha + \beta)$.
$\arcsin(-\cos(\alpha + \beta)) = -\left(\frac{\pi}{2} - \arccos(\cos(\alpha + \beta))\right) = \alpha + \beta - \frac{\pi}{2}$ (так как $\alpha + \beta \in [0; \pi]$).

**Ответ:** $\alpha + \beta - \left(\alpha + \beta - \frac{\pi}{2}\right) = \frac{\pi}{2}$.
:::

## 16–17

:::solution 16. $\arctan(\sqrt2 - 1) = \frac{\pi}{8}$
$\tan\frac{\pi}{8} = \frac{1 - \cos\frac{\pi}{4}}{\sin\frac{\pi}{4}} = \sqrt2 - 1$, и $\frac{\pi}{8}$ лежит в главном диапазоне арктангенса ∎
:::

:::solution 17. Сравнить $\arctan(\sqrt2 + \sqrt3) + \text{arccot}(\sqrt2 - \sqrt3)$ и $\frac{5\sqrt7}{3}$
Пусть $a = \sqrt3 + \sqrt2$, $b = \sqrt3 - \sqrt2$; $ab = 3 - 2 = 1$.
$\text{arccot}(\sqrt2 - \sqrt3) = \text{arccot}(-b) = \pi - \text{arccot}\,b = \pi - \arctan\frac1b = \pi - \arctan a$ (для $b > 0$ $\text{arccot}\,b = \arctan\frac1b$).
Сумма $= \arctan a + \pi - \arctan a = \pi$.
$\sqrt7 > 2{,}6$ (так как $2{,}6^2 = 6{,}76$) ⇒ $\frac{5\sqrt7}{3} > \frac{13}{3} > 4 > \pi$.

**Ответ:** $\frac{5\sqrt7}{3}$ больше.
:::
