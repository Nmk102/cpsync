---
title: "Trigonometry: mixed practice — решения A1–E5 и бонусов P1, P2"
kind: solutions
units: []
tasks: [49170921, 49321380]
order: 52
summary: Уравнения, неравенства, системы с двумя переменными, обратные функции, точные значения, два параметра. Каждый ответ проверен численно.
---

Многие задачи этого листка повторяются в Summative preparation. Там, где задача та же, я даю ссылку и короткий ответ.

:::key Приёмы, которые встречаются в этом листке
1. **Произведение ↔ сумма**: $\sin a\sin b = \frac12(\cos(a - b) - \cos(a + b))$, $\sin a + \sin b = 2\sin\frac{a + b}{2}\cos\frac{a - b}{2}$.
2. **Вспомогательный угол**: $a\sin x + b\cos x = \sqrt{a^2 + b^2}\,\sin(x + \varphi)$.
3. **Оценка**: если левая часть $\ge 8$, а правая $\le 8$, то равенство возможно только когда обе равны 8 (задача C5).
4. **Система с $\sin x\cos y$ и $\cos x\sin y$**: складываем и вычитаем — получаем $\sin(x \pm y)$.
5. **ОДЗ** — в начале решения, проверка — в конце.
:::

## A. Уравнения

:::solution A1. $\sin x\sin7x = \sin3x\sin5x$
Та же задача, что 6(d) в Summative preparation. Произведения в суммы: $\cos6x - \cos8x = \cos2x - \cos8x$ ⇒ $\cos6x = \cos2x$ ⇒ $-2\sin4x\sin2x = 0$.

**Ответ:** $x = \frac{\pi k}{4}$, $k \in \mathbb Z$.
:::

:::solution A2. $\tan x + 8|\cot x| + \cot2x = 0$
**ОДЗ:** $\sin x \ne 0$, $\cos x \ne 0$ (иначе не определены tan, cot или cot 2x) ⇒ $x \ne \frac{\pi k}{2}$.

**Шаг 1.** Выразим $\cot2x$ через $c = \cot x$:
$$\cot2x = \frac{\cot^2x - 1}{2\cot x} = \frac{c}{2} - \frac{1}{2c}.$$
Тогда $\tan x + \cot2x = \frac1c + \frac c2 - \frac{1}{2c} = \frac{1}{2c} + \frac{c}{2} = \frac{c^2 + 1}{2c}$.

**Шаг 2.** Уравнение: $\frac{c^2 + 1}{2c} + 8|c| = 0$.
- Если $c > 0$, оба слагаемых положительны — решений нет.
- Если $c < 0$, $|c| = -c$: $\frac{c^2 + 1}{2c} = 8c$ ⇒ $c^2 + 1 = 16c^2$ ⇒ $c^2 = \frac{1}{15}$ ⇒ $c = -\frac{1}{\sqrt{15}}$.

**Шаг 3.** $\cot x = -\frac{1}{\sqrt{15}}$ ⇔ $\tan x = -\sqrt{15}$.

**Ответ:** $x = -\arctan\sqrt{15} + \pi k$, $k \in \mathbb Z$.
:::

:::solution A3. $1 - \sin(3\pi + x) = \cot(\pi + x) + \sin\left(\frac{\pi}{2} + x\right)$
**Формулы приведения:** $\sin(3\pi + x) = -\sin x$, $\cot(\pi + x) = \cot x$, $\sin\left(\frac{\pi}{2} + x\right) = \cos x$.
$$1 + \sin x = \frac{\cos x}{\sin x} + \cos x,\qquad \text{ОДЗ: } \sin x \ne 0.$$
Умножаем на $\sin x$ и группируем:
$$\sin x + \sin^2x - \cos x - \sin x\cos x = 0 \iff (\sin x - \cos x) + \sin x(\sin x - \cos x) = 0 \iff (\sin x - \cos x)(1 + \sin x) = 0.$$
- $\sin x = \cos x$ ⇒ $\tan x = 1$ ⇒ $x = \frac{\pi}{4} + \pi k$;
- $\sin x = -1$ ⇒ $x = -\frac{\pi}{2} + 2\pi k$.

В обеих сериях $\sin x \ne 0$ ✓.

**Ответ:** $x = \frac{\pi}{4} + \pi k$, $x = -\frac{\pi}{2} + 2\pi k$.
:::

