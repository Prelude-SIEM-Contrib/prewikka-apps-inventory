<link rel="stylesheet" type="text/css" href="inventory/css/inventory.css">

<script type="text/javascript">
  $LAB.script("inventory/js/inventory.js").wait(function() { init_inventory("${ _("New host") }", "${ url_for('Inventory.new') }") });
</script>

<table class="inventory table table-striped table-bordered table-rounded table-condensed">
  <tr>
    <th>Hostname</th>
    <th>Address</th>
    <th>OS</th>
  </tr>
  % for host, address, os in inventory:
  <tr>
    <td>${ host }</td>
    <td>${ address }</td>
    <td>${ os }</td>
  </tr>
  % endfor
</table>

<a class="inventory-create btn btn-primary"><i class="fa fa-plus"></i> ${ _("Create") }</a>
