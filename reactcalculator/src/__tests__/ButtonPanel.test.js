import React from "react";
import ReactDOM from "react-dom";
import Enzyme, {shallow, mount} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import ButtonPanel from "../component/ButtonPanel"
import { act} from 'react-dom/test-utils';
import { create } from 'react-test-renderer';


Enzyme.configure({adapter: new Adapter()});

// Test that the ButtonPanel component renders without crashing:
test('renders ButtonPanel without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<ButtonPanel />, div);
    ReactDOM.unmountComponentAtNode(div);
  });

  // Test that ButtonPanel has the correct number of buttons.  
  // "shallow" creates a shallow rendered instance of the component, 
  // which means that it only renders the component itself and not any child components. 
  // This makes the test run faster but with less accurate rendering.
  test('ButtonPanel has 19 buttons', () => {
    const wrapper = shallow(<ButtonPanel />);
    expect(wrapper.find('Button')).toHaveLength(19);
  });

  // Test that clicking a Button triggers the handleClick function.
  // jest.fn() is creates a mock function which allows you to test that a 
  // certain function is called (in this case the clickHandler), without actually 
  // executing the function's code.
  // create() returns a virtual DOM that contains the rendered version of ButtonPanel
  // The act() function ensures that a component (in this case a button) is fully rendered  
  // before testing it with the expect() function.
  test('clicking a Button triggers handleClick', () => {
    const mockFn = jest.fn();
    const component = create(<ButtonPanel clickHandler={mockFn} />);
    const testRenderer = component.root;
  
    const buttons = testRenderer.findAllByType('button');
    const button = buttons[0];
    
    act(() => {
      button.props.onClick();
    });
    
    expect(mockFn).toHaveBeenCalledTimes(1);
  });
  
