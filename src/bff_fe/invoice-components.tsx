import * as React from "react";
import * as ReactDOM from "react-dom";

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
