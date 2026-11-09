---
title: "Ceva and Menelaus — решения всех 24 задач"
kind: solutions
units: []
tasks: [49239446, 49321380]
order: 58
summary: Теоремы Чевы и Менелая (со знаками), отношения площадей, параллельные прямые и подобие, инцентр и средние линии, координаты. Все ответы пересчитаны точно (символьно) на компьютере.
---

## Инструменты

:::formula Теорема Чевы
$D \in BC$, $E \in CA$, $F \in AB$. Прямые $AD$, $BE$, $CF$ пересекаются в одной точке ⇔
$$\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB} = 1.$$
Запоминалка: обходим треугольник $B \to C \to A \to B$, каждый раз «вершина → точка → вершина».
:::

:::formula Теорема Менелая
$D$, $E$, $F$ на **прямых** $BC$, $CA$, $AB$ лежат на одной прямой ⇔
$$\frac{\overline{BD}}{\overline{DC}}\cdot\frac{\overline{CE}}{\overline{EA}}\cdot\frac{\overline{AF}}{\overline{FB}} = -1\quad(\text{со знаками}),$$
без знаков произведение равно 1. Прямая всегда пересекает **либо две стороны внутри и одну снаружи, либо все три снаружи**.
:::

:::key Ещё три приёма
1. **Площади с общим углом:** если $X$ на прямой $AB$, $Y$ на прямой $AC$, то $\frac{S_{AXY}}{S_{ABC}} = \frac{AX}{AB}\cdot\frac{AY}{AC}$ (синус угла и смежного одинаковы).
2. **Общая высота:** если $M$ на $BC$, то $\frac{S_{ABM}}{S_{AMC}} = \frac{BM}{MC}$. Отсюда «лемма об отношении»: $\frac{BM}{MC} = \frac{AB\sin\angle BAM}{AC\sin\angle MAC}$.
3. **Теорема Ван-Обеля:** если чевианы $AD$, $BE$, $CF$ пересекаются в $O$, то $\frac{AO}{OD} = \frac{AF}{FB} + \frac{AE}{EC}$ (со знаками — для внешних точек тоже).
4. **Параллельные прямые → подобные треугольники** (в трапециях и параллелограммах это быстрее Менелая).
:::

## Треугольник и чевианы (1–5)

:::solution 1. $\angle B = 90^\circ$, $AB = 6$, $BC = 8$, $\cos\angle ABM = \frac35$
$AC = 10$. $\angle CBM = 90^\circ - \angle ABM$ ⇒ $\sin\angle CBM = \cos\angle ABM = \frac35$, а $\sin\angle ABM = \frac45$.
Лемма об отношении: $\frac{AM}{MC} = \frac{AB\sin\angle ABM}{BC\sin\angle CBM} = \frac{6\cdot\frac45}{8\cdot\frac35} = 1$ — $M$ середина $AC$.
**(a)** $S_{ABM} = \frac12S_{ABC} = \frac12\cdot\frac12\cdot6\cdot8 = 12$. **(b)** $AM = 5$.
:::

:::solution 2. $\angle ABM = 30^\circ$, $\angle MBC = 45^\circ$, $AB = 6$, $BC = 8\sqrt2$
**(a)** $\frac{AM}{MC} = \frac{6\sin30^\circ}{8\sqrt2\sin45^\circ} = \frac{3}{8}$ ⇒ $AM : AC = 3 : 11$.
**(b)** $S_{ABC} = \frac12\cdot6\cdot8\sqrt2\sin75^\circ = 24\sqrt2\cdot\frac{\sqrt6 + \sqrt2}{4} = 12 + 12\sqrt3$.
$S_{BMC} = \frac{8}{11}S_{ABC} = \frac{96(1 + \sqrt3)}{11}$.
:::

