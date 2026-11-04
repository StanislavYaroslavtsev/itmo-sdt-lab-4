# ITMO SDT Lab 2 — Geometric Lib

Библиотека на Python для вычисления площади и периметра геометрических фигур: круга, квадрата, прямоугольника и треугольника.

## Структура проекта

```
itmo-sdt-lab-2/
├── circle.py       # круг
├── square.py       # квадрат
├── rectangle.py    # прямоугольник
├── triangle.py     # треугольник
└── docs/           # документация Sphinx
```

Каждая фигура вынесена в отдельный модуль, в каждом модуле есть две функции — `area` и `perimeter`.

## Формулы

| Фигура        | Площадь         | Периметр          |
|---------------|-----------------|-------------------|
| Круг          | S = πr²         | P = 2πr           |
| Квадрат       | S = a²          | P = 4a            |
| Прямоугольник | S = a · b       | P = 2(a + b)      |
| Треугольник   | S = a · h / 2   | P = a + b + c     |

## API

### `circle` — круг

#### `area(r)`

Вычисляет площадь круга по заданному радиусу.

| Параметр | Тип     | Описание     |
|----------|---------|--------------|
| `r`      | `float` | радиус круга |

**Возвращает:** `float` — площадь круга.

```python
>>> from circle import area
>>> area(4)
50.26548245743669
```

#### `perimeter(r)`

Вычисляет длину окружности по заданному радиусу.

| Параметр | Тип     | Описание     |
|----------|---------|--------------|
| `r`      | `float` | радиус круга |

**Возвращает:** `float` — длина окружности.

```python
>>> from circle import perimeter
>>> perimeter(4)
25.132741228718345
```

### `square` — квадрат

#### `area(a)`

Вычисляет площадь квадрата по длине его стороны.

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| `a`      | `float` | длина стороны квадрата |

**Возвращает:** `float` — площадь квадрата.

```python
>>> from square import area
>>> area(4)
16
```

#### `perimeter(a)`

Вычисляет периметр квадрата по длине его стороны.

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| `a`      | `float` | длина стороны квадрата |

**Возвращает:** `float` — периметр квадрата.

```python
>>> from square import perimeter
>>> perimeter(4)
16
```

### `rectangle` — прямоугольник

#### `area(a, b)`

Вычисляет площадь прямоугольника по его длине и ширине.

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| `a`      | `float` | длина прямоугольника   |
| `b`      | `float` | ширина прямоугольника  |

**Возвращает:** `float` — площадь прямоугольника.

```python
>>> from rectangle import area
>>> area(4, 2)
8
```

#### `perimeter(a, b)`

Вычисляет периметр прямоугольника по его длине и ширине.

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| `a`      | `float` | длина прямоугольника   |
| `b`      | `float` | ширина прямоугольника  |

**Возвращает:** `float` — периметр прямоугольника.

```python
>>> from rectangle import perimeter
>>> perimeter(4, 2)
12
```

### `triangle` — треугольник

#### `area(a, h)`

Вычисляет площадь треугольника по его стороне и высоте.

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| `a`      | `float` | сторона треугольника   |
| `h`      | `float` | высота треугольника    |

**Возвращает:** `float` — площадь треугольника.

```python
>>> from triangle import area
>>> area(4, 2)
4.0
```

#### `perimeter(a, b, c)`

Вычисляет периметр треугольника по трём сторонам.

| Параметр | Тип     | Описание                     |
|----------|---------|------------------------------|
| `a`      | `float` | первая сторона треугольника  |
| `b`      | `float` | вторая сторона треугольника  |
| `c`      | `float` | третья сторона треугольника  |

**Возвращает:** `float` — периметр треугольника.

```python
>>> from triangle import perimeter
>>> perimeter(4, 2, 3)
9
```

## Документация

Документация генерируется автоматически из docstring'ов с помощью Sphinx:

```bash
cd docs
make html
```

Готовый HTML появится в `docs/_build/html`.

## История изменений

| Дата       | Коммит    | Автор                  | Описание                                           |
|------------|-----------|------------------------|----------------------------------------------------|
| 2021-03-04 | [`8ba9aeb`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460) | smartiqa | L-03: Circle and square added |
| 2021-03-04 | [`d078c8d`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2) | smartiqa | L-03: Docs added |
| 2026-10-08 | [`c182678`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/c182678ede9617b01f3ca89e3a97b10f70be4645) | Stanislav Yaroslavtsev | feat: implement rectangle functions |
| 2026-10-08 | [`a98b6d8`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/a98b6d88929e55902c52c60223c06d4892922662) | Stanislav Yaroslavtsev | fix: rectangle perimeter calculation |
| 2026-10-08 | [`b52ad3f`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/b52ad3f64bde7db9b79d8dfe3e28b53b191a40cf) | Stanislav Yaroslavtsev | feat: implement triangle functions |
| 2026-10-08 | [`b8be56e`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/b8be56e9745a1c639c2c628a2b93d16fe211f4ed) | Stanislav Yaroslavtsev | docs: add doc strings for all figures |
| 2026-10-08 | [`57f0e27`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/57f0e27889b02a258b148e7ee0dd2bed205f492a) | Stanislav Yaroslavtsev | chore: add .gitignore |
| 2026-10-08 | [`3f62c51`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/3f62c51481bbccb51339424ed53908f4f9dae25e) | Stanislav Yaroslavtsev | chore: add .DS_Store to .gitignore |
| 2026-10-08 | [`9bf5e66`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/9bf5e66075189c41910f9c19362ae9517a55b887) | Stanislav Yaroslavtsev | docs: update docstrings to conform to google's style |
| 2026-10-08 | [`8d5a3e0`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/8d5a3e01ff7e6fd8f2ee1e355920baf78106c5ba) | Stanislav Yaroslavtsev | docs: add sphinx and set it up |
| 2026-10-08 | [`07fbe93`](https://github.com/StanislavYaroslavtsev/itmo-sdt-lab-2/commit/07fbe93eecc25afc9606965f95890e218fa6a369) | Stanislav Yaroslavtsev | docs: update readme |