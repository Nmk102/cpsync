---
title: Векторы — геометрия и скалярное произведение
kind: notes
units: [2103928, 2030257]
tasks: [49291935, 49305694, 49332750, 49321380]
order: 60
summary: Сложение, разложение по базису, деление отрезка, доказательства «параллельно / на одной прямой», скалярное произведение и угол.
---

Юнит *Vectors & Spatial Dynamics*. Три листка: IGCSE Vectors, Vectors in geometry, Dot product. В экзаменационных задачах векторы нужны для двух вещей: **доказать** что-то о фигуре и **посчитать** угол или длину.

## 1. Основы

- Вектор $\overrightarrow{AB}$ — направленный отрезок; задаётся **длиной** и **направлением**. В координатах $\overrightarrow{AB} = (x_B - x_A;\ y_B - y_A)$.
- Длина: $|\vec a| = \sqrt{a_x^2 + a_y^2}$.
- **Правило треугольника**: $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$. **Правило параллелограмма**: сумма — диагональ.
- $\overrightarrow{BA} = -\overrightarrow{AB}$; $\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}$ («конец минус начало»).
- $k\vec a$ — вектор в $|k|$ раз длиннее; при $k < 0$ — противоположного направления.

## 2. Коллинеарность и «на одной прямой»

:::key Два главных доказательства
- $\vec a \parallel \vec b$ (**коллинеарны**) $\iff$ $\vec b = k\vec a$ для некоторого числа $k$.
- Точки $A$, $B$, $C$ лежат **на одной прямой** $\iff$ $\overrightarrow{AC} = k\,\overrightarrow{AB}$ (векторы с **общей точкой** коллинеарны).
:::

Формулировка для экзамена: *"$\overrightarrow{AC} = 3\,\overrightarrow{AB}$, so $AC$ is parallel to $AB$ and they share point $A$; therefore $A$, $B$, $C$ are collinear."*

## 3. Деление отрезка в отношении

Если точка $P$ делит $AB$ в отношении $AP : PB = m : n$, то
$$\overrightarrow{AP} = \frac{m}{m + n}\overrightarrow{AB}, \qquad \overrightarrow{OP} = \frac{n\,\overrightarrow{OA} + m\,\overrightarrow{OB}}{m + n}.$$
Середина: $\overrightarrow{OM} = \dfrac{\overrightarrow{OA} + \overrightarrow{OB}}{2}$. Точка пересечения медиан: $\overrightarrow{OG} = \dfrac{\overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC}}{3}$.

## 4. Метод «два пути» (задачи IGCSE)

Задан базис $\vec a$, $\vec b$ (например, $\overrightarrow{OA} = \vec a$, $\overrightarrow{OB} = \vec b$). Нужно найти отношение, в котором точка пересечения делит отрезки.

1. Выразите искомый вектор **двумя способами**, вводя неизвестные множители $\lambda$ и $\mu$.
2. Приравняйте: коэффициенты при $\vec a$ и при $\vec b$ должны совпасть (они неколлинеарны).
3. Решите систему.

:::example В треугольнике $OAB$ точка $M$ — середина $OB$, $N$ делит $OA$ в отношении $1:2$ (от $O$). Отрезки $AM$ и $BN$ пересекаются в $X$. Найти $AX : XM$.
Пусть $\overrightarrow{OA} = \vec a$, $\overrightarrow{OB} = \vec b$.

**Путь 1:** $\overrightarrow{OX} = \overrightarrow{OA} + \lambda\overrightarrow{AM} = \vec a + \lambda\left(\tfrac12\vec b - \vec a\right) = (1 - \lambda)\vec a + \tfrac\lambda2\vec b$.

**Путь 2:** $\overrightarrow{OX} = \overrightarrow{OB} + \mu\overrightarrow{BN} = \vec b + \mu\left(\tfrac13\vec a - \vec b\right) = \tfrac\mu3\vec a + (1 - \mu)\vec b$.