:::solution 3. $AB = 4$, $BC = 5$, $\angle B = 60^\circ$
**(a)** $AC^2 = 16 + 25 - 20 = 21$. $\cos C = \frac{25 + 21 - 16}{2\cdot5\sqrt{21}} = \frac{3}{\sqrt{21}}$, $\cos^2C = \frac37 < \frac12 = \cos^245^\circ$ ⇒ $\angle C > 45^\circ$ ∎
**(b)** $\angle ABL = 105^\circ > 60^\circ$ ⇒ $L$ за точкой $C$. В треугольнике $BCL$: $\angle CBL = 45^\circ$, $\angle BCL = 180^\circ - C$, значит, $\angle BLC = C - 45^\circ$ — **положителен благодаря (a)** (иначе такой точки не было бы).
$\sin C = \frac{2}{\sqrt7}$, $\cos C = \frac{\sqrt3}{\sqrt7}$, $\sin(C - 45^\circ) = \frac{2 - \sqrt3}{\sqrt{14}}$.
$CL = \frac{BC\sin45^\circ}{\sin(C - 45^\circ)} = \frac{5\sqrt7}{2 - \sqrt3} = 5\sqrt7(2 + \sqrt3) = 10\sqrt7 + 5\sqrt{21}$.
$AL = AC + CL = 10\sqrt7 + 6\sqrt{21} \approx 54{,}0$.
:::

:::solution 4. $AK$, $AL$ делят угол $A$ на три равные части α. Доказать $\frac{BK\cdot BL}{KC\cdot LC} = \frac{AB^2}{AC^2}$
Лемма об отношении для каждой чевианы:
$$\frac{BK}{KC} = \frac{AB\sin\alpha}{AC\sin2\alpha},\qquad \frac{BL}{LC} = \frac{AB\sin2\alpha}{AC\sin\alpha}.$$
Перемножаем — синусы сокращаются: $\frac{AB^2}{AC^2}$ ∎
:::

:::solution 5. $K$ — середина $BC$, $AL : LB = 3 : 4$, $O = AK \cap CL$, $M = BO \cap AC$
**(a)** Чева: $\frac{BK}{KC}\cdot\frac{CM}{MA}\cdot\frac{AL}{LB} = 1$ ⇒ $1\cdot\frac{CM}{MA}\cdot\frac34 = 1$ ⇒ $AM : MC = 3 : 4$.
**(b)** Менелай для треугольника $ABK$ и прямой $L$–$O$–$C$: $\frac{AL}{LB}\cdot\frac{BC}{CK}\cdot\frac{KO}{OA} = 1$ ⇒ $\frac34\cdot2\cdot\frac{KO}{OA} = 1$ ⇒ $\frac{AO}{AK} = \frac35$.
$S_{AOM} = \frac{AO}{AK}\cdot\frac{AM}{AC}\cdot S_{AKC} = \frac35\cdot\frac37\cdot\frac12S_{ABC}$ ⇒ **$\frac{9}{70}$**.
:::

## Пересечения и площади (6–10)

:::solution 6. $AB = 5$, $AC = 6$, $\cos A = \frac15$, $BK : KC = 2 : 1$, $BM$ — медиана
Чева: $\frac{BK}{KC}\cdot\frac{CM}{MA}\cdot\frac{AN}{NB} = 1$ ⇒ $2\cdot1\cdot\frac{AN}{NB} = 1$ ⇒ $AN = \frac13AB = \frac53$.
**(a)** $CN^2 = 36 + \frac{25}{9} - 2\cdot6\cdot\frac53\cdot\frac15 = \frac{313}{9}$ ⇒ $CN = \frac{\sqrt{313}}{3}$.
**(b)** $S_{ABC} = \frac12\cdot5\cdot6\cdot\frac{2\sqrt6}{5} = 6\sqrt6$. Отрезаем три угловых треугольника: $\frac{S_{ANM}}{S} = \frac13\cdot\frac12$, $\frac{S_{BNK}}{S} = \frac23\cdot\frac23$, $\frac{S_{CKM}}{S} = \frac13\cdot\frac12$; в сумме $\frac79$. $S_{MNK} = \frac29\cdot6\sqrt6 = \frac{4\sqrt6}{3}$.
**(c)** Ван-Обель: $\frac{CO}{ON} = \frac{CK}{KB} + \frac{CM}{MA} = \frac12 + 1 = \frac32$.
:::

