function checkSentence() {
  var sentence = prompt("Enter a sentence with 'not' and 'bad':", "The movie is not that bad, I like it");
  var result = "";

  if (sentence === null || sentence === "") {
    result = "No sentence.";
  } else {
    var wordNot = sentence.indexOf("not");
    var wordBad = sentence.indexOf("bad");

    if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
      var before = sentence.slice(0, wordNot);
      var after = sentence.slice(wordBad + 3); // 'bad'.length = 3
      result = before + "good" + after;
    } else {
      result = sentence;
    }

    console.log("Original:", sentence);
    console.log("wordNot:", wordNot, "wordBad:", wordBad);
    console.log("Result:", result);
  }

  document.getElementById("result").textContent = result;
}