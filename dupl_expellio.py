import sublime
import sublime_plugin
import re

def plugin_loaded():
    settings = sublime.load_settings("DuplExpellio.sublime-settings")
    if not settings.has("delimiters"):
        settings.set("delimiters", ["\n", ",", ";", " "])
    if not settings.has("threshold"):
        settings.set("threshold", 8)
    print("DuplExpellio plugin loaded and settings initialized.")

class SelectDuplicatesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("SelectDuplicatesCommand triggered.")  # Debug

        # Load settings
        settings = sublime.load_settings("DuplExpellio.sublime-settings")
        delimiters = settings.get("delimiters", ["\n", ",", ";", " "])
        threshold = settings.get("threshold", 8)

        regions = self.view.sel()
        if all(region.empty() for region in regions):
            regions = [sublime.Region(0, self.view.size())]

        for region in regions:
            text = self.view.substr(region)
            delimiter = self.detect_delimiter(text, delimiters, threshold)
            if not delimiter:
                continue
            self.select_duplicates(region, text, delimiter)

    def detect_delimiter(self, text, delimiters, threshold):
        for delimiter in delimiters:
            count = len(re.findall(re.escape(delimiter), text))
            if count >= threshold:
                return delimiter
        return None

    def select_duplicates(self, region, text, delimiter):
        items = text.split(delimiter)
        seen = set()
        duplicates = []
        for i, item in enumerate(items):
            stripped = item.strip()
            if stripped in seen:
                duplicates.append((i, stripped))
            else:
                seen.add(stripped)

        new_regions = []
        start = region.begin()
        for i, duplicate in duplicates:
            pos = start + sum(len(items[j]) + len(delimiter) for j in range(i))
            length = len(duplicate)
            new_regions.append(sublime.Region(pos, pos + length))

        self.view.sel().clear()
        for duplicate_region in new_regions:
            self.view.sel().add(duplicate_region)
        print("Highlighted {} duplicates.".format(len(new_regions)))  # Debug

class RemoveDuplicatesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("RemoveDuplicatesCommand triggered.")  # Debug

        # Load settings
        settings = sublime.load_settings("DuplExpellio.sublime-settings")
        delimiters = settings.get("delimiters", ["\n", ",", ";", " "])
        threshold = settings.get("threshold", 8)

        regions = self.view.sel()
        if all(region.empty() for region in regions):
            regions = [sublime.Region(0, self.view.size())]

        for region in regions:
            text = self.view.substr(region)
            delimiter = self.detect_delimiter(text, delimiters, threshold)
            if not delimiter:
                continue
            self.remove_duplicates(edit, region, text, delimiter)

    def detect_delimiter(self, text, delimiters, threshold):
        for delimiter in delimiters:
            count = len(re.findall(re.escape(delimiter), text))
            if count >= threshold:
                return delimiter
        return None

    def remove_duplicates(self, edit, region, text, delimiter):
        items = text.split(delimiter)
        unique_items = list(dict.fromkeys(item.strip() for item in items))
        result = delimiter.join(unique_items)
        self.view.replace(edit, region, result)
        print("Removed duplicates.")
