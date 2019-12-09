// JavaScript utilizado na página carrinho.html


$("tbody").on("click", "button.remover", function() {
    let produto_id = $(this).attr('data');

    let subtotal = parseFloat( $(this).parent().attr('data') );

    let novoTotal = parseFloat( $("#total").html() ) - subtotal;

    let formData = $(this).parent().serializeArray();

    let url =  $(this).parent().attr('action')

    var data = {
            produto_id: produto_id,
            csrfmiddlewaretoken: formData[0].value
        }

    console.log(data);

    $.post(url, data, function(resposta) {
        $('#' + produto_id.toString()).remove();

        $('#total').html(novoTotal);
    })
})



$("tbody").on("click", "button.alterar", function() {
    let produto_id = $(this).parent().attr('data');

    let preco = parseFloat( $('#' + produto_id.toString() + " .preco").html() );

    let adicionar = $(this).attr('data');

    // Atualiza total do carrinho
    let novoTotal = parseFloat( $("#total").html() );

    // Atualiza subtotal do produto
    let novoSubtotal = parseFloat( $('#' + produto_id.toString() + "_subtotal").html() );

    // Atualiza quantidade do produto
    let novoQtd = parseInt( $('#' + produto_id.toString() + "_qtd").html() );

    if (adicionar == 'True'){
        novoTotal += preco;
        novoSubtotal += preco;
        novoQtd += 1;
    } else {
        novoTotal -= preco;
        novoSubtotal -= preco;
        novoQtd -= 1;
    }
    
    let formData = $(this).parent().serializeArray();

    let url =  $(this).parent().attr('action')

    var data = {
        produto_id: produto_id,
        adicionar: adicionar,
        csrfmiddlewaretoken: formData[0].value
    }

    $.post(url, data, function(resposta) {

        // Atualiza total do carrinho e subtotal e quantidade do item
        $('#total').html(novoTotal);
        $('#' + produto_id.toString() + "_subtotal").html(novoSubtotal);
        $('#' + produto_id.toString() + "_qtd").html(novoQtd);
        
    })

})