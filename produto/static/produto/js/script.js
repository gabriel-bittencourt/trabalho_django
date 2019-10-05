/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(function () {
   $('[data-toggle="tooltip"]').tooltip();

   $('[data-toggle="popover"]').popover();

   // 1. Obter uma referência para a div card1 e executar o método 
   //    slideUp() na velocidade de 1000 milissegundos.

   $("#btn1").click(function () {
      
   })

   // 1. Obter uma referência para a div card1 e executar o método 
   //    slideDown() na velocidade de 1000 milissegundos.

   $("#btn2").click(function () {
      
   })

   // 1. Obter uma referência para a div card1 e executar o método 
   //    slideToggle() na velocidade slow.

   $("#btn3").click(function () {
      
   })

   // 1. Efetuar uma animação sobre a div accordion, estabelecendo
   //    a altura em 150px, a largura em 70%, a opacidade em  0.4, 
   //    a margem a esquerda (marginLeft) deve  ser  aumentada  em 
   //    80px, o tamanho da letra (fontSize) deve  ser  fixado  em
   //    11pt e a largura da borda (borderWidth) deve  ser  fixada 
   //    em 5px. A animação deve ocorrer em 1500 milissegundos.

   $("#btn4").click(function () {
      
   })

   // 1. Efetuar uma animação sobre a div accordion, estabelecendo
   //    a altura em 150px, a largura em 70%, a opacidade em  0.4, 
   //    a margem a esquerda (marginLeft) deve  ser  aumentada  em 
   //    80px, o tamanho da letra (fontSize)deve  ser  fixado   em 
   //    11pt e a largura da borda (borderWidth) deve  ser  fixada 
   //    em 5px. A animação deve ocorrer em 1500 milissegundos.

   $("#btn5").click(function () {

   })

   // 1. Enviar requisição ajax para arquivo.txt, e  substituir  o 
   // label do botão btn6 pelo conteúdo desse arquivo.

   $("#btn6").click(function () {

   })

   function recuperarInformacao() {
   
       // A função ajax do jQuery recebe como parâmetro um  objeto
       // com um conjunto de propriedades:
       // - o url desejado (no nosso caso, apenas arquivo.txt pois 
       //   este arquivo encontra-se na mesma  pasta  do  servidor 
       //   onde se encontra a página index.html),
       // - o tipo do método utilizado para  enviar  a  requisição 
       //   http, o tipo de informação que  esperamos  receber  de 
       //   volta.  No  nosso  caso,  'text'  que  é o conteúdo do 
       //   arquivo arquivo.txt,
       // - o nome  da  função  callback  que  deve  ser executada 
       //   quando a requisição é bem sucedida (sucesso),
       // - o nome  da  função  callback  que  deve  ser executada 
       //   quando a requisição falha (erro)
       // - e a função que  é  executada  quando  a  requisição  é 
       //   completada (com sucesso ou não). Essa  função  anônima 
       //   recebe dois parâmetros: xhr e status. Nenhum dos  dois 
       //   serão utilizados.
   
       //$.ajax({
       //    // O URL para a requisição
       //    url:      ,
   
       //    // o tipo da requisição
       //    type:     ,
   
       //    // o tipo de dado que esperamos receber de volta
       //    dataType:    ,
   
       //    // a funcão a ser chamada no caso de sucesso
       //    success:     , 
   
       //    // a funcão a ser chamada no caso de falha
       //    error:       ,
   
       //    // o  código  a  ser  executado   independentemente  de
       //    // sucesso ou falha. Essa função é executada sempre!
       //    complete: function( xhr, status ) {
       //        console.log("A requisição foi concluída!");
       //    }
       //});
   }
   // No caso de sucesso nós localizamos o botão cujo id é btn6  e 
   // colocamos  o  resultado  da  busca  como  label  do botão. O 
   // resultado recebido por essa função é o  conteúdo do  arquivo 
   // arquivo.txt que é recuperado através da requisição ajax.
   
   function sucesso(resultado) {
       $("#btn6").html(resultado);
   }
   
   function erro(xhr, status, strErr) {
       console.log("Ocorreu um erro!");
       console.log("xhr = ", xhr);
       console.log("status = ", status);
       console.log("strErr = ", strErr);
   }
});
