import React from 'react';
import operate from "../logic/operate";
import Big from "big.js";


describe('Operate Multiplication Tests', ()=>{
    test('4 x 3 = 12 test', () => {
        expect(operate("4","3","x")).toBe("12"); 
    });
});


describe('Operate Division Tests', ()=>{
    test('4/3 = 1.333 test', () => {
        expect(parseFloat(operate("4","3","÷"))).
            toBeCloseTo(1.3333333333, 5); 
        // parseFloat() is a string-to-float function in Javascript.   
        // Try different precisions and string lengths to see what the test does.
    });
    test('20/5 = 4 test', () => {
        expect(operate("20","5","÷")).toBe("4"); 
    });  
});