:::solution 7. $AK : KB = 4 : 1$, $O$ — середина $CK$
**(a)** Менелай для $AKC$ и прямой $B$–$O$–$L$: $\frac{AB}{BK}\cdot\frac{KO}{OC}\cdot\frac{CL}{LA} = 1$ ⇒ $5\cdot1\cdot\frac{CL}{LA} = 1$ ⇒ $AL : LC = 5 : 1$.
**(b)** Менелай для $BKC$ и прямой $A$–$O$–$M$: $\frac{BA}{AK}\cdot\frac{KO}{OC}\cdot\frac{CM}{MB} = 1$ ⇒ $\frac54\cdot\frac{CM}{MB} = 1$ ⇒ $CM : MB = 4 : 5$.
**(c)** Менелай для $ABM$ и прямой $K$–$O$–$C$: $\frac{AK}{KB}\cdot\frac{BC}{CM}\cdot\frac{MO}{OA} = 1$ ⇒ $4\cdot\frac94\cdot\frac{MO}{OA} = 1$ ⇒ $AO : OM = 9 : 1$.
:::

:::solution 8. Равнобедренная трапеция $AD = 10$, $BC = 4$, $\angle CAD = 30^\circ$, $BK = 1$, $M$ — середина $AD$
**Параллельность.** $BK \parallel AM$ ⇒ $\triangle OBK \sim \triangle OMA$: $\frac{BO}{OM} = \frac{BK}{MA} = \frac15$.
Продлим $CO$ до пересечения с прямой $AD$ в точке $P$. $BC \parallel MP$ ⇒ $\triangle OBC \sim \triangle OMP$: $MP = 5BC = 20$ — точка $P$ на 20 левее $M$, то есть на 15 левее $A$.
$BC \parallel AP$ ⇒ $\triangle NBC \sim \triangle NAP$: $\frac{AN}{NB} = \frac{AP}{BC} = \frac{15}{4}$.
Высота: $C$ на 7 правее $A$ по горизонтали, $h = 7\tan30^\circ = \frac{7}{\sqrt3}$; $AB = \sqrt{9 + \frac{49}{3}} = \frac{2\sqrt{57}}{3}$.
**(a)** $AN = \frac{15}{19}AB = \frac{10\sqrt{57}}{19} \approx 3{,}97$.
**(b)** Расстояние от $N$ до $BC$: $\frac{NB}{AB}h = \frac{4}{19}h$. $S_{BCN} = \frac12\cdot4\cdot\frac{4}{19}\cdot\frac{7}{\sqrt3} = \frac{56\sqrt3}{57}$.
:::

:::solution 9. Параллелограмм $AB = 3$, $AD = 7$, $\cos A = \frac23$, $BK = 3KD$
Цепочка подобий (везде параллельные стороны параллелограмма):
- $L = CK \cap AD$: $\triangle KDL \sim \triangle KBC$ ⇒ $DL = \frac13BC = \frac73$, $AL = \frac{14}{3}$;
- $M = BL \cap AC$: $\triangle MAL \sim \triangle MCB$ ⇒ $\frac{AM}{MC} = \frac{AL}{BC} = \frac23$;
- $N = DM \cap AB$: $\triangle MAN \sim \triangle MCD$ ⇒ $AN = \frac23CD = 2$.

**(a)** $BN = 3 - 2 = 1$.
**(b)** $S_{ABCD} = 3\cdot7\cdot\frac{\sqrt5}{3} = 7\sqrt5$, $S_{BCD} = S_{BAD} = \frac{7\sqrt5}{2}$. Делим $BCKN$ диагональю $BK$: $S_{BCK} = \frac34S_{BCD}$, $S_{BKN} = \frac34\cdot\frac13S_{BDA}$. Итого $\left(\frac34 + \frac14\right)\frac{7\sqrt5}{2} = \frac{7\sqrt5}{2}$.
:::

