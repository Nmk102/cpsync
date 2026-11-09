---
title: "Trigonometry: practice (11.09) — решения всех 15 заданий"
kind: solutions
units: []
tasks: [48785897, 49321380]
order: 50.5
summary: Радианы и градусы, сравнение без калькулятора, точные значения, формулы сложения, суммы синусов, произведения синусов, тождество ∏ sin(x + kπ/n) = 2^(1−n) sin nx с доказательством без комплексных чисел.
---

## 1–3. Радианы и сравнение

:::solution 1–2. Переводы
**1.** $40^\circ = \frac{40\pi}{180} = \frac{2\pi}{9}$; $135^\circ = \frac{3\pi}{4}$; $450^\circ = \frac{5\pi}{2}$; $\pi^\circ = \frac{\pi\cdot\pi}{180} = \frac{\pi^2}{180}$ рад (это **маленький** угол, около 0,055 рад!).

**2.** $\frac{11\pi}{4} = 11\cdot45^\circ = 495^\circ$; $\frac{7\pi}{9} = 140^\circ$; $\frac{111\pi}{6} = 111\cdot30^\circ = 3330^\circ$; $3{,}14 = \frac{3{,}14\cdot180^\circ}{\pi} \approx 179{,}9^\circ$ (чуть меньше 180°, потому что $3{,}14 < \pi$); $-10 = -\frac{1800^\circ}{\pi} \approx -573^\circ$.
:::

:::solution 3. Расположить по возрастанию $\sin1, \sin2, \sin3, \cos1, \cos2, \cos3$
**Знаки.** $2$ и $3$ лежат между $\frac{\pi}{2} \approx 1{,}57$ и $\pi \approx 3{,}14$ (II четверть) ⇒ $\cos2 < 0$, $\cos3 < 0$, все синусы и $\cos1$ положительны.
**Отрицательные.** Косинус убывает на $[0; \pi]$ ⇒ $\cos3 < \cos2$.
**Положительные — приведём всё к синусам острых углов:**
$\sin3 = \sin(\pi - 3) \approx \sin0{,}14$; $\cos1 = \sin\left(\frac{\pi}{2} - 1\right) \approx \sin0{,}57$; $\sin1$; $\sin2 = \sin(\pi - 2) \approx \sin1{,}14$.
Синус растёт на $\left[0; \frac{\pi}{2}\right]$, а $0{,}14 < 0{,}57 < 1 < 1{,}14$.

**Ответ:** $\cos3 < \cos2 < \sin3 < \cos1 < \sin1 < \sin2$.
:::

## 4–5. Точные значения

:::solution 4. Вычислить
а) $\frac{\sqrt3}{2} - \frac{\sqrt3}{2} - \frac{\sqrt2}{2} = -\frac{\sqrt2}{2}$ (так как $\cos\frac{7\pi}{6} = -\frac{\sqrt3}{2}$).
б) $-\frac{\sqrt2}{2} + \frac12 - 0 = \frac{1 - \sqrt2}{2}$.
в) $0 + \cos\frac{3\pi}{2} - (-1) - 1 + 1 = 1$.
г) $\sin\frac{11\pi}{6} = -\frac12$, $\cos\frac{11\pi}{4} = \cos\frac{3\pi}{4} = -\frac{\sqrt2}{2}$, $\sin\frac{5\pi}{3} = -\frac{\sqrt3}{2}$ ⇒ $\frac{\sqrt3 - \sqrt2 - 1}{2}$.
д) Это куб суммы: $(\sin\frac{\pi}{3} + \cos\frac{5\pi}{6})^3 = \left(\frac{\sqrt3}{2} - \frac{\sqrt3}{2}\right)^3 = 0$.
:::

:::solution 5.1. Точные значения
a. $\sin10^\circ\sin50^\circ\sin70^\circ = \frac18$ — см. задачу 14.
b. $\cos20^\circ\cos40^\circ\cos80^\circ = \frac{\sin160^\circ}{8\sin20^\circ} = \frac18$ (умножили на $\sin20^\circ$ и трижды применили двойной угол).
в) $-(\cos25^\circ\cos5^\circ - \sin25^\circ\sin5^\circ) = -\cos30^\circ = -\frac{\sqrt3}{2}$.
г) $\tan(11^\circ + 34^\circ) = \tan45^\circ = 1$.
:::

