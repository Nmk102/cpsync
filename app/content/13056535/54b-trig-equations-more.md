---
title: "Basic trigonometric equations (большой листок) — решения всех 31 номера"
kind: solutions
units: []
tasks: [48936939, 49321380]
order: 54.5
summary: Около 70 уравнений по группам «одна идея на номер»: квадратные, однородные, оценки, суммы в произведения, понижение степени, вспомогательный угол, замена t = sin x + cos x, градусы, ОДЗ. Корни проверены перебором на компьютере.
---

Оформление — как в образце учителя: равносильные переходы, разложение на множители, серии с «$k$ — любое целое». Ниже по каждому номеру сначала **идея** (она общая для всех пунктов номера), затем решения. Везде $k, n \in \mathbb Z$.

## 1–3. Простейшие

:::solution 1. 1) $\sin x = -2$; 2) $\tan x = 1$; 3) $\cot y = \frac{\sqrt3}{3}$; 4) $\cot z = -1$; 5) $\tan t + \cot x = 1$
1) Решений нет: $|\sin x| \le 1$.
2) $x = \frac{\pi}{4} + \pi k$. 3) $y = \frac{\pi}{3} + \pi k$. 4) $z = \frac{3\pi}{4} + \pi k$.
5) Если это опечатка и имелось в виду $\tan t + \cot t = 1$: $u + \frac1u = 1$ ⇔ $u^2 - u + 1 = 0$, дискриминант $< 0$ — **решений нет** (вообще $|\tan t + \cot t| \ge 2$). Если переменные действительно разные — это одно уравнение с двумя неизвестными: $t = \arctan(1 - \cot x) + \pi n$ при любом $x \ne \pi k$.
:::

:::solution 2. 1) $\cos2x = \frac{1}{\sqrt2}$; 2) $\tan\left(3x + \frac{\pi}{4}\right) = -1$; 3) $\cot\frac x2 = -\frac{1}{\sqrt3}$; 4) $\cos(\pi\sqrt x) = 0$
1) $2x = \pm\frac{\pi}{4} + 2\pi k$ ⇒ $x = \pm\frac{\pi}{8} + \pi k$.
2) $3x + \frac{\pi}{4} = -\frac{\pi}{4} + \pi k$ ⇒ $x = -\frac{\pi}{6} + \frac{\pi k}{3}$.
3) $\frac x2 = \frac{2\pi}{3} + \pi k$ ⇒ $x = \frac{4\pi}{3} + 2\pi k$.
4) $\pi\sqrt x = \frac{\pi}{2} + \pi k$, $\sqrt x \ge 0$ ⇒ $\sqrt x = k + \frac12$, $k \ge 0$ ⇒ $x = \left(k + \frac12\right)^2$, $k = 0, 1, 2, \ldots$
:::

:::solution 3. 1) $\sin\frac1x = 0$; 2) $2\cos(x^2) = 1$; 3) $\tan\frac{1 + x}{1 - x} = \frac{1}{\sqrt3}$; 4) $\sin(2x^2)\cos\left(\frac x2 + \frac{\pi}{4}\right) = 0$
1) $\frac1x = \pi k$, $k \ne 0$ ⇒ $x = \frac{1}{\pi k}$, $k \in \mathbb Z \setminus \{0\}$.
2) $x^2 = \pm\frac{\pi}{3} + 2\pi k \ge 0$ ⇒ $x = \pm\sqrt{\frac{\pi}{3} + 2\pi k}$ ($k \ge 0$), $x = \pm\sqrt{2\pi k - \frac{\pi}{3}}$ ($k \ge 1$).
3) $\frac{1 + x}{1 - x} = a_k$, $a_k = \frac{\pi}{6} + \pi k$ ⇒ $x = \frac{a_k - 1}{a_k + 1} = \frac{\pi + 6\pi k - 6}{\pi + 6\pi k + 6}$ ($a_k \ne -1$ всегда, $x \ne 1$ автоматически).
4) $2x^2 = \pi k$ ⇒ $x = \pm\sqrt{\frac{\pi k}{2}}$, $k \ge 0$; $\frac x2 + \frac{\pi}{4} = \frac{\pi}{2} + \pi k$ ⇒ $x = \frac{\pi}{2} + 2\pi k$.
:::

