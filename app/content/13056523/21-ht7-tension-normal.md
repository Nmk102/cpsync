---
title: Hometask 7. Tension. Normal reaction — разбор всех задач
kind: solutions
units: [2043420]
tasks: [49487563]
order: 21
summary: Люлька маляра, клин и стержень, клин у стены, тележка с грузом на мосту, клин между брусками.
---

Ответы есть в конце файла учителя, но **нужны полные решения**. Ниже к каждой задаче: идея, подсказка (сначала попробуйте сами), полное решение и проверка. Метод везде один — см. конспект «Законы Ньютона»: силы на **каждое** тело → второй закон в проекциях → кинематическая связь.

## Задача 1. Маляр в люльке

> Маляр $M = 72$ кг в люльке $m = 12$ кг тянет верёвку, перекинутую через блок под потолком (второй конец верёвки привязан к люльке). Сила, с которой он давит на пол люльки, упала до $N = 400$ Н. Найти ускорение люльки. $g = 9{,}8$ м/с².

<svg class="fig" viewBox="0 0 680 300" width="680">
  <line class="l" x1="60.0" y1="20.0" x2="160.0" y2="20.0"/>
  <line class="l" x1="60.0" y1="20.0" x2="54.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="70.0" y1="20.0" x2="64.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="80.0" y1="20.0" x2="74.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="90.0" y1="20.0" x2="84.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="100.0" y1="20.0" x2="94.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="110.0" y1="20.0" x2="104.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="120.0" y1="20.0" x2="114.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="130.0" y1="20.0" x2="124.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="140.0" y1="20.0" x2="134.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="150.0" y1="20.0" x2="144.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="160.0" y1="20.0" x2="154.4" y2="14.4" stroke-width="1"/>
  <line class="l" x1="110.0" y1="20.0" x2="110.0" y2="40.0"/>
  <circle class="l" cx="110.0" cy="55.0" r="15.0"/>
  <circle class="fi" cx="110.0" cy="55.0" r="3.0"/>
  <line class="l" x1="95.0" y1="55.0" x2="95.0" y2="108.0"/>
  <line class="l" x1="125.0" y1="55.0" x2="125.0" y2="150.0"/>
  <path class="l" d="M70 120 L120 95 L170 120 L170 250 L70 250 Z"/>
  <circle class="l f3" cx="130.0" cy="160.0" r="9.0"/>
  <line class="l" x1="130.0" y1="169.0" x2="130.0" y2="215.0"/>
  <line class="l" x1="130.0" y1="185.0" x2="125.0" y2="150.0"/>
  <line class="l" x1="130.0" y1="215.0" x2="120.0" y2="248.0"/>
  <line class="l" x1="130.0" y1="215.0" x2="140.0" y2="248.0"/>
  <text class="s" x="60.0" y="285.0">люлька m, маляр M</text>
  <circle class="l f3" cx="330.0" cy="120.0" r="22.0"/>
  <text class="i" x="322.0" y="126.0">M</text>
  <line class="l c1" x1="322.0" y1="98.0" x2="322.0" y2="39.0" stroke-width="2.2"/>
  <polygon class="p1" points="322.0,30.0 325.7,39.3 318.3,39.3"/>
  <text class="i tc1" x="300.0" y="42.0">T</text>
  <line class="l c2" x1="338.0" y1="142.0" x2="338.0" y2="91.0" stroke-width="2"/>
  <polygon class="p2" points="338.0,82.0 341.7,91.3 334.3,91.3"/>
  <text class="i tc2" x="344.0" y="92.0">N</text>
  <line class="l c5" x1="330.0" y1="142.0" x2="330.0" y2="206.0" stroke-width="2.2"/>
  <polygon class="p5" points="330.0,215.0 326.3,205.7 333.7,205.7"/>
  <text class="i tc5" x="338.0" y="211.0">Mg</text>
  <line class="l c3" x1="390.0" y1="150.0" x2="390.0" y2="109.0" stroke-width="2.2"/>
  <polygon class="p3" points="390.0,100.0 393.7,109.3 386.3,109.3"/>
  <text class="i tc3" x="398.0" y="112.0">a</text>
  <text class="i" x="330.0" y="262.0" text-anchor="middle">маляр: Ma = T + N − Mg</text>
  <rect class="l f1" x="540.0" y="100.0" width="60.0" height="45.0" rx="4"/>
  <text class="i" x="563.0" y="129.0">m</text>
  <line class="l c1" x1="570.0" y1="100.0" x2="570.0" y2="44.0" stroke-width="2.2"/>
  <polygon class="p1" points="570.0,35.0 573.7,44.3 566.3,44.3"/>
  <text class="i tc1" x="578.0" y="45.0">T</text>
  <line class="l c2" x1="556.0" y1="100.0" x2="556.0" y2="151.0" stroke-width="2"/>
  <polygon class="p2" points="556.0,160.0 552.3,150.7 559.7,150.7"/>
  <text class="i tc2" x="528.0" y="170.0">N</text>
  <line class="l c5" x1="584.0" y1="145.0" x2="584.0" y2="206.0" stroke-width="2.2"/>
  <polygon class="p5" points="584.0,215.0 580.3,205.7 587.7,205.7"/>
  <text class="i tc5" x="590.0" y="211.0">mg</text>
  <text class="i" x="570.0" y="290.0" text-anchor="middle">люлька: ma = T − N − mg</text>
