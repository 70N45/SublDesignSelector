import sublime, sublime_plugin

class SelectDesignCommand(sublime_plugin.WindowCommand):
	def run(self, **args):
		settings = self.load_settings();
		day_theme: settings.get("SublDesignSelector.day.theme", "Default")
		day_scheme: settings.get("SublDesignSelector.day.color_scheme", "Breakers")

		night_theme: settings.get("SublDesignSelector.night.theme", "Default")
		night_scheme: settings.get("SublDesignSelector.night.color_scheme", "Breakers")

	if "setting" in args:
		self.apply_setting(args['setting'])

	def apply_setting(setting):
		settings = self.load_settings();
		if setting == "day":
			settings.set("theme", day_theme)
			settings.set("color_scheme")
		elif setting == "night":
			settings.set("theme", night_theme)
			settings.set("color_scheme", night_scheme)
		sublime.save_settings('Preferences.settings')

    def load_settings():
        return sublime.load_settings('Preferences.settings')