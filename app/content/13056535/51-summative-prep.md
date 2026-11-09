---
title: "Summative preparation — полные решения всех 25 заданий"
kind: solutions
units: []
tasks: [49227638, 49321380]
order: 51
summary: Тождества, уравнения и неравенства, обратные функции, параметр, графики (с интерактивными графиками), треугольники и пеленги (с чертежами). Все ответы проверены численно.
---

Это пакет подготовки к тригонометрическому summative. Он же — хорошая репетиция к **End of term summative 27 ноября**: там будет всё, что прошли за триместр.

Как пользоваться: сначала решите задание сами, потом откройте «Решение». Все ответы я проверил на компьютере: подстановкой, перебором корней на числовой прямой и построением по координатам.

:::tip Что требуют на summative (из этого же файла)
Точные ответы там, где просят exact: $\frac{\sqrt3}{2}$, а не 0,866. Остальное — 3 значащие цифры, углы — до 0,1°, пеленги — тремя цифрами (*093°*). Промежуточные значения не округлять. Всегда писать ОДЗ (*domain*) и проверять исключённые точки.
:::

## Тождества и точные значения

### Задание 1. Точные значения

:::solution (a) $\dfrac{\cos75^\circ\cos15^\circ + \sin75^\circ\sin15^\circ}{\sin75^\circ\cos30^\circ - \cos75^\circ\sin30^\circ}$
Числитель — косинус разности: $\cos(75^\circ - 15^\circ) = \cos60^\circ = \frac12$.
Знаменатель — синус разности: $\sin(75^\circ - 30^\circ) = \sin45^\circ = \frac{\sqrt2}{2}$.
$$\frac{1/2}{\sqrt2/2} = \frac{1}{\sqrt2} = \frac{\sqrt2}{2}.$$
:::

:::solution (b) $\dfrac{\tan19^\circ + \tan26^\circ}{1 - \tan19^\circ\tan26^\circ}$
Это формула тангенса суммы: $\tan(19^\circ + 26^\circ) = \tan45^\circ = 1$.
:::

:::solution (c) $4\sin15^\circ\sin75^\circ$
$\sin75^\circ = \cos15^\circ$ (дополнительные углы). Тогда $4\sin15^\circ\cos15^\circ = 2\sin30^\circ = 1$.
:::

:::solution (d) $\tan\frac{\pi}{8}$
Формула половинного угла: $\tan\frac{\alpha}{2} = \frac{1 - \cos\alpha}{\sin\alpha}$. При $\alpha = \frac{\pi}{4}$:
$$\tan\frac{\pi}{8} = \frac{1 - \frac{\sqrt2}{2}}{\frac{\sqrt2}{2}} = \frac{2 - \sqrt2}{\sqrt2} = \sqrt2 - 1.$$
:::

### Задание 2. $\sin\alpha = \frac{5}{13}$, $\frac{\pi}{2} < \alpha < \pi$; $\cos\beta = \frac35$, $\frac{3\pi}{2} < \beta < 2\pi$

:::solution Решение
**(a)** α во II четверти, там косинус **отрицательный**: $\cos\alpha = -\sqrt{1 - \frac{25}{169}} = -\frac{12}{13}$.
β в IV четверти, там синус **отрицательный**: $\sin\beta = -\sqrt{1 - \frac{9}{25}} = -\frac45$.

**(b)**
$$\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta = \frac{5}{13}\cdot\frac35 + \left(-\frac{12}{13}\right)\left(-\frac45\right) = \frac{15 + 48}{65} = \frac{63}{65},$$
$$\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta = -\frac{36}{65} - \frac{20}{65} = -\frac{56}{65}.$$

**(c)** $\tan\alpha = \frac{\sin\alpha}{\cos\alpha} = -\frac{5}{12}$:
$$\tan2\alpha = \frac{2\tan\alpha}{1 - \tan^2\alpha} = \frac{-\frac{10}{12}}{1 - \frac{25}{144}} = -\frac{5}{6}\cdot\frac{144}{119} = -\frac{120}{119}.$$
$\frac{3\pi}{4} < \frac{\beta}{2} < \pi$ — II четверть, синус положительный:
$$\sin\frac{\beta}{2} = +\sqrt{\frac{1 - \cos\beta}{2}} = \sqrt{\frac{1 - \frac35}{2}} = \frac{1}{\sqrt5} = \frac{\sqrt5}{5}.$$
:::

### Задание 3. Значения без нахождения $x$

:::solution (a) $\tan\frac{x}{2} = 3$. Найти $\sin x$, $\cos x$, $5(\sin^4x - \cos^4x)$
Универсальная подстановка, $t = 3$:
$$\sin x = \frac{2t}{1 + t^2} = \frac{6}{10} = \frac35,\qquad \cos x = \frac{1 - t^2}{1 + t^2} = -\frac{8}{10} = -\frac45.$$
$\sin^4x - \cos^4x = (\sin^2x - \cos^2x)(\sin^2x + \cos^2x) = \sin^2x - \cos^2x = \frac{9}{25} - \frac{16}{25} = -\frac{7}{25}$, поэтому
$$5(\sin^4x - \cos^4x) = -\frac75.$$
:::

:::solution (b) $\sin x + \cos x = \frac12$. Найти $\sin x\cos x$, $\sin^4x + \cos^4x$, $\sin^6x + \cos^6x$
Обозначим $p = \sin x\cos x$. Возводим в квадрат: $1 + 2p = \frac14 \Rightarrow p = -\frac38$.

$\sin^4x + \cos^4x = (\sin^2x + \cos^2x)^2 - 2p^2 = 1 - 2\cdot\frac{9}{64} = \frac{23}{32}$.

$\sin^6x + \cos^6x = (\sin^2x + \cos^2x)^3 - 3p^2(\sin^2x + \cos^2x) = 1 - 3\cdot\frac{9}{64} = \frac{37}{64}$.
:::

:::key Запомните эти две формулы
$$\sin^4x + \cos^4x = 1 - 2\sin^2x\cos^2x,\qquad \sin^6x + \cos^6x = 1 - 3\sin^2x\cos^2x.$$
:::

### Задание 4. $F(x) = \dfrac{\sin x + \sin3x + \sin5x}{\cos x + \cos3x + \cos5x}$

:::solution Решение
**(a) Разложение.** Группируем крайние: $\sin x + \sin5x = 2\sin3x\cos2x$, $\cos x + \cos5x = 2\cos3x\cos2x$.
$$F(x) = \frac{\sin3x\,(2\cos2x + 1)}{\cos3x\,(2\cos2x + 1)}.$$
Там, где $2\cos2x + 1 \ne 0$ и $\cos3x \ne 0$, $F(x) = \tan3x$. Значит, $F\left(\frac{\pi}{12}\right) = \tan\frac{\pi}{4} = 1$ (в точке $\frac{\pi}{12}$ оба множителя знаменателя не ноль).

**(b) Исключённые точки на $[0; \pi)$** — где знаменатель равен нулю:
- $\cos3x = 0$: $3x = \frac{\pi}{2} + \pi k$, $x = \frac{\pi}{6} + \frac{\pi k}{3}$ → $\frac{\pi}{6},\ \frac{\pi}{2},\ \frac{5\pi}{6}$;
- $2\cos2x + 1 = 0$: $\cos2x = -\frac12$, $2x = \pm\frac{2\pi}{3} + 2\pi k$ → $\frac{\pi}{3},\ \frac{2\pi}{3}$.