## 4. Сведение к квадратному

:::key Идея
Выразить всё через одну функцию ($\cos^2x = 1 - \sin^2x$, $\cos2x = 1 - 2\sin^2x$) и решить квадратное уравнение; корни вне $[-1; 1]$ отбросить.
:::

:::solution 1) $2\cos^2x + 5\sin x - 4 = 0$; 2) $\sin x - 2\cos2x = 1$
1) $2s^2 - 5s + 2 = 0$ ⇒ $s = 2$ (нет) или $s = \frac12$ ⇒ $x = \frac{\pi}{6} + 2\pi k$, $x = \frac{5\pi}{6} + 2\pi k$.
2) $\sin x - 2(1 - 2\sin^2x) = 1$ ⇒ $4s^2 + s - 3 = 0$ ⇒ $s = \frac34$ или $s = -1$ ⇒ $x = (-1)^k\arcsin\frac34 + \pi k$, $x = -\frac{\pi}{2} + 2\pi k$.
:::

## 5. Однородные уравнения

:::key Идея
Все слагаемые одной степени по $\sin x$ и $\cos x$. Делим на $\cos^nx$ (предварительно проверив, что $\cos x = 0$ — не решение) и получаем уравнение на $\tan x$. Если справа число, умножаем его на $\sin^2x + \cos^2x$.
:::

:::solution 1)–4)
1) $\sin x + \cos x = 0$ ⇒ $\tan x = -1$ ⇒ $x = -\frac{\pi}{4} + \pi k$.
2) $\tan x = 2$ ⇒ $x = \arctan2 + \pi k$.
3) $\tan^2x - 2\tan x - 3 = 0$ ⇒ $\tan x = 3$ или $-1$ ⇒ $x = \arctan3 + \pi k$, $x = -\frac{\pi}{4} + \pi k$.
4) $6\sin^2x + \sin x\cos x - \cos^2x = 2(\sin^2x + \cos^2x)$ ⇒ $4t^2 + t - 3 = 0$ ⇒ $t = \frac34$ или $-1$ ⇒ $x = \arctan\frac34 + \pi k$, $x = -\frac{\pi}{4} + \pi k$.
:::

## 6. Оценки

:::key Идея
Сумма неотрицательных = 0 ⇔ все слагаемые = 0. Если каждое слагаемое не больше своего максимума и в сумме максимум — все одновременно в максимуме.
:::

:::solution 1) $\sin^2x + \sin^23x = 0$; 2) $\sin^{566}x + \cos^{566}x = 1$; 3) $\sin x + \cos7x = 2$; 4) $\cos4x\cos5x = 1$
1) $\sin x = 0$ и $\sin3x = 0$ ⇒ $x = \pi k$.
2) $\sin^{566}x \le \sin^2x$, $\cos^{566}x \le \cos^2x$ (степень числа из $[0; 1]$ не больше его квадрата), сумма $\le 1$. Равенство ⇔ $\sin^2x \in \{0; 1\}$ ⇒ $x = \frac{\pi k}{2}$.
3) Нужно $\sin x = 1$ и $\cos7x = 1$. Из первого $x = \frac{\pi}{2} + 2\pi k$, тогда $7x = \frac{7\pi}{2} + 14\pi k$ и $\cos7x = 0 \ne 1$. **Решений нет.**
4) Либо оба множителя равны 1, либо оба −1.
- $\cos4x = \cos5x = 1$: $x = \frac{\pi a}{2} = \frac{2\pi b}{5}$ ⇒ $5a = 4b$ ⇒ $x = 2\pi m$.
- $\cos4x = \cos5x = -1$: $\frac{\pi(1 + 2a)}{4} = \frac{\pi(1 + 2b)}{5}$ ⇒ $1 + 10a = 8b$ — слева нечётное, справа чётное: невозможно.

**Ответ:** $x = 2\pi m$.
:::

## 7–8. Суммы и произведения

:::key Идея
Сумму или разность синусов/косинусов — в произведение; произведение — в сумму. Потом «хотя бы один множитель равен нулю».
:::

