const computerChoiceDisplay = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('user-choice')
const resultDisplay = document.getElementById('result')
const possibleChoices = document.querySelectorAll('button')
let userChoice
// const options = ['rock', 'paper', 'scissors']
possibleChoices.forEach(possibleChoice => possibleChoice
  .addEventListener('click', (event) => {
    userChoice = event.target.id
    userChoiceDisplay.innerHTML = userChoice
    generateComputerChoice()

  }))

function generateComputerChoice() {
  computerChoice = possibleChoices[Math.floor((Math.random() * possibleChoices.length))].id
  computerChoiceDisplay.innerHTML = computerChoice
}
E
// function generatecomputerchoice() {
//   const randomnumber = math.floor(math.random() * possiblechoices.length)
// 
//   if (randomnumber === 1) {
//     computerchoice = 'rock'
//   }
//   if (randomNumber === 2) {
//     computerChoice = 'paper'
//   }
//   if (randomNumber === 3) {
//     computerChoice = 'scissors'
//   }
// 
//   computerChoiceDisplay.innerHTML = computerChoice
// }

function getResult() {
  if (computerChoice === userChoice) {
    result = 'its a draw'
  }
  if (computerChoice === 'rock' && userChoice === 'paper') {
    result = 'you win'
  }
  if (computerChoice === 'rock' && userChoice === 'scissors') {
    result = 'you lost'
  }
  if (computerChoice === 'paper' && userChoice === 'scissors') {
    result = 'you win'
  }
  if (computerChoice === 'paper' && userChoice === 'scissors') {
    result = 'you win'
  }
}