Исключаются: $\frac{\pi}{6},\ \frac{\pi}{3},\ \frac{\pi}{2},\ \frac{2\pi}{3},\ \frac{5\pi}{6}$.

**(c)** $\tan3x = 1 \Rightarrow 3x = \frac{\pi}{4} + \pi k \Rightarrow x = \frac{\pi}{12} + \frac{\pi k}{3}$. На $[0; \pi)$: $\frac{\pi}{12},\ \frac{5\pi}{12},\ \frac{3\pi}{4}$. Ни одна не исключена.

**(d) Нет.** При $x = \frac{\pi}{3}$ множитель $2\cos2x + 1 = 0$, поэтому исходная дробь равна $\frac{0}{0}$: числитель $\frac{\sqrt3}{2} + 0 - \frac{\sqrt3}{2} = 0$, знаменатель $\frac12 - 1 + \frac12 = 0$. $F$ в этой точке **не определена**, хотя у упрощённой формулы $\tan\pi = 0$.
:::

:::warn Главный урок задания 4
Сокращать на множитель можно, но точки, где он равен нулю, **остаются исключёнными**. На графике это «выколотые» точки (*holes*).
:::

### Задание 5. $y = 4\sqrt{3\sin x + 4\cos x + 5}$

:::solution Решение
**(a)** $3\sin x + 4\cos x = 5\sin(x + \varphi)$, где $\cos\varphi = \frac35$, $\sin\varphi = \frac45$ (метод вспомогательного угла, $\sqrt{3^2 + 4^2} = 5$). Поэтому $3\sin x + 4\cos x$ принимает **все** значения из $[-5; 5]$.

Подкоренное выражение $\in [0; 10]$ — всегда $\ge 0$, корень определён при всех $x$. Тогда
$$y \in [0;\ 4\sqrt{10}],\qquad 4\sqrt{10} \approx 12{,}65.$$

**(b)** $y$ непрерывно принимает все значения от 0 до $4\sqrt{10}$, а $12 < 4\sqrt{10} < 13$ (потому что $144 < 160 < 169$). Целые значения: $0, 1, 2, \ldots, 12$ — **13 значений**.
:::

## Уравнения, обратные функции, параметр

### Задание 6. Решить уравнения

:::solution (a) $\sin\left(2x - \frac{\pi}{6}\right) = \frac12$
$$2x - \frac{\pi}{6} = \frac{\pi}{6} + 2\pi k\quad\text{или}\quad 2x - \frac{\pi}{6} = \frac{5\pi}{6} + 2\pi k.$$
**Ответ:** $x = \frac{\pi}{6} + \pi k$, $x = \frac{\pi}{2} + \pi k$, $k \in \mathbb Z$.
:::

:::solution (b) $2\sin^2x + \sin x - 1 = 0$
Квадратное относительно $s = \sin x$: $(2s - 1)(s + 1) = 0$.
- $\sin x = \frac12$: $x = \frac{\pi}{6} + 2\pi k$, $x = \frac{5\pi}{6} + 2\pi k$;
- $\sin x = -1$: $x = -\frac{\pi}{2} + 2\pi k$.
:::

:::solution (c) $\dfrac{\sin2x}{1 + \cos x} = 0$
**ОДЗ:** $\cos x \ne -1$, то есть $x \ne \pi + 2\pi k$.
$\sin2x = 0 \Rightarrow x = \frac{\pi k}{2}$. Из этих точек исключаем $x = \pi + 2\pi k$.

**Ответ:** $x = 2\pi k$, $x = \frac{\pi}{2} + \pi k$, $k \in \mathbb Z$.
:::

:::solution (d) $\sin x\sin7x = \sin3x\sin5x$
Произведение в сумму: $\sin a\sin b = \frac12(\cos(a - b) - \cos(a + b))$.
$$\frac12(\cos6x - \cos8x) = \frac12(\cos2x - \cos8x) \iff \cos6x - \cos2x = 0 \iff -2\sin4x\sin2x = 0.$$
$\sin4x = 0 \Rightarrow x = \frac{\pi k}{4}$; $\sin2x = 0 \Rightarrow x = \frac{\pi k}{2}$ — уже входит в первую серию.

**Ответ:** $x = \frac{\pi k}{4}$, $k \in \mathbb Z$.
:::

### Задание 7. Неравенства на $[0; 2\pi)$

:::solution (a) $2\cos^2x - 3\cos x + 1 \le 0$
$(2c - 1)(c - 1) \le 0 \iff \frac12 \le \cos x \le 1$. На единичной окружности это дуга от $-\frac{\pi}{3}$ до $\frac{\pi}{3}$.

**Ответ:** $x \in \left[0; \frac{\pi}{3}\right] \cup \left[\frac{5\pi}{3}; 2\pi\right)$.
:::

:::solution (b) $\sqrt2\sin x < 2 - \sqrt2\cos x$
$\sqrt2(\sin x + \cos x) < 2 \iff 2\sin\left(x + \frac{\pi}{4}\right) < 2 \iff \sin\left(x + \frac{\pi}{4}\right) < 1$.
Синус всегда $\le 1$, и равен 1 только при $x + \frac{\pi}{4} = \frac{\pi}{2} + 2\pi k$, то есть $x = \frac{\pi}{4} + 2\pi k$.

**Ответ:** $x \in \left[0; \frac{\pi}{4}\right) \cup \left(\frac{\pi}{4}; 2\pi\right)$ — всё, кроме $\frac{\pi}{4}$.
:::

### Задание 8. Обратные функции

:::solution (a) $\arcsin\left(\sin\frac{7\pi}{6}\right)$ и $\arccos\left(\cos\frac{7\pi}{4}\right)$
$\sin\frac{7\pi}{6} = -\frac12$, а $\arcsin\left(-\frac12\right) = -\frac{\pi}{6}$ (ответ должен лежать в $\left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$, а не быть $\frac{7\pi}{6}$!).
$\cos\frac{7\pi}{4} = \frac{\sqrt2}{2}$, $\arccos\frac{\sqrt2}{2} = \frac{\pi}{4}$ (диапазон $[0; \pi]$).
:::

:::solution (b) $\sin\left(\arctan\frac34 - \arccos\frac{5}{13}\right)$
$A = \arctan\frac34$: прямоугольный треугольник 3–4–5, $\sin A = \frac35$, $\cos A = \frac45$.
$B = \arccos\frac{5}{13}$: треугольник 5–12–13, $\cos B = \frac{5}{13}$, $\sin B = \frac{12}{13}$ (оба угла острые, все значения положительны).
$$\sin(A - B) = \frac35\cdot\frac{5}{13} - \frac45\cdot\frac{12}{13} = \frac{15 - 48}{65} = -\frac{33}{65}.$$
:::

:::solution (c) $\cot\left(2\arcsin\frac35\right)$
$\theta = \arcsin\frac35$: $\sin\theta = \frac35$, $\cos\theta = \frac45$. $\sin2\theta = \frac{24}{25}$, $\cos2\theta = 1 - 2\cdot\frac{9}{25} = \frac{7}{25}$.
$$\cot2\theta = \frac{7}{24}.$$
:::

:::solution (d) Множество значений $2\arcsin x + 3\arccos x$
$\arccos x = \frac{\pi}{2} - \arcsin x$, поэтому выражение $= 2\arcsin x + \frac{3\pi}{2} - 3\arcsin x = \frac{3\pi}{2} - \arcsin x$.
$\arcsin x \in \left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$ ⇒ **ответ:** $[\pi; 2\pi]$.
:::

