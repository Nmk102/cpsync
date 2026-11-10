---
title: Блоки — часть 1. Задачи 1–17 с подробными решениями
kind: solutions
units: [2043420]
tasks: []
order: 25
summary: Полные решения задач 1.1–3.7 листка «Pulleys»: машина Атвуда, грузы на столе, подвижные блоки, «выигрыш в силе» в 2 и 4 раза и три ловушки, где натяжение равно нулю.
---

Сначала прочитайте конспект **«Блоки, нити, тележки и клинья — метод решения»**. Там объяснены правила, которыми мы пользуемся в каждой задаче: силы на невесомом блоке, длина нити и энергетическая проверка.

**Как устроен каждый разбор.** Рисунок из листка с подписями: синие буквы — блоки, оранжевые — натяжения нитей. Затем подсказка (откройте её и попробуйте решить сам). Затем полное решение по шагам и проверка.

**Соглашения во всех задачах.** Вертикальные координаты $y$ отсчитываем **от потолка вниз**, поэтому ускорение $a > 0$ означает движение **вниз**. Горизонтальная координата $x$ у тела на столе направлена **к краю стола** (к блоку). Блоки и нити невесомые, трения нет.

---

## Задача 1 (1.1). Машина Атвуда

<svg class="fig scanfig" viewBox="0 0 184 224" style="width:230px" role="img" aria-label="Задача 1"><image class="scan" href="/fig/pul/01.png" width="184" height="224"/><text class="lb lt" x="30" y="120" text-anchor="middle">T</text><text class="lb lt" x="125" y="120" text-anchor="middle">T</text></svg>

**Ответ учителя:** $a = \dfrac{m_1 - m_2}{m_1 + m_2}\,g$.

:::hint Подсказка
Одна нить, один неподвижный блок — натяжение одинаково с обеих сторон. Если один груз опускается на 1 см, другой на 1 см поднимается.
:::

:::solution Решение
**Связь.** Длина нити $y_1 + y_2 + \text{const}$. Значит, $a_2 = -a_1$: сколько один опустился, столько другой поднялся.

**Уравнения** (ось вниз, на каждый груз нить тянет вверх силой $T$):
$$m_1 a_1 = m_1 g - T, \qquad m_2 a_2 = m_2 g - T \;\Rightarrow\; -m_2 a_1 = m_2 g - T.$$

**Решаем.** Вычтем второе из первого, $T$ сократится:
$$(m_1 + m_2)a_1 = (m_1 - m_2) g \;\Rightarrow\; a_1 = \frac{m_1 - m_2}{m_1 + m_2}\,g.$$
Натяжение: $T = m_1(g - a_1) = \dfrac{2m_1 m_2}{m_1 + m_2}\,g$.

**Проверка.**
- $m_1 = m_2$: $a = 0$, равновесие. Верно.
- $m_2 \to 0$: $a \to g$, груз $m_1$ падает свободно. Верно.
- $T$ лежит между $m_2 g$ и $m_1 g$: лёгкий груз нить тянет сильнее его веса (он ускоряется вверх), тяжёлый — слабее. Верно.
- **Энергией:** $k_1 = 1$, $k_2 = -1$, поэтому $a = g\dfrac{m_1 - m_2}{m_1 + m_2}$. Совпало.
:::

## Задача 2 (1.2). Брусок на столе и висящий груз

<svg class="fig scanfig" viewBox="0 0 231 209" style="width:289px" role="img" aria-label="Задача 2"><image class="scan" href="/fig/pul/02.png" width="231" height="209"/><text class="lb lt" x="128" y="32" text-anchor="middle">T</text><text class="lb lt" x="178" y="95" text-anchor="middle">T</text></svg>

**Ответ учителя:** $a = \dfrac{m}{m + M}\,g$.

:::hint Подсказка
Брусок по горизонтали тянет только нить, вес бруска уравновешен столом. Ускорения бруска и груза по величине равны.
:::

:::solution Решение
**Связь.** Длина нити равна $(x_{\text{блока}} - x) + y$. Значит, $a_x = a_y = a$: брусок едет к краю, груз опускается с тем же ускорением.

**Уравнения:**
- брусок $M$ (по горизонтали): $Ma = T$;
- груз $m$ (вниз): $ma = mg - T$.

**Решаем.** Сложим уравнения: $(M + m)a = mg$, откуда $a = \dfrac{m}{M + m}\,g$, $T = \dfrac{Mm}{M + m}\,g$.

**Смысл.** Сила $mg$ разгоняет **оба** тела сразу, общей массой $M + m$.

**Проверка.** При $M \to 0$ получаем $a \to g$, при $M \to \infty$ получаем $a \to 0$, $T \to mg$. Натяжение меньше веса груза, иначе он бы не опускался с ускорением.
:::

## Задача 3 (1.3). Два бруска на столе

<svg class="fig scanfig" viewBox="0 0 348 209" style="width:435px" role="img" aria-label="Задача 3"><image class="scan" href="/fig/pul/03.png" width="348" height="209"/><text class="lb lt" x="127" y="32" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="250" y="32" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="298" y="95" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text></svg>

**Ответ учителя:** $a = \dfrac{m}{m + M_1 + M_2}\,g$.

:::hint Подсказка
Все три тела движутся с одним ускорением. Нитей две: между $M_1$ и $M_2$ натяжение $T_1$, между $M_2$ и грузом — $T_2$.
:::