</svg>

:::hint Подсказка
Рассмотрите маляра и люльку **по отдельности**. На маляра верёвка действует вверх (он тянет её вниз), пол — тоже вверх. На люльку верёвка действует вверх, а маляр давит на пол вниз с силой $N$. Ускорение у них общее.
:::

:::solution Решение
Натяжение невесомой верёвки через блок без трения одинаково — $T$. Ось вверх, ускорение $a$ общее.

Маляр: $\quad Ma = T + N - Mg$

Люлька: $\quad ma = T - N - mg$

Вычтем второе уравнение из первого — $T$ сократится:
$$(M - m)a = 2N - (M - m)g \;\Rightarrow\; a = \frac{2N}{M - m} - g.$$
$$a = \frac{2 \cdot 400}{72 - 12} - 9{,}8 = 13{,}33 - 9{,}8 \approx 3{,}5\ \text{м/с}^2,$$
направлено **вверх** (знак плюс).

**Проверка.** Сложив уравнения: $(M+m)(a+g) = 2T \Rightarrow T = \tfrac{84 \cdot 13{,}33}{2} = 560$ Н. Тогда для маляра: $N = M(a+g) - T = 72\cdot 13{,}33 - 560 = 400$ Н ✓.
:::

:::tip Что здесь важно
Маляр давит на пол **слабее** своего веса ($400 < 72 \cdot 9{,}8 \approx 706$ Н), а люлька всё равно ускоряется вверх: верёвка тянет систему вверх **дважды** — через руки маляра и через крепление к люльке.
:::

## Задача 2. Клин и стержень

> Сила $F$ двигает клин 1; стержень 2 может двигаться только вертикально (в направляющей) и опирается на клин. Угол клина $\alpha$, массы клина и стержня равны $m$, трения нет. Найти ускорение и силу взаимодействия клина и стержня.