### Задание 9. Уравнения с обратными функциями

:::solution (a) $\arccos(2x^2 - 1) = \arccos(3x + 1)$
$\arccos$ убывает на $[-1; 1]$, поэтому разные аргументы дают разные значения. Поэтому равенство ⇔ аргументы равны **и** лежат в $[-1; 1]$.
$2x^2 - 1 = 3x + 1 \iff 2x^2 - 3x - 2 = 0 \iff x = 2$ или $x = -\frac12$.
- $x = 2$: $3x + 1 = 7 \notin [-1; 1]$ — посторонний.
- $x = -\frac12$: $3x + 1 = -\frac12$ ✓.

**Ответ:** $x = -\frac12$.
:::

:::solution (b) $\arcsin3x = \arccos4x$
Пусть обе части равны θ. Левая часть $\in \left[-\frac{\pi}{2}; \frac{\pi}{2}\right]$, правая $\in [0; \pi]$, значит, $\theta \in \left[0; \frac{\pi}{2}\right]$, и $3x = \sin\theta \ge 0$.
$\sin\theta = 3x$, $\cos\theta = 4x$ ⇒ $9x^2 + 16x^2 = 1 \Rightarrow x = \pm\frac15$. Берём $x \ge 0$: $x = \frac15$.
Проверка: $\arcsin0{,}6 = \arccos0{,}8$ — это один и тот же угол треугольника 3–4–5 ✓.

**Ответ:** $x = \frac15$.
:::

### Задание 10. Система на $[0; 2\pi)$: $\sin x\cos y = \frac12$, $\cos x\sin y = -\frac12$

:::solution Решение
**Складываем и вычитаем** уравнения (это равносильный переход — из суммы и разности можно вернуть оба уравнения):
$$\sin(x + y) = 0,\qquad \sin(x - y) = 1.$$
Значит, $x + y = \pi m$, $x - y = \frac{\pi}{2} + 2\pi k$.

**Отбор.** При $x, y \in [0; 2\pi)$: $x - y \in (-2\pi; 2\pi)$ ⇒ $x - y = \frac{\pi}{2}$ или $-\frac{3\pi}{2}$; $x + y \in [0; 4\pi)$ ⇒ $x + y \in \{0, \pi, 2\pi, 3\pi\}$. Перебираем 8 пар, $x = \frac{(x + y) + (x - y)}{2}$, $y = \frac{(x + y) - (x - y)}{2}$:

| $x - y$ | $x + y$ | $(x; y)$ | подходит? |
|---|---|---|---|
| $\frac{\pi}{2}$ | $0$ | $\left(\frac{\pi}{4}; -\frac{\pi}{4}\right)$ | нет |
| $\frac{\pi}{2}$ | $\pi$ | $\left(\frac{3\pi}{4}; \frac{\pi}{4}\right)$ | да |
| $\frac{\pi}{2}$ | $2\pi$ | $\left(\frac{5\pi}{4}; \frac{3\pi}{4}\right)$ | да |
| $\frac{\pi}{2}$ | $3\pi$ | $\left(\frac{7\pi}{4}; \frac{5\pi}{4}\right)$ | да |
| $-\frac{3\pi}{2}$ | $2\pi$ | $\left(\frac{\pi}{4}; \frac{7\pi}{4}\right)$ | да |
| $-\frac{3\pi}{2}$ | $0, \pi, 3\pi$ | выходят за $[0; 2\pi)$ | нет |

**Ответ:** $\left(\frac{3\pi}{4}; \frac{\pi}{4}\right)$, $\left(\frac{5\pi}{4}; \frac{3\pi}{4}\right)$, $\left(\frac{7\pi}{4}; \frac{5\pi}{4}\right)$, $\left(\frac{\pi}{4}; \frac{7\pi}{4}\right)$.
:::

### Задание 11. Параметр: $\sqrt{x - a}\,\sin x = \sqrt{x - a}\,\cos x$ имеет ровно одно решение на $[0; \pi]$

:::solution Решение
**ОДЗ:** $x \ge a$.

Переносим всё влево: $\sqrt{x - a}\,(\sin x - \cos x) = 0$. Кандидаты:
- $x = a$ (корень равен нулю) — годится, если $a \in [0; \pi]$;
- $\sin x = \cos x \Rightarrow x = \frac{\pi}{4}$ (единственный на $[0; \pi]$) — годится, если $\frac{\pi}{4} \ge a$ (ОДЗ).

**Перебираем положение $a$:**

| $a$ | корни на $[0; \pi]$ | сколько |
|---|---|---|
| $a < 0$ | только $\frac{\pi}{4}$ ($x = a$ вне отрезка) | 1 ✓ |
| $0 \le a < \frac{\pi}{4}$ | $a$ и $\frac{\pi}{4}$ | 2 |
| $a = \frac{\pi}{4}$ | $\frac{\pi}{4}$ (корни совпали) | 1 ✓ |
| $\frac{\pi}{4} < a \le \pi$ | только $a$ ($\frac{\pi}{4}$ вне ОДЗ) | 1 ✓ |
| $a > \pi$ | ОДЗ не пересекается с $[0; \pi]$ | 0 |

**Ответ:** $a \in (-\infty; 0) \cup \left[\frac{\pi}{4}; \pi\right]$.
:::

:::warn Где теряют баллы
При $a = 0$ корень $x = 0$ — настоящий (√0 · что угодно = 0), поэтому $a = 0$ **не** подходит. При $a = \frac{\pi}{4}$ два «кандидата» совпадают — это один корень.
:::

## Графики

### Задание 12. $y = 2\sin\left(2x - \frac{\pi}{2}\right) + 1$

:::solution Решение
**(a)** Выносим коэффициент при $x$: $2x - \frac{\pi}{2} = 2\left(x - \frac{\pi}{4}\right)$. Сдвиг вправо на $\frac{\pi}{4}$, **а не** на $\frac{\pi}{2}$.

Удобно заметить: $\sin\left(2x - \frac{\pi}{2}\right) = -\cos2x$, то есть $y = 1 - 2\cos2x$.

**(b)** Амплитуда 2, средняя линия $y = 1$, период $\frac{2\pi}{2} = \pi$, область значений $[-1; 3]$.
- максимумы $y = 3$ при $\cos2x = -1$: $x = \pm\frac{\pi}{2}$;
- минимумы $y = -1$ при $\cos2x = 1$: $x = 0,\ \pm\pi$; пересечение с осью $y$: $(0; -1)$;
- нули: $\cos2x = \frac12 \Rightarrow x = \pm\frac{\pi}{6},\ \pm\frac{5\pi}{6}$.
:::

:::plot
{"title":"y = 2 sin(2x − π/2) + 1 на [−π, π]  (π ≈ 3,14)","x":[-3.3,3.3],"y":[-1.6,3.6],"xstep":1,"ystep":1,
"fns":[{"f":"2*sin(2*x-PI/2)+1","label":"y = 2sin(2x − π/2) + 1","domain":[-3.1416,3.1416]},{"f":"sin(x)","label":"исходная y = sin x","color":4,"dash":true}],
"hlines":[{"y":"1","label":"средняя линия y = 1","color":4}],
"points":[{"x":"PI/2","y":"3","label":"(π/2; 3)"},{"x":"-PI/2","y":"3","label":"(−π/2; 3)"},{"x":"0","y":"-1","label":"(0; −1)"},{"x":"PI/6","y":"0","color":5},{"x":"-PI/6","y":"0","color":5},{"x":"5*PI/6","y":"0","color":5},{"x":"-5*PI/6","y":"0","color":5}],
"note":"Красные точки — нули ±π/6, ±5π/6."}
:::

