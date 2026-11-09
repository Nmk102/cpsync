---
title: "Trigonometric equations (21.09) — решения всех 32 уравнений"
kind: solutions
units: []
tasks: [48915257, 49321380]
order: 54
summary: Простейшие уравнения, модули и степени, сведение к квадратному, оценки, ОДЗ и отбор корней — по образцу «уравнение → точки на окружности → общее решение». Ответы проверены перебором корней на компьютере.
---

:::key Формулы общих решений (выучить)
| Уравнение | Решение | Особые случаи |
|---|---|---|
| $\sin x = a$, $|a| \le 1$ | $x = (-1)^n\arcsin a + \pi n$ | $\sin x = 0$: $x = \pi n$; $\sin x = \pm1$: $x = \pm\frac{\pi}{2} + 2\pi n$ |
| $\cos x = a$, $|a| \le 1$ | $x = \pm\arccos a + 2\pi n$ | $\cos x = 0$: $x = \frac{\pi}{2} + \pi n$; $\cos x = 1$: $x = 2\pi n$; $\cos x = -1$: $x = \pi + 2\pi n$ |
| $\tan x = a$ | $x = \arctan a + \pi n$ | |
| $\cot x = a$ | $x = \text{arccot}\,a + \pi n$ | |

Везде $n \in \mathbb Z$. Если $|a| > 1$, у $\sin x = a$ и $\cos x = a$ решений нет.
:::

:::tip Как оформлять (как в образце учителя)
1. Записали уравнение. 2. Нарисовали единичную окружность и отметили точки. 3. Записали общее решение и «$n$ — любое целое». Если в аргументе $kx + b$, сначала решаем относительно всего аргумента, потом выражаем $x$.
:::

## 1. Простейшие уравнения

:::solution 1–4
1. $\sin x = \frac12$: $x = \frac{\pi}{6} + 2\pi n$ или $x = \frac{5\pi}{6} + 2\pi n$ (то же: $x = (-1)^n\frac{\pi}{6} + \pi n$).
2. $\cos x = -\frac{\sqrt3}{2}$: $x = \pm\frac{5\pi}{6} + 2\pi n$.
3. $\tan x = -1$: $x = -\frac{\pi}{4} + \pi n$.
4. $\cot x = \sqrt3$: $x = \frac{\pi}{6} + \pi n$.
:::

:::solution 5–8 (сложный аргумент)
5. $\sin\frac{x}{2} = 0$: $\frac{x}{2} = \pi n$ ⇒ $x = 2\pi n$.
6. $\cos3x = -1$: $3x = \pi + 2\pi n$ ⇒ $x = \frac{\pi}{3} + \frac{2\pi n}{3}$.
7. $\sin\left(2x - \frac{\pi}{4}\right) = 1$: $2x - \frac{\pi}{4} = \frac{\pi}{2} + 2\pi n$ ⇒ $x = \frac{3\pi}{8} + \pi n$.
8. $\cos\left(\frac{x}{3} + \frac{\pi}{6}\right) = 0$: $\frac{x}{3} + \frac{\pi}{6} = \frac{\pi}{2} + \pi n$ ⇒ $\frac{x}{3} = \frac{\pi}{3} + \pi n$ ⇒ $x = \pi + 3\pi n$.
:::

:::warn Частая ошибка
Делить на коэффициент нужно **и период тоже**: из $3x = \pi + 2\pi n$ получается $x = \frac{\pi}{3} + \frac{2\pi n}{3}$, а не $\frac{\pi}{3} + 2\pi n$.
:::

## 2. Степени и модули

:::solution 9–10
9. $\tan\left(3x + \frac{\pi}{6}\right) = \sqrt3$: $3x + \frac{\pi}{6} = \frac{\pi}{3} + \pi n$ ⇒ $x = \frac{\pi}{18} + \frac{\pi n}{3}$.
10. $\cot\left(\frac{x}{2} - \frac{\pi}{4}\right) = -1$: $\frac{x}{2} - \frac{\pi}{4} = -\frac{\pi}{4} + \pi n$ ⇒ $x = 2\pi n$.
:::

:::solution 11–13
11. $\sin^4(3x) = 1$ ⇔ $\sin3x = \pm1$ ⇔ $3x = \frac{\pi}{2} + \pi n$ ⇒ $x = \frac{\pi}{6} + \frac{\pi n}{3}$.
12. $\cos^2\frac{2x}{3} = 1$ ⇔ $\cos\frac{2x}{3} = \pm1$ ⇔ $\frac{2x}{3} = \pi n$ ⇒ $x = \frac{3\pi n}{2}$.
13. $|\tan2x| = 1$ ⇔ $\tan2x = \pm1$ ⇔ $2x = \pm\frac{\pi}{4} + \pi n$. Обе серии объединяются в $2x = \frac{\pi}{4} + \frac{\pi n}{2}$ ⇒ $x = \frac{\pi}{8} + \frac{\pi n}{4}$.
:::