:::solution A4. $\sqrt{\sin3x + \sin5x} = \sqrt{\sin4x}$
Равенство корней ⇔ подкоренные выражения равны **и** неотрицательны. Достаточно требовать $\sin4x \ge 0$ (второе подкоренное ему равно).

$\sin3x + \sin5x = 2\sin4x\cos x$, поэтому $2\sin4x\cos x = \sin4x$ ⇔ $\sin4x\,(2\cos x - 1) = 0$.
- $\sin4x = 0$ ⇒ $x = \frac{\pi k}{4}$. Условие $\sin4x = 0 \ge 0$ выполнено ✓.
- $\cos x = \frac12$ ⇒ $x = \pm\frac{\pi}{3} + 2\pi k$. Проверяем $\sin4x \ge 0$:
  - $x = \frac{\pi}{3}$: $\sin\frac{4\pi}{3} = -\frac{\sqrt3}{2} < 0$ — **не подходит**;
  - $x = -\frac{\pi}{3}$: $\sin\left(-\frac{4\pi}{3}\right) = \frac{\sqrt3}{2} > 0$ — подходит.

**Ответ:** $x = \frac{\pi k}{4}$, $x = -\frac{\pi}{3} + 2\pi k$.
:::

:::solution A5. $\sin6x + \cos6x\cot3x = \sqrt3$
**ОДЗ:** $\sin3x \ne 0$. Приводим к общему знаменателю:
$$\frac{\sin6x\sin3x + \cos6x\cos3x}{\sin3x} = \frac{\cos(6x - 3x)}{\sin3x} = \cot3x.$$
$\cot3x = \sqrt3$ ⇒ $3x = \frac{\pi}{6} + \pi k$.

**Ответ:** $x = \frac{\pi}{18} + \frac{\pi k}{3}$.
:::

## B. Неравенства

:::solution B1. $\sqrt{\sin^2\left(\frac{\pi}{3} - 3x\right)} < \sqrt{0{,}75}$
$\sqrt{a^2} = |a|$, $\sqrt{0{,}75} = \frac{\sqrt3}{2}$: $\left|\sin\left(3x - \frac{\pi}{3}\right)\right| < \frac{\sqrt3}{2}$.
Для $t = 3x - \frac{\pi}{3}$: $|\sin t| < \frac{\sqrt3}{2}$ ⇔ $t \in \left(-\frac{\pi}{3} + \pi k;\ \frac{\pi}{3} + \pi k\right)$ (на единичной окружности — две дуги около 0 и около π).
$$3x \in \left(\pi k;\ \frac{2\pi}{3} + \pi k\right)\ \Rightarrow\ x \in \left(\frac{\pi k}{3};\ \frac{2\pi}{9} + \frac{\pi k}{3}\right).$$
:::

:::solution B2. $2\cos\left(\frac{\pi}{3} - x\right) - \sqrt3 < 0$ и $\tan x \ge -1$
**Первое:** $\cos\left(x - \frac{\pi}{3}\right) < \frac{\sqrt3}{2}$. Неравенство нарушается только при $x - \frac{\pi}{3} \in \left[-\frac{\pi}{6}; \frac{\pi}{6}\right]$, то есть при $x \in \left[\frac{\pi}{6}; \frac{\pi}{2}\right] + 2\pi k$.

**Второе:** $\tan x \ge -1$ ⇔ $x \in \left[-\frac{\pi}{4}; \frac{\pi}{2}\right) + \pi n$. На периоде $2\pi$ это два куска: $\left[-\frac{\pi}{4}; \frac{\pi}{2}\right)$ и $\left[\frac{3\pi}{4}; \frac{3\pi}{2}\right)$.

**Пересечение:** из первого куска выбрасываем $\left[\frac{\pi}{6}; \frac{\pi}{2}\right)$, второй кусок не задевается.

**Ответ:** $x \in \left[-\frac{\pi}{4} + 2\pi k;\ \frac{\pi}{6} + 2\pi k\right) \cup \left[\frac{3\pi}{4} + 2\pi k;\ \frac{3\pi}{2} + 2\pi k\right)$.
:::

:::solution B3. $\sqrt2\sin x < 2 - \sqrt2\cos x$
Та же задача, что 7(b) в Summative preparation, но на всей прямой: $\sin\left(x + \frac{\pi}{4}\right) < 1$.