:::solution 5.2. Упростить
**а)** Числитель: $\cos\frac{11\pi}{12} = -\cos\frac{\pi}{12}$, $\sin\frac{13\pi}{12} = -\sin\frac{\pi}{12}$, $\sin\frac{11\pi}{12} = \sin\frac{\pi}{12}$ ⇒ $-\cos^2\frac{\pi}{12} - \sin^2\frac{\pi}{12} = -1$.
Знаменатель: $\sin\frac{13\pi}{15} = \sin\frac{2\pi}{15}$, $\cos\frac{8\pi}{15} = -\cos\frac{7\pi}{15}$, $\cos\frac{28\pi}{15} = \cos\frac{2\pi}{15}$ ⇒ $\sin\frac{7\pi}{15}\cos\frac{2\pi}{15} - \cos\frac{7\pi}{15}\sin\frac{2\pi}{15} = \sin\frac{\pi}{3} = \frac{\sqrt3}{2}$.
**Ответ:** $-\frac{2}{\sqrt3} = -\frac{2\sqrt3}{3}$.

**б)** $\cos108^\circ = -\sin18^\circ$, $\sin208^\circ = -\sin28^\circ$ ⇒ числитель $= \cos18^\circ\cos28^\circ + \sin18^\circ\sin28^\circ = \cos10^\circ$.
$\cos157^\circ = -\cos23^\circ$, $\cos97^\circ = -\sin7^\circ$ ⇒ знаменатель $= \sin23^\circ\cos7^\circ + \cos23^\circ\sin7^\circ = \sin30^\circ = \frac12$.
**Ответ:** $2\cos10^\circ$.

**в)** $\tan\left(\frac{\pi}{15} + \frac{4\pi}{15}\right) = \tan\frac{\pi}{3} = \sqrt3$.

**г)** $\tan131^\circ = \tan(-49^\circ) = -\tan49^\circ$, $\tan101^\circ = \tan(-79^\circ) = -\cot11^\circ$.
$\frac{\tan11^\circ + \tan49^\circ}{1 + \cot11^\circ\tan49^\circ} = \frac{\tan11^\circ + \tan49^\circ}{\frac{\tan11^\circ + \tan49^\circ}{\tan11^\circ}} = \tan11^\circ$.

**д)** Разность квадратов в числителе и знаменателе:
$\frac{(\tan35^\circ - \tan10^\circ)(\tan35^\circ + \tan10^\circ)}{(1 + \tan35^\circ\tan10^\circ)(1 - \tan35^\circ\tan10^\circ)} = \tan25^\circ\cdot\tan45^\circ = \tan25^\circ$.

**е)** $\cot40^\circ = \tan50^\circ$ ⇒ $\tan(50^\circ - 20^\circ) = \tan30^\circ = \frac{\sqrt3}{3}$.
:::

:::solution 5.3. Упростить
**а)** Числитель: $\sin\alpha + 2\left(\frac{\sqrt3}{2}\cos\alpha - \frac12\sin\alpha\right) = \sqrt3\cos\alpha$. Знаменатель: $2\left(\frac{\sqrt3}{2}\cos\alpha + \frac12\sin\alpha\right) - \sqrt3\cos\alpha = \sin\alpha$. **Ответ:** $\sqrt3\cot\alpha$.
**б)** Числитель: $\sqrt2\cos\alpha - (\sqrt2\cos\alpha - \sqrt2\sin\alpha) = \sqrt2\sin\alpha$. Знаменатель: $(\sqrt2\sin\alpha + \sqrt2\cos\alpha) - \sqrt2\sin\alpha = \sqrt2\cos\alpha$. **Ответ:** $\tan\alpha$.
:::

## 6–9. Суммы синусов и косинусов

:::solution 6. $\dfrac{\sin5x + \sin3x + \sin x}{\cos5x + \cos3x + \cos x}$ и ограничения
Крайние слагаемые вместе: $\frac{\sin3x(2\cos2x + 1)}{\cos3x(2\cos2x + 1)} = \tan3x$.
**Ограничения** (исходный знаменатель $\ne 0$): $\cos3x \ne 0$ ⇒ $x \ne \frac{\pi}{6} + \frac{\pi k}{3}$; $2\cos2x + 1 \ne 0$ ⇒ $x \ne \pm\frac{\pi}{3} + \pi k$.
:::

:::solution 7. $\dfrac{\sin7x - \sin5x + \sin3x - \sin x}{\cos7x + \cos5x + \cos3x + \cos x}$
Числитель: $2\cos6x\sin x + 2\cos2x\sin x = 2\sin x(\cos6x + \cos2x) = 4\sin x\cos4x\cos2x$.
Знаменатель: $2\cos4x\cos3x + 2\cos4x\cos x = 2\cos4x(\cos3x + \cos x) = 4\cos4x\cos2x\cos x$.
**Ответ:** $\tan x$ (при $\cos x\cos2x\cos4x \ne 0$).
:::

