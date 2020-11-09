function init(array) {
    setCurrentPage(1);
    setAllPagesNumber(array.length);
}

function changeImage(array, direction) {
    var expandScore = document.getElementById("expandedScore");
    number = calculateScoreNumberToRead(number, direction, array.length);

    var imageData = array[number];
    expandScore.src = imageData.url;

    setCurrentPage(number + 1);
    setAllPagesNumber(array.length);
}

function calculateScoreNumberToRead(currentScoreNumber, direction, arrayLength) {
    newScoreNumber = currentScoreNumber + direction;

    if (newScoreNumber == arrayLength) {
        return 0;
    } else if (newScoreNumber < 0) {
        return arrayLength - 1;
    } else {
        return newScoreNumber;
    }
}

function setCurrentPage(number) {
    document.getElementById("current_page").innerHTML = number;
}

function setAllPagesNumber(number) {
    document.getElementById("all_pages").innerHTML = number;
}