### Задание 13. $y = \tan\left(\frac{x}{2} + \frac{\pi}{4}\right)$

:::solution Решение
**(a)** $\frac{x}{2} + \frac{\pi}{4} = \frac12\left(x + \frac{\pi}{2}\right)$. Порядок преобразований: $\tan x$ → растяжение по горизонтали в 2 раза ($\tan\frac{x}{2}$, период $2\pi$) → сдвиг **влево** на $\frac{\pi}{2}$.

**Область определения:** $\frac{x}{2} + \frac{\pi}{4} \ne \frac{\pi}{2} + \pi k \iff x \ne \frac{\pi}{2} + 2\pi k$. Период $2\pi$.

**(b)** На $[-\pi; \pi]$ одна асимптота: $x = \frac{\pi}{2}$.
- ноль: $\frac{x}{2} + \frac{\pi}{4} = 0 \Rightarrow x = -\frac{\pi}{2}$; пересечение с $Oy$: $\tan\frac{\pi}{4} = 1$, точка $(0; 1)$;
- концы: $y(-\pi) = \tan\left(-\frac{\pi}{4}\right) = -1$, $y(\pi) = \tan\frac{3\pi}{4} = -1$;
- на $\left[-\pi; \frac{\pi}{2}\right)$ функция возрастает от $-1$ до $+\infty$, на $\left(\frac{\pi}{2}; \pi\right]$ — от $-\infty$ до $-1$.

**Область значений на отрезке:** все действительные числа.
:::

:::plot
{"title":"y = tan(x/2 + π/4)","x":[-3.3,3.3],"y":[-5,5],"xstep":1,"ystep":1,
"fns":[{"f":"tan(x/2+PI/4)","label":"y = tan(x/2 + π/4)","domain":[-3.1416,3.1416]}],
"vlines":[{"x":"PI/2","label":"асимптота x = π/2","color":5}],
"points":[{"x":"-PI/2","y":"0","label":"(−π/2; 0)"},{"x":"0","y":"1","label":"(0; 1)"},{"x":"-PI","y":"-1","label":"(−π; −1)"},{"x":"PI","y":"-1","label":"(π; −1)"}]}
:::

### Задание 14. $y = \dfrac{\sin x + \sin3x}{\sin2x}$

:::solution Решение
**(a)** $\sin x + \sin3x = 2\sin2x\cos x$, поэтому $y = 2\cos x$ при $\sin2x \ne 0$.
Исключены $x = \frac{\pi k}{2}$; на $[-\pi; \pi]$: $-\pi,\ -\frac{\pi}{2},\ 0,\ \frac{\pi}{2},\ \pi$.

**(b)** График — косинусоида $y = 2\cos x$ с выколотыми точками $(-\pi; -2)$, $\left(-\frac{\pi}{2}; 0\right)$, $(0; 2)$, $\left(\frac{\pi}{2}; 0\right)$, $(\pi; -2)$.

Область значений: на каждом из интервалов между выколотыми точками $2\cos x$ пробегает $(0; 2)$ или $(-2; 0)$, а значения $-2$, $0$, $2$ достигаются только в выколотых точках. **Ответ:** $(-2; 0) \cup (0; 2)$. Период исходной функции $2\pi$.
:::

:::plot
{"title":"y = (sin x + sin 3x)/sin 2x = 2cos x с выколотыми точками","x":[-3.4,3.4],"y":[-2.6,2.6],"xstep":1,"ystep":1,
"fns":[{"f":"(sin(x)+sin(3*x))/sin(2*x)","label":"исходная функция","domain":[-3.1416,3.1416]}],
"points":[{"x":"-PI","y":"-2","open":true},{"x":"-PI/2","y":"0","open":true},{"x":"0","y":"2","open":true},{"x":"PI/2","y":"0","open":true},{"x":"PI","y":"-2","open":true}]}
:::

### Задание 15. $y = |\sin^2x + 2\sin x|$

:::solution Решение
**(a)** $\sin^2x + 2\sin x = \sin x\,(\sin x + 2)$, и $\sin x + 2 > 0$ всегда. Значит, знак совпадает со знаком $\sin x$: положительно на $(0; \pi)$, отрицательно на $(-\pi; 0)$, ноль при $x = \pi k$.

**(b)** Пусть $s = \sin x$.
- На $[0; \pi]$: $y = s^2 + 2s$ — растёт с ростом $s \ge 0$. Максимум при $s = 1$: **$\left(\frac{\pi}{2}; 3\right)$**.
- На $[-\pi; 0]$: $y = -(s^2 + 2s) = 1 - (s + 1)^2$ при $s \in [-1; 0]$ — наибольшее при $s = -1$: **$\left(-\frac{\pi}{2}; 1\right)$** (локальный максимум).
- Локальный минимум: **$(0; 0)$** (там $y = 0$, а рядом $y > 0$).

**(c)** Область значений $[0; 3]$, период $2\pi$.
:::

:::plot
{"title":"y = |sin²x + 2 sin x|","x":[-3.4,3.4],"y":[-1.4,3.4],"xstep":1,"ystep":1,
"fns":[{"f":"abs(sin(x)^2+2*sin(x))","label":"y = |sin²x + 2sin x|","domain":[-3.1416,3.1416]},{"f":"sin(x)^2+2*sin(x)","label":"без модуля","color":4,"dash":true}],
"points":[{"x":"PI/2","y":"3","label":"(π/2; 3)"},{"x":"-PI/2","y":"1","label":"(−π/2; 1)"},{"x":"0","y":"0","label":"(0; 0)"}]}
:::

### Задание 16. $g(x) = 2|\sin(2x - \frac{\pi}{2})| - 1$

:::solution Решение
**(a) Цепочка:** $y = \sin x$ → $|\sin x|$ (отражаем нижние части вверх) → $|\sin2x|$ (сжатие к оси $Oy$ в 2 раза) → $\left|\sin\left(2\left(x - \frac{\pi}{4}\right)\right)\right|$ (сдвиг вправо на $\frac{\pi}{4}$) → растяжение по вертикали в 2 раза → сдвиг вниз на 1.

Проще: $\left|\sin\left(2x - \frac{\pi}{2}\right)\right| = |\cos2x|$, так что $g(x) = 2|\cos2x| - 1$.

**(b)** Область значений $[-1; 1]$. Период: у $|\cos2x|$ период $\frac{\pi}{2}$ (модуль делит период $\pi$ пополам).
Нули: $|\cos2x| = \frac12 \Rightarrow 2x = \frac{\pi}{3}, \frac{2\pi}{3}, \frac{4\pi}{3}, \frac{5\pi}{3}$ ⇒ $x = \frac{\pi}{6},\ \frac{\pi}{3},\ \frac{2\pi}{3},\ \frac{5\pi}{6}$.

**(c)** На $[0; \pi)$ значение $g = 1$ достигается при $x = 0,\ \frac{\pi}{2}$; значение $g = -1$ — при $x = \frac{\pi}{4},\ \frac{3\pi}{4}$; любое значение между ними — 4 раза (по разу на каждом из 4 монотонных кусков).

