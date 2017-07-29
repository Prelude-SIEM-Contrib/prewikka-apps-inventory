from __future__ import absolute_import, division, print_function, unicode_literals

import pkg_resources

from prewikka import version, view, template, hookmanager, database, response

"""A basic inventory plugin"""

class InventoryParameters(view.Parameters):
    """A class that handles HTTP parameters for the Inventory view"""

    def register(self):
        self.optional("search", str)
        self.optional("hostname", str)
        self.optional("address", str)
        self.optional("os", str)

class Inventory(view.View):
    plugin_name = "Inventory"
    plugin_author = "Antoine Luong, Thomas Andrejak"
    plugin_license = version.__license__
    plugin_version = version.__version__
    plugin_copyright = version.__copyright__
    plugin_description = N_("A basic inventory plugin")
    plugin_database_branch = version.__branch__
    plugin_database_version = "0"
    plugin_htdocs = (("inventory", pkg_resources.resource_filename(__name__, 'htdocs')),)

    view_parameters = InventoryParameters

    def __init__(self):
        view.View.__init__(self)
        self._db = InventoryDatabase()
        self._config = env.config.inventory

    @hookmanager.register("HOOK_LINK")
    def _get_inventory_link(self, value):
        """Create a link to the inventory to be displayed in the alert view"""
        return ("host",
                "Search in inventory",
                url_for("Inventory.render", search=value),
                False)

    @view.route("/inventory", methods=['GET','POST'], menu=(N_('Inventory'), N_('Inventory')))
    def render(self):
        dataset = {}
        if "hostname" in env.request.parameters:
            self._db.add_host(env.request.parameters.get("hostname"),
                              env.request.parameters.get("address"),
                              env.request.parameters.get("os"))
            return response.PrewikkaRedirectResponse(url_for("."))

        dataset["inventory"] = self._db.get_hosts(env.request.parameters.get("search"))
        dataset["title"] = self._config.get("title", "Inventory")
        return template.PrewikkaTemplate(__name__, "templates/inventory.mak").render(**dataset)

    @view.route("/inventory/new")
    def new(self):
        return template.PrewikkaTemplate(__name__, "templates/newhost.mak").render()

class InventoryDatabase(database.DatabaseHelper):
    """Handle database queries related to the inventory"""

    def get_hosts(self, keyword=None):
        """Return all hosts in the inventory database matching the keyword"""
        query = "SELECT hostname, address, os FROM Prewikka_Inventory"
        if keyword:
            query += (" WHERE hostname = %(keyword)s"
                      " OR address = %(keyword)s"
                      " OR os = %(keyword)s" %
                      {"keyword": self.escape(keyword)})
        return self.query(query)

    def add_host(self, hostname, address, os):
        """Add a host to the inventory database"""
        self.query("INSERT INTO Prewikka_Inventory (hostname, address, os) "
                   "VALUES (%s, %s, %s)" % (self.escape(hostname),
                                            self.escape(address),
                                            self.escape(os)))
