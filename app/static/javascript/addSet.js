// When user clicks + button a new set of weight and reps are populated.
// when button click a new sent of LI is populated.

function addSet () {

  const weightElement = document.querySelector('.card-weight');
  const repsElement = document.querySelector('.card-reps');

  const newWeightElement = weightElement.cloneNode(true);
  const newRepsElement = repsElement.cloneNode(true);

  // Reset values on click
  newWeightElement.querySelector('input').value = '';
  newRepsElement.querySelector('input').value = '';

  const exerciseList = document.getElementById('exercise-list');
  exerciseList.appendChild(newWeightElement);
  exerciseList.appendChild(newRepsElement);
}

document.getElementById("addSet").onclick = addSet;