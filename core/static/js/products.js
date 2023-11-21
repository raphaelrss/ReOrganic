const productCards = document.querySelectorAll('.cards-box__item')
const addCardButtons = document.querySelectorAll('.item__status')

const productsButtons = document.querySelectorAll('.products__link')

// troca o icone dos cards (icone de adicionar e icone de adicionado) dos cards dos produtos, e adiciona e retira uma classe deles de acordo com esse click no icone

addCardButtons.forEach((item, i) => {
  item.innerHTML = `<i class="fa-solid fa-plus status__icon"></i>`
  item.addEventListener('click', () => {
    productCards[i].classList.toggle('hide')

    item.innerHTML === '<i class="fa-solid fa-plus status__icon"></i>'
      ? (addCardButtons[i].innerHTML = `<i class="bx bx-check status__icon"></i>`)
      : (addCardButtons[i].innerHTML = `<i class="fa-solid fa-plus status__icon"></i>`)
  })
})

// mostra apenas os produtos adicionados ao clickar no botão 'Meus Produtos'
productsButtons[1].addEventListener('click', () => {
  productCards.forEach((item, i) => {
    if (!item.classList.contains('hide')) {
      item.style.display = 'none'
    }
  })
  productsButtons[1].classList.add('select')
  productsButtons[0].classList.remove('select')
})

// exibe todos os produtos ao clickar no botão 'produtos'
productsButtons[0].addEventListener('click', () => {
  productCards.forEach((item, i) => {
    item.style.display = 'flex'
  })
  productsButtons[0].classList.add('select')
  productsButtons[1].classList.remove('select')
})
