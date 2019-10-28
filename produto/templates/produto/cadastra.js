$("#botao").click(function() {
    $("#form").append('{{ form.produto_id }}')
    // $("#form").submit()
})

$('#id_data_cadastro').datepicker({
   {# minDate: new Date({{ ano_campo_minDate }}, {{ mes_campo_minDate }} - 1, {{ dia_campo_minDate }}), #}
   {# maxDate: new Date({{ ano_campo_maxDate }}, {{ mes_campo_maxDate }} - 1, {{ dia_campo_maxDate }}), #}
   dateFormat: 'dd/mm/yy',
   dayNames: ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
   dayNamesMin: ['D','S','T','Q','Q','S','S','D'],
   dayNamesShort: ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb','Dom'],
   monthNames: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
   monthNamesShort: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'],
   nextText: 'Próximo',
   prevText: 'Anterior',
   showOn: 'focus',
});

$('#id_data_cadastro').mask('00/00/0000');