:::solution 7. 1) $\sin x = \sin5x$; 2) $\cos2x = \sin5x$; 3) $1 + \cos x + \cos2x + \cos3x = 0$; 4) $\cos5x + \cos7x = \cos(\pi + 6x)$
1) $2\cos3x\sin2x = 0$ ⇒ $x = \frac{\pi}{6} + \frac{\pi k}{3}$, $x = \frac{\pi k}{2}$.
2) $\cos2x = \cos\left(\frac{\pi}{2} - 5x\right)$ ⇒ $2x = \pm\left(\frac{\pi}{2} - 5x\right) + 2\pi k$ ⇒ $x = \frac{\pi}{14} + \frac{2\pi k}{7}$, $x = \frac{\pi}{6} + \frac{2\pi k}{3}$.
3) $(1 + \cos2x) + (\cos x + \cos3x) = 2\cos^2x + 2\cos2x\cos x = 2\cos x(\cos x + \cos2x) = 4\cos x\cos\frac{3x}{2}\cos\frac x2$. Серии: $x = \frac{\pi}{2} + \pi k$; $x = \frac{\pi}{3} + \frac{2\pi k}{3}$ (серия $\cos\frac x2 = 0$, то есть $x = \pi + 2\pi k$, в неё входит).
4) $2\cos6x\cos x = -\cos6x$ ⇒ $\cos6x(2\cos x + 1) = 0$ ⇒ $x = \frac{\pi}{12} + \frac{\pi k}{6}$, $x = \pm\frac{2\pi}{3} + 2\pi k$.
:::

:::solution 8. 1) $\sin2x\sin6x = \cos x\cos3x$; 2) $\sin x\sin3x + \sin4x\sin8x = 0$
1) $\frac12(\cos4x - \cos8x) = \frac12(\cos2x + \cos4x)$ ⇒ $\cos8x + \cos2x = 0$ ⇒ $2\cos5x\cos3x = 0$ ⇒ $x = \frac{\pi}{10} + \frac{\pi k}{5}$, $x = \frac{\pi}{6} + \frac{\pi k}{3}$.
2) $\frac12(\cos2x - \cos4x) + \frac12(\cos4x - \cos12x) = 0$ ⇒ $\cos2x - \cos12x = 2\sin7x\sin5x = 0$ ⇒ $x = \frac{\pi k}{7}$, $x = \frac{\pi k}{5}$.
:::

## 9. Вспомогательный угол

:::solution 1) $\sin x - \cos x = 1$; 2) $4\sin x + 3\cos x = 5$
1) $\sqrt2\sin\left(x - \frac{\pi}{4}\right) = 1$ ⇒ $x - \frac{\pi}{4} = \frac{\pi}{4} + 2\pi k$ или $\frac{3\pi}{4} + 2\pi k$ ⇒ $x = \frac{\pi}{2} + 2\pi k$, $x = \pi + 2\pi k$.
2) $5\left(\frac45\sin x + \frac35\cos x\right) = 5$. Это $\sin(x + \varphi) = 1$ с $\cos\varphi = \frac45$, $\sin\varphi = \frac35$ ⇒ $x = \frac{\pi}{2} - \varphi + 2\pi k = \arctan\frac43 + 2\pi k$ (проверка: $\sin x = \frac45$, $\cos x = \frac35$, $\frac{16}{5} + \frac95 = 5$ ✓).
:::

## 10–11. Понижение степени

:::key Идея
$\sin^2a = \frac{1 - \cos2a}{2}$, $\cos^2a = \frac{1 + \cos2a}{2}$ — квадраты исчезают, остаётся сумма косинусов, которую раскладываем на множители.
:::

:::solution 10. 1) $\sin^22x + \sin^23x + \sin^24x + \sin^25x = 2$; 2) $\cos^2x + \cos^22x - \cos^23x - \cos^24x = 0$
1) $\cos4x + \cos6x + \cos8x + \cos10x = 0$ ⇒ $2\cos7x(\cos3x + \cos x) = 4\cos7x\cos2x\cos x = 0$ ⇒ $x = \frac{\pi}{14} + \frac{\pi k}{7}$, $x = \frac{\pi}{4} + \frac{\pi k}{2}$ (серия $\cos x = 0$ входит в первую).
2) $\cos2x + \cos4x - \cos6x - \cos8x = 0$ ⇒ $2\sin5x(\sin3x + \sin x) = 4\sin5x\sin2x\cos x = 0$ ⇒ $x = \frac{\pi k}{5}$, $x = \frac{\pi k}{2}$.
:::

