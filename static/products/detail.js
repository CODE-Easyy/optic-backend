$(".cat").change((e) => {
    var x = e.currentTarget, value = x.value
    fetchSubcats(value)
});


var fetchSubcats = (cat) => {
    var subcat_select = $('.subcat')
    subcat_select.html('')
    $.ajax({
        type: 'GET',
        url: `http://127.0.0.1:8000/api/products/subcategories/?cat=${cat}`,
        data: {},
        success: function(res) {
            subcat_select.append(`<option  class="bg-info" value=0>Select....</option>`)
            res.map((row, _) => {
                subcat_select.append(`<option class="bg-info" value=${row.id}>${row.value}</option>`)
            })
        }
    })
}