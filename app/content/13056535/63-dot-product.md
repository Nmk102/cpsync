---
title: "The dot product — решения всех 24 заданий"
kind: solutions
units: []
tasks: [49332750, 49321380]
order: 63
summary: Свойства и геометрический смысл скалярного произведения, углы между векторами, неравенство Коши–Буняковского, скалярные произведения в фигурах (через координаты), задачи с |a|, |b| и углом. Все числа проверены.
---

:::formula Скалярное произведение (*dot product*)
$$\vec v\cdot\vec w = v_1w_1 + v_2w_2 = |\vec v||\vec w|\cos\theta.$$
- $\vec v\cdot\vec v = |\vec v|^2$;
- $\vec v\perp\vec w$ ⇔ $\vec v\cdot\vec w = 0$;
- угол: $\cos\theta = \dfrac{\vec v\cdot\vec w}{|\vec v||\vec w|}$; знак $\vec v\cdot\vec w$ показывает, острый угол (+), прямой (0) или тупой (−).
:::

:::tip Как решать задачи 15–19 (фигуры)
Самый надёжный способ — **координаты**: одну вершину в начало, одну сторону вдоль оси $x$. Найти координаты всех нужных точек, вычесть — получить векторы, перемножить по формуле $v_1w_1 + v_2w_2$.
:::

## 1–3. Свойства и геометрический смысл

:::solution 1. $\vec p = \binom{4}{-3}$, $\vec q = \binom{5}{2}$, $\vec r = \binom{-2}{7}$
(a) $\vec p\cdot\vec q = 20 - 6 = 14 = \vec q\cdot\vec p$.
(b) $\vec p\cdot(2\vec r) = \binom{4}{-3}\cdot\binom{-4}{14} = -16 - 42 = -58$; $2(\vec p\cdot\vec r) = 2(-8 - 21) = -58$.
(c) $\vec p\cdot(\vec q + \vec r) = \binom{4}{-3}\cdot\binom{3}{9} = 12 - 27 = -15$; $\vec p\cdot\vec q + \vec p\cdot\vec r = 14 - 29 = -15$.
(d) В общем виде: $\vec u\cdot\vec v = u_1v_1 + u_2v_2 = v_1u_1 + v_2u_2 = \vec v\cdot\vec u$; $\vec u\cdot(a\vec v) = u_1av_1 + u_2av_2 = a(\vec u\cdot\vec v)$; $\vec u\cdot(\vec v + \vec w) = u_1(v_1 + w_1) + u_2(v_2 + w_2) = \vec u\cdot\vec v + \vec u\cdot\vec w$ — всё следует из свойств обычных чисел ∎
:::

:::solution 2. $\vec v\cdot\vec v = |\vec v|^2$
$\vec v\cdot\vec v = v_1^2 + v_2^2$, а по теореме Пифагора $|\vec v|^2 = v_1^2 + v_2^2$ ∎
:::

:::solution 3. Вывод $\vec v\cdot\vec w = |\vec v||\vec w|\cos\theta$
(a) В треугольнике $WOV$ сторона $WV$ — это вектор $\vec v - \vec w$. Теорема косинусов: $(\vec v - \vec w)\cdot(\vec v - \vec w) = |\vec v - \vec w|^2 = |\vec v|^2 + |\vec w|^2 - 2|\vec v||\vec w|\cos\theta$.
(b) По свойствам из задачи 1: $(\vec v - \vec w)\cdot(\vec v - \vec w) = \vec v\cdot\vec v - 2\vec v\cdot\vec w + \vec w\cdot\vec w = |\vec v|^2 - 2\vec v\cdot\vec w + |\vec w|^2$.
(c) Приравниваем: $-2\vec v\cdot\vec w = -2|\vec v||\vec w|\cos\theta$ ∎
:::

## 4–8. Углы, ортогональность, теория

:::solution 4. Углы между векторами
(a) $\binom{-1}{\sqrt3}\cdot\binom{0}{-2} = -2\sqrt3$, длины 2 и 2: $\cos\theta = -\frac{\sqrt3}{2}$ ⇒ **150°**.
(b) $\binom{12}{-8}\cdot\binom{2}{3} = 24 - 24 = 0$ ⇒ **90°**.
(c) $\binom{2}{1}\cdot\binom{-2 - \sqrt3}{-1 + 2\sqrt3} = -4 - 2\sqrt3 - 1 + 2\sqrt3 = -5$. Длины: $\sqrt5$ и $\sqrt{(2 + \sqrt3)^2 + (2\sqrt3 - 1)^2} = \sqrt{7 + 4\sqrt3 + 13 - 4\sqrt3} = \sqrt{20}$. $\cos\theta = \frac{-5}{\sqrt{100}} = -\frac12$ ⇒ **120°**.
:::

