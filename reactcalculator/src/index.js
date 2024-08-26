// This is the entry point of the React application. 
// It's responsible for rendering the root component, 
// which in this case is App, into a DOM element with the id "root".
// It imports React, ReactDOM, the main App component, and some CSS. 
// It then uses ReactDOM.render() to mount the App component into the 
// DOM element with the id "root".



import React from "react";
import ReactDOM from "react-dom";
import App from "./component/App";
import "./index.css";


ReactDOM.render(<App />, document.getElementById("root"));
