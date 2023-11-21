const apiUrl = 'https://api-foods-hackathon.herokuapp.com'

const ul = document.querySelector('.products__cards-box')
console.log(ul)

async function getFoods() {
  const response = await fetch(`${apiUrl}/foods`)
  const foods = await response.json()
  return foods
}

let acumulator = ''

async function showFoods() {
  const showFood = await getFoods()
  for (let i = 0; i < showFood.length; i++) {
    acumulator += ` 
    <div class="cards-box__item">
    <div class="item__status">
      <i class="fa-solid fa-plus status__icon"></i>
    </div>
    <div class="item__info">
      <img class="info__img" src="${showFood[i].image}" alt="imagem de um(a) ${showFood[i].name}" />
      <p class="info__text">${showFood[i].name}</p>
    </div>
    <a class="item__btn">Ver Detalhes</a>
  </div>
      
    `
  }
  ul.innerHTML = acumulator

  // modal da aba produtos
  const openModalButtonProducts = document.querySelector('.item__btn')
  const closeModalButtonProducts = document.querySelector('#close-modal')
  const modalProducts = document.querySelector('#modal')
  const fadeProducts = document.querySelector('#fade')

  function showAndCloseModal(modal, fade, closeModalButton, openModalButton) {
    const toggleModal = () => {
      modal.classList.toggle('hide')
      fade.classList.toggle('hide')
    }

    ;[openModalButton, closeModalButton, fade].forEach(el => {
      el.addEventListener('click', () => toggleModal())
    })
  }

  showAndCloseModal(
    modalProducts,
    fadeProducts,
    closeModalButtonProducts,
    openModalButtonProducts
  )

  const productCards = document.querySelectorAll('.cards-box__item')
  const addCardButtons = document.querySelectorAll('.item__status')

  const productsButtons = document.querySelectorAll('.products__link')

  // troca o icone dos cards (icone de adicionar e icone de adicionado) dos cards dos produtos, e adiciona e retira uma classe deles de acordo com esse click no icone

  addCardButtons.forEach((item, i) => {
    item.innerHTML = `<i class="fa-solid fa-plus status__icon"></i>`
    item.addEventListener('click', () => {
      productCards[i].classList.toggle('hide')

      item.innerHTML === '<i class="fa-solid fa-plus status__icon"></i>'
        ? (addCardButtons[
            i
          ].innerHTML = `<i class="bx bx-check status__icon"></i>`)
        : (addCardButtons[
            i
          ].innerHTML = `<i class="fa-solid fa-plus status__icon"></i>`)
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
}

showFoods()
