---
title: "Изображения как массивы — пиксели, RGB, объём файла, обработка в NumPy"
kind: notes
tasks: [49243189]
order: 40
summary: Растровая картинка = массив чисел, глубина цвета и объём памяти, RGB и оттенки серого, операции NumPy: обрезка, отражение, поворот, негатив, яркость и контраст, порог, размытие. Задачи с ответами.
---

## 1. Картинка — это массив чисел

**Растровое изображение** (*raster image*) — прямоугольная сетка **пикселей**. Каждый пиксель хранит цвет числом (или несколькими числами).

<svg class="fig" viewBox="0 0 640 260" width="640">
  <rect x="60" y="40" width="34" height="34" style="fill:rgb(0,0,0);stroke:#888;stroke-width:0.6"/>
  <text x="77.0" y="61.0" text-anchor="middle" style="fill:#fff;font-size:10px">0</text>
  <rect x="94" y="40" width="34" height="34" style="fill:rgb(40,40,40);stroke:#888;stroke-width:0.6"/>
  <text x="111.0" y="61.0" text-anchor="middle" style="fill:#fff;font-size:10px">40</text>
  <rect x="128" y="40" width="34" height="34" style="fill:rgb(80,80,80);stroke:#888;stroke-width:0.6"/>
  <text x="145.0" y="61.0" text-anchor="middle" style="fill:#fff;font-size:10px">80</text>
  <rect x="162" y="40" width="34" height="34" style="fill:rgb(120,120,120);stroke:#888;stroke-width:0.6"/>
  <text x="179.0" y="61.0" text-anchor="middle" style="fill:#fff;font-size:10px">120</text>
  <rect x="196" y="40" width="34" height="34" style="fill:rgb(160,160,160);stroke:#888;stroke-width:0.6"/>
  <text x="213.0" y="61.0" text-anchor="middle" style="fill:#000;font-size:10px">160</text>
  <rect x="230" y="40" width="34" height="34" style="fill:rgb(200,200,200);stroke:#888;stroke-width:0.6"/>
  <text x="247.0" y="61.0" text-anchor="middle" style="fill:#000;font-size:10px">200</text>
  <rect x="60" y="74" width="34" height="34" style="fill:rgb(30,30,30);stroke:#888;stroke-width:0.6"/>
  <text x="77.0" y="95.0" text-anchor="middle" style="fill:#fff;font-size:10px">30</text>
  <rect x="94" y="74" width="34" height="34" style="fill:rgb(60,60,60);stroke:#888;stroke-width:0.6"/>
  <text x="111.0" y="95.0" text-anchor="middle" style="fill:#fff;font-size:10px">60</text>
  <rect x="128" y="74" width="34" height="34" style="fill:rgb(255,255,255);stroke:#888;stroke-width:0.6"/>
  <text x="145.0" y="95.0" text-anchor="middle" style="fill:#000;font-size:10px">255</text>
  <rect x="162" y="74" width="34" height="34" style="fill:rgb(255,255,255);stroke:#888;stroke-width:0.6"/>
  <text x="179.0" y="95.0" text-anchor="middle" style="fill:#000;font-size:10px">255</text>
  <rect x="196" y="74" width="34" height="34" style="fill:rgb(90,90,90);stroke:#888;stroke-width:0.6"/>
  <text x="213.0" y="95.0" text-anchor="middle" style="fill:#fff;font-size:10px">90</text>
  <rect x="230" y="74" width="34" height="34" style="fill:rgb(120,120,120);stroke:#888;stroke-width:0.6"/>
  <text x="247.0" y="95.0" text-anchor="middle" style="fill:#fff;font-size:10px">120</text>
  <rect x="60" y="108" width="34" height="34" style="fill:rgb(60,60,60);stroke:#888;stroke-width:0.6"/>
  <text x="77.0" y="129.0" text-anchor="middle" style="fill:#fff;font-size:10px">60</text>
  <rect x="94" y="108" width="34" height="34" style="fill:rgb(255,255,255);stroke:#888;stroke-width:0.6"/>
  <text x="111.0" y="129.0" text-anchor="middle" style="fill:#000;font-size:10px">255</text>
  <rect x="128" y="108" width="34" height="34" style="fill:rgb(0,0,0);stroke:#888;stroke-width:0.6"/>
  <text x="145.0" y="129.0" text-anchor="middle" style="fill:#fff;font-size:10px">0</text>
  <rect x="162" y="108" width="34" height="34" style="fill:rgb(0,0,0);stroke:#888;stroke-width:0.6"/>
  <text x="179.0" y="129.0" text-anchor="middle" style="fill:#fff;font-size:10px">0</text>
  <rect x="196" y="108" width="34" height="34" style="fill:rgb(255,255,255);stroke:#888;stroke-width:0.6"/>
  <text x="213.0" y="129.0" text-anchor="middle" style="fill:#000;font-size:10px">255</text>
  <rect x="230" y="108" width="34" height="34" style="fill:rgb(150,150,150);stroke:#888;stroke-width:0.6"/>
  <text x="247.0" y="129.0" text-anchor="middle" style="fill:#000;font-size:10px">150</text>
  <rect x="60" y="142" width="34" height="34" style="fill:rgb(90,90,90);stroke:#888;stroke-width:0.6"/>
  <text x="77.0" y="163.0" text-anchor="middle" style="fill:#fff;font-size:10px">90</text>
  <rect x="94" y="142" width="34" height="34" style="fill:rgb(120,120,120);stroke:#888;stroke-width:0.6"/>
  <text x="111.0" y="163.0" text-anchor="middle" style="fill:#fff;font-size:10px">120</text>
  <rect x="128" y="142" width="34" height="34" style="fill:rgb(255,255,255);stroke:#888;stroke-width:0.6"/>
  <text x="145.0" y="163.0" text-anchor="middle" style="fill:#000;font-size:10px">255</text>
  <rect x="162" y="142" width="34" height="34" style="fill:rgb(255,255,255);stroke:#888;stroke-width:0.6"/>
  <text x="179.0" y="163.0" text-anchor="middle" style="fill:#000;font-size:10px">255</text>
  <rect x="196" y="142" width="34" height="34" style="fill:rgb(180,180,180);stroke:#888;stroke-width:0.6"/>
  <text x="213.0" y="163.0" text-anchor="middle" style="fill:#000;font-size:10px">180</text>
  <rect x="230" y="142" width="34" height="34" style="fill:rgb(180,180,180);stroke:#888;stroke-width:0.6"/>
  <text x="247.0" y="163.0" text-anchor="middle" style="fill:#000;font-size:10px">180</text>
  <rect x="60" y="176" width="34" height="34" style="fill:rgb(120,120,120);stroke:#888;stroke-width:0.6"/>
  <text x="77.0" y="197.0" text-anchor="middle" style="fill:#fff;font-size:10px">120</text>
  <rect x="94" y="176" width="34" height="34" style="fill:rgb(150,150,150);stroke:#888;stroke-width:0.6"/>
  <text x="111.0" y="197.0" text-anchor="middle" style="fill:#000;font-size:10px">150</text>
  <rect x="128" y="176" width="34" height="34" style="fill:rgb(180,180,180);stroke:#888;stroke-width:0.6"/>
  <text x="145.0" y="197.0" text-anchor="middle" style="fill:#000;font-size:10px">180</text>
  <rect x="162" y="176" width="34" height="34" style="fill:rgb(210,210,210);stroke:#888;stroke-width:0.6"/>
  <text x="179.0" y="197.0" text-anchor="middle" style="fill:#000;font-size:10px">210</text>
  <rect x="196" y="176" width="34" height="34" style="fill:rgb(240,240,240);stroke:#888;stroke-width:0.6"/>
  <text x="213.0" y="197.0" text-anchor="middle" style="fill:#000;font-size:10px">240</text>
  <rect x="230" y="176" width="34" height="34" style="fill:rgb(255,255,255);stroke:#888;stroke-width:0.6"/>
  <text x="247.0" y="197.0" text-anchor="middle" style="fill:#000;font-size:10px">255</text>
  <text class="s" x="77.0" y="32.0" text-anchor="middle">0</text>
  <text class="s" x="111.0" y="32.0" text-anchor="middle">1</text>
  <text class="s" x="145.0" y="32.0" text-anchor="middle">2</text>
  <text class="s" x="179.0" y="32.0" text-anchor="middle">3</text>
  <text class="s" x="213.0" y="32.0" text-anchor="middle">4</text>
  <text class="s" x="247.0" y="32.0" text-anchor="middle">5</text>
  <text class="s" x="46.0" y="61.0" text-anchor="middle">0</text>
  <text class="s" x="46.0" y="95.0" text-anchor="middle">1</text>
  <text class="s" x="46.0" y="129.0" text-anchor="middle">2</text>
  <text class="s" x="46.0" y="163.0" text-anchor="middle">3</text>
  <text class="s" x="46.0" y="197.0" text-anchor="middle">4</text>
  <text class="s" x="162.0" y="236.0" text-anchor="middle">img.shape == (5, 6) — 5 строк (y), 6 столбцов (x)</text>
  <text class="s" x="16.0" y="125.0">i ↓</text>
  <text class="s" x="274.0" y="32.0">j →</text>
  <text class="s" x="330.0" y="60.0">img[1, 2] == 255  (строка 1, столбец 2)</text>
  <text class="s" x="330.0" y="84.0">img[2] — вся строка 2</text>
  <text class="s" x="330.0" y="108.0">img[:, 0] — весь столбец 0</text>
  <text class="s" x="330.0" y="132.0">img[1:4, 1:5] — вырезать кусок</text>
  <text class="s" x="330.0" y="156.0">255 - img — негатив</text>
  <text class="s" x="330.0" y="180.0">img > 128 — маска «светлых» пикселей</text>
  <text class="s" x="330.0" y="214.0">Цветная картинка: shape == (h, w, 3)</text>
  <text class="s" x="330.0" y="232.0">img[i, j] == [R, G, B], каждое 0…255</text>