| $a$ | $a < -1$ | $a = -1$ | $-1 < a < 1$ | $a = 1$ | $a > 1$ |
|---|---|---|---|---|---|
| число решений | 0 | 2 | 4 | 2 | 0 |
:::

:::plot
{"title":"g(x) = 2|sin(2x − π/2)| − 1 на [0, π): двигайте a","x":[-0.2,3.35],"y":[-1.5,1.5],"xstep":0.5,"ystep":0.5,
"params":{"a":{"label":"a","min":-1.4,"max":1.4,"step":0.05,"value":0.3}},
"fns":[{"f":"2*abs(sin(2*x-PI/2))-1","label":"y = g(x)","domain":[0,3.1416]}],
"hlines":[{"y":"a","label":"y = a","color":5}],
"out":[{"label":"решений на [0, π)","expr":"(a<-1.0001||a>1.0001)?0:((Math.abs(a-1)<1e-6||Math.abs(a+1)<1e-6)?2:4)"}]}
:::

## Треугольники

### Задание 17. $AB = 9$, $AC = 12$, $\angle A = 60^\circ$

:::solution Решение
**(a) Теорема косинусов** (известны две стороны и угол между ними):
$$BC^2 = 9^2 + 12^2 - 2\cdot9\cdot12\cdot\cos60^\circ = 81 + 144 - 108 = 117,\qquad BC = \sqrt{117} = 3\sqrt{13} \approx 10{,}8\ \text{см}.$$

**(b)** Через косинус — он сразу покажет, острый угол или тупой:
$$\cos B = \frac{AB^2 + BC^2 - AC^2}{2\cdot AB\cdot BC} = \frac{81 + 117 - 144}{2\cdot9\cdot3\sqrt{13}} = \frac{54}{54\sqrt{13}} = \frac{1}{\sqrt{13}}\ \Rightarrow\ \angle B \approx 73{,}9^\circ.$$
(Если считать по теореме синусов, получится $\sin B \approx 0{,}961$ и два кандидата — 73,9° и 106,1°. Косинус > 0 ⇒ угол острый.)

**(c)** $S = \frac12\cdot9\cdot12\cdot\sin60^\circ = 27\sqrt3$ см². Высота к $BC$: $h = \frac{2S}{BC} = \frac{54\sqrt3}{3\sqrt{13}} = \frac{18\sqrt3}{\sqrt{13}} = \frac{18\sqrt{39}}{13} \approx 8{,}65$ см.
:::

### Задание 18. $\angle A = 30^\circ$, $BC = 7$, $AC = 10$ — неоднозначный случай

<svg class="fig" viewBox="0 0 620 280" width="620">
  <line class="l" x1="50.0" y1="230.0" x2="610.0" y2="230.0"/>
  <line class="l" x1="50.0" y1="230.0" x2="240.5" y2="120.0"/>
  <line class="l c3" x1="240.5" y1="120.0" x2="348.3" y2="230.0"/>
  <line class="l c2" x1="240.5" y1="120.0" x2="132.7" y2="230.0"/>
  <path class="l d c4" d="M385.2 172.7 A154 154 0 0 1 95.8 172.7"/>
  <circle class="fi" cx="50.0" cy="230.0" r="3.5"/>
  <text class="i" x="34.0" y="234.0">A</text>
  <circle class="fi" cx="240.5" cy="120.0" r="3.5"/>
  <text class="i" x="236.5" y="110.0">C</text>
  <circle class="fi" cx="348.3" cy="230.0" r="3.5"/>
  <text class="i" x="342.3" y="250.0">B₁</text>
  <circle class="fi" cx="132.7" cy="230.0" r="3.5"/>
  <text class="i" x="124.7" y="250.0">B₂</text>
  <path class="l" d="M86 230 A36 36 0 0 0 81.2 212.0"/>
  <text class="s" x="92.0" y="224.0">30°</text>
  <text class="i" x="115.3" y="167.0">10</text>
  <text class="s tc4" x="430.0" y="60.0">окружность радиуса 7 с центром C</text>
  <text class="s tc4" x="430.0" y="78.0">пересекает луч дважды:</text>
  <text class="s tc3" x="430.0" y="104.0">AB₁ = 5√3 + 2√6 ≈ 13,6</text>
  <text class="s tc2" x="430.0" y="122.0">AB₂ = 5√3 − 2√6 ≈ 3,76</text>
</svg>

:::solution Решение
**(a) Теорема синусов:**
$$\frac{\sin B}{AC} = \frac{\sin A}{BC}\ \Rightarrow\ \sin B = \frac{10\cdot\frac12}{7} = \frac57\ \Rightarrow\ \angle B \approx 45{,}6^\circ\ \text{или}\ \angle B \approx 134{,}4^\circ.$$
Оба подходят: $30^\circ + 134{,}4^\circ < 180^\circ$.

**(b)**
- $\angle B \approx 45{,}6^\circ$: $\angle C \approx 104{,}4^\circ$, $AB = \frac{BC\sin C}{\sin A} \approx 13{,}6$ см.
- $\angle B \approx 134{,}4^\circ$: $\angle C \approx 15{,}6^\circ$, $AB \approx 3{,}76$ см.

Точно (теорема косинусов для угла $A$): $49 = 100 + c^2 - 10\sqrt3\,c \Rightarrow c^2 - 10\sqrt3\,c + 51 = 0 \Rightarrow c = 5\sqrt3 \pm 2\sqrt6$.

**(c) Почему два треугольника.** Сторона $BC = 7$ против данного угла **короче** $AC = 10$, но **длиннее** высоты из $C$: $AC\sin30^\circ = 5$. Окружность радиуса 7 с центром $C$ пересекает луч $AB$ в двух точках (рисунок).
:::

:::key Правило неоднозначного случая (SSA)
Даны угол $A$, сторона $b$ рядом и сторона $a$ напротив. Если $b\sin A < a < b$ — **два** треугольника; $a = b\sin A$ — один (прямоугольный); $a \ge b$ — один; $a < b\sin A$ — ни одного.
:::

### Задание 19. $AB = 13$, $AC = 15$, $BC = 14$, $BD = 5$

:::solution Решение
**(a)** $\cos\angle ABC = \frac{13^2 + 14^2 - 15^2}{2\cdot13\cdot14} = \frac{140}{364} = \frac{5}{13}$.

**(b)** В треугольнике $ABD$: $AD^2 = 13^2 + 5^2 - 2\cdot13\cdot5\cdot\frac{5}{13} = 194 - 50 = 144$, $AD = 12$.
Интересно: $5^2 + 12^2 = 13^2$ — значит, $AD \perp BC$, то есть $AD$ — высота.

**(c)** $\angle ADB = 90^\circ$: $\sin\angle BAD = \frac{5}{13}$ ⇒ $\angle BAD \approx 22{,}6^\circ$. $DC = 9$, $\tan\angle DAC = \frac{9}{12}$ ⇒ $\angle DAC \approx 36{,}9^\circ$.

**(d)** $S_{ABD} = \frac12\cdot5\cdot12 = 30$, $S_{ACD} = \frac12\cdot9\cdot12 = 54$. Отношение $30 : 54 = 5 : 9$, потому что у треугольников **общая высота** $AD$, а основания $BD : DC = 5 : 9$.
:::

### Задание 20. Вписанный четырёхугольник: $AB = 5$, $BC = 6$, $CD = 7$, $DA = 8$

