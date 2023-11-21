const inventoryCards = document.querySelectorAll('.inventory__item')
const addIconMoney = document.querySelectorAll('.icon__money')

const inventoryButtons = document.querySelectorAll('.inventory__link')

console.log(inventoryButtons)
// troca o icone dos cards (icone de adicionar e icone de adicionado) dos cards dos produtos, e adiciona e retira uma classe deles de acordo com esse click no icone
addIconMoney.forEach((item, i) => {
  item.addEventListener('click', () => {
    inventoryCards[i].classList.toggle('hide')
  })
})

// mostra apenas os produtos adicionados ao clickar no botão 'Meus Produtos'
inventoryButtons[1].addEventListener('click', () => {
  inventoryCards.forEach((item, i) => {
    if (!item.classList.contains('hide')) {
      item.style.display = 'none'
    }
  })
  inventoryButtons[1].classList.add('select')
  inventoryButtons[0].classList.remove('select')
})

// exibe todos os produtos ao clickar no botão 'produtos'
inventoryButtons[0].addEventListener('click', () => {
  inventoryCards.forEach((item, i) => {
    item.style.display = 'flex'
  })
  inventoryButtons[0].classList.add('select')
  inventoryButtons[1].classList.remove('select')
})
