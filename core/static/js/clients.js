const clientsButtons = document.querySelectorAll('.client__link')
const clientsCards = document.querySelector('.box-client__item')
const priceContainer = document.querySelector('.client__price-container')

console.log(clientsButtons)

clientsButtons[0].addEventListener('click', () => {
  clientsCards.style.display = 'grid'
  priceContainer.style.display = 'none'

  clientsButtons[0].classList.add('select')
  clientsButtons[1].classList.remove('select')
})

clientsButtons[1].addEventListener('click', () => {
  clientsCards.style.display = 'none'
  priceContainer.style.display = 'grid'

  clientsButtons[1].classList.add('select')
  clientsButtons[0].classList.remove('select')
})