:::solution Решение
**Уравнения** (ускорение $a$ у всех одинаковое):
$$M_1 a = T_1, \qquad M_2 a = T_2 - T_1, \qquad m a = mg - T_2.$$
**Решаем.** Сумма трёх уравнений: $(M_1 + M_2 + m)a = mg$, натяжения сокращаются, потому что они **внутренние**. Получаем
$$a = \frac{m}{m + M_1 + M_2}\,g,\qquad T_1 = \frac{M_1 m}{m + M_1 + M_2}\,g,\qquad T_2 = \frac{(M_1 + M_2)m}{m + M_1 + M_2}\,g.$$

**Смысл натяжений.** Нить $T_1$ разгоняет только $M_1$, нить $T_2$ разгоняет $M_1 + M_2$. Поэтому $T_2 > T_1$.
:::

## Задача 4 (1.4). Брусок между двумя грузами

<svg class="fig scanfig" viewBox="0 0 345 209" style="width:431px" role="img" aria-label="Задача 4"><image class="scan" href="/fig/pul/04.png" width="345" height="209"/><text class="lb lt" x="22" y="88" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="105" y="32" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="245" y="32" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="322" y="95" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text></svg>

**Ответ учителя:** $a = \dfrac{m_2 - m_1}{M + m_1 + m_2}\,g$.

:::hint Подсказка
Пусть брусок едет вправо, к грузу $m_2$. Тогда $m_2$ опускается, а $m_1$ поднимается, и все трое с одинаковым по величине ускорением. Натяжения левой и правой нитей разные.
:::

:::solution Решение
Пусть $a$ — ускорение бруска вправо. Тогда $m_2$ опускается с ускорением $a$, а $m_1$ поднимается с ускорением $a$.

**Уравнения:**
$$m_2 a = m_2 g - T_2, \qquad M a = T_2 - T_1, \qquad m_1 a = T_1 - m_1 g.$$
**Решаем.** Сумма: $(m_1 + M + m_2)a = (m_2 - m_1)g$, откуда
$$a = \frac{m_2 - m_1}{M + m_1 + m_2}\,g.$$
Натяжения: $T_1 = m_1(g + a) = \dfrac{m_1(M + 2m_2)}{M + m_1 + m_2}g$, $\;T_2 = m_2(g - a) = \dfrac{m_2(M + 2m_1)}{M + m_1 + m_2}g$.

**Проверка.** При $m_1 = m_2$ получаем $a = 0$. При $M = 0$ задача становится машиной Атвуда (задача 1), и ответ совпадает. Если $a < 0$, всё едет влево.
:::

---

## Задача 5 (2.1). Неподвижный и подвижный блок

<svg class="fig scanfig" viewBox="0 0 205 327" style="width:256px" role="img" aria-label="Задача 5"><image class="scan" href="/fig/pul/05.png" width="205" height="327"/><text class="lb lt" x="28" y="190" text-anchor="middle">T</text><text class="lb lt" x="190" y="120" text-anchor="middle">T</text><text class="lb lt" x="168" y="232" text-anchor="middle">2T</text><text class="lb lp" x="90" y="124" text-anchor="middle">A</text><text class="lb lp" x="158" y="194" text-anchor="middle">B</text></svg>

**Ответ учителя:** $a_2 = \dfrac{m_2 - 2m_1}{4m_1 + m_2}\,g$.

:::hint Подсказка
Груз $m_2$ висит на **подвижном** блоке $B$, который огибает одна нить с натяжением $T$. Значит, вверх его тянет $2T$. А $m_1$ движется вдвое быстрее, чем $B$.
:::

:::solution Решение
Эта задача подробно разобрана в конспекте-методе. Кратко:

**Связь.** Нить: $m_1 \to A \to$ под $B \to$ потолок. Длина $y_1 + 2y_B + \text{const}$, поэтому $a_1 = -2a_2$.

**Уравнения:**
$$m_1 a_1 = m_1 g - T, \qquad m_2 a_2 = m_2 g - 2T.$$
**Решаем.** Из первого с $a_1 = -2a_2$: $T = m_1 g + 2m_1 a_2$. Подставим во второе:
$$m_2 a_2 = m_2 g - 2m_1 g - 4m_1 a_2 \;\Rightarrow\; a_2 = \frac{m_2 - 2m_1}{m_2 + 4m_1}\,g.$$
Ещё: $a_1 = -2a_2 = \dfrac{2(2m_1 - m_2)}{4m_1 + m_2}g$, $\;T = \dfrac{3m_1 m_2}{4m_1 + m_2}g$.

**Проверка.**
- Равновесие при $m_2 = 2m_1$: тогда $T = m_1 g$, и блок держит $2T = 2m_1 g = m_2 g$. Подвижный блок даёт выигрыш в силе в 2 раза.
- При $m_1 = 0$ получаем $a_2 = g$. Верно.
- Энергией: $k_2 = 1$, $k_1 = -2$, поэтому $a = g\dfrac{m_2 - 2m_1}{m_2 + 4m_1}$. Совпало.
:::

## Задача 6 (2.2). Брусок на столе тянет подвижный блок

