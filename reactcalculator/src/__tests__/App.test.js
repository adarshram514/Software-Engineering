import React from "react";
import ReactDOM from "react-dom";
import ReactTestUtils from 'react-dom/test-utils'
import App from "../component/App";
import ButtonPanel from "../component/ButtonPanel"

 
describe('App Render Tests', ()=>{
  // Creates a local html element  and renders the App component into it.
  test("Renders and destroy an element", () => {
    // Create an html element with tag 'div'
    const div = document.createElement("div");
    // Render the App into the div container
    const createdComponent = ReactDOM.render(<App />, div);
    // Test to see if it exists
    expect(createdComponent).toBeTruthy();
    // How many divs are there?
    let length = ReactTestUtils.scryRenderedDOMComponentsWithTag(createdComponent,'div').length;
    // There are 28 divs, so write a test to confirm it
    expect(length).toBe(28 );
    // console.log('found this many divs:', length);
    // Destroy the element and test whether it is deleted.
    const componentIsDeleted = ReactDOM.unmountComponentAtNode(div);
    expect(componentIsDeleted).toBeTruthy();
  });

  // Tests whether App's initial state properties are all null.
  test('Is initial state null?', ()=>{
          let component = ReactTestUtils.renderIntoDocument(<App/>);
          let state = component.state;
          expect(state.previous).toBe(null);
          expect(state.current).toBe(null);
          expect(state.operation).toBe(null);
  }); 

  // Tests to see whether there are 19 buttons
  test('How many buttons does ButtonPanel have?', ()=>{   
          const component = ReactTestUtils.renderIntoDocument(<ButtonPanel/>);
          let length = ReactTestUtils.scryRenderedDOMComponentsWithTag(component,'button').length;
          //console.log('found this many buttons:', length);
          expect(length).toBeGreaterThan(2);
          // There are 19 buttons, so write a test to confirm it
          expect(length).toBe(19);
  });  
});