<svg class="fig" viewBox="0 0 640 270" width="640">
  <line class="l" x1="30.0" y1="220.0" x2="420.0" y2="220.0"/>
  <line class="l" x1="30.0" y1="220.0" x2="24.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="40.0" y1="220.0" x2="34.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="50.0" y1="220.0" x2="44.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="60.0" y1="220.0" x2="54.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="70.0" y1="220.0" x2="64.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="80.0" y1="220.0" x2="74.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="90.0" y1="220.0" x2="84.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="100.0" y1="220.0" x2="94.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="110.0" y1="220.0" x2="104.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="120.0" y1="220.0" x2="114.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="130.0" y1="220.0" x2="124.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="140.0" y1="220.0" x2="134.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="150.0" y1="220.0" x2="144.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="160.0" y1="220.0" x2="154.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="170.0" y1="220.0" x2="164.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="180.0" y1="220.0" x2="174.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="190.0" y1="220.0" x2="184.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="200.0" y1="220.0" x2="194.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="210.0" y1="220.0" x2="204.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="220.0" y1="220.0" x2="214.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="230.0" y1="220.0" x2="224.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="240.0" y1="220.0" x2="234.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="250.0" y1="220.0" x2="244.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="260.0" y1="220.0" x2="254.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="270.0" y1="220.0" x2="264.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="280.0" y1="220.0" x2="274.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="290.0" y1="220.0" x2="284.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="300.0" y1="220.0" x2="294.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="310.0" y1="220.0" x2="304.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="320.0" y1="220.0" x2="314.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="330.0" y1="220.0" x2="324.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="340.0" y1="220.0" x2="334.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="350.0" y1="220.0" x2="344.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="360.0" y1="220.0" x2="354.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="370.0" y1="220.0" x2="364.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="380.0" y1="220.0" x2="374.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="390.0" y1="220.0" x2="384.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="400.0" y1="220.0" x2="394.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="410.0" y1="220.0" x2="404.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="420.0" y1="220.0" x2="414.4" y2="225.6" stroke-width="1"/>
  <path class="l f1" d="M60 220 L390.0 220 L390.0 73.1 Z"/>
  <path class="l" d="M105 220 A45 45 0 0 0 101.1 201.7"/>
  <text class="i" x="110.0" y="214.0">α</text>
  <rect class="l f3" x="244.0" y="20.0" width="12.0" height="115.4" rx="0"/>
  <line class="l" x1="234.0" y1="40.0" x2="234.0" y2="110.0"/>
  <line class="l" x1="266.0" y1="40.0" x2="266.0" y2="110.0"/>
  <text class="s" x="272.0" y="60.0">направляющая</text>
  <line class="l c2" x1="450.0" y1="180.0" x2="404.0" y2="180.0" stroke-width="2.2"/>
  <polygon class="p2" points="395.0,180.0 404.3,176.3 404.3,183.7"/>
  <text class="i tc2" x="425.0" y="172.0">F</text>
  <text class="s" x="200.0" y="205.0">1 (m)</text>
  <text class="s" x="210.0" y="30.0">2 (m)</text>
  <line class="l c1" x1="250.0" y1="135.4" x2="225.2" y2="79.7" stroke-width="2.2"/>
  <polygon class="p1" points="221.5,71.5 228.7,78.4 221.9,81.5"/>
  <text class="i tc1" x="197.5" y="75.5">N</text>
  <line class="l c5" x1="254.0" y1="139.4" x2="278.8" y2="195.1" stroke-width="2.2"/>
  <polygon class="p5" points="282.5,203.4 275.3,196.4 282.1,193.4"/>
  <text class="i tc5" x="286.5" y="219.4">N</text>
  <line class="l c2" x1="470.0" y1="120.0" x2="590.0" y2="120.0"/>
  <text class="s" x="504.0" y="138.0">клин сдвинулся на x</text>
  <line class="l c1" x1="590.0" y1="120.0" x2="590.0" y2="66.6"/>
  <line class="l d" x1="470.0" y1="120.0" x2="590.0" y2="66.6"/>
  <text class="i tc1" x="596.0" y="98.0">x·tg α</text>
  <text class="s" x="466.0" y="170.0">стержень поднялся на x·tg α</text>
</svg>

:::hint Подсказка
1. Сила между клином и стержнем $N$ перпендикулярна поверхности клина.
2. Кинематика: клин сместился на $x$ влево — стержень поднялся на $x\tan\alpha$. Значит, $a_{стержня} = a\tan\alpha$.
:::