<svg class="fig scanfig" viewBox="0 0 273 310" style="width:341px" role="img" aria-label="Задача 6"><image class="scan" href="/fig/pul/06.png" width="273" height="310"/><text class="lb lt" x="118" y="86" text-anchor="middle">T</text><text class="lb lt" x="164" y="160" text-anchor="middle">T</text><text class="lb lt" x="258" y="120" text-anchor="middle">T</text><text class="lb lt" x="232" y="232" text-anchor="middle">2T</text><text class="lb lp" x="226" y="194" text-anchor="middle">B</text></svg>

**Ответ учителя:** $a_m = \dfrac{m}{4M + m}\,g$.

:::hint Подсказка
Это задача 5, где $m_1$ лежит на столе. Брусок $M$ движется вдвое быстрее груза. На брусок действует только $T$, а на груз (вместе с блоком $B$) вверх действует $2T$.
:::

:::solution Решение
**Связь.** Нить: $M \to$ блок у края $\to$ вниз под $B \to$ вверх к потолку. Длина $(x_{\text{края}} - x) + (y_B - y_{\text{края}}) + y_B$, то есть $-x + 2y_B + \text{const}$. Значит, $a_M = 2a_m$.

**Уравнения:**
$$M a_M = T, \qquad m a_m = mg - 2T.$$
**Решаем.** $T = M a_M = 2M a_m$. Тогда $m a_m = mg - 4M a_m$, откуда
$$a_m = \frac{m}{m + 4M}\,g,\qquad a_M = \frac{2m}{m + 4M}\,g,\qquad T = \frac{2Mm}{4M + m}\,g.$$

**Проверка.** Энергией: $k_m = 1$ (вниз), $k_M = 2$ (по горизонтали, в числитель не входит). Получаем $a = g\dfrac{m}{m + 4M}$. Коэффициент 4 при $M$ — это $2^2$, потому что брусок движется вдвое быстрее.
:::

## Задача 7 (2.3). Подвижный блок лежит на столе

<svg class="fig scanfig" viewBox="0 0 319 290" style="width:399px" role="img" aria-label="Задача 7"><image class="scan" href="/fig/pul/07.png" width="319" height="290"/><text class="lb lt" x="100" y="44" text-anchor="middle">T</text><text class="lb lt" x="145" y="112" text-anchor="middle">T</text><text class="lb lt" x="225" y="77" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="300" y="165" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="190" y="96" text-anchor="middle">P</text></svg>

**Ответ учителя:** $a_m = \dfrac{m}{4M + m}\,g$ (тот же, что в задаче 6).

:::hint Подсказка
Большой блок $P$ подвижный, но движется **горизонтально**. Нить от стены огибает его и привязана к бруску $M$. За ось $P$ привязана вторая нить, она идёт через угловой блок к грузу $m$. Чему равно натяжение второй нити, если первая огибает $P$ с натяжением $T$?
:::

:::solution Решение
**Обозначения.** $x_M$ и $x_P$ — координаты бруска и блока $P$ вправо, $y$ — координата груза вниз. Натяжения $T$ (нить «стена → $P$ → брусок») и $T_2$ (нить «ось $P$ → угловой блок → груз»).

**Связи.**
- Нить 1: от стены до верха $P$ длина $x_P - x_{\text{ст}}$, от низа $P$ обратно до бруска длина $x_P - x_M$. Сумма $2x_P - x_M = \text{const}$, поэтому $a_M = 2a_P$.
- Нить 2: $(x_{\text{угл}} - x_P) + y = \text{const}$, поэтому $a_m = a_P$.

Итого: груз и блок $P$ движутся с ускорением $a$, а брусок с ускорением $2a$.

**Силы.**
- Блок $P$ невесомый: нить 1 тянет его влево двумя ветвями ($2T$), нить 2 тянет вправо ($T_2$). Отсюда $T_2 = 2T$.
- Брусок: $M \cdot 2a = T$.
- Груз: $ma = mg - T_2 = mg - 2T$.

**Решаем.** $T = 2Ma$, поэтому $ma = mg - 4Ma$ и
$$a = \frac{m}{m + 4M}\,g,\qquad a_M = \frac{2m}{m + 4M}\,g.$$

:::

:::tip Почему ответ как в задаче 6
Устройство то же: брусок связан с грузом «через подвижный блок», только блок повёрнут на 90°. Энергетическая проверка даёт те же коэффициенты: $k_m = 1$, $k_M = 2$.
:::

## Задача 8 (2.4). Блок, перевёрнутый «вверх ногами»

<svg class="fig scanfig" viewBox="0 0 268 292" style="width:335px" role="img" aria-label="Задача 8"><image class="scan" href="/fig/pul/08.png" width="268" height="292"/><text class="lb lt" x="140" y="44" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="213" y="105" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="182" y="240" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="248" y="172" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="212" y="152" text-anchor="middle">P</text></svg>

**Ответ учителя:** $a_m = \dfrac{4m}{4m + M}\,g$.

:::hint Подсказка
Посмотрите внимательно на блок $P$. Нить 2 идёт от пола **вверх**, огибает $P$ сверху и спускается к грузу $m$. Обе её ветви тянут $P$ **вниз**. А вверх $P$ тянет нить 1, привязанная к его оси и идущая через угловой блок к бруску. Кто движется быстрее: $P$ или груз?
:::

