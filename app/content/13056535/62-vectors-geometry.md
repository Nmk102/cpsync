---
title: "Vectors and geometry — решения заданий 0–7"
kind: solutions
units: []
tasks: [49305694, 49321380]
order: 62
summary: Длина суммы векторов через теорему косинусов и координаты, центроид, разложение по двум векторам, биссектриса, точки на прямой с условием на длину, параллелограмм и трапеция. Все длины проверены по координатам.
---

:::key Два способа найти длину векторного выражения
**1. Через два базисных вектора и угол между ними.** Выразите всё через $\vec u$, $\vec v$ из одной точки (угол θ между ними):
$$|p\vec u + q\vec v|^2 = p^2|\vec u|^2 + q^2|\vec v|^2 + 2pq|\vec u||\vec v|\cos\theta.$$
**2. Через координаты.** Поставьте фигуру на удобные оси (одну сторону — на ось $x$), найдите координаты точек и считайте как с числами. Я проверял каждый ответ вторым способом.
:::

## 0. Равнобедренный треугольник $AB = BC = 8$, $AC = 6$, $Z$ — центроид

:::solution Решение
Координаты: $A(-3; 0)$, $C(3; 0)$, $B(0; \sqrt{55})$ (высота $\sqrt{64 - 9}$). Центроид — среднее вершин: $Z\left(0; \frac{\sqrt{55}}{3}\right)$.

**(a)** $\vec{AB} + \vec{AC} = 2\vec{AD}$, где $D$ — середина $BC$ (правило параллелограмма). Координатами: $(3; \sqrt{55}) + (6; 0) = (9; \sqrt{55})$, длина $\sqrt{81 + 55} = \sqrt{136} = 2\sqrt{34}$.

**(b)** $\vec{BZ} + \vec{CB} = \vec{CB} + \vec{BZ} = \vec{CZ}$ (правило треугольника). $\vec{CZ} = \left(-3; \frac{\sqrt{55}}{3}\right)$, длина $\sqrt{9 + \frac{55}{9}} = \frac{2\sqrt{34}}{3}$.

**(c)** Для центроида $\vec{ZA} + \vec{ZB} + \vec{ZC} = \vec 0$, поэтому $\vec{AZ} + \vec{BZ} = -(\vec{ZA} + \vec{ZB}) = \vec{ZC}$. Длина та же: $\frac{2\sqrt{34}}{3}$.
:::

## 1. $AC = 4\sqrt2$, $BC = 6$, $\angle C = 45^\circ$, $CK = 2$

:::solution Решение
Координаты: $C(0; 0)$, $B(6; 0)$, $A(4; 4)$ (под 45° на расстоянии $4\sqrt2$), $K(2; 0)$.

**(a)** $BA^2 = 32 + 36 - 2\cdot4\sqrt2\cdot6\cdot\frac{\sqrt2}{2} = 20$ ⇒ $BA = 2\sqrt5$.
**(b)** $\vec{BM} = \vec{AC}$ ⇒ $\vec{AM} = \vec{AB} + \vec{BM} = \vec{AB} + \vec{AC}$. $M = B + \vec{AC} = (6 - 4; 0 - 4) = (2; -4)$, $\vec{AM} = (-2; -8)$, $AM = 2\sqrt{17}$.
**(c)** $N = B + \vec{AK} = (6 - 2; 0 - 4) = (4; -4)$, $CN = \sqrt{16 + 16} = 4\sqrt2$.
:::

## 2. $AB = 7$, $BC = 9$, $AC = 6$

:::solution Решение
Базис: $\vec{AB}$, $\vec{AC}$, угол $A$: $\cos A = \frac{49 + 36 - 81}{2\cdot7\cdot6} = \frac{1}{21}$, значит, $\vec{AB}\cdot\vec{AC} = 7\cdot6\cdot\frac{1}{21} = 2$ — пригодится во всех пунктах.

**(a)** $\left|\vec{AB} + \frac23\vec{AC}\right|^2 = 49 + \frac49\cdot36 + 2\cdot\frac23\cdot2 = 65 + \frac83 = \frac{203}{3}$ ⇒ $\sqrt{\frac{203}{3}} = \frac{\sqrt{609}}{3} \approx 8{,}23$.

**(b)** $\vec{CB} = \vec{AB} - \vec{AC}$ ⇒ $\frac12\vec{AB} + \frac23\vec{CB} = \frac76\vec{AB} - \frac23\vec{AC}$.
$|\ldots|^2 = \frac{49}{36}\cdot49 + \frac49\cdot36 - 2\cdot\frac76\cdot\frac23\cdot2 = \frac{2401}{36} + 16 - \frac{28}{9} = \frac{2865}{36}$ ⇒ $\frac{\sqrt{2865}}{6} \approx 8{,}92$.

