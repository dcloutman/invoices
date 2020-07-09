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



type InvoiceItemsContainerState = {
    item_count: number
}

type InvoiceItemsContainerProps = {
}

export class InvoiceItemsContainer extends React.Component<InvoiceItemsContainerProps, InvoiceItemsContainerState> {
    componentWillMount () {
        this.setState({
            item_count: 0
        });
    }


    render() {
        return (
            <table>
                <thead>
                    <tr>
                        <th>Quantity</th>
                        <th>Description</th>
                        <th>Unit Price</th>
                        <th>Amount</th>
                    </tr>
                </thead>
                <tbody id="invoice_items">
                    { this.props.children }
                </tbody>
            </table>
        );
    }

    addItem(item: InvoiceItem) {

    }
}

