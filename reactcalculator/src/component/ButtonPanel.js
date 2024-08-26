import Button from "./Button";
import React from "react";
import PropTypes from "prop-types";

import "./ButtonPanel.css";

export default class ButtonPanel extends React.Component {
  // The propTypes is a debugging aid, checking that the 
  // clickHandler prop is a function.
  static propTypes = {
    clickHandler: PropTypes.func,
  };

  // This method is a handler that gets called when a button is clicked. 
  // It calls the clickHandler function passed in via props.
  // buttonClicked is a ButtonPanel prop
  buttonClicked = buttonName => {
    this.props.clickHandler(buttonName);
  };

  // The ButtonPanel class overrides the inhertied method render() from React.Component.
  // This method defines how the component should be rendered on the screen. 
  // It's creating a grid of buttons using the <Button /> component.

  // Each Button component is passed a name and a clickHandler.
  // Some buttons have an additional orange property to signify a styling choice.
  // The button with the name "0" has a wide property for styling as well.
  render() {
    return (
      <div className="component-button-panel">
        <div>
          <Button name="AC" clickHandler={this.buttonClicked} />
          <Button name="+/-" clickHandler={this.buttonClicked} />
          <Button name="%" clickHandler={this.buttonClicked} />
          <Button name="÷" clickHandler={this.buttonClicked} orange />
        </div>
        <div>
          <Button name="7" clickHandler={this.buttonClicked} />
          <Button name="8" clickHandler={this.buttonClicked} />
          <Button name="9" clickHandler={this.buttonClicked} />
          <Button name="x" clickHandler={this.buttonClicked} orange />
        </div>
        <div>
          <Button name="4" clickHandler={this.buttonClicked} />
          <Button name="5" clickHandler={this.buttonClicked} />
          <Button name="6" clickHandler={this.buttonClicked} />
          <Button name="-" clickHandler={this.buttonClicked} orange />
        </div>
        <div>
          <Button name="1" clickHandler={this.buttonClicked} />
          <Button name="2" clickHandler={this.buttonClicked} />
          <Button name="3" clickHandler={this.buttonClicked} />
          <Button name="+" clickHandler={this.buttonClicked} orange />
        </div>
        <div>
          <Button name="0" clickHandler={this.buttonClicked} wide  />
          <Button name="." clickHandler={this.buttonClicked} />
          <Button name="=" clickHandler={this.buttonClicked} orange />
        </div>
      </div>
    );
  }
}