:::solution Решение
Пусть клин движется с ускорением $a$ (влево), тогда стержень — с ускорением $a\tan\alpha$ вверх.

**Стержень** (по вертикали; горизонтальную составляющую $N$ гасит направляющая):
$$m\,a\tan\alpha = N\cos\alpha - mg. \qquad (1)$$

**Клин** (по горизонтали; со стороны стержня на клин действует $N$, направленная вниз-вправо — против движения):
$$m a = F - N\sin\alpha. \qquad (2)$$

Из (1): $N = \dfrac{m(g + a\tan\alpha)}{\cos\alpha}$. Подставляем в (2):
$$ma = F - mg\tan\alpha - ma\tan^2\alpha \;\Rightarrow\; ma\,(1 + \tan^2\alpha) = F - mg\tan\alpha.$$
Так как $1 + \tan^2\alpha = \dfrac{1}{\cos^2\alpha}$:
$$\boxed{a = \frac{(F\cos\alpha - mg\sin\alpha)\cos\alpha}{m}}$$
— это ускорение клина; стержень поднимается с ускорением $a\tan\alpha$.

Сила взаимодействия:
$$N = \frac{m(g + a\tan\alpha)}{\cos\alpha} = \frac{mg\cos^2\alpha + F\sin\alpha\cos\alpha}{\cos\alpha} \;\Rightarrow\; \boxed{N = F\sin\alpha + mg\cos\alpha}.$$
:::

:::tip Проверка предельных случаев
- $\alpha \to 0$: клин плоский, стержень просто стоит на нём. $a = F/m$, $N = mg$ ✓.
- Движение начнётся, только если $F\cos\alpha > mg\sin\alpha$, то есть $F > mg\tan\alpha$. Иначе $a = 0$, и всё стоит (формула дала бы $a < 0$, а клин тянуть вправо нечем).
:::

## Задача 3. Клин упирается в стену

> Клин с углом $\alpha = 15^\circ$ лежит на гладком полу и упирается торцом в стену. По его грани без трения скользит тело $m = 0{,}20$ кг. С какой силой клин давит на стену?

