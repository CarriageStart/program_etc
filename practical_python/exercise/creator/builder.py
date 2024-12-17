
import abc
import os
import re
import sys
from html import escape


def main():
    htmlFileName = "login.html"
    htmlForm = create_login_form(HTMLFormBuilder())
    with open(htmlFileName, "w", encoding="utf-8") as file:
        file.write(htmlForm)

    tkFileName = "login.py"


def create_login_form(builder):

    builder.add_title("Login")
    builder.add_label("Username", 0, 0, target="username")
    builder.add_entry("username", 0, 1)
    builder.add_label("Password", 1, 0, target="password")
    builder.add_entry("password", 1, 1)
    builder.add_button("Login", 2, 0)
    builder.add_button("Cancel", 2, 1)
    return builder.form()


class AbstractFormBuilder(metaclass=abc.ABCMeta):   # Make class Abstract : No Instance
    
    @abc.abstractmethod # Enforce the method implementation
    def add_title(self, title):
        self.title = title

    @abc.abstractmethod
    def add_label(self, label):
        pass

    @abc.abstractmethod
    def add_entry(self, entry):
        pass

    @abc.abstractmethod
    def add_button(self, button):
        pass

    @abc.abstractmethod
    def form(self):
        pass


class HTMLFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.title = "HTMLFormBuilder"
        self.items = {}


    def add_title(self, title):
        super().add_title(escape(title))

    def add_label(self, text, row, column, **kwargs):
        self.items[(row, columns)] =
            '<td><label for="{}">{}:</label></td>'.format(kwargs["target"], excape(text))
        

    def add_entry(self, variable, row, column, **kwargs):
        self.items[(row, columns)] = 
            '<td><input name="{}" type="{}" /></td>'.format(variable, kwargs.get("kind", "text"))
        
    def add_button(self, text, row, column, **kwargs):
        self.items[(row, columns)] = 
            '<td><input type="submit" value="{}" /></td>'.format(escape(text))

    def form(self):
        html = [
            "<!doctype html>\n<html><head><title>{}</title></head><body>".format(self.title),
            '<form><table border="0">'
        ]
        thisRow = None
        for key, value in sorted(self.items.items()):
            row, column = key
            if thisRow = None:
                html.append("  <tr>")
            elif thisRow = != row:
                html.append("  </tr>\n  <tr>")
            thisRow = row
            html.append("  </tr>\n</table></form></body></html>")
        return "\n".join(html)

class TKFormBuilder(AbstractFormBuilder):
    TEMPLATE = """#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk

class {name}Form(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.withdraw()     # hide until ready to show
        self.title("{title}")
        {statements}
        self.bind("<Escape>", lambda *args: self.destroy())
        self.deiconify()    # show when widgets are created and laid out
        if self.winfo_viewable():
            self.transient(master)
        self.wait_visibility()
        self.grab_set()
        self.wait_window(self)

if __name__ == "__main__":
    application = tk.Tk()
    window = {name}Form(application)
    application.protocol("WM_DELETE_WINDOW", application.quit)
    application.mainloop()
"""
    def __init__(self):
        self.title = "TKFormBuilder"
        self.statements = []

    def add_title(self, title):
        super().add_title(title)

    def add_label(self, text, row, col, **kwargs):
        name = self._canonicalize(text)
        create = """self.{}Label = ttk.Label(self, text="{}:")""".format(name, text)
        layout = """self.{}Entry.grid(row={}, column={}, sticky=(tk.W, tk.E),\
                pady="0.75m")""".format(name,row,column)
        self.statements.extend((create,layout))

    def add_entry(self, variable, row, column, **kwargs):
        name = self._canonicalize(variable)
        extra = "" if kwargs.get("kind") != "password" else ', show="*"'
        create = "self.{}Entry = ttk.Entry(self{})".format(name, extra)
        layout = """self.{}Entry.grid(row={}, column={}, sticky=(\
tk.W, tk.E), padx="0.75m", pady="0.75m")""".format(name, row, column)
        self.statements.extend((create, layout))


    def add_button(self, text, row, column, **kwargs):
        name = self._canonicalize(text)
        create = ("""self.{}Button = ttk.Button(self, text="{}")"""
                .format(name, text))
        layout = """self.{}Button.grid(row={}, column={}, padx="0.75m", \
pady="0.75m")""".format(name, row, column)
        self.statements.extend((create, layout))

    def form(self):
        return TKFormBuilder.TEMPLATE.format(
            title=self.title,
            name=self._canonicalize(self.title, Flase),
            statements="\n      ".join(self.statements)
        )

    def _canonicalize(self, text, startLower=True):
        text = re.sub(r"\W+", "", text)
        if text[0].isdigit():
            return "_" + text
        return text if not startLower else text[0].lower() + text[1:]
        
if __name__=="__main__":
    main()

