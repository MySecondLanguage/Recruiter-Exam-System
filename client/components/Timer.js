import React, {Fragment} from "react";

class Timer extends React.Component {
    constructor() {
        super();

        this.countDownId = null;

        this.state = {
            second: 0
        }
    }

    format = (seconds) => {
        var numminutes = Math.floor((((seconds % 31536000) % 86400) % 3600) / 60);
        var numseconds = (((seconds % 31536000) % 86400) % 3600) % 60;
        return (
            String(numminutes).padStart(2, 0) + ":" +
            String(numseconds).padStart(2, 0) + "s"
        )
    }

    paintDom = () => new Promise(resolve => {
        this.setState({
            ...this.state
        }, resolve)
    })

    stopCountDown = () => {
        if(this.countDownId != null){
            clearInterval(this.countDownId)
            this.countDownId = null
        }
    }

    startCountDown = () => {
        this.stopCountDown()
        if(this.state.second == 0){
            return;
        }

        this.countDownId = setInterval(() => {
            this.state.second -= 1
            this.paintDom()
        }, 1000);

        setTimeout(() => {
            this.stopCountDown()
        }, this.state.second * 1000);
    }

    componentDidMount(){
        // this.state.second = this.props.second
        // this.startCountDown()
        // this.paintDom()
    }

    componentDidUpdate(prevProps, prevState){
        if(this.props.second !== prevProps.second){
            this.state.second = this.props.second;
            this.startCountDown()
            this.paintDom()
        }
    }


    render() {       
        return (
            <span>
                {this.format(this.state.second)}
            </span>
        );
    }
}


export default Timer;