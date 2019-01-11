$(document).ready(function(){

    $('#add_soldier').click(function(event){
        event.preventDefault();
        var body = $('#add_row').find('tr:last').clone();
        var id = parseInt(body.find('input[name=count]').val());
        body.find('input[name=count]').val(id+1);
        body.find('th').text(id+1);
        body.find('input[name=soldier_name_' + id + ']').attr('name', 'soldier_name_'+ (id+1));
        body.find('input[name=father_name_' + id + ']').attr('name', 'father_name_'+ (id+1));
        body.find('input[name=responsibility_' + id + ']').attr('name', 'responsibility_'+ (id+1));
        body.find('select[name=membership_type_' + id + ']').attr('name', 'membership_type_'+ (id+1));
        body.find('select[name=situation_' + id + ']').attr('name', 'situation_'+ (id+1));
        body.find('input[name=workplace_' + id + ']').attr('name', 'workplace_'+ (id+1));
        body.find('input[name=phone_' + id + ']').attr('name', 'phone_'+ (id+1));
        body.find('select[name=type_' + id + ']').attr('name', 'type_'+ (id+1));
        $('#add_row').append(body);
    });

    $('#add_row').on('click', '.remove_soldier', function (event) {
        event.preventDefault();
        var c = $('#add_row').find('tr').length - 1;
        console.log(c);
        if(c >= 1){
            $(this).parent('td').parent('tr').remove();
        }else{
            alert("شما نمیتوانید آخرین را حذف کنید");
        }
    });

});


function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {$('#blah').attr('src', e.target.result);};
        reader.readAsDataURL(input.files[0]);
    }
}