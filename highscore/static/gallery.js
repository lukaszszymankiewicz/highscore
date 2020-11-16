function initializePage(array) {
    if (array.length == 0) {
        document.getElementById("content").style.display = "none";
        document.getElementById("no_results").style.display = "block";
        setFirstScoreSrcAndUrlForEmptyResults();
    } else {
        setFirstScoreSrcAndUrl(array);
        setCurrentPage(1);
        setAllPagesNumber(array.length);
    }
}

function changeImage(array, direction) {
    var expandScore = document.getElementById("expandedScore");
    number = calculateScoreNumberToRead(number, direction, array.length);

    var imageData = array[number];
    expandScore.src = imageData.url;

    var visitLink = document.getElementById("visit_link");
    visitLink.href = imageData.link;

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

function setFirstScoreSrcAndUrl(array) {
    document.getElementById("expandedScore").src = array[0].url;
    document.getElementById("visit_link").href = array[0].link;
}

function setFirstScoreSrcAndUrlForEmptyResults(){w
    document.getElementById("expandedScore").src = "";
    document.getElementById("visit_link").href = "#2";
}
