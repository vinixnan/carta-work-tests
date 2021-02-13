import pluggy

hookspec = pluggy.HookspecMarker("whalesay")
hookimpl = pluggy.HookimplMarker("whalesay")
plugin_manager = pluggy.PluginManager("whalesay")


class WhalesayPlugin(object):
    @hookspec
    def messages(self):
        """
        Return a dictionary of messages to add to the whalesay service.
        """

plugin_manager.add_hookspecs(WhalesayPlugin)