:::solution Решение
**Обозначения.** $x$ — смещение бруска к краю, $y_P$ — координата блока $P$ вниз, $y$ — координата груза вниз. Натяжения $T_1$ (брусок → ось $P$) и $T_2$ (пол → $P$ → груз).

**Связи.**
- Нить 1: $(x_{\text{угл}} - x) + (y_P - y_{\text{угл}}) = \text{const}$, поэтому $a_P = a_M$. Брусок сдвинулся к краю на 1 см, блок опустился на 1 см.
- Нить 2: $(y_{\text{пола}} - y_P) + (y - y_P) = \text{const}$, поэтому $a_m = 2a_P$. Когда блок опускается на 1 см, левая ветвь (до пола) укорачивается на 1 см, и это «лишний» сантиметр нити уходит к грузу. Груз опускается на 2 см.

**Силы.**
- Блок $P$ (невесомый): вверх $T_1$, вниз $2T_2$. Значит, $T_1 = 2T_2$.
- Брусок: $M a_M = T_1 = 2T_2$, где $a_M = a_m/2$. Отсюда $T_2 = \dfrac{M a_m}{4}$.
- Груз: $m a_m = mg - T_2$.

**Решаем.** $m a_m = mg - \dfrac{M}{4}a_m$, откуда
$$a_m = \frac{4m}{4m + M}\,g,\qquad a_M = \frac{2m}{4m + M}\,g,\qquad T_2 = \frac{Mm}{M + 4m}\,g,\quad T_1 = \frac{2Mm}{M + 4m}\,g.$$

**Проверка.** Энергией возьмём $v = v_m$: тогда $k_m = 1$, $k_M = \tfrac12$. Получаем $a = g\dfrac{m}{m + M/4}$. Совпало. Здесь, в отличие от задачи 6, **груз** движется вдвое быстрее бруска, поэтому масса $M$ входит с множителем $\tfrac14$.
:::

## Задача 9 (2.5). То же, но вместо бруска — висящий груз

<svg class="fig scanfig" viewBox="0 0 188 328" style="width:235px" role="img" aria-label="Задача 9"><image class="scan" href="/fig/pul/09.png" width="188" height="328"/><text class="lb lt" x="25" y="150" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="124" y="128" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="90" y="270" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="160" y="205" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="90" y="90" text-anchor="middle">A</text><text class="lb lp" x="124" y="190" text-anchor="middle">B</text></svg>

**Ответ учителя:** $a_1 = \dfrac{m_1 - 2m_2}{m_1 + 4m_2}\,g$.

:::hint Подсказка
Блок $B$ устроен как блок $P$ в задаче 8: нить от пола огибает его сверху и идёт к $m_2$. Значит, $T_1 = 2T_2$ и $a_2 = 2a_B$. А $B$ связан с $m_1$ через неподвижный блок $A$.
:::

:::solution Решение
**Связи.**
- Нить 1 ($m_1 \to A \to$ ось $B$): $y_1 + y_B = \text{const}$, поэтому $a_B = -a_1$.
- Нить 2 (пол $\to B \to m_2$): $y_2 - 2y_B = \text{const}$, поэтому $a_2 = 2a_B = -2a_1$.

**Силы.** Блок $B$: $T_1 = 2T_2$. Груз $m_1$: $m_1 a_1 = m_1 g - T_1 = m_1 g - 2T_2$. Груз $m_2$: $m_2 a_2 = m_2 g - T_2$.

**Решаем.** Из уравнения для $m_2$ с $a_2 = -2a_1$: $T_2 = m_2 g + 2m_2 a_1$. Подставим в уравнение для $m_1$:
$$m_1 a_1 = m_1 g - 2m_2 g - 4m_2 a_1 \;\Rightarrow\; a_1 = \frac{m_1 - 2m_2}{m_1 + 4m_2}\,g.$$
Ещё: $a_2 = -2a_1$, $\;T_2 = \dfrac{3m_1 m_2}{m_1 + 4m_2}g$, $\;T_1 = 2T_2$.

**Проверка.** Равновесие при $m_1 = 2m_2$: блок $B$ держит $m_2$ «вдвое», то есть $T_1 = 2m_2 g = m_1 g$. Энергией: $k_1 = 1$, $k_2 = -2$, поэтому $a = g\dfrac{m_1 - 2m_2}{m_1 + 4m_2}$. Совпало.
:::

## Задача 10 (2.6). Два подвижных блока подряд — выигрыш в 4 раза

<svg class="fig scanfig" viewBox="0 0 238 327" style="width:298px" role="img" aria-label="Задача 10"><image class="scan" href="/fig/pul/10.png" width="238" height="327"/><text class="lb lt" x="28" y="180" text-anchor="middle">T</text><text class="lb lt" x="120" y="95" text-anchor="middle">T</text><text class="lb lt" x="128" y="170" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="222" y="120" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="197" y="240" text-anchor="middle">2T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="88" y="74" text-anchor="middle">A</text><text class="lb lp" x="157" y="135" text-anchor="middle">B</text><text class="lb lp" x="190" y="210" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_2 = \dfrac{m_2 - 4m_1}{16m_1 + m_2}\,g$.