**Ответ:** все $x$, кроме $x = \frac{\pi}{4} + 2\pi k$.
:::

:::solution B4. $2\sin2x + 3\tan x \le 5$
**ОДЗ:** $\cos x \ne 0$. Пусть $t = \tan x$, тогда $\sin2x = \frac{2t}{1 + t^2}$:
$$\frac{4t}{1 + t^2} + 3t \le 5 \iff 4t + 3t(1 + t^2) \le 5(1 + t^2) \iff 3t^3 - 5t^2 + 7t - 5 \le 0$$
(умножили на $1 + t^2 > 0$ — знак не меняется).
$t = 1$ — корень: $3 - 5 + 7 - 5 = 0$. Делим: $3t^3 - 5t^2 + 7t - 5 = (t - 1)(3t^2 - 2t + 5)$. У второй скобки дискриминант $4 - 60 < 0$, она всегда положительна. Значит, $t \le 1$.

**Ответ:** $\tan x \le 1$ ⇔ $x \in \left(-\frac{\pi}{2} + \pi k;\ \frac{\pi}{4} + \pi k\right]$.
:::

:::solution B5. $\sin^6x + \cos^6x \ge \frac58$
$\sin^6x + \cos^6x = 1 - \frac34\sin^22x = 1 - \frac38(1 - \cos4x) = \frac58 + \frac38\cos4x$.
Неравенство ⇔ $\cos4x \ge 0$ ⇔ $4x \in \left[-\frac{\pi}{2} + 2\pi k; \frac{\pi}{2} + 2\pi k\right]$.

**Ответ:** $x \in \left[-\frac{\pi}{8} + \frac{\pi k}{2};\ \frac{\pi}{8} + \frac{\pi k}{2}\right]$.
:::

## C. Уравнения и системы с двумя переменными

:::solution C1. $\cos x + \cos y = 0{,}5$, $\sin^2y + \sin^2x = 1{,}75$
Из второго: $\cos^2x + \cos^2y = 2 - 1{,}75 = 0{,}25$.
Возводим первое в квадрат: $\cos^2x + \cos^2y + 2\cos x\cos y = 0{,}25$ ⇒ $\cos x\cos y = 0$.
- $\cos x = 0$, тогда $\cos y = 0{,}5$;
- $\cos y = 0$, тогда $\cos x = 0{,}5$.

**Ответ:** $\left(\frac{\pi}{2} + \pi k;\ \pm\frac{\pi}{3} + 2\pi n\right)$ и $\left(\pm\frac{\pi}{3} + 2\pi k;\ \frac{\pi}{2} + \pi n\right)$, $k, n \in \mathbb Z$.
:::

:::solution C2. $y - x = -\frac{\pi}{3}$, $\sin x = 2\sin y$
Подставляем $y = x - \frac{\pi}{3}$:
$$\sin x = 2\left(\sin x\cdot\frac12 - \cos x\cdot\frac{\sqrt3}{2}\right) = \sin x - \sqrt3\cos x\ \Rightarrow\ \cos x = 0.$$
**Ответ:** $x = \frac{\pi}{2} + \pi k$, $y = \frac{\pi}{6} + \pi k$ (с **одним и тем же** $k$).
:::

:::solution C3. $\sqrt{\cos2x}\,\cos x = 0$, $2\sin^2x - \cos\left(2y - \frac{\pi}{3}\right) = 0$
**Первое уравнение**, ОДЗ $\cos2x \ge 0$. Либо $\cos2x = 0$, либо $\cos x = 0$. Но при $\cos x = 0$ получаем $\cos2x = 2\cos^2x - 1 = -1 < 0$ — вне ОДЗ. Значит, $\cos2x = 0$: $x = \frac{\pi}{4} + \frac{\pi k}{2}$.

**Второе.** При $\cos2x = 0$: $2\sin^2x = 1 - \cos2x = 1$. Тогда $\cos\left(2y - \frac{\pi}{3}\right) = 1$ ⇒ $2y - \frac{\pi}{3} = 2\pi n$ ⇒ $y = \frac{\pi}{6} + \pi n$.

**Ответ:** $\left(\frac{\pi}{4} + \frac{\pi k}{2};\ \frac{\pi}{6} + \pi n\right)$.
:::

