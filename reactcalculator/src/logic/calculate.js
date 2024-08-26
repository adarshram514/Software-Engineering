import Big from "big.js";

import operate from "./operate";
import isNumber from "./isNumber";

/**
 * Given a button name and a calculator data object, return an updated
 * calculator data object.
 *
 * Calculator data object contains:
 *   previous:String      the running previous
 *   current:String       the current number to be operated on with the previous
 *   operation:String  +, -, etc.
 */
export default function calculate(obj, buttonName) {
  if (buttonName === "AC") {
    return {
      previous: null,
      current: null,
      operation: null,
    };
  }

  if (isNumber(buttonName)) {
    if (buttonName === "0" && obj.current === "0") {
      return {};
    }
    // If there is an operation, update current
    if (obj.operation) {
      if (obj.current) {
        return { current: obj.current + buttonName };
      }
      return { current: buttonName };
    }
    // If there is no operation, update current and clear the value
    if (obj.current) {
      const current = obj.current === "0" ? buttonName : obj.current + buttonName;
      return {
        current,
        previous: null,
      };
    }
    return {
      current: buttonName,
      previous: null,
    };
  }

  if (buttonName === "%") {
    if (obj.operation && obj.current) {
      const result = operate(obj.previous, obj.current, obj.operation);
      return {
        previous: Big(result)
          .div(Big("100"))
          .toString(),
        current: null,
        operation: null,
      };
    }
    if (obj.current) {
      return {
        current: Big(obj.current)
          .div(Big("100"))
          .toString(),
      };
    }
    return {};
  }

  if (buttonName === ".") {
    if (obj.current) {
      // ignore a . if the current number already has one
      if (obj.current.includes(".")) {
        return {};
      }
      return { current: obj.current + "." };
    }
    return { current: "0." };
  }

  if (buttonName === "=") {
    if (obj.current && obj.operation) {
      return {
        previous: operate(obj.previous, obj.current, obj.operation),
        current: null,
        operation: null,
      };
    } else {
      // '=' with no operation, nothing to do
      return {};
    }
  }

  if (buttonName === "+/-") {
    if (obj.current) {
      return { current: (-1 * parseFloat(obj.current)).toString() };
    }
    if (obj.previous) {
      return { previous: (-1 * parseFloat(obj.previous)).toString() };
    }
    return {};
  }

  // Button must be an operation

  // When the user presses an operation button without having entered
  // a number first, do nothing.
  // if (!obj.current && !obj.previous) {
  //   return {};
  // }

  // User pressed an operation button and there is an existing operation
  if (obj.operation) {
    return {
      previous: operate(obj.previous, obj.current, obj.operation),
      current: null,
      operation: buttonName,
    };
  }

  // no operation yet, but the user typed one

  // The user hasn't typed a number yet, just save the operation
  if (!obj.current) {
    return { operation: buttonName };
  }

  // save the operation and shift 'current' into 'previous'
  return {
    previous: obj.current,
    current: null,
    operation: buttonName,
  };
}