:::hint Подсказка
Блок $B$ — подвижный, его огибает нить с натяжением $T$. Значит, нить, привязанная к оси $B$, имеет натяжение $2T$. Эта нить огибает подвижный блок $C$, поэтому $C$ (с грузом $m_2$) тянут вверх силой $4T$. Скорости: $m_1$ движется в 2 раза быстрее $B$, а $B$ — в 2 раза быстрее $C$.
:::

:::solution Решение
**Обозначения.** Нить 1 (натяжение $T$): $m_1 \to A \to$ под $B \to$ потолок. Нить 2 (натяжение $T_2$): ось $B \to$ под $C \to$ потолок.

**Связи.**
- Нить 1: $y_1 + 2y_B = \text{const}$, поэтому $a_1 = -2a_B$.
- Нить 2: $(y_C - y_B) + y_C = \text{const}$, поэтому $a_B = 2a_C$.
- Итого: $a_1 = -4a_C$.

**Силы.**
- Блок $B$: вверх $2T$, вниз $T_2$, поэтому $T_2 = 2T$.
- Блок $C$ с грузом: вверх $2T_2 = 4T$, и $m_2 a_C = m_2 g - 4T$.
- Груз $m_1$: $m_1 a_1 = m_1 g - T$.

**Решаем.** $-4m_1 a_C = m_1 g - T$, откуда $T = m_1 g + 4m_1 a_C$. Тогда
$$m_2 a_C = m_2 g - 4m_1 g - 16m_1 a_C \;\Rightarrow\; a_C = \frac{m_2 - 4m_1}{m_2 + 16m_1}\,g.$$
Ещё: $T = \dfrac{5m_1 m_2}{16m_1 + m_2}g$, $\;a_1 = \dfrac{4(4m_1 - m_2)}{16m_1 + m_2}g$.

**Проверка.** Равновесие при $m_2 = 4m_1$: два подвижных блока дают выигрыш в силе $2 \cdot 2 = 4$. Энергией: $k_2 = 1$, $k_1 = -4$, поэтому $a = g\dfrac{m_2 - 4m_1}{m_2 + 16m_1}$. Совпало.
:::

---

## Задача 11 (3.1). Ловушка: груз падает свободно

<svg class="fig scanfig" viewBox="0 0 222 565" style="width:278px" role="img" aria-label="Задача 11"><image class="scan" href="/fig/pul/11.png" width="222" height="565"/><text class="lb lt" x="33" y="250" text-anchor="middle">T</text><text class="lb lt" x="101" y="190" text-anchor="middle">T</text><text class="lb lt" x="208" y="150" text-anchor="middle">T</text><text class="lb lt" x="168" y="330" text-anchor="middle">T</text><text class="lb lt" x="122" y="468" text-anchor="middle">2T</text><text class="lb lp" x="64" y="120" text-anchor="middle">A</text><text class="lb lp" x="140" y="244" text-anchor="middle">B</text><text class="lb lp" x="76" y="394" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a = g$, $T = 0$.

:::hint Подсказка
Проследите нить от конца до конца. Она **одна**: начинается у потолка, огибает $B$ снизу, потом $A$ сверху, потом $C$ снизу и **привязана к оси блока $B$**. Запишите условие «сумма сил на невесомый блок $B$ равна нулю».
:::

:::solution Решение
**Нить одна.** Значит, натяжение $T$ везде одинаковое.

**Силы на блок $B$.** Его огибают две ветви нити, обе идут вверх (к потолку и к $A$). Они тянут блок вверх силой $2T$. Вниз ось $B$ тянет конец той же нити, с силой $T$. Блок невесомый:
$$2T - T = 0 \;\Rightarrow\; T = 0.$$

**Значит, нить не натянута.** На груз $m$ действует только сила тяжести, и он падает с ускорением $a = g$.

**Почему так получилось.** Посчитаем длину нити: $y_B + y_B + y_C + (y_C - y_B) = y_B + 2y_C + \text{const}$. Связь позволяет грузу $C$ опускаться, если $B$ поднимается вдвое быстрее. Невесомому блоку $B$ ничего не мешает подниматься, ведь он ничего не весит. Система не может удержать груз ни при каком натяжении: если бы $T > 0$, на невесомый $B$ действовала бы ненулевая сила, и он улетел бы вверх с бесконечным ускорением, «выбирая» слабину.
:::

:::tip Вывод для контрольной
Если невесомый блок огибают $n$ ветвей нити и к его оси привязаны концы **той же** нити, а силы не уравновешиваются ни при каком $T \ne 0$, значит $T = 0$. В листке это задачи **11, 16, 17**.
:::

## Задача 12 (3.2). Груз «в разрыве» нити

<svg class="fig scanfig" viewBox="0 0 222 565" style="width:278px" role="img" aria-label="Задача 12"><image class="scan" href="/fig/pul/12.png" width="222" height="565"/><text class="lb lt" x="33" y="160" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="100" y="180" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="208" y="150" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="33" y="340" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="167" y="320" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="124" y="468" text-anchor="middle">2T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="64" y="120" text-anchor="middle">A</text><text class="lb lp" x="138" y="262" text-anchor="middle">B</text><text class="lb lp" x="76" y="394" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_2 = \dfrac{4m_1 + m_2}{16m_1 + m_2}\,g$.

:::hint Подсказка
Это задача 11, в которой нить разрезали, а в разрыв вставили груз $m_1$. Теперь нитей две:
1. $T_1$: потолок → под $B$ → через $A$ → верх $m_1$;
2. $T_2$: низ $m_1$ → под $C$ → ось $B$.

