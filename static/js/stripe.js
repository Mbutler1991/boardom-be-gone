console.log('test');

document.addEventListener('DOMContentLoaded', function() {
    var stripe = Stripe('{{ stripe_public_key }}');
    var elements = stripe.elements();
    var cardElement = elements.create('card');
    
    cardElement.mount('#card-element');

    var form = document.getElementById('payment-form');
    var submitButton = document.getElementById('submit-button');
    var errorElement = document.getElementById('card-errors');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        stripe.createPaymentMethod({
            type: 'card',
            card: cardElement,
        }).then(function(result) {
            if (result.error) {
                errorElement.textContent = result.error.message;
            } else {
                var paymentMethodInput = document.createElement('input');
                paymentMethodInput.setAttribute('type', 'hidden');
                paymentMethodInput.setAttribute('name', 'payment_method_id');
                paymentMethodInput.setAttribute('value', result.paymentMethod.id);
                form.appendChild(paymentMethodInput);
                form.submit();
            }
        });
    });
});