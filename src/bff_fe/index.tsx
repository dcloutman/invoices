import * as React from "react";
import * as ReactDOM from "react-dom";
import { Clock } from './invoice-components.tsx';

ReactDOM.render(<Clock />, document.getElementById("page_interface"));

/* 
import * as _ from 'lodash';

function component() {
    const element = document.createElement('div');
    element.innerHTML = _.join(['Hello', 'webpack'], ' ');
    return element;
}

document.getElementById("page_interface").appendChild(component());
*/
