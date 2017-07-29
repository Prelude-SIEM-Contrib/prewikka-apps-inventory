<div class="container">
  <div class="widget" role="dialog" aria-labelledby="dialogLabel" aria-hidden="true" data-widget-options="modal-lg">

    <div class="modal-header">
      <button type="button" class="close" data-dismiss="modal">&times;</button>
      <h4 class="modal-title">${ _("New host") }</h4>
    </div>

    <form method="post" action="${ url_for('Inventory.render') }" class="ooo">

    <div class="modal-body" id="inventory-dialog">
        % for label, name in ("Hostname", "hostname"), ("Address", "address"), ("OS", "os"):
        <div class="form-group">
          <label>${ label }:</label>
          <input type="text" class="form-control" name="${ name }"/>
        </div>
        % endfor
    </div>

    <div class="modal-footer">
        <button class="btn btn-primary" type="submit"><i class="fa fa-save"></i> ${ _("Create") }</button>
    </div>

    </form>

  </div>
</div>
