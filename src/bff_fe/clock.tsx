import * as React from "react";
import * as ReactDOM from "react-dom";


type ClockState = {
    time: Date
}

export class Clock extends React.Component<{}, ClockState> {
    timer_id: number;

    constructor() {
        super(null);
    }

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
        this.timer_id = setInterval(() => this.tick(), 1000);
    }

    render() {
        return (<p>{this.state.time.toLocaleTimeString()}</p>)
    }


    // Teardown
    componentWillUnmount() {
        clearInterval(this.timer_id);
    }

}