Из условия для блока $B$ получится $T_2 = 2T_1$, то есть нижняя нить тянет $m_1$ вниз **сильнее**, чем верхняя вверх.
:::

:::solution Решение
**Связи.**
- Нить 1: $y_B + y_B + y_1 = \text{const}$, поэтому $a_1 = -2a_B$.
- Нить 2: $(y_C - y_1) + (y_C - y_B) = \text{const}$, поэтому $2a_C = a_1 + a_B = a_1 - \tfrac12 a_1 = \tfrac12 a_1$. Итого $a_1 = 4a_C$, $a_B = -2a_C$.

**Силы.**
- Блок $B$: вверх $2T_1$, вниз $T_2$, поэтому $T_2 = 2T_1$.
- Груз $m_1$: вверх $T_1$, вниз $T_2$ и $m_1 g$, поэтому $m_1 a_1 = m_1 g + T_2 - T_1 = m_1 g + T_1$.
- Блок $C$ с грузом $m_2$: $m_2 a_C = m_2 g - 2T_2 = m_2 g - 4T_1$.

**Решаем.** $4m_1 a_C = m_1 g + T_1$, откуда $T_1 = 4m_1 a_C - m_1 g$. Тогда
$$m_2 a_C = m_2 g - 16m_1 a_C + 4m_1 g \;\Rightarrow\; a_C = \frac{4m_1 + m_2}{16m_1 + m_2}\,g.$$
Натяжение $T_1 = \dfrac{3m_1 m_2}{16m_1 + m_2}g > 0$, значит нить натянута и решение законно.

**Интересное.** $a_1 = 4a_C = \dfrac{4(4m_1 + m_2)}{16m_1 + m_2}g$ может быть **больше $g$**: например, при $m_2 \gg m_1$ получаем $a_1 \to 4g$. Противоречия нет: на $m_1$ нить тянет **вниз** сильнее, чем вверх.

**Проверка энергией.** $k_C = 1$, $k_1 = 4$ (оба вниз): $a = g\dfrac{m_2 + 4m_1}{m_2 + 16m_1}$. Совпало.
:::

## Задача 13 (3.3). Груз жёстко связан с блоком

<svg class="fig scanfig" viewBox="0 0 221 565" style="width:276px" role="img" aria-label="Задача 13"><image class="scan" href="/fig/pul/13.png" width="221" height="565"/><text class="lb lt" x="33" y="250" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="101" y="130" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="208" y="110" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="167" y="210" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="167" y="370" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="150" y="480" text-anchor="middle">2T<tspan class="sb" dy="4">1</tspan></text><text class="lb lp" x="62" y="88" text-anchor="middle">A</text><text class="lb lp" x="138" y="175" text-anchor="middle">B</text><text class="lb lp" x="76" y="425" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_2 = \dfrac{m_2 - 2m_1}{4m_1 + m_2}\,g$.

:::hint Подсказка
Груз $m_1$ висит прямо на оси блока $B$, значит $m_1$ и $B$ движутся **как одно тело**. Длинная нить: потолок → под $B$ → через $A$ → под $C$ → вверх к низу груза $m_1$. Сколько ветвей этой нити тянут тело «$B + m_1$» вверх и сколько вниз?
:::

:::solution Решение
**Обозначения.** Нить 1 ($T_1$): потолок → под $B$ → через $A$ → под $C$ → низ $m_1$. Нить 2 ($T_2$): верх $m_1$ → ось $B$.

**Связи.**
- Нить 2 короткая: $y_1 - y_B = \text{const}$, поэтому $a_B = a_1$.
- Нить 1: $y_B + y_B + y_C + (y_C - y_1) = \text{const}$, поэтому $2a_B + 2a_C - a_1 = 0$. С $a_B = a_1$ получаем $a_1 = -2a_C$.

**Силы.**
- Блок $B$: вверх $2T_1$, вниз $T_2$, поэтому $T_2 = 2T_1$.
- Груз $m_1$: вверх $T_2 = 2T_1$, вниз $T_1$ (нить 1 тянет снизу) и $m_1 g$, поэтому $m_1 a_1 = m_1 g - T_1$.
- Блок $C$ с $m_2$: $m_2 a_C = m_2 g - 2T_1$.

**Решаем.** $-2m_1 a_C = m_1 g - T_1$, откуда $T_1 = m_1 g + 2m_1 a_C$. Тогда
$$m_2 a_C = m_2 g - 2m_1 g - 4m_1 a_C \;\Rightarrow\; a_C = \frac{m_2 - 2m_1}{m_2 + 4m_1}\,g.$$

**Смысл.** Рассмотрим «$B + m_1$» как одно тело. Две ветви нити у блока $B$ тянут его вверх ($2T_1$), одна ветвь у низа $m_1$ тянет вниз ($T_1$). В итоге вверх действует $T_1$, как на груз $m_1$ из задачи 5. При этом это тело движется вдвое быстрее $C$, как и там. Поэтому ответ совпал с задачей 5.

**Проверка энергией.** $k_C = 1$, $k_1 = -2$: $a = g\dfrac{m_2 - 2m_1}{m_2 + 4m_1}$. Совпало.
:::

## Задача 14 (3.4). Ещё один вариант с выигрышем в 4 раза

