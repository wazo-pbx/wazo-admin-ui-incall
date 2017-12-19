$(document).ready(function () {
  $('.incall-context').on("change", function (e) {
    add_available_extensions();
  });
  add_available_extensions();
  $('#caller_id_mode').on('change', function (e) {
    toggle_callerid_mode.call(this)
  })
  toggle_callerid_mode.call($('#caller_id_mode'))
});


function toggle_callerid_mode() {
  if ($(this).val() == '') {
    $('#caller_id_name').closest('div.form-group').hide()
  } else {
    $('#caller_id_name').closest('div.form-group').show()
  }
}


function add_available_extensions() {
  let extension_select = $(".incall-exten")
  let context_select = $(".incall-context")
  let ajax_url = $(extension_select).attr('data-available_extension_href')
  if (!ajax_url) {
    return;
  }

  extension_select.select2({
    theme: 'bootstrap',
    placeholder: 'Select...',
    ajax: {
      url: ajax_url,
      data: function (params) {
        return {
          term: params.term,
          context: context_select.val()
        }
      }
    }
  });
}