<svg class="fig" viewBox="0 0 600 250" width="600">
  <line class="l" x1="40.0" y1="30.0" x2="40.0" y2="220.0"/>
  <line class="l" x1="40.0" y1="30.0" x2="34.4" y2="24.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="40.0" x2="34.4" y2="34.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="50.0" x2="34.4" y2="44.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="60.0" x2="34.4" y2="54.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="70.0" x2="34.4" y2="64.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="80.0" x2="34.4" y2="74.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="90.0" x2="34.4" y2="84.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="100.0" x2="34.4" y2="94.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="110.0" x2="34.4" y2="104.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="120.0" x2="34.4" y2="114.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="130.0" x2="34.4" y2="124.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="140.0" x2="34.4" y2="134.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="150.0" x2="34.4" y2="144.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="160.0" x2="34.4" y2="154.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="170.0" x2="34.4" y2="164.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="180.0" x2="34.4" y2="174.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="190.0" x2="34.4" y2="184.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="200.0" x2="34.4" y2="194.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="210.0" x2="34.4" y2="204.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="220.0" x2="34.4" y2="214.4" stroke-width="1"/>
  <line class="l" x1="40.0" y1="220.0" x2="560.0" y2="220.0"/>
  <line class="l" x1="40.0" y1="220.0" x2="34.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="50.0" y1="220.0" x2="44.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="60.0" y1="220.0" x2="54.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="70.0" y1="220.0" x2="64.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="80.0" y1="220.0" x2="74.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="90.0" y1="220.0" x2="84.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="100.0" y1="220.0" x2="94.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="110.0" y1="220.0" x2="104.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="120.0" y1="220.0" x2="114.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="130.0" y1="220.0" x2="124.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="140.0" y1="220.0" x2="134.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="150.0" y1="220.0" x2="144.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="160.0" y1="220.0" x2="154.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="170.0" y1="220.0" x2="164.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="180.0" y1="220.0" x2="174.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="190.0" y1="220.0" x2="184.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="200.0" y1="220.0" x2="194.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="210.0" y1="220.0" x2="204.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="220.0" y1="220.0" x2="214.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="230.0" y1="220.0" x2="224.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="240.0" y1="220.0" x2="234.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="250.0" y1="220.0" x2="244.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="260.0" y1="220.0" x2="254.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="270.0" y1="220.0" x2="264.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="280.0" y1="220.0" x2="274.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="290.0" y1="220.0" x2="284.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="300.0" y1="220.0" x2="294.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="310.0" y1="220.0" x2="304.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="320.0" y1="220.0" x2="314.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="330.0" y1="220.0" x2="324.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="340.0" y1="220.0" x2="334.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="350.0" y1="220.0" x2="344.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="360.0" y1="220.0" x2="354.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="370.0" y1="220.0" x2="364.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="380.0" y1="220.0" x2="374.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="390.0" y1="220.0" x2="384.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="400.0" y1="220.0" x2="394.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="410.0" y1="220.0" x2="404.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="420.0" y1="220.0" x2="414.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="430.0" y1="220.0" x2="424.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="440.0" y1="220.0" x2="434.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="450.0" y1="220.0" x2="444.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="460.0" y1="220.0" x2="454.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="470.0" y1="220.0" x2="464.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="480.0" y1="220.0" x2="474.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="490.0" y1="220.0" x2="484.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="500.0" y1="220.0" x2="494.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="510.0" y1="220.0" x2="504.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="520.0" y1="220.0" x2="514.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="530.0" y1="220.0" x2="524.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="540.0" y1="220.0" x2="534.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="550.0" y1="220.0" x2="544.4" y2="225.6" stroke-width="1"/>
  <line class="l" x1="560.0" y1="220.0" x2="554.4" y2="225.6" stroke-width="1"/>
  <path class="l f1" d="M40 220 L40 52.6 L500 220 Z"/>
  <text class="i" x="430.0" y="212.0">α</text>
  <polygon class="l f3" points="187.1,106.1 252.9,130.1 261.8,105.6 196.0,81.7"/>
  <text class="i" x="218.4" y="110.9">m</text>
  <line class="l c1" x1="224.4" y1="105.9" x2="248.7" y2="39.2" stroke-width="2.2"/>
  <polygon class="p1" points="251.8,30.7 252.1,40.7 245.1,38.2"/>
  <text class="i tc1" x="257.8" y="34.7">N₁</text>
  <line class="l c5" x1="224.4" y1="105.9" x2="224.4" y2="171.9" stroke-width="2.2"/>
  <polygon class="p5" points="224.4,180.9 220.7,171.6 228.2,171.6"/>
  <text class="i tc5" x="230.4" y="188.9">mg</text>
  <line class="l c2" x1="226.0" y1="124.1" x2="203.4" y2="186.1" stroke-width="2.2"/>
  <polygon class="p2" points="200.3,194.6 200.0,184.6 207.0,187.1"/>
  <text class="i tc2" x="170.3" y="204.6">N₁</text>
  <line class="l c4" x1="40.0" y1="120.0" x2="91.0" y2="120.0" stroke-width="2.2"/>
  <polygon class="p4" points="100.0,120.0 90.7,123.7 90.7,116.3"/>
  <text class="i tc4" x="106.0" y="114.0">R</text>
  <text class="s" x="70.0" y="145.0">реакция стены</text>
</svg>

:::hint Подсказка
Клин прижат к стене и **не движется** — значит, тело скользит по неподвижной наклонной плоскости. Найдите силу давления тела на клин и возьмите её горизонтальную составляющую.
:::