:::solution C4. $\cos y\sin x = -0{,}5$, $\cos x\sin y = 0{,}5$
Складываем: $\sin(x + y) = 0$. Вычитаем (первое минус второе): $\sin(x - y) = -1$.
$$x + y = \pi m,\qquad x - y = -\frac{\pi}{2} + 2\pi k.$$
Отсюда $x = -\frac{\pi}{4} + \frac{\pi m}{2} + \pi k$, $y = \frac{\pi}{4} + \frac{\pi m}{2} - \pi k$. Удобнее записать так:

**Ответ:** $x = -\frac{\pi}{4} + \frac{\pi n}{2}$, $y = \frac{\pi}{4} + \frac{\pi n}{2} + 2\pi k$, $n, k \in \mathbb Z$. На $[0; 2\pi)^2$ это 4 пары: $\left(\frac{\pi}{4}; \frac{3\pi}{4}\right)$, $\left(\frac{3\pi}{4}; \frac{5\pi}{4}\right)$, $\left(\frac{5\pi}{4}; \frac{7\pi}{4}\right)$, $\left(\frac{7\pi}{4}; \frac{\pi}{4}\right)$.
:::

:::solution C5. $\left(5 + \frac{3}{\sin^2x}\right)(2 - \sin^6x) = 7 + \cos2y$
**Идея — оценка.** Пусть $u = \sin^2x \in (0; 1]$ (ноль исключён — деление).
- $5 + \frac{3}{u} \ge 5 + 3 = 8$, равенство только при $u = 1$;
- $2 - u^3 \ge 1$, равенство только при $u = 1$.

Значит, левая часть $\ge 8$. Правая $7 + \cos2y \le 8$. Равенство ⇔ обе части равны 8 ⇔ $\sin^2x = 1$ и $\cos2y = 1$.

**Ответ:** $x = \frac{\pi}{2} + \pi k$, $y = \pi n$.
:::

## D. Обратные тригонометрические функции

:::solution D1. $\cot\left(\frac14\left[\arctan\sqrt3 + \arccos\left(-\frac12\right)\right]\right)$
$\arctan\sqrt3 = \frac{\pi}{3}$, $\arccos\left(-\frac12\right) = \frac{2\pi}{3}$. Сумма π, четверть — $\frac{\pi}{4}$, $\cot\frac{\pi}{4} = 1$.
:::

:::solution D2. $\arccos(2x^2 - 1) = \arccos(3x + 1)$
Задача 9(a) из Summative preparation. **Ответ:** $x = -\frac12$ ($x = 2$ посторонний: $3x + 1 = 7 \notin [-1; 1]$).
:::

:::solution D3. $\arccos\left(\cos\frac{8\pi}{5}\right)$
$\frac{8\pi}{5} \notin [0; \pi]$, поэтому ответ не $\frac{8\pi}{5}$. $\cos\frac{8\pi}{5} = \cos\left(2\pi - \frac{8\pi}{5}\right) = \cos\frac{2\pi}{5}$, и $\frac{2\pi}{5} \in [0; \pi]$.

**Ответ:** $\frac{2\pi}{5}$.
:::

:::solution D4. $\cot\left(2\arcsin\frac35\right)$
Задача 8(c) из Summative preparation: $\frac{7}{24}$.
:::

:::solution D5. $\tan\left(\arcsin\left(-\frac35\right) + \arccos\left(-\frac{1}{\sqrt2}\right)\right)$
$A = \arcsin\left(-\frac35\right) \in \left(-\frac{\pi}{2}; 0\right)$: $\cos A = \frac45$, $\tan A = -\frac34$.
$B = \arccos\left(-\frac{1}{\sqrt2}\right) = \frac{3\pi}{4}$, $\tan B = -1$.
$$\tan(A + B) = \frac{-\frac34 - 1}{1 - \left(-\frac34\right)(-1)} = \frac{-\frac74}{\frac14} = -7.$$
:::

## E. Значения выражений

:::solution E1. $3(\sin^4x - \cos^4x)$, если $\tan\frac{x}{2} = 2$
$\sin x = \frac{2\cdot2}{1 + 4} = \frac45$, $\cos x = \frac{1 - 4}{1 + 4} = -\frac35$.
$\sin^4x - \cos^4x = \sin^2x - \cos^2x = \frac{16 - 9}{25} = \frac{7}{25}$. **Ответ:** $\frac{21}{25}$.
:::