:::solution 11. 1) $\cos^2\frac x2 + \cos^2\frac{3x}{2} - \sin^22x - \sin^24x = 0$; 2) $\sin^23x + \sin^24x = \sin^25x + \sin^26x$
1) $\cos x + \cos3x + \cos4x + \cos8x = 0$ ⇒ $2\cos2x(\cos x + \cos6x) = 4\cos2x\cos\frac{7x}{2}\cos\frac{5x}{2} = 0$ ⇒ $x = \frac{\pi}{4} + \frac{\pi k}{2}$, $x = \frac{\pi}{7} + \frac{2\pi k}{7}$, $x = \frac{\pi}{5} + \frac{2\pi k}{5}$.
2) $\cos6x + \cos8x = \cos10x + \cos12x$ ⇒ $2\cos x(\cos7x - \cos11x) = 4\cos x\sin9x\sin2x = 0$ ⇒ $x = \frac{\pi k}{9}$, $x = \frac{\pi k}{2}$.
:::

## 12–13. Четвёртые степени

:::solution 12. 1) $\sin2x = \cos^4\frac x2 - \sin^4\frac x2$; 2) $\sin^4x + \cos^4x = \frac58$
1) Правая часть $= \left(\cos^2\frac x2 - \sin^2\frac x2\right)\cdot1 = \cos x$. $\cos x(2\sin x - 1) = 0$ ⇒ $x = \frac{\pi}{2} + \pi k$, $x = \frac{\pi}{6} + 2\pi k$, $x = \frac{5\pi}{6} + 2\pi k$.
2) $\frac34 + \frac14\cos4x = \frac58$ ⇒ $\cos4x = -\frac12$ ⇒ $x = \pm\frac{\pi}{6} + \frac{\pi k}{2}$.
:::

:::solution 13. 1) $\sin^42x + \cos^42x = \sin2x\cos2x$; 2) $\sin^4x + \cos^4x = \cos4x$
1) $p = \sin2x\cos2x = \frac12\sin4x$: $1 - 2p^2 = p$ ⇒ $p = \frac12$ или $p = -1$ (нет: $|p| \le \frac12$). $\sin4x = 1$ ⇒ $x = \frac{\pi}{8} + \frac{\pi k}{2}$.
2) $\frac34 + \frac14\cos4x = \cos4x$ ⇒ $\cos4x = 1$ ⇒ $x = \frac{\pi k}{2}$.
:::

## 14–15. Симметричные выражения, замена $t = \sin x + \cos x$

:::solution 14. 1) $\tan x + \cot x = 2$; 2) $\sin^3x - \cos^3x = 1 + \sin x\cos x$
1) $\frac{1}{\sin x\cos x} = 2$ ⇒ $\sin2x = 1$ ⇒ $x = \frac{\pi}{4} + \pi k$.
2) Разность кубов: $(\sin x - \cos x)(1 + \sin x\cos x) = 1 + \sin x\cos x$ ⇒ $(1 + \sin x\cos x)(\sin x - \cos x - 1) = 0$. Первый множитель $\ge 1 - \frac12 > 0$. Значит, $\sin x - \cos x = 1$ — номер 9.1): $x = \frac{\pi}{2} + 2\pi k$, $x = \pi + 2\pi k$.
:::

:::solution 15. 1) $\sin2x + 5(\sin x + \cos x) + 1 = 0$; 2) $(1 - \sin2x)(\cos x - \sin x) = 1 - 2\sin^2x$
1) $t = \sin x + \cos x \in [-\sqrt2; \sqrt2]$, $\sin2x = t^2 - 1$: $t^2 + 5t = 0$ ⇒ $t = 0$ ($t = -5$ нет) ⇒ $x = -\frac{\pi}{4} + \pi k$.
2) $1 - \sin2x = (\cos x - \sin x)^2$, $1 - 2\sin^2x = \cos2x = (\cos x - \sin x)(\cos x + \sin x)$:
$(\cos x - \sin x)\left[(\cos x - \sin x)^2 - (\cos x + \sin x)\right] = 0$.
- $\cos x = \sin x$ ⇒ $x = \frac{\pi}{4} + \pi k$;
- $1 - (t^2 - 1) = t$ ⇒ $t^2 + t - 2 = 0$ ⇒ $t = 1$ ⇒ $\sin\left(x + \frac{\pi}{4}\right) = \frac{\sqrt2}{2}$ ⇒ $x = 2\pi k$, $x = \frac{\pi}{2} + 2\pi k$.
:::

