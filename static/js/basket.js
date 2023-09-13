var basketUpdateBtns = document.getElementsByClassName('update-basket')

for (var i = 0; i < basketUpdateBtns.length; i++) {
    basketUpdateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
    })
}