:::tip Объединение серий
Точки $\pm\frac{\pi}{4} + \pi n$ на окружности — четыре точки через каждые $\frac{\pi}{2}$, начиная с $\frac{\pi}{4}$. Поэтому их можно записать одной формулой $\frac{\pi}{4} + \frac{\pi n}{2}$. Так же $\sin x = \pm1$ даёт $\frac{\pi}{2} + \pi n$, а $\cos x = \pm1$ — $\pi n$.
:::

:::solution 14. $\cos\left(|x| - \frac{\pi}{3}\right) = 1$
$|x| - \frac{\pi}{3} = 2\pi n$ ⇒ $|x| = \frac{\pi}{3} + 2\pi n$. Модуль неотрицателен, поэтому $n \ge 0$.

**Ответ:** $x = \pm\left(\frac{\pi}{3} + 2\pi n\right)$, $n = 0, 1, 2, \ldots$
:::

:::solution 15. $\sin\left(|x| + \frac{\pi}{6}\right) = 0$
$|x| + \frac{\pi}{6} = \pi n$ ⇒ $|x| = \pi n - \frac{\pi}{6}$, нужно $\ge 0$ ⇒ $n \ge 1$.

**Ответ:** $x = \pm\left(\pi n - \frac{\pi}{6}\right)$, $n = 1, 2, 3, \ldots$
:::

:::solution 16. $\cos(\pi x) = -1$
$\pi x = \pi + 2\pi n$ ⇒ $x = 2n + 1$ — все нечётные целые числа.
:::

## 3. Алгебра и область значений

:::solution 17. $\sin^2x + \sin x = 2$
$s^2 + s - 2 = 0$ ⇒ $s = 1$ или $s = -2$ (не подходит, $|\sin x| \le 1$).

**Ответ:** $x = \frac{\pi}{2} + 2\pi n$.
:::

:::solution 18. $2\cos^2\frac{x}{2} - 3\cos\frac{x}{2} - 2 = 0$
$c = \cos\frac x2$: $2c^2 - 3c - 2 = 0$ ⇒ $c = 2$ (нет) или $c = -\frac12$.
$\frac x2 = \pm\frac{2\pi}{3} + 2\pi n$ ⇒ $x = \pm\frac{4\pi}{3} + 4\pi n$.
:::

:::solution 19. $1 + 3\sin x = \cos^2x$
$\cos^2x = 1 - \sin^2x$: $\sin^2x + 3\sin x = 0$ ⇒ $\sin x(\sin x + 3) = 0$ ⇒ $\sin x = 0$.

**Ответ:** $x = \pi n$.
:::

:::solution 20. $2\sin^2(\pi x) + \cos(\pi x) + 1 = 0$
$2(1 - c^2) + c + 1 = 0$ ⇒ $2c^2 - c - 3 = 0$ ⇒ $c = \frac32$ (нет) или $c = -1$.
$\pi x = \pi + 2\pi n$ ⇒ $x = 2n + 1$.
:::

:::solution 21. $\cos^3\frac x2 + \cos^2\frac x2 - 2\cos\frac x2 = 0$
$c(c^2 + c - 2) = c(c - 1)(c + 2) = 0$, $c = -2$ не подходит.
- $\cos\frac x2 = 0$: $x = \pi + 2\pi n$;
- $\cos\frac x2 = 1$: $x = 4\pi n$.
:::

:::solution 22. $2\sin2x - \sqrt{\sin2x} = 1$
$u = \sqrt{\sin2x} \ge 0$: $2u^2 - u - 1 = 0$ ⇒ $u = 1$ или $u = -\frac12$ (нет, $u \ge 0$).
$\sin2x = 1$ ⇒ $x = \frac{\pi}{4} + \pi n$.
:::

:::solution 23. $\sin^2x + \cos^2\frac x2 = 0$
Сумма двух неотрицательных чисел равна нулю ⇔ оба равны нулю: $\sin x = 0$ **и** $\cos\frac x2 = 0$.
$\cos\frac x2 = 0$ ⇒ $x = \pi + 2\pi n$, и при этом $\sin x = 0$ ✓.

**Ответ:** $x = \pi + 2\pi n$.
:::

:::solution 24. $\sin2x + \cos\frac{8x}{5} = 2$
Каждое слагаемое $\le 1$, поэтому сумма равна 2 ⇔ **оба** равны 1:
$$\sin2x = 1 \Rightarrow x = \frac{\pi}{4} + \pi k;\qquad \cos\frac{8x}{5} = 1 \Rightarrow x = \frac{5\pi m}{4}.$$
Нужны общие точки: $\frac{\pi}{4} + \pi k = \frac{5\pi m}{4}$ ⇔ $1 + 4k = 5m$ — уравнение в целых числах. $m$ должно давать остаток 1 при делении на 4: $m = 1 + 4j$, тогда $k = 1 + 5j$.
$x = \frac{5\pi(1 + 4j)}{4} = \frac{5\pi}{4} + 5\pi j$.

**Проверка:** $x = \frac{5\pi}{4}$: $\sin\frac{5\pi}{2} = 1$, $\cos2\pi = 1$ ✓.

