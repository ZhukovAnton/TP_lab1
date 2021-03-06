# Лабораторная работа №1 
## Команда 
Левчук Андрей, Пашкевич Сергей, Жуков Антон 
## UML ![schema](https://s4.gifyu.com/images/2020-04-19_14-13.png)
Для создания uml использовался [StarUML](http://staruml.io/). 
Со схемой можно ознакомиться [TP.mdj](https://github.com/ZhukovAnton/TP_lab1/blob/master/TP1.mdj). 
## Превью
![preview](https://s4.gifyu.com/images/ezgif.com-video-to-gif1.gif)
## Запуск
- Клонировать проект
- Запустить из корня командой python3 entrypoint.py
## Задача

- Смоделировать и реализовать программу, которая должна отображать на экране
  различные фигуры (линия, отрезок, луч, треугольник, прямоугольник, круг, ромб,
  эллипс, круг и другие необходимые фигуры).
- Координаты центра фигуры (или точку, если у фигуры нет центра), цвет линий и
  заливку выбирает пользователь.
- Классы для линии, отрезка, и луча должны наследовать друг от друга (в любом
  направлении).

## Указания

1. В базовом классе определить переменную экземпляра `theCenter` (задаёт
   координаты центра или основную точку фигуры, если у нее нет центра), а также
   основные операции:
   - `Draw` – нарисовать изображение
   - `Move` – передвинуть изображение
   - `Location` – вернуть координаты изображения (эта операция является общей
     для всех подклассов и не требует обязательного переопределения).
2. Во всех классах должны быть операции для установки и чтения значений
   переменных (`set()`, `get()`).
3. Интерфейс пользователя допускается реализовать с помощью стандартных средств
   систем программирования.
4. Точки фигуры пользователь задает щелчками мыши.
5. Модель программы (архитектура) должна быть построена таким образом, чтобы
   несложно было добавлять и удалять новые фигуры при необходимости.
