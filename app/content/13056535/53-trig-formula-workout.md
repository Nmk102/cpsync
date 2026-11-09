---
title: "Trigonometry: Formula Workout — заполненный лист формул и решения 1–7"
kind: solutions
units: []
tasks: [48832703, 49321380]
order: 53
summary: Все формулы из блока 0 (лист формул к summative), формулы приведения, суммы ↔ произведения, понижение степени, универсальная подстановка, олимпиадные произведения косинусов. Всё проверено численно.
---

## 0. Лист формул (его можно брать на summative)

:::formula Сложение и вычитание
$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta,\qquad \cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta,$$
$$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}.$$
:::

:::formula Двойной угол и понижение степени
$$\sin2\alpha = 2\sin\alpha\cos\alpha,\quad \cos2\alpha = \cos^2\alpha - \sin^2\alpha = 1 - 2\sin^2\alpha = 2\cos^2\alpha - 1,\quad \tan2\alpha = \frac{2\tan\alpha}{1 - \tan^2\alpha},$$
$$\sin^2\alpha = \frac{1 - \cos2\alpha}{2},\qquad \cos^2\alpha = \frac{1 + \cos2\alpha}{2}.$$
:::

:::formula Суммы ↔ произведения
$$\sin u + \sin v = 2\sin\frac{u + v}{2}\cos\frac{u - v}{2},\qquad \sin u - \sin v = 2\cos\frac{u + v}{2}\sin\frac{u - v}{2},$$
$$\cos u + \cos v = 2\cos\frac{u + v}{2}\cos\frac{u - v}{2},\qquad \cos u - \cos v = -2\sin\frac{u + v}{2}\sin\frac{u - v}{2},$$
$$\sin u\sin v = \tfrac12\big(\cos(u - v) - \cos(u + v)\big),\quad \cos u\cos v = \tfrac12\big(\cos(u - v) + \cos(u + v)\big),\quad \sin u\cos v = \tfrac12\big(\sin(u + v) + \sin(u - v)\big).$$
$$(*)\quad \sin x + \cos x = \sqrt2\sin\left(x + \frac{\pi}{4}\right).$$
:::

:::formula Универсальная подстановка $t = \tan\frac{x}{2}$
$$\sin x = \frac{2t}{1 + t^2},\qquad \cos x = \frac{1 - t^2}{1 + t^2},\qquad \tan x = \frac{2t}{1 - t^2}.$$
Вывод — в задаче 6(a).
:::

:::tip Как запомнить знак в $\cos u - \cos v$
Проверьте на числах: $u = 0$, $v = \pi$. Слева $1 - (-1) = 2$. Справа $-2\sin\frac{\pi}{2}\sin\left(-\frac{\pi}{2}\right) = 2$ ✓. Без минуса получилось бы −2.
:::

## 1. Формулы приведения и точные значения

:::solution (a) $\sin\left(\frac{13\pi}{6} - x\right) + \cos\left(\frac{5\pi}{3} + x\right)$
Убираем полные обороты: $\frac{13\pi}{6} = 2\pi + \frac{\pi}{6}$, $\frac{5\pi}{3} = 2\pi - \frac{\pi}{3}$.
$$\sin\left(\frac{\pi}{6} - x\right) + \cos\left(x - \frac{\pi}{3}\right) = \left(\frac12\cos x - \frac{\sqrt3}{2}\sin x\right) + \left(\frac12\cos x + \frac{\sqrt3}{2}\sin x\right) = \cos x.$$
:::

:::solution (b) $\dfrac{\sin(3\pi - \alpha)\cos\left(\frac{3\pi}{2} + \alpha\right)}{\cos(2\pi - \alpha)\sin\left(\frac{\pi}{2} - \alpha\right)}$
Правило: при $\pi$, $2\pi$ функция не меняется; при $\frac{\pi}{2}$, $\frac{3\pi}{2}$ меняется на «кофункцию»; знак — по четверти, считая α острым.
- $\sin(3\pi - \alpha) = \sin\alpha$ (II четверть, синус +);
- $\cos\left(\frac{3\pi}{2} + \alpha\right) = \sin\alpha$ (IV четверть, косинус +);
- $\cos(2\pi - \alpha) = \cos\alpha$, $\sin\left(\frac{\pi}{2} - \alpha\right) = \cos\alpha$.

**Ответ:** $\frac{\sin^2\alpha}{\cos^2\alpha} = \tan^2\alpha$.
:::