</svg>

- **Чёрно-белое (оттенки серого, *grayscale*)**: массив формы `(h, w)`, каждое число 0…255 (0 — чёрный, 255 — белый), тип `uint8`.
- **Цветное (RGB)**: массив формы `(h, w, 3)` — для каждого пикселя три числа: красный, зелёный, синий (*Red, Green, Blue*), каждое 0…255. Белый `[255, 255, 255]`, чёрный `[0, 0, 0]`, жёлтый `[255, 255, 0]` (красный + зелёный свет).
- Индексы: `img[y, x]` — **сначала строка (y), потом столбец (x)**, начало в левом верхнем углу.

## 2. Глубина цвета и объём

:::formula Объём несжатого изображения
$$V = w\cdot h\cdot i\ \text{бит},$$
где $i$ — **глубина цвета** (*bit depth*): число бит на пиксель. Число цветов $N = 2^i$, и наоборот $i = \lceil\log_2N\rceil$.
:::

| Картинка | $i$ | Цветов |
|---|---|---|
| чёрно-белая (только 2 цвета) | 1 | 2 |
| 256 оттенков серого | 8 | 256 |
| True Color (RGB по 8 бит) | 24 | $2^{24} \approx 16{,}7$ млн |

:::example Пример
Фото 1920×1080 в True Color: $1920\cdot1080\cdot24 = 49\,766\,400$ бит $= 6\,220\,800$ байт $\approx 5{,}93$ МиБ. Файлы JPEG/PNG меньше, потому что **сжаты**.
:::

