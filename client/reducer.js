var initialState = {
    question: {},
  };
  
  var Reducer = (state = initialState, action) => {
    switch (action.type) {
      
      case 'GET':
        return {
          ...state,
          question: action.response.data,
        }

      default:
        return state;
    }
  };
  
  
  export default Reducer;