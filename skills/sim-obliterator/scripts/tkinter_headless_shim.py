"""Headless tkinter shim for sim-obliterator (no GUI).

Installed by setup.py into the venv's site-packages when _tkinter
(the C extension) is missing. Provides enough stubs that
SimObliterator's eager `import tkinter` in formats/__init__.py
succeeds without a display server.

GUI features (bhav_editor) won't function. IFF parsing works fine.
"""
import sys
import types

if "_tkinter" not in sys.modules:
    # Fake the C extension
    _tk = types.ModuleType("_tkinter")
    _tk.TkVersion = 8.6
    sys.modules["_tkinter"] = _tk

    # Fake the tkinter package
    tk = types.ModuleType("tkinter")

    # Widget classes — just need to exist, never called headless
    _widgets = (
        "Tk", "Frame", "Label", "Button", "Text", "Scrollbar",
        "Toplevel", "Canvas", "Entry", "Listbox", "Menu",
        "Menubutton", "OptionMenu", "PanedWindow", "Scale",
        "Spinbox", "LabelFrame", "PhotoImage", "BitmapImage",
    )
    for name in _widgets:
        setattr(tk, name, type(name, (), {"__init__": lambda self, *a, **kw: None}))

    # Variable classes
    for name in ("StringVar", "IntVar", "BooleanVar", "DoubleVar"):
        cls = type(name, (), {
            "__init__": lambda self, *a, **kw: None,
            "get": lambda self: "",
            "set": lambda self, v: None,
        })
        setattr(tk, name, cls)

    # Constants — lowercase string stubs
    _constants = (
        "END", "LEFT", "RIGHT", "BOTH", "X", "Y", "WORD",
        "NORMAL", "DISABLED", "HORIZONTAL", "VERTICAL",
        "TOP", "BOTTOM", "CENTER",
        "NW", "NE", "SW", "SE", "N", "S", "E", "W", "NSEW",
        "RIDGE", "GROOVE", "FLAT", "SUNKEN", "RAISED", "SOLID",
        "BROWSE", "EXTENDED", "MULTIPLE", "SINGLE",
        "TRUE", "FALSE", "YES", "NO", "HIDDEN",
        "CASCADE", "CHECKBUTTON", "COMMAND", "RADIOBUTTON", "SEPARATOR",
    )
    for name in _constants:
        setattr(tk, name, name.lower())

    sys.modules["tkinter"] = tk

    # Sub-modules that SimObliterator imports
    _submodules = (
        "scrolledtext", "ttk", "messagebox", "filedialog",
        "simpledialog", "colorchooser", "font", "dnd",
    )
    _stub_classes = (
        "ScrolledText", "Treeview", "Notebook", "Combobox",
        "Progressbar", "Separator", "Sizegrip", "Style",
    )
    _stub_functions = (
        "showinfo", "showwarning", "showerror", "askquestion",
        "askokcancel", "askyesno", "askretrycancel",
        "askopenfilename", "asksaveasfilename", "askdirectory",
        "askstring", "askinteger", "askfloat", "askcolor",
        "nametofont", "families",
    )
    for sub in _submodules:
        m = types.ModuleType(f"tkinter.{sub}")
        for cls in _stub_classes:
            setattr(m, cls, type(cls, (), {"__init__": lambda self, *a, **kw: None}))
        for fn in _stub_functions:
            setattr(m, fn, lambda *a, **kw: None)
        sys.modules[f"tkinter.{sub}"] = m
