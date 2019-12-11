import React, {Fragment} from "react";
import { connect } from "react-redux";
import apiHelper from '../apiHelper';

class Home extends React.Component {
    constructor() {
        super();
        
        this.state = {};
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    componentWillUnmount(){
        // Clear prevous state when retrun to another route
        
    }


    componentDidMount(){
        // get user list on reload the page
         apiHelper.getQuestionList().then((response) => {
           // handle success
           this.props.dispatch({ type: 'GET', response }) 
         }, () => {
            // handle error
            
         });
     }

     handleChange(event) {
        this.setState({
          choice: event.target.value
        });
      }

      handleSubmit(event) {
        event.preventDefault();
        
        alert(this.state.choice);
      }



    render() {
        const question = this.props.question;
        
        return (
            <Fragment>
                <div className="spacer-50"></div>
                <div className="row">
                    <div className="col-md-3"></div>
                    <div className="col-md-6">
                        <form onSubmit={this.handleSubmit} className="exam-form">
                            <h1 className="q-title">{ question.title }</h1>
                            <hr></hr>
                            <div>
                                {question.choices ? question.choices.map((choice, index) => (
                                    <div key={index}>
                                        
                                        <input
                                            id="radio"
                                            onChange={this.handleChange}
                                            value={choice.id}
                                            type="radio">
                                        </input>
                                        <label htmlFor="radio">{choice.choice_text}</label>
                                    </div>
                                )) : <p>no choices is loaded yet, please try again</p>}
                            </div>
                            <button className="btn btn-primary">Save Answwer</button>
                            <div>
                               
                            </div>
                        </form>
                    </div>
                    <div className="col-md-3"></div>
                </div>
            </Fragment>
        );
    }
}

const mapStateToProps = (state) => ({ question: state.question });

export default connect(mapStateToProps)(Home);