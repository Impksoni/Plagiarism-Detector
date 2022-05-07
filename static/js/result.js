const test = `[
  {
    "documentName": "A comparative study of ANN.",
    "palgarizedPercent": 40
  }, {
    "documentName": "A comparative study of ANN3.",
    "palgarizedPercent": 55
  },  {
    "documentName": "A comparative study of ANN4.",
    "palgarizedPercent": 25
  }, {
    "documentName": "A comparative study of ANN6.",
    "palgarizedPercent": 10
  },  {
    "documentName": "A comparative study of ANN7.",
    "palgarizedPercent": 20
  }
]`

console.log('hello')

const result = document.querySelector('.uploadBtn')
const object = JSON.parse(test)
for(var i = 0; i < object.length; i++) {
  if (object[i].palgarizedPercent < 40){
    var concusion = 'pass'
  } else {
    concusion = 'fail'
  }
  const row = document.createElement('tr')
  row.innerHTML = `
  <td>` + object[i].documentName +`</td>
  <td>`+ object[i].palgarizedPercent + `</td>
  <td>` + concusion + `</td>
  `
  const tablebody = document.querySelector('tbody')
  tablebody.appendChild(row)
}