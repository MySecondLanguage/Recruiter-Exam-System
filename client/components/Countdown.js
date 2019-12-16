import React, {Fragment} from "react";

class CountDown extends React.Component {
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

    stopCountDown = () => {
        
        if(this.countDownId != null){
            clearInterval(this.countDownId)
            this.countDownId = null
        }
        
    }
    

    paintDom = () => new Promise(resolve => {
        this.setState({
            ...this.state
        }, resolve)
    })

    startCountDown = () => {
        this.stopCountDown()
        this.countDownId = setInterval(() => {
            this.state.second -= 1
            this.paintDom()
        }, 1000);

        setTimeout(() => {
            this.stopCountDown()
        }, this.state.second * 1000);
    }

    componentDidUpdate(prevProps, PrevState){
        if (this.props.second !== prevProps.second) {
            this.state.second = this.props.second;
            this.startCountDown()
        }
        
    }




    render() {       
        return (
            <p>
                {this.props.second ? this.format(this.state.second) : <span>Exam Finished..</span>}
            </p>
        );
    }
}


export default CountDown;