:::solution Решение
Клин неподвижен, поэтому для тела всё как на обычной наклонной плоскости: $N_1 = mg\cos\alpha$.

По третьему закону тело давит на клин с силой $N_1$, направленной перпендикулярно грани — вниз и **к стене**. Её горизонтальная составляющая
$$N_1\sin\alpha = mg\cos\alpha\sin\alpha = \tfrac12 mg\sin 2\alpha.$$

Клин в равновесии по горизонтали (пол гладкий, трения нет), значит, стена действует на него с такой же силой, а он на стену — с силой
$$N = \tfrac12 mg\sin 2\alpha = \tfrac12 \cdot 0{,}20 \cdot 9{,}8 \cdot \sin 30^\circ \approx 0{,}49\ \text{Н} \approx 0{,}5\ \text{Н}.$$
:::

:::warn Где можно ошибиться
Сказать «$N = mg\sin\alpha$» — это скатывающая сила вдоль склона, а стене передаётся **горизонтальная составляющая силы давления** $N_1$. Ещё одна ловушка — забыть, что сила давления тела на клин направлена **к стене**. Если бы она была направлена от стены, клин бы отъехал, и задача была бы совсем другой.
:::

## Задача 4. Тележка с грузом на вогнутом мосту

> Тележка $M$ едет по вогнутому мосту (дуга радиуса $R$). К ней привязан трос длины $L$ с грузом $m$. В нижней точке моста трос вертикален, скорости тележки и груза $v_1$ и $v_2$. Найти натяжение $T$ и силу $N$ давления тележки на рельсы.

<svg class="fig" viewBox="0 0 560 300" width="560">
  <path class="l" d="M48 40 A300 300 0 0 0 512 40"/>
  <rect class="l f1" x="262.0" y="136.0" width="36.0" height="14.0" rx="3"/>
  <text class="i" x="230.0" y="146.0">M</text>
  <line class="l" x1="280.0" y1="150.0" x2="280.0" y2="243.0"/>
  <circle class="l f3" cx="280.0" cy="250.0" r="7.0"/>
  <text class="i" x="254.0" y="256.0">m</text>
  <line class="l c2" x1="306.0" y1="126.0" x2="357.0" y2="126.0" stroke-width="2.2"/>
  <polygon class="p2" points="366.0,126.0 356.7,129.7 356.7,122.3"/>
  <text class="i tc2" x="372.0" y="131.0">v₁</text>
  <line class="l c2" x1="294.0" y1="262.0" x2="325.0" y2="262.0" stroke-width="2.2"/>
  <polygon class="p2" points="334.0,262.0 324.7,265.7 324.7,258.3"/>
  <text class="i tc2" x="340.0" y="267.0">v₂</text>
  <text class="i" x="288.0" y="205.0">L</text>
  <text class="s" x="70.0" y="280.0">в нижней точке: обе скорости горизонтальны, трос вертикален</text>
</svg>

:::hint Подсказка
Тележка движется по окружности радиуса $R$: её ускорение $\dfrac{v_1^2}{R}$ вверх. Груз **относительно тележки** движется по окружности радиуса $L$ с относительной скоростью $v_2 - v_1$. Полное ускорение груза — сумма.
:::

:::solution Решение
В нижней точке все силы вертикальны (трос вертикален, рельсы горизонтальны), поэтому горизонтальных ускорений нет — только вертикальные.

**Ускорение тележки:** $a_1 = \dfrac{v_1^2}{R}$, вверх (к центру дуги).

**Ускорение груза.** Перейдём в систему отсчёта, которая движется поступательно вместе с точкой крепления троса. В ней груз движется по окружности радиуса $L$ со скоростью $v_2 - v_1$, и его относительное ускорение $\dfrac{(v_1 - v_2)^2}{L}$ направлено вверх, к точке крепления. Абсолютное ускорение груза
$$a_2 = \frac{v_1^2}{R} + \frac{(v_1 - v_2)^2}{L}\quad\text{(вверх)}.$$

