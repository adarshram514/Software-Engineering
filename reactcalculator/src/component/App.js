
// The App component serves as the main container for the application. 
// It maintains the state for previous, current, and operation 

import React from "react";

import Display from "./Display";
import ButtonPanel from "./ButtonPanel";
import calculate from "../logic/calculate";
import "./App.css";

// state -  holds the values for the previous operand, the current operand, and the operation to perform.
export default class App extends React.Component {
  state = {
    previous: null,
    current: null,
    operation: null,
  };

  // handleClick - a method that updates the state based on a button click. It calls the calculate function.
  handleClick = buttonName => {
    this.setState(calculate(this.state, buttonName));
  };


  // render - a method that renders a Display component and a ButtonPanel component.
  // The Display component shows the value of the current operand, or if that's null, the previous operand. If both are null, it shows "0".
  // The ButtonPanel component sets the value of clickHandler to the value of this.handleClick.
  // It includes an (implicit) argument of buttonName.
  render() {
    return (
      <div className="component-app">
        <Display value={this.state.current || this.state.previous || "0"} />
        <ButtonPanel clickHandler={this.handleClick} />
      </div>
    );
  }
}