:::solution 5–6
**5.** Стрелки **перпендикулярны** (угол 90°, $\cos\theta = 0$).
**6. Нет.** $\vec p\cdot\vec q = \vec p\cdot\vec r$ ⇔ $\vec p\cdot(\vec q - \vec r) = 0$ — значит только, что $\vec q - \vec r \perp \vec p$. Пример: $\vec p = \binom10$, $\vec q = \binom01$, $\vec r = \binom02$: оба произведения равны 0, но $\vec q \ne \vec r$.
:::

:::solution 7. Доказать $(x_1y_1 + x_2y_2)^2 \le (x_1^2 + x_2^2)(y_1^2 + y_2^2)$
Пусть $\vec x = \binom{x_1}{x_2}$, $\vec y = \binom{y_1}{y_2}$. Тогда левая часть $= (\vec x\cdot\vec y)^2 = |\vec x|^2|\vec y|^2\cos^2\theta \le |\vec x|^2|\vec y|^2$ — это правая часть ∎
**Равенство** ⇔ $\cos^2\theta = 1$ (векторы параллельны) или один из них нулевой ⇔ $x_1y_2 = x_2y_1$.
(Это неравенство Коши–Буняковского.)
:::

:::solution 8. Линейная функция $g$: вектор → число
(a) $g(x\vec i + y\vec j) = g(x\vec i) + g(y\vec j) = x\,g(\vec i) + y\,g(\vec j)$ — сначала свойство (ii), потом (i).
(b) Возьмём $\vec v = \binom{g(\vec i)}{g(\vec j)}$. Тогда $\vec v\cdot\binom{x}{y} = g(\vec i)x + g(\vec j)y = g(\vec w)$ по (a). **Единственность:** если $\vec v\cdot\vec w = \vec v\,'\cdot\vec w$ для всех $\vec w$, подставим $\vec w = \vec i$ и $\vec w = \vec j$: компоненты $\vec v$ и $\vec v\,'$ совпадают.
:::

## 9–14. Вычисления

:::solution 9–12
**9.** (a) $-10 - 12 = -22$; (b) $0 + 3 = 3$.
**10.** $(\vec u - \vec v)\cdot(\vec u + \vec v) = |\vec u|^2 - |\vec v|^2 = 169 - 25 = 144$.
**11.** $\binom{x}{y}\perp\binom{-1}{2}$ ⇔ $-x + 2y = 0$ ⇔ $x = 2y$. Если $x = 5$: $\binom{5}{2{,}5}$; если $y = 5$: $\binom{10}{5}$.
**12.** $\binom{4}{-6}\perp\binom{9}{6}$ ($36 - 36 = 0$) и $\binom{-3}{4}\perp\binom{8}{6}$ ($-24 + 24 = 0$).
:::

:::solution 13. Углы треугольника $A(0; 5)$, $B(1; -3)$, $C(-5; 4)$
$\vec{AB} = (1; -8)$, $\vec{AC} = (-5; -1)$: $\cos A = \frac{-5 + 8}{\sqrt{65}\sqrt{26}} \approx 0{,}073$ ⇒ $\angle A \approx 86^\circ$.
$\vec{BA} = (-1; 8)$, $\vec{BC} = (-6; 7)$: $\cos B = \frac{6 + 56}{\sqrt{65}\sqrt{85}} \approx 0{,}834$ ⇒ $\angle B \approx 33^\circ$.
$\angle C \approx 180^\circ - 86^\circ - 33^\circ = 61^\circ$ (по формуле тоже 60,7° ≈ 61°).
:::

:::solution 14. Ещё одно доказательство через полярные координаты
(a) $\vec v = r_v(\cos\theta_v; \sin\theta_v)$, $\vec w = r_w(\cos\theta_w; \sin\theta_w)$, угол между ними $\varphi = \theta_v - \theta_w$ (косинус от знака не зависит):
$$|\vec v||\vec w|\cos\varphi = r_vr_w\cos(\theta_v - \theta_w).$$
(b) $= r_vr_w(\cos\theta_v\cos\theta_w + \sin\theta_v\sin\theta_w) = (r_v\cos\theta_v)(r_w\cos\theta_w) + (r_v\sin\theta_v)(r_w\sin\theta_w) = v_1w_1 + v_2w_2$ ∎
:::