<svg class="fig" viewBox="0 0 480 330" width="480">
  <circle class="l t" cx="220.0" cy="165.0" r="79.3"/>
  <line class="l" x1="173.3" y1="100.9" x2="142.1" y2="179.9"/>
  <line class="l" x1="142.1" y1="179.9" x2="221.2" y2="244.3"/>
  <line class="l" x1="221.2" y1="244.3" x2="298.5" y2="153.9"/>
  <line class="l" x1="298.5" y1="153.9" x2="173.3" y2="100.9"/>
  <line class="l d c5" x1="173.3" y1="100.9" x2="221.2" y2="244.3"/>
  <circle class="fi" cx="173.3" cy="100.9" r="3.5"/>
  <text class="i" x="151.3" y="92.9">A</text>
  <circle class="fi" cx="142.1" cy="179.9" r="3.5"/>
  <text class="i" x="120.1" y="199.9">B</text>
  <circle class="fi" cx="221.2" cy="244.3" r="3.5"/>
  <text class="i" x="231.2" y="264.3">C</text>
  <circle class="fi" cx="298.5" cy="153.9" r="3.5"/>
  <text class="i" x="308.5" y="145.9">D</text>
  <text class="i" x="142.8" y="139.5" text-anchor="middle">5</text>
  <text class="i" x="171.5" y="229.5" text-anchor="middle">6</text>
  <text class="i" x="272.0" y="214.5" text-anchor="middle">7</text>
  <text class="i" x="242.2" y="117.6" text-anchor="middle">8</text>
  <text class="i tc5" x="205.3" y="166.6">x</text>
</svg>

:::solution Решение
**(a)** Теорема косинусов в треугольниках $ABC$ и $ADC$ (общая сторона $AC = x$):
$$\cos\angle ABC = \frac{25 + 36 - x^2}{60} = \frac{61 - x^2}{60},\qquad \cos\angle ADC = \frac{64 + 49 - x^2}{112} = \frac{113 - x^2}{112}.$$

**(b)** Во вписанном четырёхугольнике $\angle ABC + \angle ADC = 180^\circ$, поэтому $\cos\angle ABC = -\cos\angle ADC$:
$$\frac{61 - x^2}{60} = -\frac{113 - x^2}{112} \iff 112(61 - x^2) = -60(113 - x^2) \iff 13\,612 = 172x^2,$$
$$x^2 = \frac{3403}{43},\qquad x = \sqrt{\frac{3403}{43}} \approx 8{,}90\ \text{см}.$$

**(c)** $\cos B = \frac{61 - 3403/43}{60} = -\frac{13}{43}$, $\sin B = \sin D = \sqrt{1 - \frac{169}{1849}} = \frac{4\sqrt{105}}{43}$.
$$S = \frac12\cdot5\cdot6\sin B + \frac12\cdot8\cdot7\sin D = (15 + 28)\cdot\frac{4\sqrt{105}}{43} = 4\sqrt{105} \approx 41{,}0\ \text{см}^2.$$
Проверка формулой Брахмагупты: $p = 13$, $S = \sqrt{8\cdot7\cdot6\cdot5} = \sqrt{1680} = 4\sqrt{105}$ ✓.
:::

## Пеленги (bearings)

:::key Правила пеленгов
- Пеленг — угол **от севера по часовой стрелке**, всегда тремя цифрами: 040°, 125°, 310°.
- Обратный пеленг: $\pm180^\circ$. Если $B$ от $A$ на 038°, то $A$ от $B$ на 218°.
- В каждой точке рисуйте **свою** стрелку севера (они параллельны) — углы между ними переносятся как накрест лежащие / соответственные.
:::

### Задание 21. $A \to B$ на 038°, $B \to C$ на 124°

<svg class="fig" viewBox="0 0 560 330" width="560">
  <line class="l " x1="110.0" y1="290.0" x2="110.0" y2="251.2" style="stroke-width:1.3"/>
  <polygon class="fi" points="110.0,244.0 113.0,251.4 107.0,251.4"/>
  <text class="s" x="106.0" y="238.0">N</text>
  <line class="l " x1="243.0" y1="119.8" x2="243.0" y2="81.0" style="stroke-width:1.3"/>
  <polygon class="fi" points="243.0,73.8 246.0,81.2 240.0,81.2"/>
  <text class="s" x="239.0" y="67.8">N</text>
  <line class="l c3" x1="110.0" y1="290.0" x2="237.4" y2="126.9" style="stroke-width:2"/>
  <polygon class="p3" points="243.0,119.8 240.2,129.4 234.3,124.8"/>
  <line class="l c3" x1="243.0" y1="119.8" x2="399.7" y2="225.5" style="stroke-width:2"/>
  <polygon class="p3" points="407.1,230.5 397.4,228.4 401.5,222.2"/>
  <line class="l d" x1="243.0" y1="119.8" x2="176.5" y2="204.9"/>
  <circle class="fi" cx="110.0" cy="290.0" r="3.5"/>
  <text class="i" x="92.0" y="294.0">A</text>
  <circle class="fi" cx="243.0" cy="119.8" r="3.5"/>
  <text class="i" x="221.0" y="121.8">B</text>
  <circle class="fi" cx="407.1" cy="230.5" r="3.5"/>
  <text class="i" x="415.1" y="234.5">C</text>
  <path class="l c4" d="M110.0 260.0 A30 30 0 0 1 128.5 266.4"/>
  <text class="s tc4" x="125.0" y="251.5" text-anchor="middle">038°</text>
  <path class="l c2" d="M243.0 97.8 A22 22 0 0 1 261.2 132.1"/>
  <text class="s tc2" x="278.3" y="106.0" text-anchor="middle">124°</text>
  <path class="l c5" d="M222.1 146.6 A34 34 0 0 0 271.2 138.8"/>
  <text class="s tc5" x="251.1" y="176.1" text-anchor="middle">94°</text>
  <text class="s" x="330.0" y="40.0">от B на север — 0°,</text>
  <text class="s" x="330.0" y="58.0">на A — 038° + 180° = 218°,</text>
  <text class="s" x="330.0" y="76.0">на C — 124°.</text>
  <text class="i tc5" x="330.0" y="106.0">∠ABC = 218° − 124° = 94°</text>
</svg>

:::solution Решение
**(a)** Пеленг $A$ от $B$: $038^\circ + 180^\circ = 218^\circ$. Из $B$ на $A$ — 218°, на $C$ — 124°, угол между этими направлениями: $\angle ABC = 218^\circ - 124^\circ = 94^\circ$.

**(b)** $124^\circ - 38^\circ = 86^\circ$ — это угол **поворота** курса (насколько лодка «повернула руль»), он измеряется от продолжения отрезка $AB$ за точку $B$. Внутренний угол — дополнение до 180°: $180^\circ - 86^\circ = 94^\circ$.
:::

### Задание 22. Спасательная лодка: 12 км на 040°, затем 18 км на 125°