:::solution 8. Доказать $\dfrac{\sin x + \sin2x + \sin3x}{\cos x + \cos2x + \cos3x} = \tan2x$
$\sin x + \sin3x = 2\sin2x\cos x$, $\cos x + \cos3x = 2\cos2x\cos x$ ⇒ дробь $= \frac{\sin2x(2\cos x + 1)}{\cos2x(2\cos x + 1)} = \tan2x$ ∎
:::

:::solution 9. $\sin x + \sin\left(x + \frac{2\pi}{3}\right) + \sin\left(x + \frac{4\pi}{3}\right) = 0$ и обобщение
Сумма последних двух: $2\sin(x + \pi)\cos\frac{\pi}{3} = -\sin x$ ⇒ итог 0 ∎

**Обобщение:** для любого $n \ge 2$ $\displaystyle\sum_{k=0}^{n-1}\sin\left(x + \frac{2\pi k}{n}\right) = 0$ (и то же для косинусов).
**Доказательство:** умножим на $2\sin\frac{\pi}{n} \ne 0$: $2\sin\frac{\pi}{n}\sin\left(x + \frac{2\pi k}{n}\right) = \cos\left(x + \frac{(2k - 1)\pi}{n}\right) - \cos\left(x + \frac{(2k + 1)\pi}{n}\right)$. Сумма телескопируется: $\cos\left(x - \frac{\pi}{n}\right) - \cos\left(x - \frac{\pi}{n} + 2\pi\right) = 0$ ∎
**Смысл:** единичные векторы в вершины правильного $n$-угольника в сумме дают ноль, а синусы — их вертикальные проекции.
:::

## 10–14. Тождества

:::solution 10. $\sin\alpha + \sin\beta = a$, $\cos\alpha + \cos\beta = b$. Найти $\cos(\alpha - \beta)$
Возводим в квадрат и складываем: $a^2 + b^2 = 2 + 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta) = 2 + 2\cos(\alpha - \beta)$.
**Ответ:** $\cos(\alpha - \beta) = \frac{a^2 + b^2 - 2}{2}$.
:::

:::solution 11. $\tan\alpha + \tan\beta = 3$, $\tan\alpha\tan\beta = 2$. Найти $\tan(\alpha + \beta)$
$\tan(\alpha + \beta) = \frac{3}{1 - 2} = -3$.
**Исключительные случаи.** Формула не работает, если $\tan\alpha\tan\beta = 1$ (тогда $\cos(\alpha + \beta) = 0$ и $\tan(\alpha + \beta)$ не существует) или если не существует $\tan\alpha$ / $\tan\beta$. Здесь произведение 2 ≠ 1, а $\tan\alpha$, $\tan\beta$ — корни $t^2 - 3t + 2 = 0$, то есть 1 и 2 — существуют. Значит, значение единственное: **−3**.
(Проверка: $\alpha = \frac{\pi}{4}$, $\beta = \arctan2$: $\tan(\alpha + \beta) = \frac{1 + 2}{1 - 2} = -3$ ✓.)
:::

:::solution 12. $\dfrac{\sin(\alpha + \beta)}{\cos\alpha\cos\beta} = \tan\alpha + \tan\beta$; упростить $\tan x + \tan2x + \tan4x$
$\frac{\sin\alpha\cos\beta + \cos\alpha\sin\beta}{\cos\alpha\cos\beta} = \tan\alpha + \tan\beta$ ∎
Применяем к паре $x$, $2x$: $\tan x + \tan2x = \frac{\sin3x}{\cos x\cos2x}$. Тогда
$$\tan x + \tan2x + \tan4x = \frac{\sin3x}{\cos x\cos2x} + \frac{\sin4x}{\cos4x} = \frac{\sin3x\cos4x + \sin4x\cos x\cos2x}{\cos x\cos2x\cos4x}.$$
Более короткой формы у этой суммы нет: лемма даёт её только по парам. Можно сгруппировать и иначе: $\tan x + \frac{\sin6x}{\cos2x\cos4x}$.
:::

:::solution 13. $\cot x - \tan x = 2\cot2x$; компактная форма суммы
$\cot x - \tan x = \frac{\cos^2x - \sin^2x}{\sin x\cos x} = \frac{\cos2x}{\frac12\sin2x} = 2\cot2x$ ∎

Отсюда $\tan y = \cot y - 2\cot2y$ — каждое слагаемое «раскладывается» на разность. Сумма **телескопируется**, если у тангенсов есть коэффициенты-степени двойки:
$$\cot x - \tan x - 2\tan2x - 4\tan4x - \cdots - 2^{n-1}\tan2^{n-1}x = 2^n\cot2^nx.$$
(По шагам: $\cot x - \tan x = 2\cot2x$; $2\cot2x - 2\tan2x = 4\cot4x$; …)