## 15–19. Скалярные произведения в фигурах

:::solution 15. Прямоугольник $AB = 3$, $AD = 4$
$A(0; 0)$, $B(3; 0)$, $C(3; 4)$, $D(0; 4)$, $O(1{,}5; 2)$.
(a) $\vec{AC}\cdot\vec{BC} = (3; 4)\cdot(0; 4) = 16$.
(b) $\vec{BO}\cdot\vec{CD} = (-1{,}5; 2)\cdot(-3; 0) = 4{,}5$.
(c) $\vec{AC}\cdot\vec{DO} = (3; 4)\cdot(1{,}5; -2) = 4{,}5 - 8 = -3{,}5$.
:::

:::solution 16. Параллелограмм $AB = 4$, $AD = 5$, $\cos\angle DAB = \frac15$, $K$ — середина $CD$
Без координат: $\vec u = \vec{AB}$, $\vec v = \vec{AD}$, $\vec u\cdot\vec v = 4\cdot5\cdot\frac15 = 4$, $|\vec u|^2 = 16$, $|\vec v|^2 = 25$.
(a) $\vec{BD}\cdot\vec{AC} = (\vec v - \vec u)\cdot(\vec v + \vec u) = 25 - 16 = 9$.
(b) $\vec{BK} = \vec v - \frac12\vec u$, $\vec{DC} = \vec u$: $\vec u\cdot\vec v - \frac12|\vec u|^2 = 4 - 8 = -4$.
(c) $\left(\vec v - \frac12\vec u\right)\cdot(\vec u + \vec v) = \vec u\cdot\vec v + 25 - 8 - 2 = 19$.
:::

:::solution 17. $AB = 4$, $BC = 7$, $AC = 5$, $BK : KC = 2 : 1$, $M$ — середина $AK$
Базис $\vec b = \vec{AB}$, $\vec c = \vec{AC}$: $\vec b\cdot\vec c = \frac{16 + 25 - 49}{2} = -4$.
$\vec{AK} = \vec b + \frac23(\vec c - \vec b) = \frac13\vec b + \frac23\vec c$, $\vec{AM} = \frac16\vec b + \frac13\vec c$, $\vec{KM} = -\frac12\vec{AK}$.
(a) $\vec{BC}\cdot\vec{CA} = (\vec c - \vec b)\cdot(-\vec c) = -25 + (-4) = -29$.
(b) $\vec{AB}\cdot\vec{KM} = -\frac12\vec b\cdot\left(\frac13\vec b + \frac23\vec c\right) = -\frac12\left(\frac{16}{3} - \frac83\right) = -\frac43$.
(c) $\vec{BK}\cdot\vec{AM} = \frac23(\vec c - \vec b)\cdot\left(\frac16\vec b + \frac13\vec c\right) = \frac23\left(-\frac46 + \frac{25}{3} - \frac{16}{6} + \frac43\right) = \frac{38}{9}$.
:::

:::solution 18. $AB = 7$, $BC = 8$, $\cos\angle BAC = \frac17$, $Z$ — центроид, $CK = 2$
Сначала $AC = x$: $64 = 49 + x^2 - 2x$ ⇒ $x^2 - 2x - 15 = 0$ ⇒ $x = 5$. Тогда $\vec b\cdot\vec c = 7\cdot5\cdot\frac17 = 5$ ($\vec b = \vec{AB}$, $\vec c = \vec{AC}$).
$\vec{AZ} = \frac{\vec b + \vec c}{3}$, $\vec{AK} = \vec c + \frac14(\vec b - \vec c) = \frac14\vec b + \frac34\vec c$ ($CK = 2 = \frac14 BC$).
(a) $\vec{CZ} = \frac{\vec b - 2\vec c}{3}$: $\vec{AK}\cdot\vec{CZ} = \frac{1}{12}(\vec b + 3\vec c)\cdot(\vec b - 2\vec c) = \frac{1}{12}(49 + 5 - 150) = -8$.
(b) $\vec{AZ}\cdot\vec{BC} = \frac13(\vec b + \vec c)\cdot(\vec c - \vec b) = \frac13(25 - 49) = -8$.
(c) $\vec{ZK} = \vec{AK} - \vec{AZ} = -\frac{1}{12}\vec b + \frac{5}{12}\vec c$: $\vec{ZK}\cdot\vec{AB} = -\frac{49}{12} + \frac{25}{12} = -2$.
:::

