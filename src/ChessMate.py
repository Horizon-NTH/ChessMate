import json
import hgui

class ChessMate:
    def __init__(self):
        hgui.init()
        with open("assets/settings.json", 'r') as file:
            self._settings = json.load(file)
        self._monitor: hgui.Monitor = hgui.Monitor.get_primary_monitor()
        self._icon: hgui.Image = hgui.Image(self._settings["logo"])
        self._window: hgui.Window = hgui.Window(windowName="ChessMate", size=self._monitor.size, position=hgui.point(0),
                                                icon=self._icon, options={hgui.options.MAXIMIZED: True})
        self._font: hgui.Font = hgui.Font(self._settings["font"])
        self._title: hgui.Label = None
        self._logo: hgui.Sprite = None
        self._menu: str = "main"
        self._buttons: dict[str, hgui.Button] = {
            "local": None,
            "ai": None,
            "option": None,
            "theme": None,
            "exit": None
        }
        hgui.TagManager.create_tag("main")
        hgui.TagManager.create_tag("all")
        hgui.TagManager.create_tag("option")
        hgui.TagManager.create_tag("not_ready")
        self.main_menu()
        self.option_menu()
        self.update()
        self.set_theme(self._settings["theme"])
        self._window.set_size_callback(function=self.update)

    def start(self):
        self.render("main")
        hgui.loop()

    def render(self, menu: str):
        if menu == "main":
            hgui.Renderer.draw(["all", "main", "not_ready"])
            hgui.Renderer.draw(["HGUI_TAG_MAIN"], hgui.effects.BLURRED)
            hgui.active(["all", "main"])
        elif menu == "option":
            hgui.Renderer.draw(["all", "option"])
            hgui.Renderer.draw([self._menu, "not_ready"] if self._menu == "main" else [self._menu], hgui.effects.BLURRED)
            hgui.active(["all", "option"])

    def main_menu(self):
        hgui.TagManager.set_current_tag("main")
        self._logo = hgui.Sprite(texture=self._icon, size=hgui.size(hgui.em(25)).set_reference(hgui.reference.HEIGHT),
                                 position=hgui.point(hgui.em(40), hgui.em(30)) - self._icon.size / 2)
        self._title = hgui.Label("ChessMate", position=hgui.point(0), font=self._font)
        self._buttons["local"] = hgui.Button(function=None, size=hgui.size(hgui.em(20), hgui.em(10)),
                                             position=hgui.point(hgui.em(40), hgui.em(45)), text="Two players",
                                             font=self._font)
        hgui.TagManager.set_current_tag("not_ready")
        self._buttons["ai"] = hgui.Button(function=None, size=hgui.size(hgui.em(20), hgui.em(10)),
                                          position=hgui.point(hgui.em(40), hgui.em(60)), text="Play against AI",
                                          font=self._font)

        def switch_option():
            if "option" in hgui.kernel.Widget.get_active_tag():
                self.render(self._menu)
            else:
                self.render("option")

        hgui.TagManager.set_current_tag("all")
        self._buttons["option"] = hgui.Button(function=switch_option,
                                              size=hgui.size(hgui.em(10)).set_reference(hgui.reference.HEIGHT),
                                              position=self.grid(1, 1),
                                              texture=hgui.Texture(hgui.Image(self._settings["icon"]["option"])),
                                              blurrOnHover=False)
        hgui.KeyBoardManager.bind((hgui.keys.ESCAPE, hgui.actions.PRESS), function=switch_option)

    def option_menu(self):
        def switch_theme():
            self._settings["theme"] = "light" if self._settings["theme"] == "dark" else "dark"
            with open("assets/settings.json", 'w') as file:
                json.dump(self._settings, file, indent=4)
            with open("assets/settings.json", 'r') as file:
                self._settings = json.load(file)

            self.set_theme(self._settings["theme"])

        hgui.TagManager.set_current_tag("option")
        self._buttons["theme"] = hgui.Button(function=switch_theme,
                                             size=hgui.size(hgui.em(10)).set_reference(hgui.reference.HEIGHT),
                                             position=self.grid(2, 1),
                                             blurrOnHover=False)
        self._buttons["exit"] = hgui.Button(function=hgui.end,
                                            size=hgui.size(hgui.em(10)).set_reference(hgui.reference.HEIGHT),
                                            position=self.grid(3, 1),
                                            blurrOnHover=False,
                                            texture=hgui.Texture(hgui.Image(self._settings["icon"]["exit"])))

    def set_theme(self, theme: str):
        hgui.Renderer.set_background_color(hgui.color(self._settings["colors"][theme]["background"]))
        self._title.color = hgui.color(self._settings["colors"][theme]["title"])
        self._buttons["local"].color = hgui.color(self._settings["colors"][theme]["button"])
        self._buttons["local"].text.color = hgui.color(self._settings["colors"][theme]["text"])
        self._buttons["ai"].color = hgui.color(self._settings["colors"][theme]["disable"])
        self._buttons["ai"].text.color = hgui.color(self._settings["colors"][theme]["text"])
        self._buttons["option"].color = (
            hgui.color(self._settings["colors"][theme]["option"]),
                    hgui.color(self._settings["colors"][theme]["focus"]),
                    hgui.color(self._settings["colors"][theme]["focus"]))
        self._buttons["theme"].texture = hgui.Texture(hgui.Image(self._settings["icon"][theme]))
        self._buttons["theme"].color = (
            hgui.color(self._settings["colors"][theme]["option"]),
                    hgui.color(self._settings["colors"][theme]["focus"]),
                    hgui.color(self._settings["colors"][theme]["focus"]))
        self._buttons["exit"].color = (
            hgui.color(self._settings["colors"][theme]["option"]),
                    hgui.color(self._settings["colors"][theme]["focus"]),
                    hgui.color(self._settings["colors"][theme]["focus"]))

    def update(self):
        if self._title:
            self._title.height = round(hgui.em(10).get_height_value())
            self._title.position = hgui.point(self._logo.position.x + self._logo.size.width,
                                              self._logo.position.y +
                                              self._logo.size.height / 2 - self._title.size.height / 2)

    @staticmethod
    def grid(row: int, column: int):
        BUTTON_SIZE: hgui.point = hgui.point(hgui.em(10)).set_reference(hgui.reference.HEIGHT)
        GAP: hgui.point = hgui.point(hgui.em(1)).set_reference(hgui.reference.HEIGHT)
        pos: hgui.point = GAP
        pos.em_x += (column - 1) * (BUTTON_SIZE + GAP).em_x
        pos.em_y += (row - 1) * (BUTTON_SIZE + GAP).em_y
        pos.update()
        return pos