**Ответ:** $x = \frac{5\pi}{4} + 5\pi n$.
:::

## 4. ОДЗ и отбор корней

:::solution 25. $\sin x\sqrt{\cos x} = 0$
**ОДЗ:** $\cos x \ge 0$.
- $\sqrt{\cos x} = 0$ ⇒ $x = \frac{\pi}{2} + \pi n$ ✓ (подходят все);
- $\sin x = 0$ ⇒ $x = \pi n$, но нужно $\cos x \ge 0$: при $x = \pi$ косинус $-1$. Остаются $x = 2\pi n$.

**Ответ:** $x = 2\pi n$, $x = \frac{\pi}{2} + \pi n$.
:::

:::solution 26. $\sin\frac x2\cot\frac x3 = 0$
**ОДЗ:** $\sin\frac x3 \ne 0$ ⇔ $x \ne 3\pi k$.
- $\sin\frac x2 = 0$ ⇒ $x = 2\pi n$. Исключаем те, что кратны $3\pi$: $2\pi n = 3\pi k$ ⇔ $n$ кратно 3. Остаются $x = 2\pi n$, $n$ **не делится на 3**.
- $\cot\frac x3 = 0$ ⇒ $\frac x3 = \frac{\pi}{2} + \pi m$ ⇒ $x = \frac{3\pi}{2} + 3\pi m$ (все в ОДЗ).

**Ответ:** $x = 2\pi n$ ($n \ne 3k$); $x = \frac{3\pi}{2} + 3\pi m$.
:::

:::solution 27. $\dfrac{\sin\left(x + \frac{\pi}{3}\right)}{\cos3x + 1} = 0$
**ОДЗ:** $\cos3x \ne -1$. Числитель: $x = -\frac{\pi}{3} + \pi n$.
Проверяем: $3x = -\pi + 3\pi n$, $\cos3x = \cos(\pi(3n - 1)) = (-1)^{3n - 1}$.
- $n$ чётное: $3n - 1$ нечётное, $\cos3x = -1$ — вне ОДЗ;
- $n$ нечётное: $\cos3x = 1$ ✓.

$n = 2m + 1$: $x = -\frac{\pi}{3} + \pi + 2\pi m$. **Ответ:** $x = \frac{2\pi}{3} + 2\pi m$.
:::

:::solution 28. $\dfrac{\sin\left(2x + \frac{\pi}{4}\right)}{\sin4x + 1} = 0$
Числитель: $2x + \frac{\pi}{4} = \pi n$ ⇒ $4x = -\frac{\pi}{2} + 2\pi n$ ⇒ $\sin4x = -1$ — знаменатель **всегда** обращается в ноль.

**Ответ:** решений нет.
:::

:::solution 29. $\sin x\sqrt{4 - x^2} = 0$
**ОДЗ:** $-2 \le x \le 2$.
- $\sqrt{4 - x^2} = 0$ ⇒ $x = \pm2$;
- $\sin x = 0$ ⇒ $x = \pi n$, в $[-2; 2]$ только $x = 0$ (π ≈ 3,14 > 2).

**Ответ:** $x \in \{-2;\ 0;\ 2\}$.
:::

:::solution 30. $\cos2x\sqrt{6x - x^2} = 0$
**ОДЗ:** $6x - x^2 \ge 0$ ⇔ $0 \le x \le 6$.
- корень $= 0$: $x = 0$, $x = 6$;
- $\cos2x = 0$ ⇒ $x = \frac{\pi}{4} + \frac{\pi n}{2}$: $\frac{\pi}{4} \approx 0{,}79$, $\frac{3\pi}{4} \approx 2{,}36$, $\frac{5\pi}{4} \approx 3{,}93$, $\frac{7\pi}{4} \approx 5{,}50$ — подходят; $\frac{9\pi}{4} \approx 7{,}07 > 6$.

**Ответ:** $x \in \left\{0;\ \frac{\pi}{4};\ \frac{3\pi}{4};\ \frac{5\pi}{4};\ \frac{7\pi}{4};\ 6\right\}$.
:::

:::solution 31. $\dfrac{\sin(2\pi x)}{\sqrt{-2x - x^2}} = 0$
**ОДЗ:** $-2x - x^2 > 0$ (строго — знаменатель) ⇔ $x(x + 2) < 0$ ⇔ $-2 < x < 0$.
$\sin2\pi x = 0$ ⇒ $x = \frac n2$. В $(-2; 0)$: $-\frac32,\ -1,\ -\frac12$.
:::

:::solution 32. $\dfrac{\cos\left(\frac{\pi}{4} + \pi x\right)}{\sqrt{42x - x^2 - 440}} = 0$
**ОДЗ:** $x^2 - 42x + 440 < 0$. Корни: $x = \frac{42 \pm \sqrt{1764 - 1760}}{2} = 21 \pm 1$ ⇒ $20 < x < 22$.
$\frac{\pi}{4} + \pi x = \frac{\pi}{2} + \pi n$ ⇒ $x = \frac14 + n$. В $(20; 22)$: $20{,}25$ и $21{,}25$.
:::