**(c)** $\vec{BN} = \vec{AN} - \vec{AB} = \frac23(\vec{AB} - \vec{AC}) - \vec{AB} = -\frac13\vec{AB} - \frac23\vec{AC}$. Тогда $\frac12\vec{AC} + \vec{BN} = -\frac13\vec{AB} - \frac16\vec{AC}$:
$|\ldots|^2 = \frac{49}{9} + 1 + 2\cdot\frac13\cdot\frac16\cdot2 = \frac{60}{9}$ ⇒ $\frac{2\sqrt{15}}{3} \approx 2{,}58$.
:::

## 3. $AK : AC = 2 : 3$, $BL : BC = 3 : 4$, $AL \cap BK = O$

:::solution Решение
$A$ — начало, $\vec b = \vec{AB}$, $\vec c = \vec{AC}$. Тогда $\vec{AK} = \frac23\vec c$, $\vec{AL} = \vec b + \frac34(\vec c - \vec b) = \frac14\vec b + \frac34\vec c$, $\vec{BK} = \frac23\vec c - \vec b$.

**(a)** Из $\vec{AL}$: $\vec c = \frac{4\vec{AL} - \vec b}{3}$. Подставим в $\vec{BK}$: $\vec{BK} = \frac29(4\vec{AL} - \vec b) - \vec b = \frac89\vec{AL} - \frac{11}{9}\vec b$ ⇒
$$\vec{AB} = \frac{8}{11}\vec{AL} - \frac{9}{11}\vec{BK}.$$

**(b)** $O = s\cdot\vec{AL} = \vec b + u\,\vec{BK}$: $\frac s4\vec b + \frac{3s}{4}\vec c = (1 - u)\vec b + \frac{2u}{3}\vec c$ ⇒ $\frac s4 = 1 - u$, $\frac{3s}{4} = \frac{2u}{3}$ ⇒ $s = \frac{8}{11}$.
$\vec{AO} = \frac{8}{11}\vec{AL}$ ⇒ $\vec{LO} = -\frac{3}{11}\vec{AL}$ ⇒ $\vec{AL} = -\frac{11}{3}\vec{LO}$, **$t = -\frac{11}{3}$** (знак минус: $\vec{LO}$ смотрит обратно к $A$).

**(c)** $\vec{CO} = \vec{AO} - \vec c = \frac{8}{11}\left(\frac14\vec b + \frac34\vec c\right) - \vec c = \frac{2}{11}\vec b - \frac{5}{11}\vec c$. Выражаем $\vec b$ из (a) и $\vec c = \frac{12\vec{AL} + 3\vec{BK}}{11}$:
$$\vec{CO} = -\frac{4}{11}\vec{AL} - \frac{3}{11}\vec{BK}.$$
:::

## 4. Биссектриса $AL$ и вектор $\vec u = \frac{\vec{AB}}{AB} + \frac{\vec{AC}}{AC}$

:::solution Решение
**(a)** $\frac{\vec{AB}}{AB}$ и $\frac{\vec{AC}}{AC}$ — единичные векторы вдоль сторон угла $A$. Их сумма — диагональ **ромба** со сторонами 1, а диагональ ромба делит его угол пополам. Значит, $\vec u$ направлен по биссектрисе, как $\vec{AL}$ ∎

**(b)** По свойству биссектрисы $BL : LC = AB : AC = c : b$ ($c = AB$, $b = AC$). Тогда
$$\vec{AL} = \frac{b\,\vec{AB} + c\,\vec{AC}}{b + c} = \frac{bc}{b + c}\left(\frac{\vec{AB}}{c} + \frac{\vec{AC}}{b}\right) = \frac{bc}{b + c}\,\vec u.$$
**Ответ:** $\lambda = \frac{AB\cdot AC}{AB + AC}$.
:::

## 5. $A(-2; -4)$, $B(6; 2)$, $C(1; 5)$

:::solution Решение
**(a)** $K$ — середина $AB$: $(2; -1)$. $CK = \sqrt{1^2 + 6^2} = \sqrt{37}$.

**(b)** Прямая (а не отрезок!) — две точки:
- внутри отрезка: $N = A + \frac13\vec{AC} = (-2 + 1; -4 + 3) = (-1; -1)$;
- за точкой $A$: $N = A - \vec{AC} = (-5; -13)$ (тогда $AN = AC$, $CN = 2AC$).