:::solution 10. $\frac{\overline{AK}}{\overline{KB}} = -\frac34$, $BL : BC = 3 : 4$
Знак минус: $K$ вне отрезка $AB$, за точкой $A$; $AK : KB = 3 : 4$ ⇒ $AK = 3AB$, $BK = 4AB$.
**(a)** Чева со знаками: $\frac{\overline{AK}}{\overline{KB}}\cdot\frac{\overline{BL}}{\overline{LC}}\cdot\frac{\overline{CM}}{\overline{MA}} = 1$ ⇒ $-\frac34\cdot3\cdot\frac{\overline{CM}}{\overline{MA}} = 1$ ⇒ $\frac{\overline{AM}}{\overline{MC}} = -\frac94$ ($M$ за точкой $C$, $AM = \frac95AC$).
**(b)** $S = S_{ABC}$. $S_{BKL} = \frac{BK}{BA}\cdot\frac{BL}{BC}S = 4\cdot\frac34S = 3S$.
Менелай для $ABL$ и прямой $K$–$O$–$C$: $\frac{\overline{AK}}{\overline{KB}}\cdot\frac{\overline{BC}}{\overline{CL}}\cdot\frac{\overline{LO}}{\overline{OA}} = -1$ ⇒ $-\frac34\cdot(-4)\cdot\frac{\overline{LO}}{\overline{OA}} = -1$ ⇒ $O$ за точкой $L$, $AO = \frac32AL$.
$CLOM$ = треугольник $AOM$ без треугольника $ALC$: $S_{AOM} = \frac32\cdot\frac95S_{ALC} = \frac{27}{10}S_{ALC}$, $S_{ALC} = \frac14S$ ⇒ $S_{CLOM} = \frac{17}{10}\cdot\frac14S = \frac{17}{40}S$.
**Ответ:** $\frac{17}{40} : 3 = \frac{17}{120}$.
:::

## Коллинеарность и направленные отношения (11–15)

:::solution 11. $AB = \sqrt{15}$, $BC = \sqrt{23}$, $AC = \sqrt{42}$, $\frac{\overline{AK}}{\overline{KC}} = -\frac52$, $\frac{\overline{AL}}{\overline{LB}} = -\frac43$
$K$ за $C$ ($AK = \frac53AC$), $L$ за $B$ ($AL = 4AB$, $BL = 3AB$).
Чева: $\frac{\overline{AL}}{\overline{LB}}\cdot\frac{\overline{BT}}{\overline{TC}}\cdot\frac{\overline{CK}}{\overline{KA}} = 1$ ⇒ $-\frac43\cdot\frac{BT}{TC}\cdot\left(-\frac25\right) = 1$ ⇒ $\frac{BT}{TC} = \frac{15}{8}$.
$S_{ABC}$: $\cos A = \frac{15 + 42 - 23}{2\sqrt{630}} = \frac{17}{\sqrt{630}}$, $\sin A = \sqrt{\frac{341}{630}}$, $S = \frac12\sqrt{630}\sqrt{\frac{341}{630}} = \frac{\sqrt{341}}{2}$.
**(a)** $S_{BLT} = \frac{BL}{BA}\cdot\frac{BT}{BC}\cdot S = 3\cdot\frac{15}{23}\cdot\frac{\sqrt{341}}{2} = \frac{45\sqrt{341}}{46}$.
**(b)** Ван-Обель со знаками: $\frac{\overline{AO}}{\overline{OT}} = \frac{\overline{AL}}{\overline{LB}} + \frac{\overline{AK}}{\overline{KC}} = -\frac43 - \frac52 = -\frac{23}{6}$.
:::

