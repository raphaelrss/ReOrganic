const faqsItems = document.querySelectorAll('.faq__question-box')

console.log(faqsItems)
faqsItems.forEach(item => {
  item.addEventListener('click', () => {
    item.classList.toggle('active')
  })
})
