import React, {Fragment} from "react";
import { connect } from "react-redux";


class Home extends React.Component {

    componentWillUnmount(){
        // Clear prevous state when retrun to another route
        
    }


    componentDidMount(){
        // get user list on reload the page
         
     }
    render() {
        return (
            <Fragment>
                <h1>hello world</h1>
            </Fragment>
        );
    }
}


export default connect(null)(Home);