<svg class="fig scanfig" viewBox="0 0 221 565" style="width:276px" role="img" aria-label="Задача 14"><image class="scan" href="/fig/pul/14.png" width="221" height="565"/><text class="lb lt" x="126" y="118" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="31" y="250" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="98" y="255" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="206" y="150" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="165" y="350" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="150" y="480" text-anchor="middle">2T<tspan class="sb" dy="4">1</tspan></text><text class="lb lp" x="62" y="88" text-anchor="middle">A</text><text class="lb lp" x="137" y="294" text-anchor="middle">B</text><text class="lb lp" x="76" y="425" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_2 = \dfrac{m_2 - 4m_1}{16m_1 + m_2}\,g$.

:::hint Подсказка
Нитей две:
1. $T_1$: верх $m_1$ → через $A$ → под $C$ → ось $B$;
2. $T_2$: низ $m_1$ → под $B$ → потолок.

Сравните с задачей 10: ответ тот же.
:::

:::solution Решение
**Связи.**
- Нить 2: $(y_B - y_1) + y_B = \text{const}$, поэтому $a_B = \tfrac12 a_1$.
- Нить 1: $y_1 + y_C + (y_C - y_B) = \text{const}$, поэтому $a_1 + 2a_C - a_B = 0$, то есть $\tfrac12 a_1 + 2a_C = 0$. Итого $a_1 = -4a_C$.

**Силы.**
- Блок $B$: вверх $2T_2$ (его огибает нить 2), вниз $T_1$ (нить 1 привязана к оси). Поэтому $T_1 = 2T_2$.
- Груз $m_1$: вверх $T_1$, вниз $T_2$ и $m_1 g$, поэтому $m_1 a_1 = m_1 g - T_1 + T_2 = m_1 g - T_2$.
- Блок $C$ с $m_2$: вверх $2T_1 = 4T_2$, поэтому $m_2 a_C = m_2 g - 4T_2$.

**Решаем.** $-4m_1 a_C = m_1 g - T_2$, откуда $T_2 = m_1 g + 4m_1 a_C$. Тогда
$$m_2 a_C = m_2 g - 4m_1 g - 16m_1 a_C \;\Rightarrow\; a_C = \frac{m_2 - 4m_1}{m_2 + 16m_1}\,g.$$
Натяжения: $T_2 = \dfrac{5m_1 m_2}{16m_1 + m_2}g$, $T_1 = 2T_2$.

**Проверка энергией.** $k_C = 1$, $k_1 = -4$ — те же числа, что в задаче 10, поэтому и ответ тот же.
:::

## Задача 15 (3.5). Сложная схема, а ответ как у машины Атвуда

<svg class="fig scanfig" viewBox="0 0 231 566" style="width:289px" role="img" aria-label="Задача 15"><image class="scan" href="/fig/pul/15.png" width="231" height="566"/><text class="lb lt" x="33" y="225" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="168" y="225" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="33" y="410" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="127" y="400" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="208" y="350" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="80" y="172" text-anchor="middle">A</text><text class="lb lp" x="137" y="312" text-anchor="middle">B</text><text class="lb lp" x="62" y="478" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_2 = \dfrac{m_2 - m_1}{m_1 + m_2}\,g$.

:::hint Подсказка
Блок $C$ прикреплён к **полу** (неподвижный). Нитей две:
1. $T_1$: верх $m_1$ → через $A$ → ось $B$;
2. $T_2$: низ $m_1$ → под $C$ → вверх через $B$ → $m_2$.

Обе ветви нити 2 у блока $B$ идут **вниз**. Найдите связь: окажется, что $a_2 = -a_1$.
:::

:::solution Решение
**Связи.**
- Нить 1: $y_1 + y_B = \text{const}$, поэтому $a_B = -a_1$.
- Нить 2: $(y_C - y_1) + (y_C - y_B) + (y_2 - y_B) = \text{const}$, где $y_C$ — константа (блок на полу). Получаем $-a_1 - 2a_B + a_2 = 0$, то есть $a_2 = a_1 + 2a_B = a_1 - 2a_1 = -a_1$.

**Силы.**
- Блок $B$: вверх $T_1$, вниз две ветви нити 2, $2T_2$. Поэтому $T_1 = 2T_2$.
- Груз $m_1$: вверх $T_1$, вниз $T_2$ и $m_1 g$, поэтому $m_1 a_1 = m_1 g - 2T_2 + T_2 = m_1 g - T_2$.
- Груз $m_2$: $m_2 a_2 = m_2 g - T_2$.

**Решаем.** С $a_2 = -a_1$ это **ровно уравнения машины Атвуда** с натяжением $T_2$:
$$a_2 = \frac{m_2 - m_1}{m_1 + m_2}\,g,\qquad T_2 = \frac{2m_1 m_2}{m_1 + m_2}\,g,\qquad T_1 = 2T_2.$$

**Проверка энергией.** $k_2 = 1$, $k_1 = -1$, а блок невесомый и в энергию не входит. Получаем как в задаче 1. Смысл: важно только, **как связаны скорости грузов**, а не сколько блоков между ними.
:::

## Задача 16 (3.6). Ловушка №2: всё падает вместе