:::solution 12. $M$ — середина $AC$, $\frac{AK}{AB} = \frac{CL}{CB}$. Доказать: $B$, $O$, $M$ коллинеарны
Пусть общее отношение $t$: $\frac{AK}{KB} = \frac{t}{1 - t}$, $\frac{BL}{LC} = \frac{1 - t}{t}$, $\frac{CM}{MA} = 1$.
Произведение Чевы $= 1$ ⇒ по обратной теореме Чевы $AL$, $CK$, $BM$ пересекаются в одной точке, то есть $BM$ проходит через $O$ ∎
:::

:::solution 13. Трапеция: $O$ — пересечение диагоналей, $M = AB \cap CD$. Доказать, что $O$, $M$ и середины оснований на одной прямой
Пусть $P$, $Q$ — середины $AD$ и $BC$. В треугольнике $MAD$ отрезок $BC \parallel AD$, поэтому $\frac{MB}{BA} = \frac{MC}{CD}$ (Фалес).
Чева для $MAD$ с чевианами $AC$, $DB$, $MP$: $\frac{MB}{BA}\cdot\frac{AP}{PD}\cdot\frac{DC}{CM} = \frac{MB}{BA}\cdot1\cdot\frac{CD}{MC} = 1$ ⇒ $MP$ проходит через $O$.
Гомотетия с центром $M$, переводящая $BC$ в $AD$, переводит середину $Q$ в середину $P$ ⇒ $Q$ на прямой $MP$ ∎
:::

:::solution 14. $AK : AB = 3 : 5$, $BL : BC = 5 : 7$, $M = KL \cap AC$
Менелай: $\frac{AK}{KB}\cdot\frac{BL}{LC}\cdot\frac{\overline{CM}}{\overline{MA}} = -1$ ⇒ $\frac32\cdot\frac52\cdot\frac{\overline{CM}}{\overline{MA}} = -1$ ⇒ $M$ за $C$, $CM : MA = 4 : 15$.
**(a)** $AC = 11$ частей, $CM = 4$ ⇒ $\frac{\overline{AC}}{\overline{CM}} = \frac{11}{4}$.
**(b)** Общий угол при $C$ (смежный): $\frac{S_{CLM}}{S_{ABC}} = \frac{CL}{CB}\cdot\frac{CM}{CA} = \frac27\cdot\frac{4}{11} = \frac{8}{77}$.
:::

:::solution 15. $\frac{\overline{AB}}{\overline{BK}} = 4$, $\frac{\overline{AC}}{\overline{CL}} = 5$, $M = KL \cap BC$
$K$ за $B$ ($BK = \frac14AB$), $L$ за $C$ ($CL = \frac15AC$). Тогда $\frac{\overline{AK}}{\overline{KB}} = \frac{5/4}{-1/4} = -5$, $\frac{\overline{CL}}{\overline{LA}} = \frac{1/5}{-6/5} = -\frac16$.
Менелай: $(-5)\cdot\frac{\overline{BM}}{\overline{MC}}\cdot\left(-\frac16\right) = -1$ ⇒ $\frac{\overline{BM}}{\overline{MC}} = -\frac65$.
**(a)** $\frac{\overline{CM}}{\overline{MB}} = -\frac56$ ($M$ за точкой $C$, $CM = 5BC$).
**(b)** $S_{BKC} = \frac14S$. $S_{AMC} = \frac{CM}{CB}S = 5S$, $S_{AML} = \frac{AL}{AC}S_{AMC} = \frac65\cdot5S = 6S$. **Ответ:** 24.
:::

## Длины и площади (16–20)