:::solution (c) $\sin75^\circ\cos15^\circ - \cos75^\circ\sin15^\circ$ и (d) $\cos105^\circ\cos15^\circ + \sin105^\circ\sin15^\circ$
(c) $= \sin(75^\circ - 15^\circ) = \sin60^\circ = \frac{\sqrt3}{2}$.
(d) $= \cos(105^\circ - 15^\circ) = \cos90^\circ = 0$.
:::

## 2. Сложение и двойной угол

:::solution (a) $\sin\alpha = \frac35$, $\alpha \in \left(\frac{\pi}{2}; \pi\right)$
$\cos\alpha = -\frac45$ (II четверть).
$$\sin2\alpha = 2\cdot\frac35\cdot\left(-\frac45\right) = -\frac{24}{25},\quad \cos2\alpha = 1 - 2\cdot\frac{9}{25} = \frac{7}{25},\quad \tan2\alpha = -\frac{24}{7}.$$
:::

:::solution (b) $\dfrac{\sin3x + \sin x}{\cos3x + \cos x}$ и (c) $\dfrac{1 - \cos4x}{\sin4x}$
(b) $\frac{2\sin2x\cos x}{2\cos2x\cos x} = \tan2x$.
(c) $\frac{2\sin^22x}{2\sin2x\cos2x} = \tan2x$.
:::

:::solution (d) $\dfrac{\sin(x + y)\sin(x - y)}{\cos^2x - \sin^2y}$
Два полезных тождества (раскройте скобки — проверите):
$$\sin(x + y)\sin(x - y) = \sin^2x - \sin^2y,\qquad \cos(x + y)\cos(x - y) = \cos^2x - \sin^2y.$$
Второе — это как раз знаменатель. **Ответ:** $\tan(x + y)\tan(x - y)$.
:::

## 3. Суммы и произведения

:::solution (a)–(e)
- (a) $\sin\alpha + \sin7\alpha = 2\sin4\alpha\cos3\alpha$.
- (b) $\cos11\alpha - \cos3\alpha = -2\sin7\alpha\sin4\alpha$.
- (c) $\sin\alpha + \sin5\alpha + 2\cos2\alpha = 2\sin3\alpha\cos2\alpha + 2\cos2\alpha = 2\cos2\alpha(1 + \sin3\alpha)$. Можно дальше: $1 + \sin3\alpha = 2\sin^2\left(\frac{3\alpha}{2} + \frac{\pi}{4}\right)$, итог $4\cos2\alpha\sin^2\left(\frac{3\alpha}{2} + \frac{\pi}{4}\right)$.
- (d) Группируем «крайние» и «средние»: $(\cos\alpha + \cos11\alpha) - (\cos3\alpha + \cos9\alpha) = 2\cos6\alpha\cos5\alpha - 2\cos6\alpha\cos3\alpha = 2\cos6\alpha(\cos5\alpha - \cos3\alpha) = -4\cos6\alpha\sin4\alpha\sin\alpha$.
- (e) $2\sin7x\sin3x = \cos4x - \cos10x$.
:::

:::solution (f) $4\cos x\cos2x\cos4x$
**Как сумма:** $4\cos x\cos2x\cos4x = 2(\cos x + \cos3x)\cos4x = \cos3x + \cos5x + \cos x + \cos7x$.

**Как одна дробь** (трюк «умножить на синус»): при $\sin x \ne 0$
$$8\sin x\cos x\cos2x\cos4x = 4\sin2x\cos2x\cos4x = 2\sin4x\cos4x = \sin8x\ \Rightarrow\ 4\cos x\cos2x\cos4x = \frac{\sin8x}{2\sin x}.$$
:::

:::key Трюк «умножить на синус»
Произведение косинусов удвоенных углов $\cos x\cos2x\cos4x\cdots\cos2^{n-1}x$ умножаем на $\sin x$ — и формула двойного угла «схлопывает» его по цепочке:
$$\cos x\cos2x\cdots\cos2^{n-1}x = \frac{\sin2^nx}{2^n\sin x}.$$
Этим решаются 3(g), 3(h), 7(a), 7(b).
:::

:::solution (g) $\sin10^\circ\cos20^\circ\cos40^\circ$
$\sin10^\circ = \cos80^\circ$. Произведение $\cos20^\circ\cos40^\circ\cos80^\circ$ — цепочка удвоений, $n = 3$:
$$\frac{\sin160^\circ}{8\sin20^\circ} = \frac{\sin20^\circ}{8\sin20^\circ} = \frac18.$$
:::

