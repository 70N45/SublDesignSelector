import sublime, sublime_plugin

class SelectDesignCommand(sublime_plugin.WindowCommand):
    def run(self, **args):
        settings = self.load_settings();
        default_scheme      = "Packages/Color Scheme - Default/Monokai.tmTheme",
        default_theme       = "Default.sublime-theme",
        self.day_theme      = settings.get("SublDesignSelector_daytheme", default_theme)
        self.day_scheme     = settings.get("SublDesignSelector_dayscheme", default_scheme)

        self.night_theme    = settings.get("SublDesignSelector_nighttheme", default_theme)
        self.night_scheme   = settings.get("SublDesignSelector_nightscheme", default_scheme)

        if "setting" in args:
            self.apply_setting(args['setting'])

    def apply_setting(self, setting):
        settings = self.load_settings();
        if setting == "day":
            settings.set("theme", self.day_theme)
            settings.set("color_scheme", self.day_scheme)
        elif setting == "night":
            settings.set("theme", self.night_theme)
            settings.set("color_scheme", self.night_scheme)
        sublime.save_settings('Preferences.sublime-settings')

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')