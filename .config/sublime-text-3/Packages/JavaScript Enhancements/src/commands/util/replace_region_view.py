import sublime, sublime_plugin

class JavascriptEnhancementsReplaceRegionViewCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):
    view = self.view
    view.erase(edit, sublime.Region(args.get("start"), args.get("end")))
    view.insert(edit, args.get("start"), args.get("text"))
    region = sublime.Region(args.get("start"), args.get("start")+len(args.get("text")))
    if "key" in args:
      scope = args.get("scope") if "scope" in args else ""
      scope_dot = "." + scope if scope else ""
      icon = args.get("icon") if "icon" in args else ""
      flags = args.get("flags") if "flags" in args else sublime.HIDDEN
      key = args.get("key") + scope_dot
      regions = [region] + view.get_regions(args.get("key") + scope_dot)

      view.add_regions(key, regions, scope, icon, flags)

      if "region_id" in args and args.get("region_id"):
        view.add_regions(args.get("region_id"), [region], scope, icon, flags)