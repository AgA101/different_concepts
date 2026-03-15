from mimetypes import init
from tkinter import*
from turtle import title

from tkinter import Tk, Label




 

class GridState:
    def __init__(self) -> None:
        self.row = 0
        self.column = 0

class WidgetOwner:
    _root = None
    _state = GridState()

    @staticmethod
    def build():
        WidgetOwner.get_root().mainloop() 

    @classmethod
    def get_root(cls):
        if WidgetOwner._root is None:
            WidgetOwner._root = Tk()
            WidgetOwner._root.minsize(width=400, height=200)
        return WidgetOwner._root

    @property
    def row(self):
        return self.state.row

    @row.setter
    def row(self, value):
        self.state.row = value

    @property
    def column(self):
        return self.state.column

    @column.setter
    def column(self, value):
        self.state.column = value

    def __init__(self):
        self.root = WidgetOwner.get_root()
        self.state = WidgetOwner._state


class Render(WidgetOwner):
    def __init__(self):
        self.root = self.get_root()
        super().__init__()

    def vertical(self, widgets):
        for widget in widgets:
            widget.render(1)

    def horizontal(self, widgets):
        for widget in widgets:
            widget.render(0)
        
        self.row += 1
        self.column = 0
        

class TotalRow(WidgetOwner):
    def __init__(self, label: str, value: int):
        super().__init__()
        self.label = Label(self.root, text=label)
        self.value = Label(self.root, text=str(value))


    def render(self, direction: int):
        self.label.grid(row=self.row, column=self.column)
        self.value.grid(row=self.row, column=self.column+1)

        if direction:
            self.row += 1
        else:
            self.column += 1

    def set_value(self, value: int):
        self.value.config(text=str(value))


class SubTotalRow(TotalRow):
    def __init__(self, label: str, value: int):
        super().__init__(label, value)


class Dish(WidgetOwner):
    def __init__(self, name: str, price: int):
        super().__init__()
        # числовая цена блюда для вычислений
        self.unit_price = price
        self.checked = IntVar(value=0)
        self.name = Checkbutton(self.root, text=name, variable=self.checked, onvalue=1, offvalue=0)
        # отдельный виджет только для отображения цены
        self.price = Label(self.root, text=str(price))
        self.qty = IntVar(value=0)
        self.count = Spinbox(self.root, from_=0, to=99, width=10, increment=1, textvariable=self.qty)
       

    def render(self, direction: int):
        self.name.grid(row=self.row, column=self.column)
        self.price.grid(row=self.row, column=self.column+1)
        self.count.grid(row=self.row, column=self.column+2)
        
        if direction:
            self.row += 1
        else:
            self.column += 1

    def get_total(self) -> int:
        if self.checked.get():
            return self.unit_price * self.qty.get()
        return 0

class Section(WidgetOwner):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.title = Label(self.root, text=title)
        self.title_text = title
        self.dishes = []
        self.subtotal = SubTotalRow('Итого: ', 0)

    def render(self, direction: int):
        self.title.grid(row=self.row, column=self.column)
        if direction:
            self.row += 1
        else:
            self.column += 1

        for i in self.dishes:
            i.render(1)
        self.subtotal.render(1)
        if direction:
            self.row += 1
        else:
            self.column += 1

    
    def add_dish(self, *items):
        """Добавить одно или несколько блюд. Каждый аргумент — пара (название, цена)."""
        if len(items) == 2 and not isinstance(items[0], (tuple, list)):
            self.dishes.append(Dish(items[0], items[1]))
        else:
            for name, price in items:
                self.dishes.append(Dish(name, price))
        return self


    def update_subtotal(self) -> int:
        total = sum(d.get_total() for d in self.dishes)
        self.subtotal.set_value(total)
        return total

class Title(WidgetOwner):
    def __init__(self, label: str) -> None:
        super().__init__()
        self.label = Label(self.root, text=label)
        
    def render(self, direction: int):
        self.label.grid(row=self.row, column=self.column)
        if direction:
            self.row += 1
        else:
            self.column += 1

class Discount(WidgetOwner):
    def __init__(self, label: str, i: int, var: IntVar) -> None:
        super().__init__()
        self.var = var
        self.label = Radiobutton(self.root, text=f'{label}%', value=i+1, variable=self.var, padx=15, pady=10)
        
    def render(self, direction: int):
        self.label.grid(row=self.row, column=self.column)
        if direction:
            self.row += 1
        else:
            self.column += 1

class Discount_title(WidgetOwner):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Скидка:')
        
    def render(self, direction: int):
        self.label.grid(row=self.row, column=self.column)
        if direction:
            self.row += 1
        else:
            self.column += 1
   


class RestaurantMenu:
    def __init__(self):
        self.column = list[Title]()
        self.section = list[Section]()
        self.discount = list[Discount]()
        self.discount_title = Discount_title()
        self.discount_var = IntVar(value=0)
        self.total = TotalRow('Общий счет:', 0)
        self.render = Render()

    def build(self):
        self.render.vertical((self.total,))
        return WidgetOwner.build()

    def set_column(self, *categories: str):
        for category in categories: 
            self.column.append(Title(category))

    def get_columns(self):
        return self.column

    def set_section(self, *titles: str):
        for title in titles:
            self.section.append(Section(title))

    def get_sections(self) -> Section:
        return self.section

    def get_section(self, name_or_index) -> Section:
        """Получить раздел по имени ('Супы') или по номеру (0, 1, 2). Можно сразу вызывать: menu.get_section(0).add_dish(...)"""
        if isinstance(name_or_index, int):
            return self.section[name_or_index]
        for s in self.section:
            if s.title_text == name_or_index:
                return s
        raise KeyError(f'Раздел "{name_or_index}" не найден')

    def set_discount(self, *discounts: int):
        for i, pct in enumerate(discounts):
            self.discount.append(Discount(str(pct), i, self.discount_var))

    def get_discount(self):
        return self.discount_title , *self.discount

    def recalc(self):
        total = 0
        for section in self.section:
            total += section.update_subtotal()
        discount_factor = {0: 1.0, 1: 0.95, 2: 0.90, 3: 0.85}
        total = int(total * discount_factor.get(self.discount_var.get(), 1.0))
        self.total.set_value(total)
    

menu = RestaurantMenu()
menu.set_column('Меню', 'Цена', 'Количество')
NAMES_MENU_SECTIONS = ['Супы', 'Горячие блюда', 'Десерты']
menu.set_section(*NAMES_MENU_SECTIONS)

CONFIG_MENU_SECTION_1 = [
    ('Борщ', 300),
    ('Щи', 400), 
]

CONFIG_MENU_SECTION_2 = [
    ('Шашлык', 200),
    ('Стейк', 300),
    ('Лосось', 250) 
]

CONFIG_MENU_SECTION_3 = [
    ('Наполеон', 100),
    ('Тирамису', 150), 
]

CONFIG_MENU = [ CONFIG_MENU_SECTION_1, CONFIG_MENU_SECTION_2, CONFIG_MENU_SECTION_3 ]
for i, section in enumerate(CONFIG_MENU):
    menu.get_section(i).add_dish(*section)

DISCOUNT_OPTIONS_CONFIG = ['5', '10', '15']
menu.set_discount(*DISCOUNT_OPTIONS_CONFIG)


menu.render.horizontal(menu.get_columns())
menu.render.vertical(menu.get_sections())
menu.render.horizontal(menu.get_discount())

WidgetOwner.get_root().bind('<Return>', lambda e: menu.recalc())
menu.build()