<svg class="fig scanfig" viewBox="0 0 233 566" style="width:291px" role="img" aria-label="Задача 16"><image class="scan" href="/fig/pul/16.png" width="233" height="566"/><text class="lb lt" x="31" y="300" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="124" y="430" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="166" y="180" text-anchor="middle">T<tspan class="sb" dy="4">1</tspan></text><text class="lb lt" x="98" y="290" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lt" x="207" y="330" text-anchor="middle">T<tspan class="sb" dy="4">2</tspan></text><text class="lb lp" x="80" y="122" text-anchor="middle">A</text><text class="lb lp" x="135" y="262" text-anchor="middle">B</text><text class="lb lp" x="60" y="478" text-anchor="middle">C</text></svg>

**Ответ учителя:** $a_1 = a_2 = g$.

:::hint Подсказка
Нитей две:
1. $T_1$: ось $B$ → через $A$ → под $C$ (на полу) → низ $m_1$;
2. $T_2$: верх $m_1$ → через $B$ → $m_2$.

Найдите связи. Окажется, что $m_1$, $m_2$ и $B$ движутся **с одинаковым ускорением**. Что тогда даёт сложение уравнений для грузов?
:::

:::solution Решение
**Связи.**
- Нить 1: $y_B + y_C + (y_C - y_1) = \text{const}$, поэтому $a_B = a_1$.
- Нить 2: $(y_1 - y_B) + (y_2 - y_B) = \text{const}$, поэтому $a_1 + a_2 = 2a_B = 2a_1$, то есть $a_2 = a_1$.

Все три тела ($m_1$, $m_2$, $B$) движутся с одним ускорением $a$.

**Силы.**
- Блок $B$: вверх $T_1$, вниз $2T_2$, поэтому $T_1 = 2T_2$.
- Груз $m_1$: вниз $m_1 g$ и $T_1$ (нить 1 уходит вниз к блоку на полу), вверх $T_2$. Получаем $m_1 a = m_1 g + T_1 - T_2 = m_1 g + T_2$.
- Груз $m_2$: $m_2 a = m_2 g - T_2$.

**Решаем.** Сложим: $(m_1 + m_2)a = (m_1 + m_2)g$, поэтому $a = g$. Из второго уравнения $T_2 = 0$, а значит и $T_1 = 0$.

**Смысл.** Если $m_1$, $m_2$ и $B$ одновременно опускаются на одно и то же расстояние, длины обеих нитей не меняются. Свободное падение всей конструкции **разрешено связями**, поэтому нитям незачем натягиваться. Это обязательно проверять: если свободное падение всех грузов не нарушает ни одной связи, ответ $a = g$.
:::

## Задача 17 (3.7). Ловушка №3

<svg class="fig scanfig" viewBox="0 0 231 548" style="width:289px" role="img" aria-label="Задача 17"><image class="scan" href="/fig/pul/17.png" width="231" height="548"/><text class="lb lt" x="33" y="250" text-anchor="middle">T</text><text class="lb lt" x="126" y="330" text-anchor="middle">T</text><text class="lb lt" x="167" y="190" text-anchor="middle">T</text><text class="lb lt" x="207" y="380" text-anchor="middle">T</text><text class="lb lt" x="96" y="440" text-anchor="middle">2T</text><text class="lb lp" x="80" y="122" text-anchor="middle">A</text><text class="lb lp" x="138" y="276" text-anchor="middle">B</text><text class="lb lp" x="62" y="394" text-anchor="middle">D</text></svg>

**Ответ учителя:** $a_1 = a_2 = g$, $T = 0$.

:::hint Подсказка
Нить одна: ось $B$ → через $A$ → под $D$ → через $B$ → $m_2$. Сколько раз нить тянет невесомый блок $B$ вниз и сколько вверх?
:::

:::solution Решение
**Нить одна**, натяжение $T$.

**Блок $B$.** Вверх его тянет нить, привязанная к оси (идёт к $A$), с силой $T$. Вниз его тянут две ветви, огибающие его (к $D$ и к $m_2$), с силой $2T$. Блок невесомый:
$$T - 2T = 0 \;\Rightarrow\; T = 0.$$

Нить не натянута, оба груза падают свободно: $a_1 = a_2 = g$.

**Проверка через связь.** Длина нити $y_B + y_D + (y_D - y_B) + (y_2 - y_B) = 2y_D + y_2 - y_B + \text{const}$. Если $m_1$ (на блоке $D$) и $m_2$ падают с ускорением $g$, блоку $B$ достаточно двигаться вниз с ускорением $3g$, и длина не изменится. Невесомому блоку это ничего не стоит, поэтому никакого натяжения не возникает.
:::

---

:::key Что вынести из части 1
1. **Подвижный блок**: сила в 2 раза больше, путь (скорость, ускорение) в 2 раза меньше. Два подвижных блока подряд дают 4.
2. **Связь берём из длины нити**, а не «на глаз». Особенно когда блок перевёрнут (задачи 8, 9, 15) или груз вставлен в разрыв нити (12, 14).
3. **Проверка энергией**: $a = g\sum m_i\kappa_i / \sum m_i k_i^2$. Отсюда коэффициенты 4 и 16 в знаменателях.
4. **Нить не толкает.** Если условие «сумма сил на невесомый блок равна 0» даёт $T = 0$ (задачи 11, 17) или свободное падение всех тел не нарушает связей (16), то ответ $a = g$.
:::