:::solution 16. $AB = 4$, $AC = 8\sqrt3$, $\angle A = 150^\circ$, $K$ — середина $AB$, $BL : LC = 1 : 3$
**(a)** Менелай: $\frac{AK}{KB}\cdot\frac{BL}{LC}\cdot\frac{\overline{CM}}{\overline{MA}} = -1$ ⇒ $\frac{\overline{CM}}{\overline{MA}} = -3$ ⇒ $M$ за $A$, $AM = \frac12AC = 4\sqrt3$, $CM = 12\sqrt3$.
**(b)** Менелай для $ABM$ и прямой $K$–$T$–$C$: $\frac{AK}{KB}\cdot\frac{\overline{BT}}{\overline{TM}}\cdot\frac{\overline{MC}}{\overline{CA}} = -1$, $\frac{\overline{MC}}{\overline{CA}} = \frac{12\sqrt3}{-8\sqrt3} = -\frac32$ ⇒ $\frac{BT}{TM} = \frac23$.
В треугольнике $ABM$: $\angle BAM = 30^\circ$, $BM^2 = 16 + 48 - 2\cdot4\cdot4\sqrt3\cdot\frac{\sqrt3}{2} = 16$, $BM = 4$ ⇒ $BT = \frac85$.
**(c)** $S_{AMT} = \frac{MT}{MB}S_{ABM} = \frac35\cdot\frac12\cdot4\cdot4\sqrt3\cdot\frac12 = \frac{12\sqrt3}{5}$.
:::

:::solution 17. $AB = 8$, $AC = 7$, $BC = 5$, $AK = 12$ (на луче $AB$), $BL = 2$
$K$ за $B$ ($BK = 4$), $L$ внутри $BC$ ⇒ $M$ внутри $AC$.
**(a)** Менелай: $\frac{12}{4}\cdot\frac23\cdot\frac{CM}{MA} = 1$ ⇒ $AM : MC = 2 : 1$.
**(b)** Герон: $p = 10$, $S_{ABC} = \sqrt{10\cdot2\cdot3\cdot5} = 10\sqrt3$. $S_{LMC} = \frac{CL}{CB}\cdot\frac{CM}{CA}\cdot S = \frac35\cdot\frac13\cdot10\sqrt3 = 2\sqrt3$.
**(c)** $\cos C = \frac{25 + 49 - 64}{70} = \frac17$, $CL = 3$, $CM = \frac73$: $LM^2 = 9 + \frac{49}{9} - 2\cdot3\cdot\frac73\cdot\frac17 = \frac{112}{9}$ ⇒ $LM = \frac{4\sqrt7}{3}$.
:::

:::solution 18. $AB = 5$, $BC = 6$, $\cos A = \frac{19}{35}$, $AK = 3$, $CL = 2$
$AC$: $36 = 25 + b^2 - \frac{38}{7}b$ ⇒ $7b^2 - 38b - 77 = 0$ ⇒ $b = 7$.
**(a)** Менелай: $\frac32\cdot\frac42\cdot\frac{CM}{MA} = 1$ ⇒ $\frac{CM}{MA} = \frac13$, $M$ за $C$ ⇒ $CM = 3{,}5$, $AC : CM = 2$.
**(b)** Менелай для $ALC$ и прямой $B$–$T$–$M$ (оси: $B = 0$, $L = 4$, $C = 6$; $A = 0$, $C = 7$, $M = 10{,}5$): $\frac{\overline{AT}}{\overline{TL}}\cdot\left(-\frac23\right)\cdot\left(-\frac13\right) = -1$ ⇒ $\frac{\overline{AT}}{\overline{TL}} = -\frac92$ ⇒ $T$ за $L$, $AL : LT = 7 : 2$ ⇒ $\frac{\overline{LA}}{\overline{AT}} = -\frac79$.
**(c)** $\sin A = \frac{12\sqrt6}{35}$, $S_{ABC} = 6\sqrt6$, $S_{ABL} = \frac46S = 4\sqrt6$. $KBTL$ = треугольник $ABT$ без $AKL$:
$S_{ABT} = \frac97\cdot4\sqrt6$, $S_{AKL} = \frac35\cdot4\sqrt6$ ⇒ $S_{KBTL} = 4\sqrt6\left(\frac97 - \frac35\right) = \frac{96\sqrt6}{35}$.
:::

