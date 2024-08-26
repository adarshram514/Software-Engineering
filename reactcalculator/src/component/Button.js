// Renders the individual buttons.
import React from "react";
import PropTypes from "prop-types";
import "./Button.css";

export default class Button extends React.Component {
  // propTypes is checks to that the props are being 
  // treated as defined in the body of propTypes.  If not,
  // a warning message will be logged in the console.
  // This is a debugging aid that is turned off when creating 
  // a production build.
  static propTypes = {
    name: PropTypes.string,
    orange: PropTypes.bool,
    wide: PropTypes.bool,
    clickHandler: PropTypes.func,
  };

  // name - the label for the button.
  // orange and wide -  boolean flags that affect the button's styling.
  // clickHandler is the function that gets called when the button is clicked. 
  // This function is passed from the parent (ButtonPanel) to this button, and eventually, 
  // it invokes the handleClick method defined in the App component.

  iAmClicked = () => {
    this.props.clickHandler(this.props.name);
  };

  render() {
    const className = [
      "component-button",
      this.props.orange ? "orange" : "",
      this.props.wide ? "wide" : "",
    ];

    // The join(" ").trim() all the css to be access correctly. 
    return (
      <div className={className.join(" ").trim()}>
        <button onClick={this.iAmClicked}>{this.props.name}</button>
      </div>
    );
  }
}
