import * as React from "react";
import * as ReactDOM from "react-dom";


type InvoiceItemState = {
    quantity: number,
    description: string,
    unit_price: number,
    amount: number
}

type InvoiceItemProps = {
    quantity: number,
    description: string,
    unitPrice: number
}

export class InvoiceItem extends React.Component<InvoiceItemProps, InvoiceItemState> {
    componentWillMount () {
        this.setState(
            {
                quantity: this.props.quantity,
                description: this.props.description,
                unit_price: this.props.unitPrice,
                amount: this.props.quantity * this.props.unitPrice
            }
        ); 
    }

    render() {

        return (
            <tr>
                <td>{ this.state.quantity }</td>
                <td>{ this.state.description }</td>
                <td>{ this.state.unit_price }</td>
                <td>{ this.state.amount }</td>
            </tr>
        );
    }
}




type ClockState = {
    time: Date
}

export class Clock extends React.Component<{}, ClockState> {

    // Sets the current time with a date object. 
    tick() {
        this.setState({
            time: new Date()
        });
    }

    // Before the component mounts, initialise the clock's state
    componentWillMount() {
        this.tick();
    } 

    // After the component has mounted, reset the state every second.
    componentDidMount() {
        setInterval(() => this.tick(), 1000);
    }

    render() {
        return (<p>{this.state.time.toLocaleTimeString()}</p>)
    }
}
