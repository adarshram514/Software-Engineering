import calculate from "../logic/calculate";

 
describe('Number buttons tests', ()=>{
    test('null, null, null, 3', () => {
        expect(calculate({
                previous: null,
                current: null,
                operation: null},"3")).toHaveProperty('current', "3");
    });
    test('null, 1, null, 1', () => {
        expect(calculate({
                previous: null,
                current: "1",
                operation: null},"1")).toHaveProperty('current', "11");
    });

});    

describe('Equal Button Tests', ()=>{
    test('2,2,+,=', () => {
        expect(calculate({
                previous: "2",
                current: "2",
                operation: "+"},"=")).toHaveProperty('previous', "4");
    });

});