## 16–17. Градусы и дополнительные углы

:::solution 16. 1) $\tan(70^\circ + x) + \tan(20^\circ - x) = 2$; 2) $\sin(15^\circ + x) + \sin(45^\circ - x) = 1$; 3) $\cos(20^\circ + x) + \cos(100^\circ - x) = \frac12$
1) Углы в сумме дают 90° ⇒ $\tan(20^\circ - x) = \cot(70^\circ + x)$. $u + \frac1u = 2$ ⇒ $u = 1$ ⇒ $70^\circ + x = 45^\circ + 180^\circ k$ ⇒ $x = -25^\circ + 180^\circ k$.
2) $2\sin30^\circ\cos(x - 15^\circ) = 1$ ⇒ $\cos(x - 15^\circ) = 1$ ⇒ $x = 15^\circ + 360^\circ k$.
3) $2\cos60^\circ\cos(x - 40^\circ) = \frac12$ ⇒ $\cos(x - 40^\circ) = \frac12$ ⇒ $x = 100^\circ + 360^\circ k$, $x = -20^\circ + 360^\circ k$.
:::

:::solution 17. 1) $\tan(35^\circ + x)\cot(10^\circ - x) = \frac23$; 2) $\tan x + \tan50^\circ + \tan70^\circ = \tan x\tan50^\circ\tan70^\circ$
1) $A = 35^\circ + x$, $B = 10^\circ - x$, $A + B = 45^\circ$ ⇒ $\tan B = \frac{1 - t}{1 + t}$, $t = \tan A$. $\frac{t(1 + t)}{1 - t} = \frac23$ ⇒ $3t^2 + 5t - 2 = 0$ ⇒ $t = \frac13$ или $t = -2$.
$x = \arctan\frac13 - 35^\circ + 180^\circ k$ (≈ −16,6°), $x = -\arctan2 - 35^\circ + 180^\circ k$ (≈ −98,4°).
2) $\tan x\,(1 - \tan50^\circ\tan70^\circ) = -(\tan50^\circ + \tan70^\circ)$ ⇒ $\tan x = -\tan120^\circ = \sqrt3$ ⇒ $x = 60^\circ + 180^\circ k$.
(Это частный случай тождества: если $A + B + C = 180^\circ$, то $\tan A + \tan B + \tan C = \tan A\tan B\tan C$.)
:::

## 18–31. Разные идеи

:::solution 18. $\sin2x + 2\cot x = 3$
ОДЗ $\sin x \ne 0$. $t = \cot x$, $\sin2x = \frac{2t}{1 + t^2}$: $2t^3 - 3t^2 + 4t - 3 = 0$ ⇒ $(t - 1)(2t^2 - t + 3) = 0$ ⇒ $t = 1$ ⇒ $x = \frac{\pi}{4} + \pi k$.
:::

:::solution 19. $\cos3x - \sin x = \sqrt3(\cos x - \sin3x)$
$\cos3x + \sqrt3\sin3x = \sqrt3\cos x + \sin x$ ⇒ $2\cos\left(3x - \frac{\pi}{3}\right) = 2\cos\left(x - \frac{\pi}{6}\right)$ ⇒ $3x - \frac{\pi}{3} = \pm\left(x - \frac{\pi}{6}\right) + 2\pi k$ ⇒ $x = \frac{\pi}{12} + \pi k$, $x = \frac{\pi}{8} + \frac{\pi k}{2}$.
:::

