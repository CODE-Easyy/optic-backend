if ($('input.is_discount').is(':checked') == true) {
    $('input#discount').prop('disabled', false);
    console.log('checked');
} else {
    $('input#discount').val('').prop('disabled', true);
    console.log('unchecked');
}
$(".cat").change((e) => {
    var x = e.currentTarget, value = x.value
    fetchSubcats(value)
});

$('input.is_discount').change(function () {
    if ($('input.is_discount').is(':checked') == true) {
        $('input#discount').prop('disabled', false);
        console.log('checked');
    } else {
        $('input#discount').val('').prop('disabled', true);
        console.log('unchecked');
    }
});

var fetchSubcats = (cat) => {
    var subcat_select = $('.subcat')
    subcat_select.html('')
    $.ajax({
        type: 'GET',
        url: `http://127.0.0.1:8000/api/products/subcategories/?cat=${cat}`,
        data: {},
        success: function (res) {
            subcat_select.append(`<option  class="bg-info" value=0>Select....</option>`)
            res.map((row, _) => {
                subcat_select.append(`<option class="bg-info" value=${row.id}>${row.value}</option>`)
            })
        }
    })
}