## 3. Загрузка и сохранение

```python
import numpy as np
from PIL import Image          # pip install pillow

img = np.array(Image.open("cat.jpg"))     # (h, w, 3), uint8
print(img.shape, img.dtype)
Image.fromarray(img).save("copy.png")
# в Jupyter: import matplotlib.pyplot as plt; plt.imshow(img); plt.show()
```

## 4. Обработка — всё одной строкой

```python
h, w = img.shape[:2]
crop  = img[100:300, 50:250]            # обрезка: строки 100–299, столбцы 50–249
flipx = img[:, ::-1]                    # отражение слева направо
flipy = img[::-1, :]                    # отражение сверху вниз
rot   = np.rot90(img)                   # поворот на 90° против часовой
neg   = 255 - img                       # негатив (uint8 не переполнится: 255 − x ∈ [0; 255])
red   = img.copy(); red[:, :, 1:] = 0   # оставить только красный канал
small = img[::2, ::2]                   # уменьшить в 2 раза (каждый второй пиксель)
```

**Оттенки серого.** Глаз сильнее всего чувствует зелёный, слабее всего синий, поэтому берут взвешенное среднее:
$$Y = 0{,}299R + 0{,}587G + 0{,}114B.$$
```python
gray = (img @ np.array([0.299, 0.587, 0.114])).astype(np.uint8)   # (h, w, 3) @ (3,) → (h, w)
```

