let show = false

const linkItems = document.querySelectorAll('.sidebar li a')
const sectionsDashboard = document.querySelectorAll('.section-Dashboard')

const body = document.querySelector('body')
const sidebar = body.querySelector('aside')
const toggle = body.querySelector('.toggle')
const modeSwitch = body.querySelector('.toggle-switch')
const modeText = body.querySelector('.mode-text')
const logo = document.querySelector('.header__logo-box')

toggle.addEventListener('click', () => {
  sidebar.classList.toggle('close', show)
  setTimeout(() => {
    show
      ? (logo.innerHTML = `          
          <h2 class="image logo logo--dashboard ">
            R<span class="logo__span--dashboard">O</span>
          </h2>`)
      : (logo.innerHTML = `   
          <h2 class="image logo logo--dashboard ">
            Re<span class="logo__span--dashboard">Organic</span>
          </h2>`)
    show = !show
  }, 100)
})

modeSwitch.addEventListener('click', () => {
  body.classList.toggle('dark')

  if (body.classList.contains('dark')) {
    modeText.innerText = 'Modo Escuro'
  } else {
    modeText.innerText = 'Modo Claro'
  }
})

// active icon sidebar
linkItems.forEach((linkItem, index) => {
  linkItem.addEventListener('click', () => {
    document.querySelector('.active').classList.remove('active')
    linkItem.classList.add('active')

    showSectionDashboard(index)
  })
})

//evibe a seção correspondente à aba clickada
function showSectionDashboard(index) {
  sectionsDashboard.forEach((section, i) => {
    sectionsDashboard[i].style.display = 'none'
  })

  sectionsDashboard[index].style.display = 'block'
}