**Груз:** $T - mg = m a_2$:
$$\boxed{T = m\left(g + \frac{v_1^2}{R} + \frac{(v_1 - v_2)^2}{L}\right)}$$

**Тележка:** на неё действуют $N$ вверх, $Mg$ и $T$ вниз: $N - Mg - T = M\dfrac{v_1^2}{R}$:
$$\boxed{N = (m + M)\left(g + \frac{v_1^2}{R}\right) + m\,\frac{(v_1 - v_2)^2}{L}}$$
:::

:::tip Проверка
Если груз неподвижен относительно тележки ($v_2 = v_1$), то система ведёт себя как одно тело массы $m + M$: $N = (m+M)\left(g + \frac{v_1^2}{R}\right)$ ✓.
:::

## Задача 5. Клин между двумя брусками

> Клин массы $m_2$ с углом $\alpha$ при вершине вставлен между двумя одинаковыми гладкими брусками массы $m_1$. Найти ускорения тел.

<svg class="fig" viewBox="0 0 560 260" width="560">
  <line class="l" x1="60.0" y1="210.0" x2="500.0" y2="210.0"/>
  <line class="l" x1="60.0" y1="210.0" x2="54.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="70.0" y1="210.0" x2="64.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="80.0" y1="210.0" x2="74.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="90.0" y1="210.0" x2="84.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="100.0" y1="210.0" x2="94.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="110.0" y1="210.0" x2="104.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="120.0" y1="210.0" x2="114.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="130.0" y1="210.0" x2="124.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="140.0" y1="210.0" x2="134.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="150.0" y1="210.0" x2="144.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="160.0" y1="210.0" x2="154.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="170.0" y1="210.0" x2="164.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="180.0" y1="210.0" x2="174.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="190.0" y1="210.0" x2="184.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="200.0" y1="210.0" x2="194.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="210.0" y1="210.0" x2="204.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="220.0" y1="210.0" x2="214.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="230.0" y1="210.0" x2="224.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="240.0" y1="210.0" x2="234.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="250.0" y1="210.0" x2="244.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="260.0" y1="210.0" x2="254.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="270.0" y1="210.0" x2="264.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="280.0" y1="210.0" x2="274.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="290.0" y1="210.0" x2="284.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="300.0" y1="210.0" x2="294.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="310.0" y1="210.0" x2="304.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="320.0" y1="210.0" x2="314.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="330.0" y1="210.0" x2="324.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="340.0" y1="210.0" x2="334.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="350.0" y1="210.0" x2="344.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="360.0" y1="210.0" x2="354.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="370.0" y1="210.0" x2="364.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="380.0" y1="210.0" x2="374.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="390.0" y1="210.0" x2="384.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="400.0" y1="210.0" x2="394.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="410.0" y1="210.0" x2="404.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="420.0" y1="210.0" x2="414.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="430.0" y1="210.0" x2="424.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="440.0" y1="210.0" x2="434.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="450.0" y1="210.0" x2="444.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="460.0" y1="210.0" x2="454.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="470.0" y1="210.0" x2="464.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="480.0" y1="210.0" x2="474.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="490.0" y1="210.0" x2="484.4" y2="215.6" stroke-width="1"/>
  <line class="l" x1="500.0" y1="210.0" x2="494.4" y2="215.6" stroke-width="1"/>
  <rect class="l f1" x="139.0" y="140.0" width="120.0" height="70.0" rx="0"/>
  <rect class="l f1" x="301.0" y="140.0" width="120.0" height="70.0" rx="0"/>
  <text class="i" x="154.0" y="196.0">m₁</text>
  <text class="i" x="351.0" y="182.0">m₁</text>
  <path class="l f3" d="M280 170 L189.0 40 L371.0 40 Z"/>
  <text class="i" x="270.0" y="70.0">m₂</text>
  <path class="l" d="M268.5 153.6 A20 20 0 0 1 291.5 153.6"/>
  <text class="i s" x="274.0" y="144.0">α</text>
  <line class="l c2" x1="259.0" y1="140.0" x2="309.0" y2="105.0" stroke-width="2.2"/>
  <polygon class="p2" points="316.3,99.8 310.9,108.2 306.6,102.1"/>
  <text class="i tc2" x="320.3" y="95.8">N</text>
  <line class="l c5" x1="259.0" y1="140.0" x2="209.0" y2="175.0" stroke-width="2.2"/>
  <polygon class="p5" points="201.7,180.2 207.1,171.8 211.4,177.9"/>
  <text class="i tc5" x="179.7" y="194.2">N</text>
  <line class="l c3" x1="500.0" y1="60.0" x2="500.0" y2="111.0" stroke-width="2.2"/>
  <polygon class="p3" points="500.0,120.0 496.3,110.7 503.7,110.7"/>
  <text class="i tc3" x="508.0" y="112.0">a₂</text>
  <line class="l c3" x1="100.0" y1="110.0" x2="49.0" y2="110.0" stroke-width="2.2"/>
  <polygon class="p3" points="40.0,110.0 49.3,106.3 49.3,113.7"/>
  <text class="i tc3" x="30.0" y="100.0">a₁</text>
