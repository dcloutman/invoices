import * as React from "react";
import * as ReactDOM from "react-dom";
import { Clock, InvoiceItem } from './invoice-components.tsx';

ReactDOM.render(<Clock />, document.getElementById("clock_container"));

//const test_item = ();
//test_item.setState();

ReactDOM.render(<InvoiceItem quantity={2} description="Fool's Gold" unitPrice={0.50} />, document.getElementById("invoice_item_container"));

/* 
import * as _ from 'lodash';

function component() {
    const element = document.createElement('div');
    element.innerHTML = _.join(['Hello', 'webpack'], ' ');
    return element;
}

document.getElementById("page_interface").appendChild(component());
*/
