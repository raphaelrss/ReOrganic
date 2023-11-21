// modal da aba produtos
const openModalButtonProducts = document.querySelector('.item__btn')
const closeModalButtonProducts = document.querySelector('#close-modal')
const modalProducts = document.querySelector('#modal')
const fadeProducts = document.querySelector('#fade')

//modal da aba estoque
const openModalButtonInventory = document.querySelector('.inventory__info')
const closeModalButtonInventory = document.querySelector(
  '#close-modal-inventory'
)
const modalInventory = document.querySelector('#modalInventory')
const fadeInventory = document.querySelector('#fadeInventory')

//modal de um novo estoque
const openModalButtonNewInventory = document.querySelector('.inventory__btn')
const closeModalButtonNewInventory = document.querySelector(
  '#close-modal-newinventory'
)
const modalNewInventory = document.querySelector('#modalNewInventory')
const fadeNewInventory = document.querySelector('#fadeNewInventory')

//modal de um novo Lembrete
const openModalButtonNewNotification =
  document.querySelector('.notification__btn')
const closeModalButtonNewNotification = document.querySelector(
  '#close-modal-newnotification'
)
const modalNewNotification = document.querySelector('#modalNewNotification')
const fadeNewNotification = document.querySelector('#fadeNewNotification')

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
  modalInventory,
  fadeInventory,
  closeModalButtonInventory,
  openModalButtonInventory
)

showAndCloseModal(
  modalNewInventory,
  fadeNewInventory,
  closeModalButtonNewInventory,
  openModalButtonNewInventory
)

showAndCloseModal(
  modalNewNotification,
  fadeNewNotification,
  closeModalButtonNewNotification,
  openModalButtonNewNotification
)