:::solution 19. Прямоугольная трапеция $AB = 4$, $BC = 3$, $AD = 6$, $\angle A = 90^\circ$
$A(0; 0)$, $B(0; 4)$, $C(3; 4)$, $D(6; 0)$, $L = (4{,}5; 2)$. $O = AC \cap BD$: треугольники $OBC$ и $ODA$ подобны с коэффициентом $\frac36$, поэтому $AO = \frac23AC$ ⇒ $O\left(2; \frac83\right)$.
(a) $\vec{BL}\cdot\vec{AD} = (4{,}5; -2)\cdot(6; 0) = 27$.
(b) $\vec{AL}\cdot\vec{BO} = (4{,}5; 2)\cdot\left(2; -\frac43\right) = 9 - \frac83 = \frac{19}{3}$.
(c) $\vec{OL}\cdot\vec{AB} = \left(2{,}5; -\frac23\right)\cdot(0; 4) = -\frac83$.
:::

## 20–24. Задачи с длинами и углом

:::solution 20. $|2\vec a + \vec b|$, $|\vec a| = 6$, $|\vec b| = 2$, угол 60°
$|2\vec a + \vec b|^2 = 4\cdot36 + 4 + 4\cdot6\cdot2\cdot\frac12 = 172$ ⇒ $2\sqrt{43}$.
:::

:::solution 21. При каких $a$ $\vec c = a\vec p - 2\vec q \perp \vec d = 15\vec p + a\vec q$; $|\vec p| = 4$, $|\vec q| = 3$, угол 120°
$\vec p\cdot\vec q = 4\cdot3\cdot\left(-\frac12\right) = -6$.
$\vec c\cdot\vec d = 15a\cdot16 + a^2(-6) - 30(-6) - 2a\cdot9 = -6a^2 + 222a + 180 = 0$ ⇔ $a^2 - 37a - 30 = 0$.
**Ответ:** $a = \frac{37 \pm \sqrt{1489}}{2}$ (≈ 37,79 и ≈ −0,79).
:::

:::solution 22. $|\vec a| = 2$, $|\vec b| = 1$, $|3\vec a - 2\vec b| = 4$
$16 = 9\cdot4 + 4\cdot1 - 12\,\vec a\cdot\vec b$ ⇒ $\vec a\cdot\vec b = 2 = |\vec a||\vec b|$ ⇒ $\cos\theta = 1$, **θ = 0** (векторы сонаправлены).
:::

:::solution 23. Угол между $\vec p = 3\vec a + \vec b$ и $\vec q = \vec a - 2\vec b$; $|\vec a| = 1$, $|\vec b| = 2$, $\cos(\vec a, \vec b) = \frac14$
$\vec a\cdot\vec b = 1\cdot2\cdot\frac14 = \frac12$.
$\vec p\cdot\vec q = 3 - 6\cdot\frac12 + \frac12 - 2\cdot4 = -7{,}5$; $|\vec p|^2 = 9 + 6\cdot\frac12 + 4 = 16$; $|\vec q|^2 = 1 - 4\cdot\frac12 + 16 = 15$.
$\cos\theta = \frac{-7{,}5}{4\sqrt{15}} = -\frac{\sqrt{15}}{8}$ ⇒ **$\theta = \arccos\left(-\frac{\sqrt{15}}{8}\right) \approx 119{,}0^\circ$**.
:::

:::solution 24. $|\vec b| = 2$, $|\vec a + 2\vec b| = \sqrt{13}$, $(2\vec a - \vec b)\cdot(3\vec a + \vec b) = 53$
Неизвестные: $x = |\vec a|^2$, $m = \vec a\cdot\vec b$.
- $|\vec a + 2\vec b|^2 = x + 4m + 16 = 13$ ⇒ $x + 4m = -3$;
- $6x + 2m - 3m - 4 = 53$ ⇒ $6x - m = 57$.

Из первого $m = -\frac{3 + x}{4}$; подставляем: $6x + \frac{3 + x}{4} = 57$ ⇒ $25x = 225$ ⇒ $x = 9$, $|\vec a| = 3$, $m = -3$.
$\cos\theta = \frac{-3}{3\cdot2} = -\frac12$ ⇒ **θ = 120°**.
:::