:::solution 20. $2\sin4x + 16\sin^3x\cos x + 3\cos2x - 5 = 0$
$16\sin^3x\cos x = 8\sin2x\sin^2x = 4\sin2x(1 - \cos2x) = 4\sin2x - 2\sin4x$. Остаётся $4\sin2x + 3\cos2x = 5$ — как 9.2) с $2x$: $2x = \arctan\frac43 + 2\pi k$ ⇒ $x = \arctan\frac12 + \pi k$ (так как $\tan\left(\frac12\arctan\frac43\right) = \frac{4/5}{1 + 3/5} = \frac12$).
:::

:::solution 21. $2\cos x(2\sin x - 1) = -2 + 3\sin x + 2\sin^2x$
Правая часть $= (2\sin x - 1)(\sin x + 2)$ ⇒ $(2\sin x - 1)(2\cos x - \sin x - 2) = 0$.
- $\sin x = \frac12$: $x = \frac{\pi}{6} + 2\pi k$, $\frac{5\pi}{6} + 2\pi k$;
- $2\cos x - \sin x = 2$: подстановка $t = \tan\frac x2$: $2(1 - t^2) - 2t = 2(1 + t^2)$ ⇒ $t(2t + 1) = 0$ ⇒ $x = 2\pi k$, $x = -2\arctan\frac12 + 2\pi k = -\arctan\frac43 + 2\pi k$. Потерянные подстановкой точки $x = \pi + 2\pi k$ не подходят: $-2 \ne 2$.
:::

:::solution 22. $1 + 2\cos3x\cos x - \cos2x = 0$
$2\cos3x\cos x = \cos4x + \cos2x$ ⇒ $1 + \cos4x = 0$ ⇒ $x = \frac{\pi}{4} + \frac{\pi k}{2}$.
:::

:::solution 23. $4\cos^3x + 3\sqrt2\sin2x = 8\cos x$
$2\cos x\,(2\cos^2x + 3\sqrt2\sin x - 4) = 0$.
- $\cos x = 0$: $x = \frac{\pi}{2} + \pi k$;
- $2s^2 - 3\sqrt2s + 2 = 0$ ⇒ $s = \sqrt2$ (нет) или $s = \frac{\sqrt2}{2}$ ⇒ $x = \frac{\pi}{4} + 2\pi k$, $\frac{3\pi}{4} + 2\pi k$.
:::

:::solution 24. $8\sin^4x + 13\cos2x = 7$
$c = \cos2x$, $\sin^4x = \frac{(1 - c)^2}{4}$: $2(1 - c)^2 + 13c - 7 = 0$ ⇒ $2c^2 + 9c - 5 = 0$ ⇒ $c = \frac12$ ($c = -5$ нет) ⇒ $x = \pm\frac{\pi}{6} + \pi k$.
:::

:::solution 25. $\cos\left(x - \frac{\pi}{6}\right) + \sin\left(x - \frac{\pi}{3}\right) + \cos2x = 1$
Первые два слагаемых в сумме дают $\sin x$ (члены с $\cos x$ сокращаются). $\sin x + 1 - 2\sin^2x = 1$ ⇒ $\sin x(1 - 2\sin x) = 0$ ⇒ $x = \pi k$, $x = \frac{\pi}{6} + 2\pi k$, $x = \frac{5\pi}{6} + 2\pi k$.
:::

:::solution 26. $\cot^4x = \cos^32x + 1$
ОДЗ $\sin x \ne 0$, $c = \cos2x \in [-1; 1)$, $\cot^2x = \frac{1 + c}{1 - c}$: $\frac{(1 + c)^2}{(1 - c)^2} = (1 + c)(1 - c + c^2)$.
- $1 + c = 0$ ⇒ $x = \frac{\pi}{2} + \pi k$ (проверка: $0 = -1 + 1$ ✓);
- иначе $1 + c = (1 - c)^2(1 - c + c^2)$ ⇒ $c(c^3 - 3c^2 + 4c - 4) = 0 = c(c - 2)(c^2 - c + 2)$ ⇒ $c = 0$ ⇒ $x = \frac{\pi}{4} + \frac{\pi k}{2}$.
:::

