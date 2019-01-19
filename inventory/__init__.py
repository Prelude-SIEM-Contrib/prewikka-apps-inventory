from __future__ import absolute_import, division, print_function, unicode_literals

import pkg_resources

from prewikka import database, hookmanager, response, template, view

"""A basic inventory plugin"""

class Inventory(view.View):
    plugin_name = "Inventory"
    plugin_author = "Antoine Luong, Thomas Andrejak"
    plugin_license = "GPL"
    plugin_version = "5.0.0"
    plugin_copyright = "CSSI"
    plugin_description = "A basic inventory plugin"
    plugin_database_version = "0"
    plugin_htdocs = (("inventory", pkg_resources.resource_filename(__name__, 'htdocs')),)

    def __init__(self):
        view.View.__init__(self)
        self._db = InventoryDatabase()
        self._title = env.config.inventory.get("title", "Inventory")

        paths = [
            "alert.source.node.address.address",
            "alert.source.node.name",
            "alert.target.node.address.address",
            "alert.target.node.name",
        ]
        env.linkmanager.add_link("Search in inventory", paths, lambda x: url_for("Inventory.hosts", search=x))

    @view.route("/inventory/save", methods=["POST"])
    def save(self):
        self._db.add_host(env.request.parameters["hostname"],
                          env.request.parameters.get("address"),
                          env.request.parameters.get("os"))
        return response.PrewikkaRedirectResponse(url_for("Inventory.hosts"))

    @view.route("/inventory/hosts", menu=("Inventory", "Inventory"))
    def hosts(self):
        tmpl = template.PrewikkaTemplate(__name__, "templates/inventory.mak")
        inventory = self._db.get_hosts(env.request.parameters.get("search"))
        return tmpl.render(inventory=inventory, title=self._title)


class InventoryDatabase(database.DatabaseHelper):
    """Handle database queries related to the inventory"""

    def get_hosts(self, keyword=None):
        """Return all hosts in the inventory database matching the keyword"""
        query = "SELECT hostname, address, os FROM Prewikka_Inventory"
        if keyword:
            query += (" WHERE hostname = %(keyword)s"
                      " OR address = %(keyword)s"
                      " OR os = %(keyword)s")
        return self.query(query, keyword=keyword)

    def add_host(self, hostname, address, os):
        """Add a host to the inventory database"""
        self.query("INSERT INTO Prewikka_Inventory (hostname, address, os) "
                   "VALUES (%s, %s, %s)", hostname, address, os)