Приравниваем: $1 - \lambda = \frac\mu3$, $\frac\lambda2 = 1 - \mu$. Из второго $\mu = 1 - \frac\lambda2$; подставляем: $1 - \lambda = \frac13 - \frac\lambda6 \Rightarrow \frac23 = \frac{5\lambda}6 \Rightarrow \lambda = \frac45$.

$AX : XM = \lambda : (1 - \lambda) = 4 : 1$.
:::

## 5. Скалярное произведение (*dot product*)

:::formula Два способа посчитать
$$\vec a\cdot\vec b = |\vec a|\,|\vec b|\cos\theta = a_xb_x + a_yb_y\ (+\,a_zb_z)$$
:::

| Что даёт | Формула |
|---|---|
| угол между векторами | $\cos\theta = \dfrac{\vec a\cdot\vec b}{|\vec a|\,|\vec b|}$ |
| перпендикулярность | $\vec a \perp \vec b \iff \vec a\cdot\vec b = 0$ |
| длина | $\vec a\cdot\vec a = |\vec a|^2$ |
| знак | $> 0$ — угол острый, $< 0$ — тупой |
| проекция $\vec a$ на $\vec b$ | $\dfrac{\vec a\cdot\vec b}{|\vec b|}$ |

Свойства: $\vec a\cdot\vec b = \vec b\cdot\vec a$; $\vec a\cdot(\vec b + \vec c) = \vec a\cdot\vec b + \vec a\cdot\vec c$; $(\vec a + \vec b)^2 = a^2 + 2\vec a\cdot\vec b + b^2$.

:::warn Нулевой вектор (замечание учителя к суммативной)
У нулевого вектора **есть** скалярное произведение ($\vec 0\cdot\vec b = 0$), но **нет** определённого направления. Поэтому фраза «$\vec a\cdot\vec b = 0$, значит, векторы перпендикулярны» верна только для **ненулевых** векторов — оговаривайте это.
:::

:::example Угол между $\vec a = (3;\,4)$ и $\vec b = (4;\,-3)$; между $\vec c = (1;\,2)$ и $\vec d = (3;\,1)$
$\vec a\cdot\vec b = 12 - 12 = 0$ → $90^\circ$.

$\vec c\cdot\vec d = 3 + 2 = 5$, $|\vec c| = \sqrt5$, $|\vec d| = \sqrt{10}$: $\cos\theta = \frac{5}{\sqrt{50}} = \frac{1}{\sqrt2}$ → $\theta = 45^\circ$.
:::

:::example Доказательство через скалярное произведение: диагонали ромба перпендикулярны
Ромб со сторонами $\vec a$ и $\vec b$, $|\vec a| = |\vec b|$. Диагонали $\vec a + \vec b$ и $\vec a - \vec b$:
$(\vec a + \vec b)\cdot(\vec a - \vec b) = |\vec a|^2 - |\vec b|^2 = 0$ ✓.
:::

## 6. Проверь себя

:::task 1. $A(1;\,2)$, $B(4;\,6)$, $C(10;\,14)$. Лежат ли точки на одной прямой?
:::answer
$\overrightarrow{AB} = (3;\,4)$, $\overrightarrow{AC} = (9;\,12) = 3\overrightarrow{AB}$, общая точка $A$ → **да**.
:::
:::

:::task 2. При каком $k$ векторы $(2;\,k)$ и $(k - 1;\,3)$ перпендикулярны?
:::answer
$2(k - 1) + 3k = 0 \Rightarrow k = \frac25$.
:::
:::

:::task 3. $|\vec a| = 3$, $|\vec b| = 4$, угол между ними $60^\circ$. Найдите $|\vec a + \vec b|$.
:::answer
$|\vec a + \vec b|^2 = 9 + 2\cdot3\cdot4\cdot\frac12 + 16 = 37$ → $\sqrt{37}$.
:::
:::