</svg>

:::hint Подсказка
Каждая грань клина отклонена от вертикали на $\frac\alpha2$. Если клин опустился на $y$, каждый брусок отъехал на $y\tan\frac\alpha2$.
:::

:::solution Решение
Пусть клин опускается с ускорением $a_2$, бруски разъезжаются с ускорениями $a_1$ (по модулю одинаковыми, по симметрии).

**Связь:** $a_1 = a_2\tan\dfrac{\alpha}{2}$.

Сила $N$ между клином и бруском перпендикулярна грани клина. Грань отклонена от вертикали на $\frac\alpha2$, поэтому нормаль отклонена от **горизонтали** на $\frac\alpha2$:
- на брусок — горизонтальная составляющая $N\cos\frac\alpha2$ (наружу);
- на клин от каждого бруска — вертикальная составляющая $N\sin\frac\alpha2$ (вверх).

**Брусок** (по горизонтали): $m_1 a_1 = N\cos\dfrac\alpha2$.

**Клин** (по вертикали, вниз): $m_2 a_2 = m_2 g - 2N\sin\dfrac\alpha2$.

Из первого: $N = \dfrac{m_1 a_2\tan\frac\alpha2}{\cos\frac\alpha2}$. Подставляем:
$$m_2 a_2 = m_2 g - 2m_1 a_2\tan^2\frac\alpha2 \;\Rightarrow\; \boxed{a_2 = \frac{m_2 g}{m_2 + 2m_1\tan^2\frac\alpha2}}, \qquad \boxed{a_1 = \frac{m_2 g\tan\frac\alpha2}{m_2 + 2m_1\tan^2\frac\alpha2}}.$$
:::

:::tip Проверка
- $m_1 \to 0$ (бруски невесомые): $a_2 = g$ — клин падает свободно ✓.
- $\alpha \to 0$ (очень острый клин): $a_2 \to g$, а бруски почти не двигаются ($a_1 \to 0$) ✓.
:::

## Как оформить решение для сдачи

1. Для каждого тела — **отдельная диаграмма сил** (учитель снимает баллы, если есть только рисунок и ответ, см. комментарий к Hometask 3).
2. Явно выпишите **кинематическую связь** и откуда она взялась (маленький рисунок со смещением $x$).
3. Второй закон — в проекциях, с указанием оси.
4. Ответ — в общем виде, затем число с единицами, **направление** ускорения словами (учитель отдельно просит указывать направление).
5. Короткая проверка предельного случая — это плюс к оценке.
