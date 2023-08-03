// When user clicks + button a new set of weight and reps are populated.
// when button click a new sent of LI is populated.

function addSet() {
	const weightElement = document.getElementById("weightInput");
	const repsElement = document.getElementById("repsInput");

	const newWeightElement = weightElement.cloneNode(true);
	const newRepsElement = repsElement.cloneNode(true);

	// Reset values on click
	newWeightElement.value = "";
	newRepsElement.value = "";

	const exerciseList = document.querySelector(".weight-reps-container");
	exerciseList.appendChild(newWeightElement);
	exerciseList.appendChild(newRepsElement);
}

document.getElementById("addSet").onclick = addSet;