<svg class="fig" viewBox="0 0 560 330" width="560">
  <line class="l " x1="70.0" y1="260.0" x2="70.0" y2="221.2" style="stroke-width:1.3"/>
  <polygon class="fi" points="70.0,214.0 73.0,221.4 67.0,221.4"/>
  <text class="s" x="66.0" y="208.0">N</text>
  <line class="l " x1="166.4" y1="145.1" x2="166.4" y2="106.3" style="stroke-width:1.3"/>
  <polygon class="fi" points="166.4,99.1 169.4,106.5 163.5,106.5"/>
  <text class="s" x="162.4" y="93.1">N</text>
  <line class="l c3" x1="70.0" y1="260.0" x2="160.6" y2="152.0" style="stroke-width:2"/>
  <polygon class="p3" points="166.4,145.1 163.3,154.6 157.6,149.8"/>
  <text class="i tc3" x="102.4" y="175.1">12 км</text>
  <line class="l c3" x1="166.4" y1="145.1" x2="343.4" y2="269.0" style="stroke-width:2"/>
  <polygon class="p3" points="350.7,274.1 341.0,271.9 345.2,265.8"/>
  <text class="i tc3" x="342.7" y="234.1">18 км</text>
  <line class="l d c5" x1="70.0" y1="260.0" x2="350.7" y2="274.1"/>
  <circle class="fi" cx="70.0" cy="260.0" r="3.5"/>
  <text class="i" x="52.0" y="264.0">H</text>
  <circle class="fi" cx="166.4" cy="145.1" r="3.5"/>
  <text class="i" x="146.4" y="149.1">P</text>
  <circle class="fi" cx="350.7" cy="274.1" r="3.5"/>
  <text class="i" x="358.7" y="280.1">Q</text>
  <path class="l c4" d="M70.0 226.0 A34 34 0 0 1 91.9 234.0"/>
  <text class="s tc4" x="87.8" y="216.1" text-anchor="middle">040°</text>
  <path class="l c2" d="M166.4 123.1 A22 22 0 0 1 184.4 157.7"/>
  <text class="s tc2" x="201.9" y="131.6" text-anchor="middle">125°</text>
  <path class="l c1" d="M147.1 168.1 A30 30 0 0 0 191.0 162.3"/>
  <text class="s tc1" x="172.4" y="195.7" text-anchor="middle">95°</text>
  <path class="l c5" d="M108.6 214.0 A60 60 0 0 1 129.9 263.0"/>
  <text class="s tc5" x="141.5" y="233.8" text-anchor="middle">52,9°</text>
  <text class="s tc5" x="300.0" y="310.0">HQ ≈ 22,5 км, пеленг Q от H ≈ 093°</text>
</svg>

:::solution Решение
**Угол в $P$:** из $P$ на $H$ — пеленг $040^\circ + 180^\circ = 220^\circ$, на $Q$ — 125°. $\angle HPQ = 220^\circ - 125^\circ = 95^\circ$.

**(a)** По теореме косинусов:
$$HQ^2 = 12^2 + 18^2 - 2\cdot12\cdot18\cos95^\circ \approx 468 + 37{,}65 = 505{,}65,\qquad HQ \approx 22{,}5\ \text{км}.$$
По теореме синусов: $\sin\angle PHQ = \frac{18\sin95^\circ}{22{,}487} \approx 0{,}797$ ⇒ $\angle PHQ \approx 52{,}9^\circ$ (острый: он лежит против не самой большой стороны).
Пеленг $Q$ от $H$: $040^\circ + 52{,}9^\circ \approx 093^\circ$.

**(b)** Обратный путь $Q \to H$: $093^\circ + 180^\circ = 273^\circ$.

**(c)** Через $P$: 30 км → 75 мин. Напрямую: $\frac{22{,}49}{24}$ ч ≈ 56,2 мин. Экономия ≈ **19 мин**.
Допущение: скорость постоянна, движение по прямой, нет течения, ветра и препятствий.
:::

### Задание 23. Береговые станции $A$ и $B$ (16 км, $B$ к востоку от $A$); лодка $S$: 032° от $A$, 310° от $B$

<svg class="fig" viewBox="0 0 560 300" width="560">
  <line class="l " x1="80.0" y1="240.0" x2="80.0" y2="193.2" style="stroke-width:1.3"/>
  <polygon class="fi" points="80.0,186.0 83.0,193.4 77.0,193.4"/>
  <text class="s" x="76.0" y="180.0">N</text>
  <line class="l " x1="432.0" y1="240.0" x2="432.0" y2="193.2" style="stroke-width:1.3"/>
  <polygon class="fi" points="432.0,186.0 435.0,193.4 429.0,193.4"/>
  <text class="s" x="428.0" y="180.0">N</text>
  <line class="l" x1="80.0" y1="240.0" x2="432.0" y2="240.0"/>
  <line class="l" x1="80.0" y1="240.0" x2="201.1" y2="46.2"/>
  <line class="l" x1="432.0" y1="240.0" x2="201.1" y2="46.2"/>
  <line class="l d c5" x1="201.1" y1="46.2" x2="201.1" y2="240.0"/>
  <circle class="fi" cx="80.0" cy="240.0" r="3.5"/>
  <text class="i" x="62.0" y="244.0">A</text>
  <circle class="fi" cx="432.0" cy="240.0" r="3.5"/>
  <text class="i" x="440.0" y="244.0">B</text>
  <circle class="fi" cx="201.1" cy="46.2" r="3.5"/>
  <text class="i" x="197.1" y="34.2">S</text>
  <circle class="fi" cx="201.1" cy="240.0" r="3.5"/>
  <text class="i" x="207.1" y="258.0">F</text>
  <path class="l c4" d="M80.0 210.0 A30 30 0 0 1 95.9 214.6"/>
  <text class="s tc4" x="92.7" y="200.8" text-anchor="middle">032°</text>
  <path class="l c2" d="M432.0 218.0 A22 22 0 1 1 415.1 225.9"/>
  <text class="s tc2" x="448.1" y="279.4" text-anchor="middle">310°</text>
  <path class="l c1" d="M120.0 240.0 A40 40 0 0 0 101.2 206.1"/>
  <text class="s tc1" x="129.0" y="217.9" text-anchor="middle">58°</text>
  <path class="l c1" d="M392.0 240.0 A40 40 0 0 1 401.4 214.3"/>
  <text class="s tc1" x="379.4" y="225.8" text-anchor="middle">40°</text>
  <path class="l c1" d="M186.2 70.0 A28 28 0 0 0 222.5 64.2"/>
  <text class="s tc1" x="208.0" y="94.7" text-anchor="middle">82°</text>
  <text class="s" x="256.0" y="262.0" text-anchor="middle">16 км</text>
  <text class="s tc5" x="209.1" y="143.1">≈ 8,81 км</text>
</svg>

:::solution Решение
**(a) Углы.** Из $A$ на $B$ — 090°, на $S$ — 032°: $\angle A = 90^\circ - 32^\circ = 58^\circ$. Из $B$ на $A$ — 270°, на $S$ — 310°: $\angle B = 40^\circ$. $\angle S = 180^\circ - 58^\circ - 40^\circ = 82^\circ$.
Теорема синусов:
$$AS = \frac{16\sin40^\circ}{\sin82^\circ} \approx 10{,}4\ \text{км},\qquad BS = \frac{16\sin58^\circ}{\sin82^\circ} \approx 13{,}7\ \text{км}.$$

**(b)** Расстояние от $S$ до $AB$: $h = AS\sin58^\circ \approx 8{,}81$ км. Основание перпендикуляра $F$: $AF = AS\cos58^\circ \approx 5{,}50$ км, $BF = BS\cos40^\circ \approx 10{,}50$ км, в сумме 16 км ✓. Оба угла при основании острые ⇒ $F$ лежит **на отрезке** $AB$.

**(c)** Отвечать должна станция $A$ (она ближе): $\frac{10{,}39}{20}$ ч ≈ 31 мин против $\frac{13{,}70}{20}$ ч ≈ 41 мин — примерно на **10 мин** раньше.
Допущения: лодки готовы одновременно, идут по прямой с постоянной скоростью, лодка $S$ стоит на месте, нет течения и препятствий.
:::