:::solution E2. $\dfrac{\cos^239^\circ - \sin^221^\circ}{\cos162^\circ}$
Полезное тождество: $\cos^2a - \sin^2b = \cos(a + b)\cos(a - b)$.
Числитель $= \cos60^\circ\cos18^\circ = \frac12\cos18^\circ$, знаменатель $\cos162^\circ = -\cos18^\circ$.

**Ответ:** $-\frac12$.
:::

:::solution E3. $\dfrac{\cos40^\circ - \sqrt3\sin40^\circ}{\sin190^\circ}$
Числитель $= 2\left(\frac12\cos40^\circ - \frac{\sqrt3}{2}\sin40^\circ\right) = 2\cos(40^\circ + 60^\circ) = 2\cos100^\circ = -2\sin10^\circ$.
Знаменатель $\sin190^\circ = -\sin10^\circ$.

**Ответ:** 2.
:::

:::solution E4. $6\sqrt2\left(\sin28^\circ\sin17^\circ - \frac12\sin79^\circ\right)$
$\sin28^\circ\sin17^\circ = \frac12(\cos11^\circ - \cos45^\circ)$, а $\sin79^\circ = \cos11^\circ$. В скобке остаётся $-\frac12\cos45^\circ = -\frac{\sqrt2}{4}$.

**Ответ:** $6\sqrt2\cdot\left(-\frac{\sqrt2}{4}\right) = -3$.
:::

:::solution E5. Сколько целых значений принимает $y = 10\sqrt{3\cos x - 4\sin x + 4{,}8}$?
$3\cos x - 4\sin x \in [-5; 5]$ (вспомогательный угол, $\sqrt{9 + 16} = 5$). Подкоренное $\in [-0{,}2; 9{,}8]$, но корень существует только при подкоренном $\ge 0$: $[0; 9{,}8]$.
$y \in \left[0; 10\sqrt{9{,}8}\right] = \left[0; \sqrt{980}\right]$, $31^2 = 961 < 980 < 1024 = 32^2$.

**Ответ:** целые $0, 1, \ldots, 31$ — **32 значения**.
:::

:::warn Сравните с задачей 5 из Summative preparation
Там подкоренное $\ge 0$ при всех $x$. Здесь — нет: при некоторых $x$ корень не определён. Ответ от этого не меняется, но упомянуть это нужно.
:::

## Бонус: параметры

:::solution P1. $\sqrt{x - a}\sin x = \sqrt{x - a}\cos x$ — ровно одно решение на $[0; \pi]$
Задача 11 из Summative preparation (там подробная таблица). **Ответ:** $a \in (-\infty; 0) \cup \left[\frac{\pi}{4}; \pi\right]$.
:::

:::solution P2. $|3\sin x + a^2 - 22| + |7\sin x + a + 12| \le 11\sin x + |a^2 + a - 20| + 11$ при всех $x$
**Замена.** Пусть $d = \sin x + 1 \in [0; 2]$. Тогда
$$3\sin x + a^2 - 22 = (a^2 - 25) + 3d = A + 3d,\qquad 7\sin x + a + 12 = (a + 5) + 7d = B + 7d,$$
где $A = a^2 - 25$, $B = a + 5$. Заметим: $A + B = a^2 + a - 20$, а $11\sin x + 11 = 11d$. Неравенство:
$$|A + 3d| + |B + 7d| \le |A + B| + 11d\quad\text{для всех } d \in [0; 2].$$

**Необходимое условие ($d = 0$, то есть $\sin x = -1$):** $|A| + |B| \le |A + B|$. Но всегда $|A| + |B| \ge |A + B|$, поэтому нужно равенство, а оно бывает, только когда $A$ и $B$ одного знака (или один из них 0):
$$AB = (a - 5)(a + 5)^2 \ge 0 \iff a \ge 5\ \text{или}\ a = -5.$$

**Достаточность.**
- $a \ge 5$: $A \ge 0$, $B > 0$, все модули раскрываются с плюсом: $A + B + 10d \le A + B + 11d$ ⇔ $d \ge 0$ ✓.
- $a = -5$: $A = B = 0$: $10d \le 11d$ ✓.

**Ответ:** $a \in \{-5\} \cup [5; +\infty)$.

*Проверка компьютером:* перебор $a$ от −15 до 15 с шагом 0,01 и $\sin x$ от −1 до 1 — неравенство выполняется ровно при $a = -5$ и $a \ge 5$ ✓.
:::
