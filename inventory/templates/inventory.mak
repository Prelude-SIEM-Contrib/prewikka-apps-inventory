<link rel="stylesheet" type="text/css" href="inventory/css/inventory.css">

<script type="text/javascript">
  $LAB.script("inventory/js/inventory.js");
</script>

<table class="inventory table table-striped table-bordered table-rounded table-condensed">
  <tr>
    <th>Hostname</th>
    <th>Address</th>
    <th>OS</th>
  </tr>
  % for host, address, os in inventory:
  <tr>
    <td>${host}</td>
    <td>${address}</td>
    <td>${os}</td>
  </tr>
  % endfor
</table>

<button class="create btn btn-primary"><i class="fa fa-plus"></i> Create</button>

<div id="inventory-dialog" class="modal fade" role="dialog" data-backdrop="false">
  <form action="${url_for('Inventory.save')}" method="post">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title">${title}</h4>
        </div>
        <div class="modal-body">
        % for label, name in ("Hostname", "hostname"), ("Address", "address"), ("OS", "os"):
          <div class="form-group">
            <label>${label}:</label>
            <input type="text" class="form-control" name="${name}"/>
          </div>
        % endfor
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-primary">OK</button>
        </div>
      </div>
    </div>
  </form>
</div>