**(c)** $\vec{AM} = s\vec{AB} = (8s; 6s)$, $\vec{BC} = (-5; 3)$. $2\vec{AM} - \vec{BC} = (16s + 5;\ 12s - 3)$.
$(16s + 5)^2 + (12s - 3)^2 = 90$ ⇔ $400s^2 + 88s - 56 = 0$ ⇔ $50s^2 + 11s - 7 = 0$ ⇒ $s = \frac{-11 \pm 39}{100}$: $s = 0{,}28$ или $s = -0{,}5$.
**Ответ:** $M\left(\frac{6}{25}; -\frac{58}{25}\right)$ и $M(-6; -7)$.
:::

## 6. Параллелограмм $AB = 6$, $AD = 4$, $\cos\angle DAB = -\frac23$, $AM : MB = 3 : 2$

:::solution Решение
$\vec u = \vec{AB}$, $\vec v = \vec{AD}$, $\vec u\cdot\vec v = 6\cdot4\cdot\left(-\frac23\right) = -16$. Точки: $M = \frac35\vec u$, $O = \frac{\vec u + \vec v}{2}$, $C = \vec u + \vec v$.

**(a)** $\vec{CM} = -\frac25\vec u - \vec v$, $\vec{OM} = \frac{1}{10}\vec u - \frac12\vec v$ ⇒ $\vec u = 10\vec{OM} + 5\vec v$:
$$\vec{CM} = -4\vec{OM} - 3\vec{AD}.$$
**(b)** $\vec{OA} = -\frac{\vec u + \vec v}{2}$. Решая систему, $\vec u = \frac53(\vec{CM} - 2\vec{OA})$, $\vec v = \frac43\vec{OA} - \frac53\vec{CM}$:
$$\vec{BD} = \vec v - \vec u = \frac{14}{3}\vec{OA} - \frac{10}{3}\vec{CM}.$$
**(c)** $\vec{CO} - \vec{AD} = -\frac12\vec u - \frac32\vec v$.
$|\ldots|^2 = \frac14\cdot36 + \frac94\cdot16 + 2\cdot\frac12\cdot\frac32\cdot(-16) = 9 + 36 - 24 = 21$ ⇒ **$\sqrt{21}$**.
:::

## 7. Трапеция: $AD \parallel BC$, $\angle A = 90^\circ$, $\angle D = 60^\circ$, $BC = 3$, $AD = 8$

:::solution Решение
Координаты: $A(0; 0)$, $D(8; 0)$, $B(0; h)$, $C(3; h)$. Угол $D = 60^\circ$: $\tan60^\circ = \frac{h}{8 - 3}$ ⇒ $h = 5\sqrt3$.
$M = \left(\frac{11}{2}; \frac{5\sqrt3}{2}\right)$. Прямая $AM$: точки $t\cdot M$; на высоте $5\sqrt3$ при $t = 2$ ⇒ $L(11; 5\sqrt3)$ — **за точкой $C$** на продолжении $BC$.

**(a)** $\vec{AD} = \frac83\vec{BC}$, $\vec{AB} = \vec{AD} - \vec{BD} = \frac83\vec{BC} - \vec{BD}$, $\vec{AC} = \vec{AB} + \vec{BC} = \frac{11}{3}\vec{BC} - \vec{BD}$.
$$\vec{AM} = \frac{\vec{AC} + \vec{AD}}{2} = \frac{19}{6}\vec{BC} - \frac12\vec{BD}.$$
**(b)** $\vec{DL} = (3; 5\sqrt3)$, $\vec{AB} = (0; 5\sqrt3)$, $\vec{CM} = \left(\frac52; -\frac{5\sqrt3}{2}\right)$. Ищем $\alpha\vec{AB} + \beta\vec{CM}$: по $x$ $\frac52\beta = 3$ ⇒ $\beta = \frac65$; по $y$ $5\alpha - 3 = 5$ ⇒ $\alpha = \frac85$.
$$\vec{DL} = \frac85\vec{AB} + \frac65\vec{CM}.$$
**(c)** $\vec{AC} + 2\vec{BC} - \frac12\vec{DB} = (3; 5\sqrt3) + (6; 0) + \left(4; -\frac{5\sqrt3}{2}\right) = \left(13; \frac{5\sqrt3}{2}\right)$.
Длина $\sqrt{169 + \frac{75}{4}} = \frac{\sqrt{751}}{2} \approx 13{,}7$.
:::