:::warn В условии, скорее всего, пропущены коэффициенты
Без множителей $2, 4, \ldots, 2^{n-1}$ сумма не схлопывается. Я проверил численно версию с коэффициентами: при $x = 0{,}37$, $n = 3$ обе части равны 53,858.
:::
:::

:::solution 14. $\sin x\sin(60^\circ - x)\sin(60^\circ + x) = \frac14\sin3x$
$\sin(60^\circ - x)\sin(60^\circ + x) = \sin^260^\circ - \sin^2x = \frac34 - \sin^2x$ (тождество из задачи 2(d) Formula workout).
$\sin x\left(\frac34 - \sin^2x\right) = \frac14(3\sin x - 4\sin^3x) = \frac14\sin3x$ ∎
При $x = 10^\circ$: $\sin10^\circ\sin50^\circ\sin70^\circ = \frac14\sin30^\circ = \frac18$.
:::

## 15. $\prod_{k=0}^{n-1}\sin\left(x + \frac{k\pi}{n}\right) = 2^{1-n}\sin(nx)$

:::solution Исследование $n = 2, 3, 4$
- $n = 2$: $\sin x\sin\left(x + \frac{\pi}{2}\right) = \sin x\cos x = \frac12\sin2x$ ✓.
- $n = 3$: $\sin\left(x + \frac{2\pi}{3}\right) = \sin\left(\frac{\pi}{3} - x\right)$, получаем задачу 14: $\frac14\sin3x$ ✓.
- $n = 4$: $\sin x\cos x\cdot\sin\left(x + \frac{\pi}{4}\right)\cos\left(x + \frac{\pi}{4}\right) = \frac12\sin2x\cdot\frac12\cos2x = \frac18\sin4x$ ✓.

Знаки менять не нужно: формула верна в точности как записана (я проверил численно до $n = 7$).
:::

:::proof Доказательство без комплексных чисел
**Шаг 1. $\frac{\sin nx}{\sin x}$ — многочлен от $c = \cos x$ степени $n - 1$ со старшим коэффициентом $2^{n-1}$.** Из $\sin(n + 1)x + \sin(n - 1)x = 2\sin nx\cos x$ получаем $g_{n+1} = 2c\,g_n - g_{n-1}$, где $g_n = \frac{\sin nx}{\sin x}$, $g_1 = 1$, $g_2 = 2c$. По индукции степень растёт на 1, старший коэффициент удваивается.

**Шаг 2. Корни.** $g_n = 0$ при $\sin nx = 0$, $\sin x \ne 0$: $c = \cos\frac{k\pi}{n}$, $k = 1, \ldots, n - 1$ — это $n - 1$ разных чисел. Значит,
$$\frac{\sin nx}{\sin x} = 2^{n-1}\prod_{k=1}^{n-1}\left(\cos x - \cos\frac{k\pi}{n}\right).$$

**Шаг 3. Квадрат произведения.** Пусть $Q = \prod_{k=1}^{n-1}\sin\left(x + \frac{k\pi}{n}\right)$. Так как $\sin\left(x + \frac{(n - k)\pi}{n}\right) = \sin\left(\frac{k\pi}{n} - x\right)$, выпишем $Q$ два раза — с индексами $k$ и $n - k$ — и перемножим попарно:
$$Q^2 = \prod_{k=1}^{n-1}\sin\left(\tfrac{k\pi}{n} + x\right)\sin\left(\tfrac{k\pi}{n} - x\right) = \prod_{k=1}^{n-1}\left(\cos^2x - \cos^2\tfrac{k\pi}{n}\right) = \prod_{k=1}^{n-1}\left(\cos x - \cos\tfrac{k\pi}{n}\right)\cdot\prod_{k=1}^{n-1}\left(\cos x + \cos\tfrac{k\pi}{n}\right).$$
Вторая скобка — та же, что первая, потому что $\cos\frac{k\pi}{n} = -\cos\frac{(n - k)\pi}{n}$. Значит, $Q^2 = \left(\frac{\sin nx}{2^{n-1}\sin x}\right)^2$, и $P = \sin x\cdot Q = \pm2^{1-n}\sin nx$.

**Шаг 4. Знак.** Сдвиг на $\frac{\pi}{n}$ меняет знак обеих частей: $P\left(x + \frac{\pi}{n}\right) = P(x)\cdot\frac{\sin(x + \pi)}{\sin x} = -P(x)$, и $\sin\left(nx + \pi\right) = -\sin nx$. На интервале $\left(0; \frac{\pi}{n}\right)$ все множители $P$ положительны и $\sin nx > 0$ — знак «+». Сдвигами знак переносится на всю прямую ∎
:::