### Задание 24. Дорога $A \to B$ 24 км на 070°, лагерь $C$ 18 км от $A$ на 110°

<svg class="fig" viewBox="0 0 600 300" width="600">
  <line class="l " x1="60.0" y1="170.0" x2="60.0" y2="131.2" style="stroke-width:1.3"/>
  <polygon class="fi" points="60.0,124.0 63.0,131.4 57.0,131.4"/>
  <text class="s" x="56.0" y="118.0">N</text>
  <line class="l " x1="364.5" y1="280.8" x2="364.5" y2="242.0" style="stroke-width:1.3"/>
  <polygon class="fi" points="364.5,234.8 367.4,242.2 361.5,242.2"/>
  <text class="s" x="360.5" y="228.8">N</text>
  <line class="l c3" x1="60.0" y1="170.0" x2="465.9" y2="22.2"/>
  <line class="l" x1="60.0" y1="170.0" x2="364.5" y2="280.8"/>
  <line class="l d c5" x1="364.5" y1="280.8" x2="293.2" y2="85.1"/>
  <circle class="fi" cx="60.0" cy="170.0" r="3.5"/>
  <text class="i" x="42.0" y="174.0">A</text>
  <circle class="fi" cx="465.9" cy="22.2" r="3.5"/>
  <text class="i" x="473.9" y="26.2">B</text>
  <circle class="fi" cx="364.5" cy="280.8" r="3.5"/>
  <text class="i" x="372.5" y="294.8">C</text>
  <circle class="fi" cx="293.2" cy="85.1" r="3.5"/>
  <text class="i" x="287.2" y="73.1">F</text>
  <path class="l c4" d="M60.0 140.0 A30 30 0 0 1 88.2 159.7"/>
  <text class="s tc4" x="87.5" y="135.7" text-anchor="middle">070°</text>
  <path class="l c2" d="M60.0 114.0 A56 56 0 0 1 112.6 189.2"/>
  <text class="s tc2" x="119.0" y="133.7" text-anchor="middle">110°</text>
  <path class="l c1" d="M364.5 256.8 A24 24 0 1 1 356.3 258.3"/>
  <text class="s tc1" x="371.4" y="325.2" text-anchor="middle">340°</text>
  <text class="s tc5" x="338.8" y="183.0">≈ 11,6 км</text>
  <text class="s tc3" x="315.0" y="72.1">дорога 24 км</text>
</svg>

:::solution Решение
**(a)** $\angle CAB = 110^\circ - 70^\circ = 40^\circ$. Кратчайшее расстояние до прямой — перпендикуляр $CF$:
$$CF = 18\sin40^\circ \approx 11{,}6\ \text{км},\qquad AF = 18\cos40^\circ \approx 13{,}8\ \text{км} < 24.$$
$0 < AF < AB$, значит, $F$ лежит на отрезке дороги.

**(b)** $CF \perp AB$, а дорога идёт на 070°. Перпендикулярные направления: $070^\circ \pm 90^\circ$ = 160° или 340°. Лагерь лежит **справа** от дороги (110° — по часовой от 070°), значит, к дороге нужно идти влево-вверх: **340°**.

**(c)** $\frac{11{,}57}{4} \approx 2{,}89$ ч ≈ 2 ч 54 мин < 3 ч — **успеет**, но с запасом всего ~6 мин. Реальность: рельеф, лес, река, отдых, невозможность идти строго по прямой — любой из факторов может «съесть» эти 6 минут.
:::

### Задание 25. Две лодки из $O$: $A$ — 18 км/ч на 050°, $B$ — 26 км/ч на 130°

<svg class="fig" viewBox="0 0 560 330" width="560">
  <line class="l " x1="100.0" y1="150.0" x2="100.0" y2="111.2" style="stroke-width:1.3"/>
  <polygon class="fi" points="100.0,104.0 103.0,111.4 97.0,111.4"/>
  <text class="s" x="96.0" y="98.0">N</text>
  <line class="l " x1="243.4" y1="270.3" x2="243.4" y2="237.5" style="stroke-width:1.3"/>
  <polygon class="fi" points="243.4,230.3 246.4,237.8 240.4,237.8"/>
  <text class="s" x="239.4" y="224.3">N</text>
  <line class="l c3" x1="100.0" y1="150.0" x2="192.4" y2="72.5" style="stroke-width:2"/>
  <polygon class="p3" points="199.3,66.7 194.5,75.5 189.8,69.8"/>
  <line class="l c2" x1="100.0" y1="150.0" x2="236.5" y2="264.5" style="stroke-width:2"/>
  <polygon class="p2" points="243.4,270.3 233.9,267.2 238.7,261.5"/>
  <text class="s tc3" x="97.6" y="108.3">27 км</text>
  <text class="s tc2" x="121.7" y="224.2">39 км</text>
  <line class="l d c5" x1="199.3" y1="66.7" x2="243.4" y2="270.3"/>
  <circle class="fi" cx="100.0" cy="150.0" r="3.5"/>
  <text class="i" x="82.0" y="154.0">O</text>
  <circle class="fi" cx="199.3" cy="66.7" r="3.5"/>
  <text class="i" x="207.3" y="62.7">A</text>
  <circle class="fi" cx="243.4" cy="270.3" r="3.5"/>
  <text class="i" x="251.4" y="278.3">B</text>
  <path class="l c1" d="M123.0 130.7 A30 30 0 0 1 123.0 169.3"/>
  <text class="s tc1" x="146.0" y="155.0" text-anchor="middle">80°</text>
  <text class="s tc5" x="231.3" y="168.5">≈ 43,4 км</text>
  <text class="s" x="330.0" y="40.0">через 1,5 ч:</text>
  <text class="s" x="330.0" y="58.0">OA = 18·1,5 = 27 км</text>
  <text class="s" x="330.0" y="76.0">OB = 26·1,5 = 39 км</text>
  <text class="s" x="330.0" y="106.0">угол AOB = 130° − 50° = 80°</text>
</svg>

:::solution Решение
**(a)** Через 1,5 ч: $OA = 27$ км, $OB = 39$ км, $\angle AOB = 130^\circ - 50^\circ = 80^\circ$.
$$AB^2 = 27^2 + 39^2 - 2\cdot27\cdot39\cos80^\circ \approx 1884{,}3,\qquad AB \approx 43{,}4\ \text{км}.$$
Пеленг $A$ от $B$: удобно через координаты (восток; север): $A \approx (20{,}68;\ 17{,}36)$, $B \approx (29{,}88;\ -25{,}07)$. $\vec{BA} \approx (-9{,}19;\ 42{,}42)$ — почти на север и немного на запад: угол от севера $\arctan\frac{9{,}19}{42{,}42} \approx 12{,}2^\circ$ к западу ⇒ пеленг $360^\circ - 12{,}2^\circ \approx 348^\circ$.

**(b)** Треугольники $OAB$ в разные моменты **подобны** (угол 80° тот же, стороны растут пропорционально $t$), поэтому расстояние растёт линейно:
$$d(t) = t\sqrt{18^2 + 26^2 - 2\cdot18\cdot26\cos80^\circ} \approx 28{,}94\,t.$$
$d = 45 \Rightarrow t \approx 1{,}555$ ч ≈ **1 ч 33 мин**.
Это верно, потому что лодки стартуют из одной точки одновременно и не меняют скорость и курс.
:::
