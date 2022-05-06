const result = document.querySelector('#result')
result.addEventListener("click", (e) => {
  e.preventDefault()

  
  const row = document.createElement('tr')
  row.innerHTML = `
  <td>random document</td>
  <td>55%</td>
  <td>fail</td>
  `
  const tablebody = document.querySelector('tbody')
  tablebody.appendChild(row)
})
