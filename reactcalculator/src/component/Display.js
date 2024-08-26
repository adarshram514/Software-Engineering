import React from "react";
import PropTypes from "prop-types";

import "./Display.css";
// This component is simply responsible for displaying a string value, passed in as a prop.
export default class Display extends React.Component {
  // propTypes is checks to see that the value Display 
  // recieves is a string.  If a string is not recieved,
  // a warning message will be logged in the console.
  // This is a debugging aid that is turned off when creating 
  // a production build.
  static propTypes = {
    value: PropTypes.string,
  };

  render() {
    return (
      <div className="component-display">
        <div>{this.props.value}</div>
      </div>
    );
  }
}
