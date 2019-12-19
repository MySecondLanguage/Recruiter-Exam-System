import React, {Fragment} from "react";
import { connect } from "react-redux";
import apiHelper from '../apiHelper';
// import Timer from '../components/Timer'
import CountDown from '../components/Countdown';
import ResultSummery from '../components/ResultSummery';
class Home extends React.Component {
    constructor() {
        super();
        
        this.state = {
            result: {},
            timer: 0,
            startTime: null
        };
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    componentWillUnmount(){
        // Clear prevous state when retrun to another route
        
    }

    continueOnTimeOut = (time) => {
        if (time) {
            time = parseInt(time) * 1000
        setTimeout(() => {
            this.inputElement.click();
          }, time);
        };
        
    }

    elpased = (startTime) => {
        var endTime = new Date();
        var elapsedMilliSecond = endTime - startTime;
        var elapsed = Math.round(elapsedMilliSecond / 1000);
        return elapsed;
    }

    getQuestion() {
        apiHelper.getQuestionList().then((response) => {
            // handle success
            this.setState({
                timer: response.data.total_second
            })
            this.props.dispatch({ type: 'GET', response })
            this.continueOnTimeOut(response.data.total_second);
            
          }, () => {
             // handle error
          });

        this.setState({
            startTime: new Date(),
        })
        
    }


    componentDidMount(){
         this.getQuestion()
     }

     handleChange(event) {
        this.state.result[event.target.name] = event.target.value
        this.setState({
          result: {
              ...this.state.result
          }
        });
      }

      handleSubmit(event) {
        //   this.getQuestion()
        // event.preventDefault();
        
        const result = {
            question: this.props.question.id,
            answer: Object.keys(this.state.result).map((key) => (
                parseInt(this.state.result[key])
            )),
            elapsed: this.elpased(this.state.startTime),
        }

        apiHelper.setResult(result).then((response) => {
            // console.log(response);
        })

      }



    render() {
        const question = this.props.question;
        
        return (
            <Fragment>
                <div className="spacer-50"></div>
                <div className="countdown">
                    <CountDown second={this.state.timer} />
                </div>
                <div className="row">
                    <div className="col-md-1"></div>
                    <div className="col-md-10">
                        {question.id ? <form onSubmit={this.handleSubmit} className="exam-form">
                            <h1 className="q-title">{ question.title }</h1>
                            <hr></hr>
                            <div className="checkbox-main-container">
                                {question.choices ? question.choices.map((choice, index) => (
                                    <div className="checkbox-container" key={index}>
                                        
                                        <input
                                            id={index}
                                            name={`choice${index}`}
                                            onChange={this.handleChange}
                                            value={choice.id}
                                            type="checkbox">
                                        </input>
                                        <label htmlFor={index}>{choice.choice_text}</label>
                                    </div>
                                )) : <p>no choices are loaded yet, please try again</p>}
                            </div>
                            <button ref={input => this.inputElement = input} className="btn btn-primary">Submit</button>
                            <div>
                               
                            </div>
                        </form> : <div className="">
                            <ResultSummery />
                        </div> }
                        
                    </div>
                    <div className="col-md-1"></div>
                </div>
            </Fragment>
        );
    }
}

const mapStateToProps = (state) => ({ question: state.question });

export default connect(mapStateToProps)(Home);