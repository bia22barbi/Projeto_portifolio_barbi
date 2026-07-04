$(document).ready(function() {
    
    // EFEITO INTERATIVO 1: Slide Toggle do card/mensagem na Home
    $('#btn-efeito').on('click', function() {
        $('#mensagem-oculta').slideToggle(400);
    });

    // EFEITO INTERATIVO 2: Animação suave de hover nos itens do menu (Modifica opacidade)
    $('.nav-links li').hover(
        function() {
            $(this).siblings().css('opacity', '0.5');
        }, 
        function() {
            $(this).siblings().css('opacity', '1');
        }
    );

    // VALIDAÇÃO DO FORMULÁRIO DE CONTATO
    $('#contactForm').on('submit', function(event) {
        let isValid = true;
        
        // Limpar erros anteriores
        $('.error-msg').hide();

        // Validar Nome
        const nome = $('#nome').val().trim();
        if (nome === "") {
            $('#error-nome').text("Por favor, preencha seu nome.").show();
            isValid = false;
        }

        // Validar Email
        const email = $('#email').val().trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            $('#error-email').text("Insira um e-mail válido.").show();
            isValid = false;
        }

        // Validar Mensagem
        const mensagem = $('#mensagem').val().trim();
        if (mensagem.length < 10) {
            $('#error-mensagem').text("A mensagem deve conter pelo menos 10 caracteres.").show();
            isValid = false;
        }

        // Se não for válido, impede o envio do formulário
        if (!isValid) {
            event.preventDefault();
        } else {
            alert("Formulário validado e enviado com sucesso!");
        }
    });
});