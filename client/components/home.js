import React, {Fragment} from "react";
import { connect } from "react-redux";
import apiHelper from '../apiHelper';

class Home extends React.Component {
    constructor() {
        super();
        
        this.state = {
            result: {},
            timer: 10,
        };
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    componentWillUnmount(){
        // Clear prevous state when retrun to another route
        
    }

    continueOnTimeOut = () => {
        setTimeout(() => {
            this.inputElement.click();
          }, 8000);
    }

    getQuestion() {
        apiHelper.getQuestionList().then((response) => {
            // handle success
            this.props.dispatch({ type: 'GET', response })
            this.continueOnTimeOut();
            
          }, () => {
             // handle error
             
          });
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
            ))
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
                <div>
                    <p>{ this.state.timer }</p>
                </div>
                <div className="row">
                    <div className="col-md-1"></div>
                    <div className="col-md-10">
                        <form onSubmit={this.handleSubmit} className="exam-form">
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
                        </form>
                    </div>
                    <div className="col-md-1"></div>
                </div>
            </Fragment>
        );
    }
}

const mapStateToProps = (state) => ({ question: state.question });

export default connect(mapStateToProps)(Home);