**Яркость и контраст** — обязательно через `int`/`float` и `clip`, иначе переполнение `uint8`:
```python
f = img.astype(float)
brighter = np.clip(f + 50, 0, 255).astype(np.uint8)            # ярче на 50
contrast = np.clip((f - 128) * 1.5 + 128, 0, 255).astype(np.uint8)   # контраст × 1,5
```

**Порог (бинаризация)** — маска:
```python
bw = np.where(gray > 128, 255, 0).astype(np.uint8)
print((gray > 128).mean())     # доля светлых пикселей
```

**Размытие 3×3 (среднее соседей)** — без циклов, сдвигами:
```python
g = gray.astype(float)
blur = (g[:-2, :-2] + g[:-2, 1:-1] + g[:-2, 2:] +
        g[1:-1, :-2] + g[1:-1, 1:-1] + g[1:-1, 2:] +
        g[2:, :-2] + g[2:, 1:-1] + g[2:, 2:]) / 9     # результат на 2 меньше по каждой оси
```
Это частный случай **свёртки** (*convolution*): каждый пиксель заменяется взвешенной суммой соседей. Другие ядра дают резкость или выделение краёв — так работают фильтры в фоторедакторах и первые слои нейросетей.

## 5. Проверь себя

:::task 1. Сколько памяти займёт несжатая картинка 800×600 с палитрой из 64 цветов?
:::answer
$i = \log_264 = 6$ бит. $800\cdot600\cdot6 = 2\,880\,000$ бит $= 360\,000$ байт ≈ 351,6 КиБ.
:::
:::

:::task 2. Картинку 1024×768 сохранили с 16 цветами, а потом с 65 536 цветами. Во сколько раз вырос объём?
:::answer
$i_1 = 4$, $i_2 = 16$ бит — в 4 раза (размеры одинаковые, объём пропорционален $i$).
:::
:::

:::task 3. `img` формы (480, 640, 3). Что вернёт `img[10, 20]`? А `img[:, :, 2].mean()`?
:::answer
`img[10, 20]` — пиксель в строке 10, столбце 20: массив из трёх чисел `[R, G, B]`. `img[:, :, 2].mean()` — средняя интенсивность **синего** канала по всей картинке.
:::
:::

:::task 4. Почему `img + 100` для `uint8` даёт странные цвета?
:::answer
Значения больше 255 «заворачиваются» по модулю 256: $200 + 100 = 300 \to 44$. Яркие места становятся тёмными. Правильно: `np.clip(img.astype(int) + 100, 0, 255).astype(np.uint8)`.
:::
:::

:::task 5. Как одной строкой сделать «шахматную» маску 8×8 из 0 и 1?
:::answer
`(np.arange(8)[:, None] + np.arange(8)) % 2` — broadcasting `(8, 1) + (8,)` даёт матрицу сумм индексов $i + j$, а её чётность чередуется как на шахматной доске.
:::
:::
