//get elements from DOM
var lang_select = (document.getElementById("language"));
var corp_select = (document.getElementById("corpus"));
var alg_select = (document.getElementById("algorithm"));
var feature_select = (document.getElementById("feature"));

var language, corpus, algorithm, feature;
//initially hide corpus, algorithm, feature select fields
$(corp_select).hide()
$(alg_select).hide()
$(feature_select).hide()

//on changing the language select field, shows corpus select field with possible options according to the db
lang_select.innerHTML = '<option>Select language</option>' + lang_select.innerHTML;
lang_select.onchange = function () {
    lang_select.disabled = true;
    language = lang_select.options[lang_select.selectedIndex].text;
    $(corp_select).show();
    fetch('/query/' + language).then(function (response) {
        response.json().then(function (data) {
            var optionHTML = '';
            optionHTML += '<option>Select corpus size</option>';
            for (var corp of data.corpus) {
                optionHTML += '<option>' + corp + '</option>';
            }
            corp_select.innerHTML = optionHTML;
        })

    });
}
//on changing the corpus select field, shows algorithm select field with possible options according to the db

corp_select.onchange = function () {
    corp_select.disabled = true;
    corpus = corp_select.options[corp_select.selectedIndex].text;
    $(alg_select).show();
    fetch('/query/' + language + "/" + corpus).then(function (response) {
        response.json().then(function (data) {
            var optionHTML = '';
            optionHTML += '<option>Select algorithm</option>';
            for (var alg of data.algorithm) {
                optionHTML += '<option>' + alg + '</option>';
            }
            alg_select.innerHTML = optionHTML;
        })

    });

}
//on changing the algorithm select field, shows feature select field with possible options according to the db
alg_select.onchange = function () {
    alg_select.disabled = true;
    algorithm = alg_select.options[alg_select.selectedIndex].text;
    $(feature_select).show();
    fetch('/query/' + language + "/" + corpus + "/" + algorithm).then(function (response) {
        response.json().then(function (data) {
            var optionHTML = '';
            optionHTML += "<option> Select feature </option>";
            for (var feature of data.feature) {
                optionHTML += '<option>' + feature + '</option>';
            }
            feature_select.innerHTML = optionHTML;
        })

    });

}

feature_select.onchange = function () {
    feature_select.disabled = true;
    feature = feature_select.options[feature_select.selectedIndex].text;
    //attach event handler
    $("#querysubmit").click(
        function () {
            //get accuracy from db and display
            fetch('/query/' + language + "/" + corpus + "/" + algorithm + "/" + feature).then(function (response) {
                response.json().then(function (data) {
                    document.getElementById("accuracy").innerHTML = "The accuracy is " + data.accuracy[0];

                })

            });
        }
    )

}

