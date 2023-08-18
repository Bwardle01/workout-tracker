// When a user clicks add exercise, a new exercise field will be populated along with weight and reps.
// When a new exercise is populated a + button is also added to add a new set.
function addExercise() { 

	const weightElement = document.getElementById("weightInput");
	const repsElement = document.getElementById("repsInput");
  const exerciseElement = document.getElementById("exerciseInput");
  const setElement = document.getElementById("addSet")

	const newWeightElement = weightElement.cloneNode(true);
	const newRepsElement = repsElement.cloneNode(true);
  const newExerciseElement = exerciseElement.cloneNode(true);
  const newSetElement = setElement.cloneNode(true);

  newWeightElement.value = "";
	newRepsElement.value = "";
  newExerciseElement.value = "";

  const exerciseList = document.querySelector(".weight-reps-container");
  const exerciseContainer = document.querySelector(".exercise-container");
  const addSetContainer = document.querySelector(".add-set-container");


	exerciseList.appendChild(newWeightElement);
	exerciseList.appendChild(newRepsElement);
  exerciseContainer.appendChild(newExerciseElement);
  addSetContainer.appendChild(newSetElement);
};

document.getElementById('addExercise').onclick = addExercise;













// When user clicks + button a new set of weight and reps are populated.
// when button click a new set of LI is populated of input fields.