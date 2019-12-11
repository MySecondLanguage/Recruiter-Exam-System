import React, {Fragment} from "react";
import { connect } from "react-redux";
import apiHelper from '../apiHelper';

class Home extends React.Component {

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



    render() {
        const question = this.props.question;
        
        return (
            <Fragment>
                <div className="spacer-50"></div>
                <div className="row">
                    <div className="col-md-3"></div>
                    <div className="col-md-6">
                        <form className="exam-form">
                            <h1 className="q-title">{ question.title }</h1>
                            <hr></hr>
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