:::solution 27. $\sin x + \sin^2x + \cos^3x = 0$
$\sin x(1 + \sin x) + \cos x(1 - \sin x)(1 + \sin x) = (1 + \sin x)(\sin x + \cos x - \sin x\cos x) = 0$.
- $\sin x = -1$: $x = -\frac{\pi}{2} + 2\pi k$;
- $t = \sin x + \cos x$, $\sin x\cos x = \frac{t^2 - 1}{2}$: $t^2 - 2t - 1 = 0$ ⇒ $t = 1 - \sqrt2$ ($1 + \sqrt2 > \sqrt2$ нет) ⇒ $\sin\left(x + \frac{\pi}{4}\right) = \frac{\sqrt2}{2} - 1$ ⇒ $x = -\frac{\pi}{4} + (-1)^{k+1}\arcsin\left(1 - \frac{\sqrt2}{2}\right) + \pi k$.
:::

:::solution 28. $2\sin x + 8\cos x\cos2x = \sin2x(\cos x - \sin x)$
Раскрываем правую часть и переносим: $2\sin x - 2\sin x\cos^2x = 2\sin^3x$, поэтому уравнение принимает вид $2\sin^3x + 2\sin^2x\cos x + 8\cos x\cos2x = 0$.
$\cos2x = (\cos x - \sin x)(\cos x + \sin x)$ ⇒ $(\sin x + \cos x)\left[2\sin^2x + 8\cos x(\cos x - \sin x)\right] = 0$.
- $\tan x = -1$: $x = -\frac{\pi}{4} + \pi k$;
- однородное: $\tan^2x - 4\tan x + 4 = 0$ ⇒ $\tan x = 2$ ⇒ $x = \arctan2 + \pi k$.
:::

:::solution 29. $2\cos2x + \cos^2\frac x2 - 10\cos\left(\frac{5\pi}{2} - x\right) + \frac72 = \frac12\cos x$
$\cos\left(\frac{5\pi}{2} - x\right) = \sin x$, $\cos^2\frac x2 = \frac{1 + \cos x}{2}$ — слагаемые с $\cos x$ сокращаются: $2\cos2x - 10\sin x + 4 = 0$ ⇒ $2s^2 + 5s - 3 = 0$ ⇒ $s = \frac12$ ⇒ $x = \frac{\pi}{6} + 2\pi k$, $\frac{5\pi}{6} + 2\pi k$.
:::

:::solution 30. $\sqrt2\cos\left(\frac x5 - \frac{\pi}{12}\right) - \sqrt6\sin\left(\frac x5 - \frac{\pi}{12}\right) = 2\sin\left(\frac x5 + \frac{2\pi}{3}\right) - 2\sin\left(\frac{3x}{5} + \frac{\pi}{6}\right)$
Пусть $y = \frac x5 + \frac{\pi}{4}$.
Слева: $2\sqrt2\cos\left(\frac x5 - \frac{\pi}{12} + \frac{\pi}{3}\right) = 2\sqrt2\cos y$.
Справа (разность синусов): $4\cos\left(\frac{2x}{5} + \frac{5\pi}{12}\right)\sin\left(\frac{\pi}{4} - \frac x5\right) = 4\cos\left(2y - \frac{\pi}{12}\right)\cos y$.
$\cos y\left[2\cos\left(2y - \frac{\pi}{12}\right) - \sqrt2\right] = 0$:
- $\cos y = 0$ ⇒ $x = \frac{5\pi}{4} + 5\pi k$;
- $2y - \frac{\pi}{12} = \pm\frac{\pi}{4} + 2\pi k$ ⇒ $y = \frac{\pi}{6} + \pi k$ или $y = -\frac{\pi}{12} + \pi k$ ⇒ $x = -\frac{5\pi}{12} + 5\pi k$, $x = -\frac{5\pi}{3} + 5\pi k$.
:::

:::solution 31. $\dfrac{1}{\sqrt{-2\sin x}} = \sqrt{-2\cos x}$ на $(-\pi; \pi)$
**ОДЗ:** $\sin x < 0$, $\cos x \le 0$ ⇒ $x \in \left(-\pi; -\frac{\pi}{2}\right]$.
Обе части $\ge 0$, возводим в квадрат: $\frac{1}{-2\sin x} = -2\cos x$ ⇒ $\sin2x = \frac12$ ⇒ $x = \frac{\pi}{12} + \pi k$ или $\frac{5\pi}{12} + \pi k$.
В ОДЗ: $x = -\frac{11\pi}{12}$, $x = -\frac{7\pi}{12}$.
:::
