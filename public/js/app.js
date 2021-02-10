"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var MainApp = function (_React$Component) {
    _inherits(MainApp, _React$Component);

    function MainApp() {
        _classCallCheck(this, MainApp);

        return _possibleConstructorReturn(this, (MainApp.__proto__ || Object.getPrototypeOf(MainApp)).apply(this, arguments));
    }

    _createClass(MainApp, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                null,
                React.createElement(Header, null),
                React.createElement("br", null),
                React.createElement("br", null),
                React.createElement("br", null),
                React.createElement("br", null),
                React.createElement(Form, null)
            );
        }
    }]);

    return MainApp;
}(React.Component);

var Header = function (_React$Component2) {
    _inherits(Header, _React$Component2);

    function Header() {
        _classCallCheck(this, Header);

        return _possibleConstructorReturn(this, (Header.__proto__ || Object.getPrototypeOf(Header)).apply(this, arguments));
    }

    _createClass(Header, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                null,
                React.createElement(
                    "h1",
                    null,
                    "Heart Failure Prediction"
                )
            );
        }
    }]);

    return Header;
}(React.Component);

var Form = function (_React$Component3) {
    _inherits(Form, _React$Component3);

    function Form() {
        _classCallCheck(this, Form);

        return _possibleConstructorReturn(this, (Form.__proto__ || Object.getPrototypeOf(Form)).apply(this, arguments));
    }

    _createClass(Form, [{
        key: "GetPrediction",
        value: function GetPrediction(e) {
            e.preventDefault();
            var array = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"];
            var values = [e.target.age.value, e.target.sex.value, e.target.cp.value, e.target.trestbps.value, e.target.chol.value, e.target.fbs.value, e.target.restecg.value, e.target.thalach.value, e.target.exang.value, e.target.oldpeak.value, e.target.slope.value, e.target.ca.value, e.target.thal.value];
            var url = "http://localhost:5000/predict?";
            for (var i = 0; i < array.length; i++) {
                url += array[parseInt(i)] + "=" + values[i];
                if (parseInt(i) != array.length - 1) {
                    url += "&";
                }
            }
            var prediction = document.getElementById("prediction");
            prediction.innerHTML = "loading....";
            fetch(url, { headers: {
                    'Content-Type': 'application/json'
                } }).then(function (response) {
                return response.json();
            }).then(function (data) {
                if (data.prediction == 1) {
                    prediction.innerHTML = "POSITIVE";
                } else {
                    prediction.innerHTML = "NEGATIVE";
                }
            });

            console.log(url);
        }
    }, {
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                null,
                React.createElement(
                    "form",
                    { method: "get", autoComplete: "off", onSubmit: this.GetPrediction },
                    React.createElement("input", { id: "age", name: "age", placeholder: "AGE", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "sex", name: "sex", placeholder: "SEX", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "cp", name: "cp", placeholder: "CP", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "trestbps", name: "trestbps", placeholder: "TRESTBPS", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "chol", name: "chol", placeholder: "CHOL", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "fbs", name: "fbs", placeholder: "FBS", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "restecg", name: "restecg", placeholder: "RESTECG", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "thalach", name: "thalach", placeholder: "THALACH", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "exang", name: "exang", placeholder: "EXANG", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "oldpeak", name: "oldpeak", placeholder: "OLDPEAK", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "slope", name: "slope", placeholder: "SLOPE", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "ca", name: "ca", placeholder: "CA", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement("input", { id: "thal", name: "thal", placeholder: "THAL", required: true }),
                    React.createElement("br", null),
                    React.createElement("br", null),
                    React.createElement(
                        "button",
                        null,
                        "PREDICT"
                    )
                )
            );
        }
    }]);

    return Form;
}(React.Component);

var app = document.getElementById("mainform");
ReactDOM.render(React.createElement(MainApp, null), app);