:::solution (h) $\cos\frac{\pi}{7}\cos\frac{2\pi}{7}\cos\frac{3\pi}{7}$
$\cos\frac{3\pi}{7} = -\cos\frac{4\pi}{7}$ (формула приведения). Получаем цепочку удвоений со знаком минус:
$$-\cos\frac{\pi}{7}\cos\frac{2\pi}{7}\cos\frac{4\pi}{7} = -\frac{\sin\frac{8\pi}{7}}{8\sin\frac{\pi}{7}} = -\frac{-\sin\frac{\pi}{7}}{8\sin\frac{\pi}{7}} = \frac18.$$
:::

:::solution (i) $\sin\frac{\pi}{7}\sin\frac{2\pi}{7}\sin\frac{3\pi}{7}$
Обозначим $Q$ и найдём $Q^2$. По формуле понижения степени $\sin^2\frac{k\pi}{7} = \frac{1 - c_k}{2}$, где $c_1 = \cos\frac{2\pi}{7}$, $c_2 = \cos\frac{4\pi}{7}$, $c_3 = \cos\frac{6\pi}{7}$:
$$Q^2 = \frac18(1 - c_1)(1 - c_2)(1 - c_3) = \frac18\big(1 - (c_1 + c_2 + c_3) + (c_1c_2 + c_2c_3 + c_3c_1) - c_1c_2c_3\big).$$
- **Сумма:** $c_1 + c_2 + c_3 = -\frac12$. Доказательство: умножим на $2\sin\frac{\pi}{7}$, каждое слагаемое $2\sin\frac{\pi}{7}\cos\frac{2k\pi}{7} = \sin\frac{(2k + 1)\pi}{7} - \sin\frac{(2k - 1)\pi}{7}$ — сумма «телескопируется» в $\sin\pi - \sin\frac{\pi}{7} = -\sin\frac{\pi}{7}$.
- **Попарные произведения:** $c_1c_2 = \frac12(c_3 + c_1)$, $c_2c_3 = \frac12(c_2 + c_1)$, $c_3c_1 = \frac12(c_3 + c_2)$ (произведение в сумму, плюс $\cos\frac{8\pi}{7} = c_3$, $\cos\frac{10\pi}{7} = c_2$). В сумме $c_1 + c_2 + c_3 = -\frac12$.
- **Произведение:** $c_1c_2c_3 = \cos\frac{2\pi}{7}\cos\frac{4\pi}{7}\left(-\cos\frac{\pi}{7}\right) = -\left(-\frac18\right) = \frac18$ (из пункта (h)).

$$Q^2 = \frac18\left(1 + \frac12 - \frac12 - \frac18\right) = \frac{7}{64},\qquad Q = \frac{\sqrt7}{8}\ (Q > 0).$$
:::

## 4. Понижение степени и симметричные выражения

:::solution (a) $\sin^4x + \cos^4x$ через $\cos4x$ и (b) $\sin^6x + \cos^6x$
(a) $= 1 - 2\sin^2x\cos^2x = 1 - \frac12\sin^22x = 1 - \frac14(1 - \cos4x) = \frac34 + \frac14\cos4x$.
(b) $= (\sin^2x + \cos^2x)^3 - 3\sin^2x\cos^2x = 1 - \frac34\sin^22x = \frac58 + \frac38\cos4x$.
:::

:::solution (c) $\sin x + \cos x = -\frac12$
Квадрат: $1 + 2\sin x\cos x = \frac14$ ⇒ $\sin x\cos x = -\frac38$.
$\sin^3x + \cos^3x = (\sin x + \cos x)(1 - \sin x\cos x) = -\frac12\cdot\frac{11}{8} = -\frac{11}{16}$.
:::

:::solution (d) $\tan x + \cot x = 3$
$\tan x + \cot x = \frac{\sin^2x + \cos^2x}{\sin x\cos x} = \frac{1}{\sin x\cos x}$ ⇒ $p = \sin x\cos x = \frac13$.
$\sin^4x + \cos^4x = 1 - 2p^2 = \frac79$, $\sin^6x + \cos^6x = 1 - 3p^2 = \frac23$.
:::

## 5. Выбери формулу сам

:::solution (a)–(d)
- (a) $\dfrac{\sin5x - \sin x}{\cos x - \cos5x} = \dfrac{2\cos3x\sin2x}{2\sin3x\sin2x} = \cot3x$.
- (b) $\dfrac{\cos2x - \cos6x}{\sin2x + \sin6x} = \dfrac{2\sin4x\sin2x}{2\sin4x\cos2x} = \tan2x$.
- (c) Крайние вместе: $\dfrac{\sin3x(2\cos2x + 1)}{\cos3x(2\cos2x + 1)} = \tan3x$ (как задача 4 в Summative preparation).
- (d) $\cos x + \cos11x = 2\cos6x\cos5x$, $\cos4x + \cos8x = 2\cos6x\cos2x$. Числитель $= 2\cos6x(\cos5x + \cos2x) = 4\cos6x\cos\frac{7x}{2}\cos\frac{3x}{2}$. **Ответ:** $4\cos6x$.
:::

