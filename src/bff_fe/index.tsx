import * as React from "react";
import * as ReactDOM from "react-dom";
import { InvoiceItem, InvoiceItemsContainer } from './invoice-components.tsx';
import { Clock } from './clock.tsx'

ReactDOM.render(<Clock />, document.getElementById("clock_container"));


ReactDOM.render(
<InvoiceItemsContainer>
	<InvoiceItem quantity={2} description="Fool's Gold" unitPrice={0.50} />
</InvoiceItemsContainer>,
document.getElementById("invoice_item_container"));

/* 
import * as _ from 'lodash';

function component() {
    const element = document.createElement('div');
    element.innerHTML = _.join(['Hello', 'webpack'], ' ');
    return element;
}

document.getElementById("page_interface").appendChild(component());
*/