:::solution 19. Параллелограмм $AB = 3$, $AD = 5$, $BD = 6$, $BK : KC = 1 : 3$, $BL : LD = 3 : 2$
Менелай для $BCD$ и прямой $K$–$L$–$M$: $\frac{BK}{KC}\cdot\frac{\overline{CM}}{\overline{MD}}\cdot\frac{DL}{LB} = -1$ ⇒ $\frac13\cdot\frac{\overline{CM}}{\overline{MD}}\cdot\frac23 = -1$ ⇒ $M$ за $D$, $DM = \frac27CD = \frac67$.
**(a)** $\vec{AM} = \vec{AD} - \frac27\vec{AB}$; $\vec{AB}\cdot\vec{AD} = \frac{9 + 25 - 36}{2} = -1$.
$AM^2 = 25 + \frac{4}{49}\cdot9 + \frac47 = \frac{1289}{49}$ ⇒ $AM = \frac{\sqrt{1289}}{7} \approx 5{,}13$.
**(b)** $\cos A = -\frac{1}{15}$, $\sin A = \frac{4\sqrt{14}}{15}$, $S_{BCD} = \frac12\cdot15\cdot\frac{4\sqrt{14}}{15} = 2\sqrt{14}$.
$S_{KCDL} = S_{BCD} - S_{BKL} = 2\sqrt{14}\left(1 - \frac14\cdot\frac35\right) = \frac{17\sqrt{14}}{10}$.
:::

:::solution 20. Равнобедренная трапеция $AD = 12$, $BC = 4$, $\cos\angle BAD = \frac{2}{\sqrt{13}}$; $DM = 16$, $BN = \frac52\sqrt{13}$
$\tan A = \frac32$, горизонтальный выступ $\frac{12 - 4}{2} = 4$ ⇒ высота 6, $AB = 2\sqrt{13}$.
**(a)** $S = \frac{12 + 4}{2}\cdot6 = 48$.
**(b)** Продолжим боковые стороны до точки $F$: $\frac{FB}{FA} = \frac{BC}{AD} = \frac13$ ⇒ $FA = FD = 3\sqrt{13}$, $FC = \sqrt{13}$.
$M$ за $A$ ($AM = 4$), $N$ за $A$ на прямой $FA$ ($AN = \frac{\sqrt{13}}{2}$). Менелай для $FAD$ и прямой $M$–$N$–$E$:
$\frac{\overline{AM}}{\overline{MD}}\cdot\frac{\overline{DE}}{\overline{EF}}\cdot\frac{\overline{FN}}{\overline{NA}} = -1$ ⇒ $\left(-\frac14\right)\cdot\frac{\overline{DE}}{\overline{EF}}\cdot(-7) = -1$ ⇒ $E$ за $D$, $DE = 4\sqrt{13}$.
$\frac{\overline{CE}}{\overline{ED}} = \frac{2\sqrt{13} + 4\sqrt{13}}{-4\sqrt{13}} = -\frac32$.
**(c)** Координаты $A(0; 0)$, $D(12; 0)$, $F(6; 9)$: $E = D + \frac43(D - F) = (20; -12)$, $M(-4; 0)$ ⇒ $ME = \sqrt{24^2 + 12^2} = 12\sqrt5$.
:::

## Вписанная окружность и координаты (21–24)