## 6. Универсальная подстановка

:::solution (a) Вывод формул
Делим на $1 = \sin^2\frac{x}{2} + \cos^2\frac{x}{2}$, потом числитель и знаменатель — на $\cos^2\frac{x}{2}$:
$$\sin x = \frac{2\sin\frac x2\cos\frac x2}{\sin^2\frac x2 + \cos^2\frac x2} = \frac{2t}{t^2 + 1},\qquad \cos x = \frac{\cos^2\frac x2 - \sin^2\frac x2}{\cos^2\frac x2 + \sin^2\frac x2} = \frac{1 - t^2}{1 + t^2},$$
$\tan x = \frac{\sin x}{\cos x} = \frac{2t}{1 - t^2}$. Формулы верны там, где $\cos\frac x2 \ne 0$, то есть $x \ne \pi + 2\pi k$ — эти точки при подстановке **теряются**, их проверяют отдельно.
:::

:::solution (b) $\dfrac{2\sin x + 3\cos x - 1}{1 + \sin x - \cos x}$ через $t$
Числитель: $\frac{4t + 3(1 - t^2) - (1 + t^2)}{1 + t^2} = \frac{-4t^2 + 4t + 2}{1 + t^2}$. Знаменатель: $\frac{(1 + t^2) + 2t - (1 - t^2)}{1 + t^2} = \frac{2t^2 + 2t}{1 + t^2}$.
$$\frac{-4t^2 + 4t + 2}{2t^2 + 2t} = \frac{1 + 2t - 2t^2}{t(t + 1)}.$$
:::

:::solution (c) $\dfrac{1 - \cos x}{\sin x}$
$\frac{2t^2/(1 + t^2)}{2t/(1 + t^2)} = t = \tan\frac x2$. Это естественно: это та же формула половинного угла $\frac{1 - \cos x}{\sin x} = \frac{2\sin^2\frac x2}{2\sin\frac x2\cos\frac x2} = \tan\frac x2$.
:::

## 7. Challenge

:::solution (a) $16\cos6^\circ\cos12^\circ\cos24^\circ\cos48^\circ = \cot6^\circ$
Умножаем левую часть на $\sin6^\circ$ и 4 раза применяем двойной угол:
$$16\sin6^\circ\cos6^\circ\cos12^\circ\cos24^\circ\cos48^\circ = 8\sin12^\circ\cos12^\circ\cdots = \ldots = \sin96^\circ = \cos6^\circ.$$
Значит, левая часть $= \frac{\cos6^\circ}{\sin6^\circ} = \cot6^\circ$ ∎
:::

:::solution (b) $\cos\frac{\pi}{11}\cos\frac{2\pi}{11}\cos\frac{3\pi}{11}\cos\frac{4\pi}{11}\cos\frac{5\pi}{11}$
**Превратим в цепочку удвоений.** $\cos\frac{3\pi}{11} = -\cos\frac{8\pi}{11}$ и $\cos\frac{5\pi}{11} = -\cos\frac{6\pi}{11} = -\cos\frac{16\pi}{11}$ (потому что $\frac{16\pi}{11} = 2\pi - \frac{6\pi}{11}$). Два минуса дают плюс:
$$P = \cos\frac{\pi}{11}\cos\frac{2\pi}{11}\cos\frac{4\pi}{11}\cos\frac{8\pi}{11}\cos\frac{16\pi}{11} = \frac{\sin\frac{32\pi}{11}}{32\sin\frac{\pi}{11}}.$$
$\sin\frac{32\pi}{11} = \sin\left(\frac{32\pi}{11} - 2\pi\right) = \sin\frac{10\pi}{11} = \sin\frac{\pi}{11}$. **Ответ:** $\frac{1}{32}$.
:::

:::solution (c) $\sin2^\circ + \sin6^\circ + \cdots + \sin178^\circ = \csc2^\circ$
В сумме 45 слагаемых $\sin(4k + 2)^\circ$, $k = 0, \ldots, 44$. Умножим каждое на $2\sin2^\circ$:
$$2\sin2^\circ\sin(4k + 2)^\circ = \cos(4k)^\circ - \cos(4k + 4)^\circ.$$
Сумма телескопируется: $\cos0^\circ - \cos180^\circ = 2$. Значит, $S\cdot2\sin2^\circ = 2$, $S = \frac{1}{\sin2^\circ} = \csc2^\circ$ ∎
:::