:::solution 21. $AB = 6$, $BC = 9$, $AC = 7$; касания $P$, $Q$; биссектриса $BM$; $R$, $S$ — середины $BC$, $AC$
$p = 11$, $AP = AQ = p - BC = 2$. $\frac{AM}{MC} = \frac{AB}{BC} = \frac23$ ⇒ $AM = \frac{14}{5}$, $MQ = \frac45$.
**(a)** Менелай для $ABM$ и прямой $P$–$T$–$Q$: $\frac{AP}{PB}\cdot\frac{\overline{BT}}{\overline{TM}}\cdot\frac{\overline{MQ}}{\overline{QA}} = -1$ ⇒ $\frac12\cdot\frac{\overline{BT}}{\overline{TM}}\cdot\frac25 = -1$ ⇒ $T$ за $M$, $BT = 5MT$ ⇒ $BM : MT = 4 : 1$.
**(b)** Расстояние до прямой $AB$ меняется вдоль $BM$ линейно: $d(M) = \frac{AM}{AC}d(C) = \frac25d(C)$, значит, $d(T) = \frac{BT}{BM}d(M) = \frac54\cdot\frac25d(C) = \frac12d(C)$. Но средняя линия $RS$ — это ровно множество точек на расстоянии $\frac12d(C)$ от $AB$ (с той же стороны). Значит, $T \in RS$ ∎
:::

:::solution 22. Общий случай: $T = PQ \cap RS$ лежит на биссектрисе угла $B$
Возьмём на прямой $RS$ точку $T'$ с $RT' = RB = \frac a2$ (в сторону $S$). Треугольник $RBT'$ равнобедренный ⇒ $\angle RBT' = \angle RT'B = \angle T'BA$ (накрест лежащие, $RS \parallel AB$) ⇒ $BT'$ — биссектриса.
Покажем, что $T'$ на $PQ$. $AP = AQ = p - a$, $QS = \left|\frac b2 - (p - a)\right| = \frac{|a - c|}{2}$. Прямая $PQ$ пересекает $RS$ в точке $T''$, и $\triangle QST'' \sim \triangle QAP$ (так как $ST'' \parallel AP$), а $\triangle QAP$ равнобедренный ⇒ $ST'' = QS = \frac{|a - c|}{2}$.
С другой стороны, $ST' = RT' - RS = \frac a2 - \frac c2$ (по модулю то же). Точки совпадают: $T'' = T'$ ∎
:::

:::solution 23. $A(-7; -3)$, $B(5; 0)$, $C(1; 3)$, $AM : MB = 1 : 2$, $AN : NC = 2 : 3$
**(a)** Чева: $\frac12\cdot\frac{BL}{LC}\cdot\frac32 = 1$ ⇒ $\frac{BL}{LC} = \frac43$ ⇒ $L = B + \frac47(C - B) = \left(\frac{19}{7}; \frac{12}{7}\right)$.
**(b)** $CA = 10$, $CB = 5$ ⇒ $\frac{AF}{FB} = 2$ ⇒ $F = A + \frac23(B - A) = (1; -1)$, $CF = |(0; -4)| = 4$.
**(c)** $S_{ABC} = \frac12|12\cdot6 - 3\cdot8| = 24$. $S_{BLF} = \frac{BL}{BC}\cdot\frac{BF}{BA}\cdot24 = \frac47\cdot\frac13\cdot24 = \frac{32}{7}$.
:::

:::solution 24. $A(-5; 1)$, $B(7; -2)$, $C(4; 4)$, $AM : AB = 2 : 3$, $CN : NB = 1 : 3$
**(a)** Чева: $\frac{AM}{MB}\cdot\frac{BN}{NC}\cdot\frac{CL}{LA} = 2\cdot3\cdot\frac{CL}{LA} = 1$ ⇒ $AL : LC = 6 : 1$ ⇒ $L = A + \frac67(C - A) = \left(\frac{19}{7}; \frac{25}{7}\right)$.
**(b)** $\vec{LA} \parallel (-3; -1)$, $\vec{LB} \parallel (10; -13)$: $\cos\angle ALB = \frac{-30 + 13}{\sqrt{10}\sqrt{269}} = -\frac{17}{\sqrt{2690}}$ ⇒ $\angle ALB \approx 109{,}1^\circ$.
**(c)** $M = (3; -1)$, $\vec{CM} = (-1; -5)$ — нормаль искомой прямой: $-(x + 5) - 5(y - 1) = 0$ ⇔ **$x + 5y = 0$**.
:::
